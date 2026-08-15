#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path
from PIL import Image,PngImagePlugin
import self_describing_card as sdc
key='vad-promptless'
def embed(image_path,card_path,out_path):
 card=sdc.load(card_path); sdc.validate_envelope(card); im=Image.open(image_path).convert('RGBA'); meta=PngImagePlugin.PngInfo()
 for k,v in getattr(im,'info',{}).items():
  if isinstance(v,str) and k!=key: meta.add_itxt(k,v)
 meta.add_itxt(key,json.dumps(card,ensure_ascii=False,separators=(',',':'))); im.save(out_path,'PNG',pnginfo=meta)
def extract(image_path,out_path):
 raw=Image.open(image_path).info.get(key)
 if not raw: raise ValueError(f'png 缺少 metadata key: {key}')
 card=json.loads(raw); sdc.validate_envelope(card); sdc.dump(card,out_path)
def main():
 ap=argparse.ArgumentParser(); sub=ap.add_subparsers(dest='command',required=True); e=sub.add_parser('embed'); e.add_argument('image',type=Path); e.add_argument('card',type=Path); e.add_argument('--out',type=Path,required=True); x=sub.add_parser('extract'); x.add_argument('image',type=Path); x.add_argument('--out',type=Path,required=True); a=ap.parse_args(); embed(a.image,a.card,a.out) if a.command=='embed' else extract(a.image,a.out); print(a.out)
if __name__=='__main__': main()
