# Promptless Skill × VAD｜無提示詞技能與視覺代理設計方法論

> **讓使用 AI 不再以「先學會寫 Prompt」為前提，並把 Skill 進一步升級為可設計、可治理、可協作的 Agent。**

**版本：0.2.0**  
**語言：繁體中文（zh-TW）**  
**定位：開源教學／企業導入／AI Skill／Agent／VAD 方法論**

---

## 1. 專案一句話

**Promptless Skill 封裝能力；Promptless Agent 調度能力；VAD（Visual Agent Design）把整個 Agent 系統變成可看懂、可設計、可驗證的藍圖。**

> **Skill 是能力，Agent 是大腦，VAD 是藍圖。**

---

## 2. Promptless 是什麼？

Promptless **不代表系統內完全沒有 Prompt**。

本專案的定義是：

> **Promptless = Zero Prompting for End Users**

底層仍可包含：

- Prompt
- Context
- Rules
- Knowledge
- Workflow
- Tools
- MCP
- Agent
- Evaluation
- QA

差別在於：**終端使用者不需要每次從零撰寫完整提示詞。**

傳統：

```text
需求 → 學 Prompt → 寫 Prompt → 改 Prompt → AI → 結果
```

Promptless：

```text
需求 → 選 Skill／提供素材 → AI 執行 → QA → 結果
```

Agentic Promptless：

```text
需求
  ↓
Promptless Skill
  ↓
Workflow
  ↓
VAD Agent
  ├─ Skills
  ├─ Tools
  ├─ Knowledge
  ├─ MCP
  ├─ Sub-Agents
  └─ A2A
  ↓
Evaluation / Human Review
  ↓
Output
```

---

## 3. 兩大核心方法論

### A. Promptless Skill｜無提示詞技能方法論

解決：**AI 會什麼？一般使用者如何直接使用這項能力？**

六欄核心：

| 欄位 | 目的 |
|---|---|
| TASK | 要完成什麼 |
| INPUT | 使用哪些素材與資料 |
| STYLE | 語言、品牌、格式、限制 |
| PROCESS | 如何分析與執行 |
| OUTPUT | 最後交付什麼 |
| QA | 如何判斷合格 |

### B. Promptless Agent × VAD｜無提示詞代理與視覺代理設計

解決：**AI 如何依目標自主規劃、選 Skill、用 Tool、查 Knowledge、呼叫 MCP、委派 Sub-Agent，並在必要時進行 A2A 協作？**

VAD 十欄：

| 欄位 | 目的 |
|---|---|
| GOAL | 最終目標 |
| ROLE | 角色、責任與邊界 |
| SKILLS | 可調度的技能 |
| TOOLS | 可執行工具 |
| KNOWLEDGE | 知識、記憶、RAG、規則 |
| WORKFLOW | 預設工作流程 |
| DECISION | 自主決策節點與升級規則 |
| SUB-AGENTS | 可委派的子代理 |
| MCP / A2A | 外部系統與代理協作 |
| QA / GOVERNANCE | 驗收、風險、人工審核與治理 |

---

## 4. 為什麼不是「做一個小 Agent」？

本專案把 Agent 視為**可重複召喚的任務作業系統**，而不是一段固定提示詞。

一個完整 Promptless Agent 應具備：

1. 明確目標與角色邊界。
2. 可選擇與組合的 Skills。
3. 可使用的 Tools / Connectors / MCP。
4. 可引用的 Knowledge / Memory / RAG。
5. 根據中間結果做決策的能力。
6. 可委派 Sub-Agent 的規則。
7. 必要時進行 A2A 協作。
8. QA、Evaluation、Human Review 與風險治理。
9. 可版本化、可分享、可安裝、可回溯。
10. 能以 VAD 視覺方式讓人看懂整個執行藍圖。

---

## 5. Repository 結構

```text
Promptless-Skill/
├── README.md
├── SKILL.md
├── AGENTS.md
├── CLAUDE.md
├── GEMINI.md
├── CHATGPT.md
├── CONTRIBUTING.md
├── SECURITY.md
├── CHANGELOG.md
├── CITATION.cff
├── LICENSE
├── agents/
│   └── promptless-vad-agent.md
├── .claude/
│   └── agents/
│       └── promptless-vad-agent.md
├── .gemini/
│   └── agents/
│       └── promptless-vad-agent.md
├── docs/
│   ├── 01-methodology.md
│   ├── 02-skill-vad.md
│   ├── 03-agent-vad.md
│   ├── 04-visual-skill-card.md
│   ├── 05-cross-model-install.md
│   ├── 06-official-references.md
│   ├── 07-promptless-agent-methodology.md
│   ├── 08-cross-model-agent.md
│   ├── 09-teaching-guide.md
│   ├── 10-evaluation-framework.md
│   ├── 11-governance.md
│   └── 12-roadmap.md
├── templates/
│   ├── PROMPTLESS-SKILL-TEMPLATE.md
│   ├── PROMPTLESS-AGENT-TEMPLATE.md
│   ├── VISUAL-SKILL-CARD-TEMPLATE.md
│   └── VAD-AGENT-CARD-TEMPLATE.md
└── examples/
    ├── enterprise-infographic/
    │   └── README.md
    └── enterprise-research-agent/
        └── README.md
```

---

## 6. 如何召喚

安裝後可直接說：

- 「使用 Promptless Skill 完成這個任務。」
- 「依照這張資訊卡執行，不要叫我重寫 Prompt。」
- 「把這個流程封裝成 Promptless Skill。」
- 「把這個 Skill 升級成 Agent。」
- 「用 VAD 設計這個 Agent。」
- 「建立 Promptless Agent，讓它自己選 Skill、Tool 與 MCP。」
- 「把這個部門工作轉成 Multi-Agent + A2A 架構。」

平台若支援技能自動發現，可在符合 `SKILL.md` 描述時自動啟用。

---

## 7. 跨模型策略：一份核心，多個平台入口

本專案避免為 ChatGPT、Gemini、Claude 維護三套互相漂移的方法論。

**Single Source of Truth：`SKILL.md` + `docs/` + `agents/promptless-vad-agent.md`**

平台入口只做「發現與啟用」：

- **ChatGPT / Codex**：`SKILL.md`、`AGENTS.md`、`CHATGPT.md`
- **Claude Code**：`CLAUDE.md`、`.claude/agents/promptless-vad-agent.md`
- **Gemini CLI**：`GEMINI.md`、`.gemini/agents/promptless-vad-agent.md`

詳見 `docs/05-cross-model-install.md` 與 `docs/08-cross-model-agent.md`。

---

## 8. 教學路徑

### Level 1｜USE
**不用先學 Prompt：選 Skill → 放資料 → 得結果**

### Level 2｜COMPOSE
**Skill + Skill → Workflow**

### Level 3｜ORCHESTRATE
**Agent 根據目標調度 Skill / Tool / Knowledge / MCP**

### Level 4｜COLLABORATE
**Sub-Agent / Multi-Agent / A2A**

### Level 5｜DESIGN & GOVERN
**用 VAD 設計整體架構，加入 Evaluation、Human Review、權限與治理**

---

## 9. Visual Skill Card 與 VAD Agent Card

### Visual Skill Card
面向「能力」：

```text
TASK | INPUT | STYLE | PROCESS | OUTPUT | QA
```

### VAD Agent Card
面向「代理」：

```text
GOAL | ROLE | SKILLS | TOOLS | KNOWLEDGE
WORKFLOW | DECISION | SUB-AGENTS | MCP/A2A | QA/GOVERNANCE
```

兩張卡不是單純圖卡，而是**可視化的人機任務規格介面**。

---

## 10. 研究與驗證

建議以相同任務比較：

- A：Prompt-first
- B：文字型 Skill-first
- C：Visual Promptless Skill
- D：Promptless Agent + VAD

可測量：

- 任務完成率
- 完成時間
- 修改次數
- 錯誤率
- 成果品質
- 認知負荷
- 初學者成功率
- 學習滿意度
- Agent 決策正確率
- Tool / Skill 選擇正確率
- Human Review 次數

詳見 `docs/10-evaluation-framework.md`。

---

## 11. 設計原則

1. **Intent First**：先理解使用者想完成什麼。
2. **Skill Before Prompt**：可重複工作先封裝能力。
3. **Agent Only When Needed**：固定流程不要硬做成 Agent。
4. **VAD for Explainability**：複雜代理必須可視化角色、能力、決策與工具。
5. **Progressive Disclosure**：只在需要時載入詳細規格。
6. **QA by Design**：驗收不是最後補上。
7. **Human-in-the-loop**：高風險與高影響決策保留人工節點。
8. **Platform Native**：優先使用各平台原生 Skill / Agent / Tool / MCP 能力。
9. **Single Source of Truth**：避免跨模型規格漂移。
10. **Version Everything**：Skill、Agent、VAD、資料與規則都應版本化。

---

## 12. 核心口號

> **不要要求每個人先學會寫提示詞，把專業知識封裝成人人都能使用的技能。**

> **Skill 是能力，Agent 是大腦，VAD 是藍圖。**

> **從 Prompt-first，走向 Skill-first，再走向 Agent-first。**

---

## 13. 授權

MIT License。可學習、修改、再利用與散布；請保留原授權聲明。
