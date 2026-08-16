# VAD-Promptless｜Promptless UX for Visual Agent Design

> **把可重複的任務邏輯封裝起來，讓終端使用者不必每次從零撰寫 Prompt。**

**版本：0.5.0**  
**語言：繁體中文（zh-TW）**  
**定位：Visual Agent Design 的 Promptless UX／Self-Describing Visual Card／Zero-Prompt Execution 實作層**

VAD-Promptless 是 [Visual Agent Design（VAD）](https://github.com/draiagent/Visual-Agent-Design) 的 companion project。

本 Repository 專注於：

- Zero Prompting for End Users
- Promptless Skill / Workflow / Agent
- Visual Card Parsing
- Self-Describing Visual Card
- Machine-readable Card
- SHA-256 Integrity
- PNG Metadata / Sidecar JSON
- Promptless Bridge
- 跨模型啟用與實作

> **Visual-Agent-Design 是 VAD Core 的唯一 Source of Truth；VAD-Promptless 不再維護第二份 TRC-3D、VAC-8、Five-Pack、VAD Core Agent Blueprint 或研究框架。**

---

## Repository Relationship｜兩個 Repo 的責任邊界

```text
Visual-Agent-Design
VAD Core Framework
│
├── TRC-3D
├── VAC-8
├── Standard VAC Five-Pack
├── VAD Agent Blueprint
├── Routing / Execution / QA
└── Research Protocol
        ↓
        VAC / Spec / Interface
        ↓
VAD-Promptless
│
├── Promptless UX
├── Vision Extraction
├── Self-Describing Visual Card
├── PNG Metadata
├── Sidecar JSON
├── Integrity Verification
└── Zero-Prompt Execution
```

### Core VAD

官方方法論、標準與 Five-Pack：

**https://github.com/draiagent/Visual-Agent-Design**

### VAD-Promptless

本 Repo 負責把已定義的任務、Skill、VAC 或視覺卡，進一步封裝成使用者低提示或無需重複寫提示詞的互動方式。

---

## Core Definition｜核心定義

**Promptless ≠ 系統內完全沒有 Prompt。**

> **Promptless = Zero Prompting for End Users**

底層仍可包含：

```text
Prompt
+ Context
+ Rules
+ Knowledge
+ Skill
+ Workflow
+ Tools
+ Agent
+ Evaluation
+ QA
```

差異在於終端使用者不必每次重新組裝這些內容。

---

## VAD Promptless Bridge

VAD-Promptless 的核心橋接模型：

```text
VAD Core
   ↓
VAC / Task Spec / Skill Spec
   ↓
Promptless Bridge
   ↓
Self-Describing Visual Card
   ↓
Human Layer + Machine Layer + Integrity
   ↓
Promptless Execution
```

若使用者提供 VAD Visual Agent Card，VAD-Promptless 應將其視為上游任務規格，不重新發明另一套 VAC 標準。

---

## Self-Describing Visual Card

```text
Visual Card
├─ Human Layer      → 人類閱讀、教學、審查
├─ Machine Layer    → Skill / Agent JSON
├─ Integrity Layer  → SHA-256
├─ Binding Layer    → PNG metadata / sidecar JSON / URI / QR reference
└─ Sync Layer       → 人機內容不一致時的處理規則
```

核心原則：

> **VAD-Promptless 的目的不是讓 AI 猜圖，而是讓視覺卡能攜帶、連結或恢復可驗證的機器規格。**

---

## From Visual Card to Execution｜從圖片到執行

```text
圖片資訊卡
→ Vision Extraction
→ Extraction JSON
→ Normalize
→ Visual Skill Card / Agent Card
→ Self-Describing Envelope
→ SHA-256 Verify
→ Compile / Execute
```

若輸入是 VAD VAC，任務本體的標準由上游 `Visual-Agent-Design` 定義；本 Repo 負責 Promptless 轉換、綁定、驗證與執行介面。

---

## Repository Structure

```text
VAD-Promptless/
├── README.md
├── AGENTS.md
├── CHATGPT.md
├── CLAUDE.md
├── GEMINI.md
├── CHANGELOG.md
├── CITATION.cff
├── LICENSE
│
├── skills/
│   └── vad-promptless/
│       ├── SKILL.md
│       ├── agents/
│       ├── adapters/
│       ├── docs/
│       ├── examples/
│       ├── schemas/
│       ├── templates/
│       ├── tests/
│       └── tools/
│
├── .claude/
│   └── agents/
│       └── vad-promptless-agent.md
│
├── .gemini/
│   └── agents/
│       └── vad-promptless-agent.md
│
└── .github/
    └── workflows/
```

`visual-agent-design/` 已自本 Repo 移除；完整 VAD 請直接使用官方 Core Repo。

---

## Main Components

### Skill Entry

```text
skills/vad-promptless/SKILL.md
```

### Promptless Agent

```text
skills/vad-promptless/agents/vad-promptless-agent.md
```

### Visual Extraction

```text
skills/vad-promptless/adapters/visual-card-extractor.md
skills/vad-promptless/schemas/visual-card-extraction.schema.json
skills/vad-promptless/tools/visual_card_parser.py
```

### Machine-readable Cards

```text
skills/vad-promptless/schemas/visual-skill-card.schema.json
skills/vad-promptless/schemas/vad-agent-card.schema.json
skills/vad-promptless/tools/promptless_card.py
```

### Self-Describing Cards

```text
skills/vad-promptless/schemas/self-describing-visual-card.schema.json
skills/vad-promptless/tools/self_describing_card.py
skills/vad-promptless/tools/png_card_metadata.py
```

---

## Skill / Workflow / Agent Boundary

```text
固定目標 + 固定步驟 + 固定工具
→ Skill

多個固定 Skill 串接
→ Workflow

需要根據中間結果改路徑、換工具、重新規劃或委派
→ Agent
```

> **多步驟不等於 Agent；動態決策才是主要分界。**

如果需要完整 VAD 的 TRC-3D 路由、VAC-8、Agent Blueprint 或研究方法，使用：

**https://github.com/draiagent/Visual-Agent-Design**

---

## Cross-Model Entry Points

| 平台 | 本 Repo 入口 |
|---|---|
| ChatGPT / Codex | `CHATGPT.md` / `AGENTS.md` |
| Claude Code | `CLAUDE.md` / `.claude/agents/vad-promptless-agent.md` |
| Gemini CLI | `GEMINI.md` / `.gemini/agents/vad-promptless-agent.md` |
| 通用 Skill | `skills/vad-promptless/SKILL.md` |

這些入口只負責 **VAD-Promptless**。若任務要求 VAD Core，應轉向 `draiagent/Visual-Agent-Design`，而不是讀取本 Repo 的舊複本。

---

## Install

```bash
git clone https://github.com/draiagent/VAD-Promptless.git
cd VAD-Promptless
```

### Claude Code

```bash
mkdir -p ~/.claude/skills/vad-promptless
cp -R skills/vad-promptless/. ~/.claude/skills/vad-promptless/
```

### Gemini CLI

```bash
gemini skills install https://github.com/draiagent/VAD-Promptless.git --path skills/vad-promptless
```

### ChatGPT / Codex

使用根目錄 `CHATGPT.md`、`AGENTS.md` 與 `skills/vad-promptless/`。

---

## Self-Describing Card Quick Test

```bash
cd skills/vad-promptless
python tools/self_describing_card.py wrap \
  examples/machine-readable/visual-skill-card.example.json \
  --out /tmp/card.self.json

python tools/self_describing_card.py validate /tmp/card.self.json

python tools/png_card_metadata.py embed \
  card.png \
  /tmp/card.self.json \
  --out card.self.png
```

---

## Compatibility with Visual Agent Design

VAD-Promptless v0.5.0 採用以下責任模型：

```text
VAD Core standards
→ maintained upstream

Promptless implementation
→ maintained here
```

相容原則：

- 不複製 VAD Core 文件作為第二份標準。
- 不自行修改 TRC-3D / VAC-8 的正式定義。
- VAD 任務卡若進入 Promptless pipeline，保留 Card ID、版本、限制與 Acceptance Criteria。
- Human Layer 與 Machine Layer 發生重大衝突時，不靜默猜測，應 Human Review。
- 高風險或不可逆行為仍遵守平台安全、權限與確認機制。

---

## Research Scope

本 Repo 的研究焦點縮回 Promptless 本身，例如：

- Visual Card 是否降低終端使用者 Prompt 撰寫負擔？
- Self-Describing Card 是否提高跨模型一致性？
- Human-readable + Machine-readable 雙層／多層表示是否降低解析錯誤？
- Promptless UX 是否降低初學者操作時間與修改次數？
- 圖卡、少量文字與 Zero Prompting 的最佳組合為何？

完整 VAD 跨任務研究框架請參考：

**https://github.com/draiagent/Visual-Agent-Design**

---

## License

MIT License。可用於公開教學、研究、企業導入與二次開發。

---

> **VAD 定義任務與 Agent；VAD-Promptless 降低人啟動與操作它們的提示詞負擔。**
