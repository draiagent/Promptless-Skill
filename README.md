# Promptless Skill × VAD｜無提示詞技能與視覺代理設計方法論

> **讓使用 AI 不再以「先學會寫 Prompt」為前提，並把 Skill 進一步升級為可設計、可治理、可協作的 Agent。**

**版本：0.3.1**  
**語言：繁體中文（zh-TW）**  
**定位：開源教學／企業導入／AI Skill／Agent／VAD 方法論**

---

## v0.3.1｜圖片資訊卡直接進入機器流程

```text
圖片資訊卡 → Vision Extraction JSON → Schema 驗證 → Card 正規化 → Skill / Agent → 編譯輸出
```

- 視覺抽取規格：`schemas/visual-card-extraction.schema.json`
- 跨模型抽取器：`adapters/visual-card-extractor.md`
- Parser：`tools/visual_card_parser.py`
- 詳細說明：`docs/16-visual-card-parser.md`

> 圖片不是直接執行碼。先抽取、保留信心與不確定性，再進入可驗證規格。

## 核心關係

> **Promptless Skill 封裝能力；Promptless Agent 調度能力；VAD 描述與治理代理藍圖。**

> **Skill 是能力，Agent 是大腦，VAD 是藍圖。**

Promptless = **Zero Prompting for End Users**。底層仍可包含 Prompt、Context、Rules、Knowledge、Workflow、Tools、MCP、Agent、Evaluation 與 QA；差別是終端使用者不需要每次從零撰寫完整提示詞。

## Skill 六欄

`TASK | INPUT | STYLE | PROCESS | OUTPUT | QA`

## VAD Agent 十欄

`GOAL | ROLE | SKILLS | TOOLS | KNOWLEDGE | WORKFLOW | DECISION | SUB-AGENTS | MCP/A2A | QA/GOVERNANCE`

## v0.3.0 Machine-readable Card

`Card JSON → Schema Validate → Skill-or-Agent Classifier → SKILL.md / VAD Agent`

核心原則：**多步驟不等於 Agent；只有需要動態決策、選工具、重新規劃、持續狀態或委派時才升級 Agent。**

## v0.3.1 Visual Card Parser

```text
Visual Card Image
  ↓ Vision Extraction
Extraction JSON + confidence + uncertainties
  ↓ Schema Validation
Normalizer
  ↓
Skill Card / VAD Agent Card
  ↓
Compiler
```

使用中介 Extraction JSON，把「看懂圖片」與「建立可執行規格」分離，讓錯誤可追蹤、模型可比較、結果可驗證。

## 主要檔案

- `SKILL.md`：核心可召喚方法論
- `schemas/visual-skill-card.schema.json`
- `schemas/vad-agent-card.schema.json`
- `schemas/visual-card-extraction.schema.json`
- `tools/promptless_card.py`
- `tools/visual_card_parser.py`
- `adapters/visual-card-extractor.md`
- `docs/16-visual-card-parser.md`
- `.github/workflows/schema-validation.yml`

## 跨模型

- ChatGPT / Codex：`SKILL.md`、`AGENTS.md`、`CHATGPT.md`
- Claude Code：`CLAUDE.md`、`.claude/agents/`
- Gemini CLI：`GEMINI.md`、`.gemini/agents/`

## 召喚方式

- 「使用 Promptless Skill 完成這個任務。」
- 「依照這張資訊卡執行，不要叫我重寫 Prompt。」
- 「把這張資訊卡轉成可機器讀取 Skill。」
- 「把這個 Skill 升級成 Agent。」
- 「用 VAD 設計這個 Agent。」

## 核心口號

> **不要要求每個人先學會寫提示詞，把專業知識封裝成人人都能使用的技能。**

> **從 Prompt-first，走向 Skill-first，再走向 Agent-first。**

## 授權

MIT License。
