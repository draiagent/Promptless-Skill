import json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
import visual_card_parser as v
import promptless_card as p

def load(name): return json.loads((ROOT/'examples/visual-parser'/name).read_text(encoding='utf-8'))

def test_skill_visual_extraction_normalizes_to_skill():
    card=v.normalize(load('skill-card.extraction.json'))
    assert card['card_type']=='skill'
    p.validate(card)
    target,reasons=p.classify_skill(card)
    assert target=='skill'

def test_agent_visual_extraction_normalizes_to_agent():
    card=v.normalize(load('agent-card.extraction.json'))
    assert card['card_type']=='agent'
    p.validate(card)
    assert card['decision']['replanning_allowed'] is True
    assert len(card['interoperability']['a2a']) >= 1

def test_extraction_schema():
    for n in ['skill-card.extraction.json','agent-card.extraction.json']:
        v.validate_extraction(load(n))

def test_chinese_title_gets_stable_non_generic_id():
    a=v.normalize(load('skill-card.extraction.json'))
    b=v.normalize(load('skill-card.extraction.json'))
    assert a['id']==b['id']
    assert a['id'].startswith('card-')
