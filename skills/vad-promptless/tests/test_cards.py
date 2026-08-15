import json
import importlib.util
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("promptless_card", ROOT/"tools"/"promptless_card.py")
mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)

def load(name):
    return json.loads((ROOT/"examples"/"machine-readable"/name).read_text(encoding="utf-8"))

def test_skill_stays_skill():
    card=load("visual-skill-card.example.json"); mod.validate(card)
    target,reasons=mod.classify_skill(card)
    assert target=="skill" and reasons==[]

def test_skill_upgrades_agent():
    card=load("skill-to-agent-upgrade.example.json"); mod.validate(card)
    target,reasons=mod.classify_skill(card)
    assert target=="agent"
    assert "dynamic_tool_selection" in reasons and "replanning" in reasons

def test_agent_validates():
    mod.validate(load("vad-agent-card.example.json"))
