# Visual Agent Design（VAD）｜視覺代理設計

> **先判斷任務，再選擇 AI，最後把工作畫給 Agent 看。**

**版本：1.1.0**  
**語言：繁體中文（zh-TW）**  
**定位：公開教學／跨模型 Agent／企業 AI 導入／Visual Task Interface／研究方法論**

Visual Agent Design（VAD）不是單一提示詞、單一 Skill，也不是單純的資訊圖卡。它是一套把「任務診斷、智能路由、視覺任務規格、Agent 執行、成果驗收、知識回存」整合在一起的人機協作方法論。

## v1.1.0｜Standard VAC Five-Pack

本版本加入第一組可直接重用的五張標準執行型 Visual Agent Cards：

| Card ID | 任務 | Human-readable | Machine-readable |
|---|---|---|---|
| `VAC-VIDEO-001` | 影片剪輯 | `examples/video-editing-vac.md` | `examples/machine-readable/vac-video-001.json` |
| `VAC-SLIDE-001` | 簡報製作 | `examples/slide-deck-vac.md` | `examples/machine-readable/vac-slide-001.json` |
| `VAC-WEB-001` | 網站生成 | `examples/website-vac.md` | `examples/machine-readable/vac-web-001.json` |
| `VAC-DATA-001` | 數據分析 | `examples/data-analysis-vac.md` | `examples/machine-readable/vac-data-001.json` |
| `VAC-REPORT-001` | 報告製作 | `examples/report-vac.md` | `examples/machine-readable/vac-report-001.json` |

標準卡索引：`CARD-REGISTRY.md`  
機器索引：`examples/cards-manifest.json`

Agent 收到上述五類任務時，應優先重用既有標準卡，而不是從零重建流程。

## 核心架構

```text
任務需求
  ↓
TRC-3D 任務三維路由
  ↓
CARD-REGISTRY 標準任務卡匹配
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
├── CARD-REGISTRY.md            # 標準 VAC 任務卡註冊表
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
├── tools/
│   └── vac_runner.py           # 路由、驗證、Plan、Execution Envelope
├── tests/
│   └── test_vac_five_pack.py
└── examples/
    ├── README.md
    ├── cards-manifest.json
    ├── video-editing-vac.md
    ├── slide-deck-vac.md
    ├── website-vac.md
    ├── data-analysis-vac.md
    ├── report-vac.md
    └── machine-readable/
        ├── vac-video-001.json
        ├── vac-slide-001.json
        ├── vac-web-001.json
        ├── vac-data-001.json
        └── vac-report-001.json
```

## VAC Runner

`tools/vac_runner.py` 提供一個不依賴特定模型的命令列工具，負責標準卡探索、任務路由、VAC 驗證與執行計畫編譯。

```bash
cd visual-agent-design

python tools/vac_runner.py list
python tools/vac_runner.py route "把這份 Excel 分析並產出圖表"
python tools/vac_runner.py validate VAC-DATA-001
python tools/vac_runner.py plan VAC-DATA-001
python tools/vac_runner.py envelope VAC-DATA-001
```

如果環境有安裝 `jsonschema`，`validate` 會同時依 `schemas/vac-8.schema.json` 做完整 Schema 驗證；否則仍執行內建基本驗證。

## 快速使用

### OpenAI Codex

將 `visual-agent-design/` 當作工作目錄。Codex 先讀 `AGENTS.md`，再依 `CARD-REGISTRY.md` 選擇標準 VAC。需要確定性卡片路由或驗證時，可執行 `tools/vac_runner.py`。

### Gemini CLI

Gemini CLI 可使用 `.agents/skills/` 形式的 Agent Skills。進入本目錄後可讓 Gemini 掃描或安裝 `visual-agent-design` skill；需要 VAD 時要求「使用 visual-agent-design 分析這個任務」。`GEMINI.md` 會引導它先做 TRC-3D，再查標準卡 Registry。

### Claude Code

將本目錄作為專案開啟，`CLAUDE.md` 會引導 Claude 讀取 `AGENT.md`、`CARD-REGISTRY.md` 與方法論文件。若使用支援 Agent Skills 的環境，也可把 `.agents/skills/visual-agent-design/` 複製或連結至相對應的 skills 目錄。

### ChatGPT

`CHATGPT.md` 提供適合貼入 Project Instructions／自訂專案指令的短版入口。若在 Codex 專案環境中使用，優先使用 `AGENTS.md`。支援專案檔案與工具執行的環境可直接讀取機器版 VAC JSON 或執行 VAC Runner。

## 使用原則

- 簡單任務不要過度 Agent 化。
- 影片、簡報、網站、數據與報告任務先查 `CARD-REGISTRY.md`。
- 優先重用標準 VAC；只有流程、規則或驗收契約真的改變，才建立新 Card ID。
- 圖卡負責結構，文字負責精確規格。
- 不因「圖卡看起來清楚」而省略限制與驗收。
- 缺少 Critical 素材或規則時，先回報，不自行捏造。
- 高風險或不可逆外部行為保留 Human Review。
- 執行完成不等於任務完成；必須通過 Acceptance Criteria。

## CI / Regression Test

Repository 內含 `.github/workflows/vad-five-pack.yml`，會：

- 執行 Five-Pack regression tests
- 驗證 5 張 machine-readable VAC
- 執行 Schema validation
- Smoke-test 五種標準任務路由

本地測試：

```bash
cd visual-agent-design
python -m unittest discover -s tests -p 'test_*.py' -v
```

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

研究流程詳見 `research/RESEARCH-PROTOCOL.md`。

## 方法論主張

> **VAD 的目的不是讓圖卡更漂亮，而是讓任務更容易被人與 AI 共同理解、執行與驗收。**

> **一張卡，讓人看懂；同一張卡，也讓 AI 能執行與驗收。**

## 授權

本套件沿用 Repository 的 MIT License，可用於公開教學、研究、企業導入與二次開發；引用研究概念時建議標示 Visual Agent Design（VAD）與原 Repository。