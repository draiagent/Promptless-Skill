import json, sys
from pathlib import Path
from PIL import Image
root=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(root/'tools'))
import self_describing_card as sdc
import png_card_metadata as pcm

def load(p): return json.loads(p.read_text(encoding='utf-8'))

def test_wrap_verify_roundtrip(tmp_path):
    payload=load(root/'examples/machine-readable/visual-skill-card.example.json'); card=sdc.wrap(payload)
    assert sdc.validate_envelope(card); assert card['protocol']=='vad-promptless'; assert card['integrity']['payload_sha256']==sdc.sha256_payload(payload); assert sdc.uri(card).startswith('vadp://card/')

def test_png_metadata_roundtrip(tmp_path):
    payload=load(root/'examples/machine-readable/visual-skill-card.example.json'); card=sdc.wrap(payload)
    card_path=tmp_path/'card.self.json'; sdc.dump(card,card_path)
    src=tmp_path/'src.png'; Image.new('RGB',(16,16),'white').save(src)
    dst=tmp_path/'dst.png'; out=tmp_path/'out.json'; pcm.embed(src,card_path,dst); pcm.extract(dst,out)
    assert load(out)['integrity']['payload_sha256']==card['integrity']['payload_sha256']
