from pathlib import Path
import json
import re

SKILL_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = Path(__file__).resolve().parents[3]
REQUIRED_REPO=['AGENTS.md','CLAUDE.md','GEMINI.md','README.md','LICENSE','CITATION.cff','CONTRIBUTING.md','SECURITY.md','CHANGELOG.md']
LOWERCASE_FORBIDDEN_REPO=['agents.md','claude.md','gemini.md','readme.md','license','citation.cff','contributing.md','security.md','changelog.md']

def test_skill_entrypoint_uses_canonical_case():
    assert (SKILL_ROOT/'SKILL.md').is_file(); assert not (SKILL_ROOT/'skill.md').exists()

def test_project_entrypoints_use_canonical_case():
    assert not [n for n in REQUIRED_REPO if not (REPO_ROOT/n).is_file()]
    assert not [n for n in LOWERCASE_FORBIDDEN_REPO if (REPO_ROOT/n).exists()]

def test_skill_name_matches_lowercase_parent_directory():
    text=(SKILL_ROOT/'SKILL.md').read_text(encoding='utf-8'); m=re.search(r'^name:\s*([^\n]+)$',text,re.MULTILINE)
    assert m and m.group(1).strip()=='vad-promptless' and SKILL_ROOT.name=='vad-promptless'

def test_schema_ids_use_new_repository_name():
    for path in (SKILL_ROOT/'schemas').glob('*.json'):
        assert 'github.com/draiagent/VAD-Promptless/' in json.loads(path.read_text(encoding='utf-8')).get('$id','')

def test_agent_definition_filenames_remain_lowercase():
    expected=[SKILL_ROOT/'agents/vad-promptless-agent.md',REPO_ROOT/'.claude/agents/vad-promptless-agent.md',REPO_ROOT/'.gemini/agents/vad-promptless-agent.md']
    assert all(p.is_file() for p in expected)
