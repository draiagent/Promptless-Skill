# Promptless Skill｜無提示詞技能方法論

> **讓使用 AI 不再以「先學會寫 Prompt」為前提。**  
> Promptless ≠ 系統裡完全沒有 Prompt；Promptless = **Zero Prompting for End Users**。

**版本：0.1.0**  
**語言：繁體中文（zh-TW）**  
**定位：開源教學／企業導入／AI Skill 與 Agent 方法論**

---

## 1. 這是什麼？

**Promptless Skill** 是一套「技能優先（Skill-first）」的 AI 學習與操作方法論。

傳統 AI 教學通常先要求使用者學習 Prompt Engineering：角色、任務、情境、限制、格式、範例、驗收條件等。Promptless Skill 的做法是把這些專業操作封裝在可重複使用的 Skill 裡，讓一般使用者只需：

**選擇 Skill → 提供資料 → 執行 → 驗證成果**

而不是：

**先學 Prompt → 寫 Prompt → 改 Prompt → 再開始工作**

---

## 2. 核心主張

### Promptless 不等於沒有 Prompt

底層仍可能存在：

- Prompt
- Context
- Rules
- Knowledge
- Workflow
- Tools
- Output Schema
- QA

只是這些內容被封裝成 Skill，終端使用者不需要每次自己撰寫。

> **Promptless = Zero Prompting for End Users**

### 從 Prompt-first 轉向 Skill-first

```text
傳統：需求 → 寫 Prompt → 修改 Prompt → AI → 結果

Promptless Skill：需求 → 選 Skill → 放資料 → AI／工具 → QA → 結果
```

---

## 3. Promptless Skill 與 VAD 的關係

Promptless Skill 解決「**AI 會什麼、使用者如何直接使用能力**」。

VAD（Visual Agent Design，視覺代理設計）解決「**Agent 如何規劃、決策、調度 Skill、Tool、MCP 與其他 Agent**」。

一句話：

> **Skill 是能力，Agent 是大腦，VAD 是藍圖。**

```text
Human Intent
    ↓
Promptless Skill
    ↓
Skill / Workflow
    ↓
VAD
    ↓
Agent
    ↓
Skills / Tools / MCP / A2A
    ↓
Output + QA
```

完整說明請見：

- `docs/02-skill-vad.md`
- `docs/03-agent-vad.md`

---

## 4. 這個 Repository 可以做什麼？

本專案同時提供四種用途：

1. **方法論**：理解 Promptless Skill、Skill-first、Agent-first 與 VAD。
2. **可安裝 Skill**：`SKILL.md` 是主要可召喚技能檔。
3. **跨模型使用**：ChatGPT、Claude、Gemini CLI 可依各自支援方式安裝／載入。
4. **教學模板**：可把任何重複任務轉換成 Promptless Skill。

---

## 5. Repository 結構

```text
Promptless-Skill/
├── README.md
├── SKILL.md
├── AGENTS.md
├── CLAUDE.md
├── GEMINI.md
├── CHANGELOG.md
├── LICENSE
├── docs/
│   ├── 01-methodology.md
│   ├── 02-skill-vad.md
│   ├── 03-agent-vad.md
│   ├── 04-visual-skill-card.md
│   └── 05-cross-model-install.md
├── templates/
│   ├── PROMPTLESS-SKILL-TEMPLATE.md
│   └── VISUAL-SKILL-CARD-TEMPLATE.md
└── examples/
    └── enterprise-infographic/
        └── README.md
```

---

## 6. 最簡單的召喚方式

安裝後，使用者可以說：

- 「使用 Promptless Skill 完成這個任務。」
- 「套用無提示詞技能方法處理這份資料。」
- 「依照這張資訊卡直接執行，不要叫我重寫 Prompt。」
- 「把這個工作流程封裝成 Promptless Skill。」
- 「把這個 Skill 升級成 Agent，並用 VAD 表示。」

如果平台支援 Skill 自動發現，也可以不寫 Skill 名稱，直接提出符合 Skill 描述的任務。

---

## 7. Promptless Skill 六欄核心規格

任何 Promptless Skill 至少應清楚定義：

| 欄位 | 功能 |
|---|---|
| TASK | 要完成什麼 |
| INPUT | 使用什麼資料 |
| STYLE | 語言、風格、品牌或限制 |
| PROCESS | AI 應如何完成 |
| OUTPUT | 最後交付什麼 |
| QA | 如何判定合格 |

當任務升級成 Agent，則加入 VAD 欄位：

**GOAL / ROLE / SKILLS / TOOLS / KNOWLEDGE / DECISION / WORKFLOW / SUB-AGENTS / QA**

---

## 8. 學習路徑

### Level 1｜USE
不用先學 Prompt：**選 Skill → 放資料 → 得結果**

### Level 2｜COMPOSE
將多個 Skill 組成 Workflow。

### Level 3｜ORCHESTRATE
讓 Agent 根據目標調度 Skill、Tool、MCP。

### Level 4｜BUILD
理解 Prompt、Context、Knowledge、RAG、Rules、Tools、Evaluation。

### Level 5｜DESIGN
使用 VAD 設計 Multi-Agent、MCP、A2A 與治理機制。

---

## 9. 跨模型定位

本專案以 `SKILL.md` 為主要規格來源，平台入口檔只負責告訴模型優先讀取核心 Skill 與方法論文件，避免多套規格互相漂移。

- **ChatGPT**：使用支援 Skills 的工作區／產品時，可上傳 Skill 套件。
- **Claude / Claude Code**：支援自訂 Agent Skills；Claude Code 可從 Skill 目錄自動發現。
- **Gemini CLI**：支援 Agent Skills，亦可從 Git Repository 安裝 Skill。

詳細安裝步驟見 `docs/05-cross-model-install.md`。

---

## 10. 設計原則

1. **User Intent First**：先理解使用者要完成什麼，不先要求他學 Prompt。
2. **Skill Before Prompt**：可重複工作先封裝成 Skill。
3. **Progressive Disclosure**：核心 Skill 保持精簡，詳細知識放 docs／templates／examples。
4. **Human-in-the-loop**：涉及重要決策時仍保留人的確認與判斷。
5. **QA by Design**：品質驗收是 Skill 的一部分，不是最後才補。
6. **Platform Native**：能使用平台原生 Tool／Skill／Agent 就不重造一套。
7. **VAD for Agentic Tasks**：任務需要自主決策與多步驟協作時，升級為 VAD Agent 設計。

---

## 11. 適合的應用

- 企業簡報
- 資訊圖卡
- 市場研究
- 數據分析
- 會議紀錄
- 報告撰寫
- 品牌內容
- 短影音腳本
- SOP
- 教學設計
- 知識庫整理
- Agent 工作流

---

## 12. 核心口號

> **不要要求每個人先學會寫提示詞，把專業知識封裝成人人都能使用的技能。**

> **一技即用，一卡即執行。**

> **Skill 是能力，Agent 是大腦，VAD 是藍圖。**

---

## 13. 官方技術參考

請見 `docs/06-official-references.md`。

---

## 14. 授權

本專案採 MIT License。你可以學習、修改、再利用與散布，但請保留原授權聲明。
