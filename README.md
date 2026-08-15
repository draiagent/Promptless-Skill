# VAD-Promptless｜無提示詞技能 × 視覺代理設計

> **一張卡，讓人看懂；同一張卡，也讓 AI 直接讀懂與執行。**

**版本：0.4.0**  
**語言：繁體中文（zh-TW）**  
**定位：公開教學／企業 AI 導入／Skill-first／Agent／VAD／Self-Describing Visual Card**

## 🆕 Visual Agent Design 完整 Agent 套件

本 Repository 現在同時提供兩個層次：

1. **VAD-Promptless**：研究「Zero Prompting for End Users」，把視覺卡片封裝成可直接召喚的 Skill / Workflow / Agent。
2. **Visual Agent Design（VAD）**：更上層的完整方法論與跨模型 Agent，負責 **任務診斷 → 三維路由 → VAC-8 視覺任務卡 → Agent 執行 → 驗收 → 知識回存**。

完整 VAD Agent 套件位於：

- [`visual-agent-design/README.md`](visual-agent-design/README.md)
- [`visual-agent-design/AGENT.md`](visual-agent-design/AGENT.md)
- [`visual-agent-design/AGENTS.md`](visual-agent-design/AGENTS.md)
- [`visual-agent-design/CLAUDE.md`](visual-agent-design/CLAUDE.md)
- [`visual-agent-design/GEMINI.md`](visual-agent-design/GEMINI.md)
- [`visual-agent-design/CHATGPT.md`](visual-agent-design/CHATGPT.md)

> **Promptless 是介面策略；VAD 是任務與 Agent 設計方法論。**

## 核心概念

```text
需求 → 視覺卡片 → Skill → Workflow → Agent → VAD → Tools / MCP / A2A → QA
```

> **Promptless = Zero Prompting for End Users**

> **Skill 是能力，Agent 是大腦，VAD 是藍圖。**

## v0.4.0：Self-Describing Visual Card

```text
Visual Card
├─ Human Layer      → 人類閱讀、教學、審查
├─ Machine Layer    → Skill / Agent JSON
├─ Integrity Layer  → SHA-256
├─ Binding Layer    → PNG metadata / sidecar JSON / URI / QR reference
└─ Sync Layer       → 人機內容不一致時的處理規則
```

## 標準相容結構

```text
VAD-Promptless/
├── README.md
├── AGENTS.md
├── CLAUDE.md
├── GEMINI.md
├── CHATGPT.md
├── LICENSE
├── visual-agent-design/         # 完整 VAD Agent / 方法論
│   ├── AGENT.md
│   ├── AGENTS.md
│   ├── CLAUDE.md
│   ├── GEMINI.md
│   ├── CHATGPT.md
│   ├── .agents/skills/
│   ├── docs/
│   ├── templates/
│   ├── rubrics/
│   ├── research/
│   ├── schemas/
│   └── examples/
├── skills/
│   └── vad-promptless/
│       ├── SKILL.md
│       ├── docs/
│       ├── schemas/
│       ├── tools/
│       ├── adapters/
│       ├── templates/
│       ├── examples/
│       ├── tests/
│       └── agents/
├── .claude/agents/
├── .gemini/agents/
└── .github/workflows/
```

YAML：`name: vad-promptless`；父資料夾：`skills/vad-promptless/`；技能入口：`skills/vad-promptless/SKILL.md`。

**重要：**`SKILL.md`、`AGENTS.md`、`CLAUDE.md`、`GEMINI.md`、`README.md`、`LICENSE` 等固定／慣例入口保留標準大小寫；一般 slug、schema、agent 定義檔採小寫。

詳見 `skills/vad-promptless/docs/18-file-naming-compatibility.md`。

## 從圖片到執行

```text
圖片資訊卡 → Vision Extraction → Extraction JSON → Normalize
→ Visual Skill Card / VAD Agent Card → Self-Describing Envelope
→ SHA-256 Verify → Compile / Execute
```

## 主要規格與工具

- `skills/vad-promptless/SKILL.md`
- `skills/vad-promptless/schemas/self-describing-visual-card.schema.json`
- `skills/vad-promptless/tools/self_describing_card.py`
- `skills/vad-promptless/tools/png_card_metadata.py`
- `skills/vad-promptless/tools/visual_card_parser.py`
- `skills/vad-promptless/tools/promptless_card.py`

## Clone 與安裝

```bash
git clone https://github.com/draiagent/VAD-Promptless.git
cd VAD-Promptless
```

### 使用完整 VAD Agent

```bash
cd visual-agent-design
```

此目錄包含 OpenAI Codex、Claude Code、Gemini CLI 與一般 ChatGPT 使用入口。詳細說明見 `visual-agent-design/README.md`。

### Claude Code｜VAD-Promptless Skill

```bash
mkdir -p ~/.claude/skills/vad-promptless
cp -R skills/vad-promptless/. ~/.claude/skills/vad-promptless/
```

### Gemini CLI｜VAD-Promptless Skill

```bash
gemini skills install https://github.com/draiagent/VAD-Promptless.git --path skills/vad-promptless
```

### ChatGPT / Codex｜VAD-Promptless

將 `skills/vad-promptless/` 下載或封裝為 Skill 套件；Codex 專案層可讀取根目錄 `AGENTS.md`。

## Self-Describing Card

```bash
cd skills/vad-promptless
python tools/self_describing_card.py wrap examples/machine-readable/visual-skill-card.example.json --out /tmp/card.self.json
python tools/self_describing_card.py validate /tmp/card.self.json
python tools/png_card_metadata.py embed card.png /tmp/card.self.json --out card.self.png
```

## Skill 與 Agent 分界

固定目標、固定步驟、固定工具 → Skill / Workflow。需要 dynamic branching、dynamic tool selection、replanning、persistent state、delegation、multi-agent、MCP 或 A2A → Agent。

> **多步驟不等於 Agent；動態決策才是主要分界。**

## VAD 十欄

`GOAL | ROLE | SKILLS | TOOLS | KNOWLEDGE | WORKFLOW | DECISION | SUB-AGENTS | MCP/A2A | QA/GOVERNANCE`

## 授權

MIT License。