#!/usr/bin/env python3
"""Promptless Skill v0.3.1 Visual Card Parser.

本工具不綁定特定 Vision API。ChatGPT / Gemini / Claude 先依 adapters/visual-card-extractor.md
將圖片抽取為 extraction JSON；本工具再正規化、驗證、分類、編譯。

用法：
  python tools/visual_card_parser.py validate-extraction extraction.json
  python tools/visual_card_parser.py normalize extraction.json --out card.json
  python tools/visual_card_parser.py pipeline extraction.json --card-out card.json --md-out generated.md
"""
from __future__ import annotations
import argparse, json, re, sys, hashlib
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SCHEMAS=ROOT/'schemas'
sys.path.insert(0,str(ROOT/'tools'))
import promptless_card

def load(p): return json.loads(Path(p).read_text(encoding='utf-8'))
def dump(obj,p): Path(p).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def validate_extraction(x):
    try: import jsonschema
    except ImportError: raise RuntimeError('請安裝 jsonschema>=4.22')
    schema=load(SCHEMAS/'visual-card-extraction.schema.json')
    v=jsonschema.Draft202012Validator(schema)
    errs=sorted(v.iter_errors(x),key=lambda e:list(e.absolute_path))
    if errs:
        raise ValueError('\n'.join(f"{'.'.join(map(str,e.absolute_path)) or '<root>'}: {e.message}" for e in errs))

def slug(s):
    v=re.sub(r'[^A-Za-z0-9._-]+','-',s.strip()).strip('-').lower()
    generic={'skill','agent','card','promptless','vad'}
    if len(v)>=3 and v not in generic: return v
    return 'card-' + hashlib.sha256(s.encode('utf-8')).hexdigest()[:10]

def infer_input_type(text):
    t=text.lower()
    if any(k in t for k in ['圖片','image','照片']): return 'image'
    if 'pdf' in t: return 'pdf'
    if any(k in t for k in ['excel','試算表','spreadsheet']): return 'spreadsheet'
    if any(k in t for k in ['網址','url','網站']): return 'url'
    if any(k in t for k in ['json']): return 'json'
    return 'file'

def build_skill(x):
    f=x.get('fields',{}); sig=x.get('signals',{})
    objective=x['intent']['objective']; success=x['intent'].get('success_definition') or '產出符合卡片指定內容與品質要求的成果。'
    inputs=f.get('input') or ['使用者提供的主要素材']
    proc=f.get('process') or ['理解任務與素材','依卡片規格完成任務','執行品質檢查']
    outs=f.get('output') or ['最終成果']
    checks=f.get('qa') or ['內容符合任務目標','輸出完整且可用']
    dynamic=sum(bool(sig.get(k)) for k in ['dynamic_branching','dynamic_tool_selection','replanning','persistent_state','delegation','multi_agent'])
    autonomy=3 if dynamic else (2 if sig.get('external_side_effects') else 1)
    return {
      'schema_version':'0.3.0','card_type':'skill','id':slug(x['intent']['name']),'name':x['intent']['name'],
      'description':objective,'language':x.get('source',{}).get('language_hint','zh-TW'),
      'metadata':{'version':'1.0.0','tags':['visual-card','promptless']},
      'task':{'objective':objective,'success_definition':success},
      'input':[{'name':v,'type':infer_input_type(v),'required':True} for v in inputs],
      'style':{'language':'zh-TW','format_constraints':f.get('style',[])},
      'process':[{'id':f'step-{i+1}','name':v[:40],'action':v,'on_failure':'human_review'} for i,v in enumerate(proc)],
      'output':{'artifacts':[{'name':v,'type':'artifact','required':True} for v in outs]},
      'qa':{'checks':[{'id':f'qa-{i+1}','criterion':v,'severity':'blocker','method':'model'} for i,v in enumerate(checks)],'pass_policy':'all_blockers'},
      'execution':{'autonomy_level':autonomy,'dynamic_branching':bool(sig.get('dynamic_branching')),'dynamic_tool_selection':bool(sig.get('dynamic_tool_selection')),
        'replanning':bool(sig.get('replanning')),'persistent_state':bool(sig.get('persistent_state')),'delegation':bool(sig.get('delegation')),'multi_agent':bool(sig.get('multi_agent')),
        'external_side_effects':bool(sig.get('external_side_effects')),'human_approval_required':bool(sig.get('human_approval_required'))},
      'upgrade_policy':{'allow_agent_upgrade':True,'mode':'suggest'}
    }

def build_agent(x):
    f=x.get('fields',{}); sig=x.get('signals',{})
    objective=x['intent']['objective']; success=x['intent'].get('success_definition') or '完成目標並通過 QA / Governance。'
    workflow=f.get('process') or ['理解目標','規劃與選擇能力','執行','驗證與必要時重規劃']
    return {
      'schema_version':'0.3.0','card_type':'agent','id':slug(x['intent']['name']),'name':x['intent']['name'],'description':objective,'language':'zh-TW',
      'metadata':{'version':'1.0.0','tags':['visual-card','vad','promptless-agent']},
      'goal':{'objective':objective,'success_definition':success,'stop_conditions':['達成成功定義','人工要求停止']},
      'role':{'responsibility':f.get('role') or '依目標規劃、調度能力、執行與驗證。','boundaries':f.get('governance') or ['遵守平台安全與人工核准規則']},
      'skills':[{'id':s,'required':False} for s in f.get('skills',[])],
      'tools':[{'id':t,'purpose':'由卡片抽取','write_capable':bool(sig.get('external_side_effects')),'approval_required':bool(sig.get('human_approval_required'))} for t in f.get('tools',[])],
      'knowledge':[{'id':k,'type':'other'} for k in f.get('knowledge',[])],
      'workflow':[{'id':f'step-{i+1}','name':v[:40],'action':v,'on_failure':'replan' if sig.get('replanning') else 'human_review'} for i,v in enumerate(workflow)],
      'decision':{'autonomy_level':max(3,3+int(bool(sig.get('delegation') or sig.get('multi_agent')))),'rules':[{'when':d,'then':'依規則選擇下一步或請求人工作業','requires_human':bool(sig.get('human_approval_required'))} for d in (f.get('decisions') or ['依中間結果決定下一步'])],'replanning_allowed':bool(sig.get('replanning')),'max_replans':3 if sig.get('replanning') else 0},
      'sub_agents':[{'id':a,'purpose':'由卡片抽取'} for a in f.get('sub_agents',[])],
      'interoperability':{'mcp':[v for v in f.get('interoperability',[]) if 'mcp' in v.lower()],'a2a':[v for v in f.get('interoperability',[]) if 'a2a' in v.lower()]},
      'qa_governance':{'checks':[{'id':f'qa-{i+1}','criterion':v,'severity':'blocker','method':'human' if '人工' in v else 'model'} for i,v in enumerate(f.get('qa') or ['目標達成','結果可追溯'])],'human_review':(f.get('governance') or ['高影響決策']) if sig.get('human_approval_required') else [],'audit':True,'data_rules':f.get('governance',[]),'failure_policy':'human_review'}
    }

def normalize(x):
    validate_extraction(x)
    candidate=x['intent']['candidate_type']; sig=x.get('signals',{})
    agent_signal= any(sig.get(k) for k in ['dynamic_branching','dynamic_tool_selection','replanning','persistent_state','delegation','multi_agent'])
    if candidate=='agent' or agent_signal: return build_agent(x)
    return build_skill(x)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('command',choices=['validate-extraction','normalize','pipeline'])
    ap.add_argument('extraction',type=Path)
    ap.add_argument('--out',type=Path)
    ap.add_argument('--card-out',type=Path)
    ap.add_argument('--md-out',type=Path)
    args=ap.parse_args(); x=load(args.extraction); validate_extraction(x)
    if args.command=='validate-extraction': print('VALID_EXTRACTION'); return
    card=normalize(x); promptless_card.validate(card)
    if args.command=='normalize':
        if args.out: dump(card,args.out); print(args.out)
        else: print(json.dumps(card,ensure_ascii=False,indent=2))
        return
    target = card['card_type']
    if target=='skill':
        cls,reasons=promptless_card.classify_skill(card)
        md=promptless_card.compile_skill(card)
    else: md=promptless_card.compile_agent(card)
    if args.card_out: dump(card,args.card_out)
    if args.md_out: args.md_out.write_text(md,encoding='utf-8')
    print(json.dumps({'card_type':target,'confidence':x['confidence'],'uncertainties':len(x['uncertainties']),'card_out':str(args.card_out) if args.card_out else None,'md_out':str(args.md_out) if args.md_out else None},ensure_ascii=False))
if __name__=='__main__': main()
