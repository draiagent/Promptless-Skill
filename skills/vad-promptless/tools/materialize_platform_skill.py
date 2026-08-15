#!/usr/bin/env python3
from __future__ import annotations
import argparse,shutil
from pathlib import Path
root=Path(__file__).resolve().parents[1]
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--out',type=Path,required=True); a=ap.parse_args(); out=a.out
 if out.exists(): shutil.rmtree(out)
 out.mkdir(parents=True); shutil.copy2(root/'SKILL.md',out/'SKILL.md')
 for n in ['docs','schemas','adapters','templates','examples','tools','agents']:
  if (root/n).exists(): shutil.copytree(root/n,out/n,ignore=shutil.ignore_patterns('__pycache__','.pytest_cache'))
 print(out)
if __name__=='__main__': main()
