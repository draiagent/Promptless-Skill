# Promptless Skill × VAD｜無提示詞技能與視覺代理設計方法論

> **讓使用 AI 不再以「先學會寫 Prompt」為前提，並把 Skill 進一步升級為可設計、可治理、可協作的 Agent。**

**版本：0.3.0**  
**語言：繁體中文（zh-TW）**  
**定位：開源教學／企業導入／AI Skill／Agent／VAD 方法論**

---

## 1. 專案一句話

**Promptless Skill 封裝能力；Promptless Agent 調度能力；VAD（Visual Agent Design）把整個 Agent 系統變成可看懂、可設計、可驗證的藍圖。**

> **Skill 是能力，Agent 是大腦，VAD 是藍圖。**

---

## 2. Promptless 是什麼？

Promptless **不代表系統內完全沒有 Prompt**。

> **Promptless = Zero Prompting for End Users**

底層仍可包含 Prompt、Context、Rules、Knowledge、Workflow、Tools、MCP、Agent、Evaluation 與 QA；差別在於：**終端使用者不需要每次從零撰寫完整提示詞。**

```text
傳統：需求 → 學 Prompt → 寫 Prompt → 改 Prompt → AI → 結果
Promptless：需求 → 選 Skill／提供素材 → AI 執行 → QA → 結果
Agentic Promptless：需求 → Skill → Workflow → VAD Agent → Evaluation / Human Review → Output
```

---

## 3. 兩大核心方法論

### A. Promptless Skill｜無提示詞技能方法論

解決：**AI 會什麼？一般使用者如何直接使用這項能力？**

`TASK | INPUT | STYLE | PROCESS | OUTPUT | QA`

### B. Promptless Agent × VAD｜無提示詞代理與視覺代理設計

解決：**AI 如何依目標自主規劃、選 Skill、用 Tool、查 Knowledge、呼叫 MCP、委派 Sub-Agent，並在必要時進行 A2A 協作？**

`GOAL | ROLE | SKILLS | TOOLS | KNOWLEDGE | WORKFLOW | DECISION | SUB-AGENTS | MCP/A2A | QA/GOVERNANCE`

---

## 4. 為什麼不是「做一個小 Agent」？

完整 Promptless Agent 應具備：目標與角色邊界、Skills、Tools / Connectors / MCP、Knowledge / Memory / RAG、決策、Sub-Agent / A2A、QA / Evaluation / Human Review、版本化與 VAD 視覺藍圖。

> **固定流程不要為了名稱硬做成 Agent。多步驟 ≠ Agent；動態決策才是主要分界。**

---

## 5. Repository 結構

```text
Promptless-Skill/
├── README.md / SKILL.md / AGENTS.md
├── CHATGPT.md / CLAUDE.md / GEMINI.md
├── agents/
├── .claude/agents/
├── .gemini/agents/
├── docs/01-methodology.md ... 15-agent-upgrade-decision.md
├── schemas/
│   ├── visual-skill-card.schema.json
│   ├── vad-agent-card.schema.json
│   └── promptless-card.schema.json
├── tools/
│   ├── promptless_card.py
│   └── requirements.txt
├── tests/test_cards.py
├── .github/workflows/schema-validation.yml
├── templates/
└── examples/
    └── machine-readable/
```

---

## 6. 如何召喚

- 「使用 Promptless Skill 完成這個任務。」
- 「依照這張資訊卡執行，不要叫我重寫 Prompt。」
- 「把這個流程封裝成 Promptless Skill。」
- 「把這個 Skill 升級成 Agent。」
- 「用 VAD 設計這個 Agent。」
- 「建立 Promptless Agent，讓它自己選 Skill、Tool 與 MCP。」

平台若支援技能自動發現，可在符合 `SKILL.md` 描述時自動啟用。

---

## 7. 跨模型策略

**Single Source of Truth：`SKILL.md` + `docs/` + `agents/promptless-vad-agent.md`**

- **ChatGPT / Codex**：`SKILL.md`、`AGENTS.md`、`CHATGPT.md`
- **Claude Code**：`CLAUDE.md`、`.claude/agents/promptless-vad-agent.md`
- **Gemini CLI**：`GEMINI.md`、`.gemini/agents/promptless-vad-agent.md`

---

## 8. 教學路徑

1. **USE**：選 Skill → 放資料 → 得結果
2. **COMPOSE**：Skill + Skill → Workflow
3. **ORCHESTRATE**：Agent 調度 Skill / Tool / Knowledge / MCP
4. **COLLABORATE**：Sub-Agent / Multi-Agent / A2A
5. **DESIGN & GOVERN**：VAD + Evaluation + Human Review + Governance

---

## 9. Visual Skill Card 與 VAD Agent Card

**Visual Skill Card** 面向能力：`TASK | INPUT | STYLE | PROCESS | OUTPUT | QA`

**VAD Agent Card** 面向代理：`GOAL | ROLE | SKILLS | TOOLS | KNOWLEDGE | WORKFLOW | DECISION | SUB-AGENTS | MCP/A2A | QA/GOVERNANCE`

兩張卡不是單純圖卡，而是**可視化的人機任務規格介面**。

---

## 10. Machine-readable Card（v0.3.0）

v0.3.0 新增可被程式驗證、分類與轉換的 Schema：

- `schemas/visual-skill-card.schema.json`
- `schemas/vad-agent-card.schema.json`
- `schemas/promptless-card.schema.json`
- `tools/promptless_card.py`
- `.github/workflows/schema-validation.yml`

```text
一張資訊卡 / VAD Card
        ↓
Machine-readable JSON
        ↓
Schema Validate
        ↓
Skill-or-Agent Classifier
     ┌──┴──┐
     ↓     ↓
   Skill  Agent
     ↓     ↓
SKILL.md  VAD Agent
        ↓
Platform Adapter
ChatGPT / Codex / Claude / Gemini
```

### 參考指令

```bash
pip install -r tools/requirements.txt
python tools/promptless_card.py validate examples/machine-readable/visual-skill-card.example.json
python tools/promptless_card.py classify examples/machine-readable/skill-to-agent-upgrade.example.json
python tools/promptless_card.py compile examples/machine-readable/visual-skill-card.example.json --out generated-skill.md
```

### Skill → Agent 升級條件

參考分類器在 `allow_agent_upgrade=true` 時，遇到下列條件會建議升級：

- `autonomy_level >= 3`
- `dynamic_branching`
- `dynamic_tool_selection`
- `replanning`
- `persistent_state`
- `delegation`
- `multi_agent`

詳見 `docs/13-machine-readable-schema.md`、`docs/14-card-to-skill-compiler.md`、`docs/15-agent-upgrade-decision.md`。

---

## 11. 研究與驗證

可比較 A：Prompt-first、B：文字 Skill-first、C：Visual Promptless Skill、D：Promptless Agent + VAD，測量任務完成率、時間、修改次數、錯誤率、成果品質、認知負荷、初學者成功率、Agent 決策與工具選擇正確率。

---

## 12. 設計原則

1. Intent First
2. Skill Before Prompt
3. Agent Only When Needed
4. VAD for Explainability
5. Progressive Disclosure
6. QA by Design
7. Human-in-the-loop
8. Platform Native
9. Single Source of Truth
10. Version Everything

---

## 13. 核心口號

> **不要要求每個人先學會寫提示詞，把專業知識封裝成人人都能使用的技能。**

> **Skill 是能力，Agent 是大腦，VAD 是藍圖。**

> **從 Prompt-first，走向 Skill-first，再走向 Agent-first。**

---

## 14. 授權

MIT License。可學習、修改、再利用與散布；請保留原授權聲明。
