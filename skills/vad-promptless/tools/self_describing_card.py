#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
import promptless_card
root=Path(__file__).resolve().parents[1]; schema_path=root/'schemas'/'self-describing-visual-card.schema.json'
def load(path): return json.loads(Path(path).read_text(encoding='utf-8'))
def dump(obj,path): Path(path).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def canonical(obj): return json.dumps(obj,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode('utf-8')
def sha256_payload(obj): return hashlib.sha256(canonical(obj)).hexdigest()
def validate_envelope(card):
 import jsonschema
 errors=sorted(jsonschema.Draft202012Validator(load(schema_path)).iter_errors(card),key=lambda e:list(e.absolute_path))
 if errors: raise ValueError('\n'.join(f"{'.'.join(map(str,e.absolute_path)) or '<root>'}: {e.message}" for e in errors))
 payload=card['machine_layer']['payload']; promptless_card.validate(payload)
 if card['card_kind'] not in (payload['card_type'],'auto') or card['id']!=payload['id']: raise ValueError('envelope 與 payload 不一致')
 if sha256_payload(payload)!=card['integrity']['payload_sha256']: raise ValueError('payload_sha256 驗證失敗')
 return True
def human_from_payload(p):
 if p['card_type']=='skill':
  return {'language':p.get('language','zh-TW'),'title':p['name'],'summary':p['task']['success_definition'],'sections':[{'label':'task','items':[p['task']['objective']]},{'label':'input','items':[x['name'] for x in p.get('input',[])]},{'label':'process','items':[x['action'] for x in p.get('process',[])]},{'label':'output','items':[x['name'] for x in p.get('output',{}).get('artifacts',[])]},{'label':'qa','items':[x['criterion'] for x in p.get('qa',{}).get('checks',[])]}]}
 return {'language':p.get('language','zh-TW'),'title':p['name'],'summary':p['goal']['success_definition'],'sections':[{'label':'goal','items':[p['goal']['objective']]},{'label':'role','items':[p['role']['responsibility']]},{'label':'skills','items':[x['id'] for x in p.get('skills',[])]},{'label':'tools','items':[x['id'] for x in p.get('tools',[])]},{'label':'workflow','items':[x['action'] for x in p.get('workflow',[])]}]}
def wrap(payload,mode='hybrid',reference_uri=None):
 promptless_card.validate(payload); carriers=['sidecar-json']
 if mode in ('embedded','hybrid'): carriers.append('png-metadata')
 if reference_uri: carriers.extend(['uri','qr-reference'])
 card={'protocol':'vad-promptless','spec_version':'0.4.0','id':payload['id'],'display_name':payload['name'],'card_kind':payload['card_type'],'human_layer':human_from_payload(payload),'machine_layer':{'media_type':'application/vnd.vad-promptless.card+json','encoding':'json','payload':payload},'binding':{'mode':mode,'carriers':list(dict.fromkeys(carriers)),'metadata_key':'vad-promptless'},'integrity':{'algorithm':'sha256','canonicalization':'json-sort-keys-utf8','payload_sha256':sha256_payload(payload)},'sync':{'execution_source':'machine_layer','mismatch_policy':'human_review'}}
 if reference_uri: card['binding']['reference_uri']=reference_uri
 validate_envelope(card); return card
def uri(card): validate_envelope(card); return f"vadp://card/{card['id']}?v={card['spec_version']}&sha256={card['integrity']['payload_sha256']}"
def main():
 ap=argparse.ArgumentParser(); sub=ap.add_subparsers(dest='command',required=True)
 w=sub.add_parser('wrap'); w.add_argument('payload',type=Path); w.add_argument('--out',type=Path,required=True); w.add_argument('--mode',choices=['embedded','sidecar','reference','hybrid'],default='hybrid'); w.add_argument('--reference-uri')
 v=sub.add_parser('validate'); v.add_argument('card',type=Path); x=sub.add_parser('extract'); x.add_argument('card',type=Path); x.add_argument('--out',type=Path,required=True); u=sub.add_parser('uri'); u.add_argument('card',type=Path)
 a=ap.parse_args()
 if a.command=='wrap': dump(wrap(load(a.payload),a.mode,a.reference_uri),a.out); print(a.out)
 elif a.command=='validate': validate_envelope(load(a.card)); print('valid_self_describing_card')
 elif a.command=='extract': c=load(a.card); validate_envelope(c); dump(c['machine_layer']['payload'],a.out); print(a.out)
 else: print(uri(load(a.card)))
if __name__=='__main__': main()
