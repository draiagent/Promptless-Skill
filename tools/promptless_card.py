#!/usr/bin/env python3
"""Promptless Skill v0.3.0 Card validator / classifier / compiler.

用法：
  python tools/promptless_card.py validate card.json
  python tools/promptless_card.py classify card.json
  python tools/promptless_card.py compile card.json --out generated.md
"""
from __future__ import annotations
import argparse, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SCHEMAS=ROOT/'schemas'

def load_json(p: Path):
    return json.loads(p.read_text(encoding='utf-8'))

def schema_for(card):
    t=card.get('card_type')
    if t=='skill': return SCHEMAS/'visual-skill-card.schema.json'
    if t=='agent': return SCHEMAS/'vad-agent-card.schema.json'
    raise ValueError("card_type 必須為 skill 或 agent")

def validate(card):
    try:
        import jsonschema
    except ImportError:
        raise RuntimeError('請先安裝 jsonschema：pip install jsonschema>=4.22')
    schema=load_json(schema_for(card))
    jsonschema.Draft202012Validator.check_schema(schema)
    validator=jsonschema.Draft202012Validator(schema)
    errors=sorted(validator.iter_errors(card), key=lambda e:list(e.absolute_path))
    if errors:
        lines=[]
        for e in errors:
            path='.'.join(map(str,e.absolute_path)) or '<root>'
            lines.append(f'{path}: {e.message}')
        raise ValueError('\n'.join(lines))

def classify_skill(card):
    ex=card['execution']; reasons=[]
    tests=[('autonomy_level>=3',ex['autonomy_level']>=3),('dynamic_branching',ex['dynamic_branching']),('dynamic_tool_selection',ex['dynamic_tool_selection']),('replanning',ex['replanning']),('persistent_state',ex['persistent_state']),('delegation',ex['delegation']),('multi_agent',ex['multi_agent'])]
    reasons.extend(k for k,v in tests if v)
    reasons.extend(card.get('upgrade_policy',{}).get('forced_reasons',[]))
    if ex.get('external_side_effects') and (ex.get('dynamic_branching') or ex.get('dynamic_tool_selection') or ex.get('replanning')):
        reasons.append('dynamic_external_side_effects')
    reasons=list(dict.fromkeys(reasons))
    return ('agent' if reasons and card['upgrade_policy']['allow_agent_upgrade'] else 'skill', reasons)

def compile_skill(card):
    target,reasons=classify_skill(card)
    if target=='agent':
        return '# 建議升級為 Promptless Agent\n\n偵測原因：\n'+''.join(f'- {r}\n' for r in reasons)+'\n請依 `schemas/vad-agent-card.schema.json` 建立 VAD Agent Card。\n'
    inputs='\n'.join(f"- {x['name']} ({x['type']})：{'必填' if x['required'] else '選填'}" for x in card['input'])
    proc='\n'.join(f"{i+1}. {x.get('name',x['id'])}：{x['action']}" for i,x in enumerate(card['process']))
    checks='\n'.join(f"- [{x['severity']}] {x['criterion']}" for x in card['qa']['checks'])
    return f"---\nname: {card['id']}\ndescription: {card.get('description',card['name'])}\n---\n\n# {card['name']}\n\n## TASK\n{card['task']['objective']}\n\n成功定義：{card['task']['success_definition']}\n\n## INPUT\n{inputs}\n\n## PROCESS\n{proc}\n\n## OUTPUT\n"+'\n'.join(f"- {a['name']}：{a['type']} / {a.get('format','unspecified')}" for a in card['output']['artifacts'])+f"\n\n## QA\n{checks}\n"

def compile_agent(card):
    return f"# {card['name']}\n\n## GOAL\n{card['goal']['objective']}\n\n成功定義：{card['goal']['success_definition']}\n\n## ROLE\n{card['role']['responsibility']}\n\n## SKILLS\n"+'\n'.join(f"- {s['id']}" for s in card['skills'])+"\n\n## TOOLS\n"+'\n'.join(f"- {t['id']}：{t.get('purpose','')}" for t in card['tools'])+"\n\n## WORKFLOW\n"+'\n'.join(f"{i+1}. {s['action']}" for i,s in enumerate(card['workflow']))+f"\n\n## DECISION\nAutonomy Level: {card['decision']['autonomy_level']}\nReplanning: {card['decision']['replanning_allowed']}\n\n## QA / GOVERNANCE\nAudit: {card['qa_governance']['audit']}\nFailure policy: {card['qa_governance']['failure_policy']}\n"

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('command',choices=['validate','classify','compile']); ap.add_argument('card',type=Path); ap.add_argument('--out',type=Path); args=ap.parse_args()
    card=load_json(args.card); validate(card)
    if args.command=='validate': print('VALID'); return
    if args.command=='classify':
        if card['card_type']=='agent': print(json.dumps({'target':'agent','reasons':['already_agent']},ensure_ascii=False)); return
        target,reasons=classify_skill(card); print(json.dumps({'target':target,'reasons':reasons},ensure_ascii=False)); return
    text=compile_skill(card) if card['card_type']=='skill' else compile_agent(card)
    if args.out: args.out.write_text(text,encoding='utf-8'); print(args.out)
    else: print(text)
if __name__=='__main__': main()
