# Visual Agent Design（VAD）｜視覺代理設計

> **先判斷任務，再選擇 AI，最後把工作畫給 Agent 看。**

**版本：1.0.0**  
**語言：繁體中文（zh-TW）**  
**定位：公開教學／跨模型 Agent／企業 AI 導入／Visual Task Interface／研究方法論**

Visual Agent Design（VAD）不是單一提示詞、單一 Skill，也不是單純的資訊圖卡。它是一套把「任務診斷、智能路由、視覺任務規格、Agent 執行、成果驗收、知識回存」整合在一起的人機協作方法論。

## 核心架構

```text
任務需求
  ↓
TRC-3D 任務三維路由
  ↓
選擇 Prompt / Research / Monitoring / Workflow / Agent
  ↓
VAC-8 視覺任務卡
  ↓
模型 + Skill + Tool + Knowledge + MCP / A2A
  ↓
Agent 執行
  ↓
驗收 / Human Review
  ↓
案例回存與版本優化
```

## 三個核心標準

### 1. TRC-3D｜AI Task Routing Cube

用三個維度先判斷任務：

- **X：任務資訊已知程度**：未知 ↔ 已知
- **Y：任務發生頻率**：單次 ↔ 連續
- **Z：任務推理深度**：快速處理 ↔ 複雜推理

再路由到最適合的執行模式，而不是所有工作都直接升級成 Agent。

### 2. VAC-8｜Visual Agent Card

每張可執行視覺任務卡包含八區：

1. Task Goal
2. Input Assets
3. Process Flow
4. Tools & Capabilities
5. Decision Rules
6. Constraints
7. Output Specification
8. Acceptance Criteria

### 3. VAD Agent Blueprint｜Agent 十欄藍圖

用於設計 Agent 本身，而不是單一任務：

`GOAL | ROLE | SKILLS | TOOLS | KNOWLEDGE | WORKFLOW | DECISION | SUB-AGENTS | MCP/A2A | QA/GOVERNANCE`

> **TRC-3D 決定「怎麼做」；VAC-8 定義「這次任務怎麼交付」；VAD 十欄定義「Agent 本身怎麼設計」。**

## 跨模型套件結構

```text
visual-agent-design/
├── README.md
├── AGENT.md                    # 通用 VAD Agent 核心規格
├── AGENTS.md                   # OpenAI Codex 專案入口
├── CLAUDE.md                   # Claude Code 專案入口
├── GEMINI.md                   # Gemini CLI 專案入口
├── CHATGPT.md                  # ChatGPT / Project 使用入口
├── .agents/skills/
│   └── visual-agent-design/
│       └── SKILL.md            # 可按需召喚的 VAD Skill
├── docs/
│   └── METHODOLOGY.md
├── templates/
│   ├── TRC-3D.md
│   └── VAC-8.md
├── rubrics/
│   └── VAC-QI.md
├── research/
│   └── RESEARCH-PROTOCOL.md
├── schemas/
│   └── vac-8.schema.json
└── examples/
    └── video-editing-vac.md
```

## 快速使用

### OpenAI Codex

將 `visual-agent-design/` 當作工作目錄，Codex 會依專案層 `AGENTS.md` 取得入口指令；`AGENTS.md` 保持精簡，完整方法論再由它指向其他文件。

### Gemini CLI

Gemini CLI 可使用 `.agents/skills/` 形式的 Agent Skills。進入本目錄後可讓 Gemini 掃描或安裝 `visual-agent-design` skill；需要 VAD 時要求「使用 visual-agent-design 分析這個任務」。

### Claude Code

將本目錄作為專案開啟，`CLAUDE.md` 會引導 Claude 讀取 `AGENT.md` 與方法論文件。若使用支援 Agent Skills 的環境，也可把 `.agents/skills/visual-agent-design/` 複製或連結至相對應的 skills 目錄。

### ChatGPT

`CHATGPT.md` 提供適合貼入 Project Instructions／自訂專案指令的短版入口。若在 Codex 專案環境中使用，優先使用 `AGENTS.md`。

## 使用原則

- 簡單任務不要過度 Agent 化。
- 圖卡負責結構，文字負責精確規格。
- 不因「圖卡看起來清楚」而省略限制與驗收。
- 缺少 Critical 素材或規則時，先回報，不自行捏造。
- 高風險或不可逆外部行為保留 Human Review。
- 執行完成不等於任務完成；必須通過 Acceptance Criteria。

## 研究驗證

建議比較：

| 組別 | 任務介面 |
|---|---|
| A | 純文字提示詞 |
| B | 素材 + VAC |
| C | 素材 + VAC + 少量文字 |
| D | 與 VAC 等資訊量的純文字 SOP |
| E | 裝飾型圖卡 |
| F | TRC-3D + VAC + Agent |

評估任務完成率、首次通過率、修改次數、人工操作時間、初學者理解度、成果一致性、錯誤率、人機共享理解與使用滿意度。

## 方法論主張

> **VAD 的目的不是讓圖卡更漂亮，而是讓任務更容易被人與 AI 共同理解、執行與驗收。**

## 授權

本套件沿用 Repository 的 MIT License，可用於公開教學、研究、企業導入與二次開發；引用研究概念時建議標示 Visual Agent Design（VAD）與原 Repository。