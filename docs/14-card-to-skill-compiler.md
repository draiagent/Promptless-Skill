# Card → Skill / Agent Compiler

## 目的

把 Machine-readable Card 轉成可執行／可召喚的 Skill 或 VAD Agent 規格，讓「一張卡」不只代表視覺說明，而能成為跨模型的標準輸入。

## 四階段

```text
1. Parse      解析 JSON
2. Validate   依 JSON Schema 驗證
3. Classify   判斷 Skill 或 Agent
4. Compile    產生 SKILL.md / Agent 規格
```

本專案提供最小參考實作：`tools/promptless_card.py`。

```bash
pip install -r tools/requirements.txt
python tools/promptless_card.py validate examples/machine-readable/visual-skill-card.example.json
python tools/promptless_card.py classify examples/machine-readable/visual-skill-card.example.json
python tools/promptless_card.py compile examples/machine-readable/visual-skill-card.example.json --out /tmp/generated-skill.md
```

## Compiler 與平台 Adapter 分離

Compiler 只負責產生平台中立規格；ChatGPT、Codex、Claude、Gemini 的差異應由 Adapter 層處理，避免核心方法論被平台綁死。
