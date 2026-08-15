---
name: promptless-skill
description: 將使用者的任務、素材、資訊卡或既有工作流程轉換成「終端使用者不必撰寫長提示詞」的可重複 Skill，並在需要自主規劃、動態工具選擇、重新規劃、持續狀態、MCP、Sub-Agent 或 A2A 時升級為 Promptless Agent；使用 VAD 描述 GOAL、ROLE、SKILLS、TOOLS、KNOWLEDGE、WORKFLOW、DECISION、SUB-AGENTS、MCP/A2A 與 QA/GOVERNANCE。當使用者說「使用 Promptless Skill」「不要叫我寫 Prompt」「依照資訊卡執行」「把流程封裝成 Skill」「把 Skill 升級成 Agent」「用 VAD 設計 Agent」或任務明顯可重複、可標準化、可代理化時使用。
---

# Promptless Skill｜無提示詞技能方法論

**規格版本：0.3.0**

## 0. 核心定義

**Promptless ≠ 系統內完全沒有 Prompt。**

> **Promptless = Zero Prompting for End Users**

底層可以包含 Prompt、Context、Rules、Knowledge、Workflow、Tools、MCP、Agent、Evaluation 與 QA；終端使用者不必每次從零撰寫。

> **Promptless Skill 封裝能力；Promptless Agent 調度能力；VAD 描述與治理代理藍圖。**

> **Skill 是能力，Agent 是大腦，VAD 是藍圖。**

---

## 1. 啟用後的基本行為

1. 先理解使用者的 Job-to-be-Done，不先教 Prompt 格式。
2. 現有對話、圖片、附件、範例或規則足夠時直接開始，不要求重寫同一需求。
3. 自動將任務正規化成 Skill 六欄。
4. 可重複工作優先設計成可版本化 Skill，而不是一次性 Prompt。
5. 若輸入包含 Visual Skill Card / VAD Agent Card 或 JSON，優先正規化成 `schemas/` 的 Machine-readable Card 並驗證。
6. 若需要中途判斷、動態工具選擇、重新規劃、持續狀態、委派或多代理協作，依 `docs/15-agent-upgrade-decision.md` 判斷是否升級 Agent。
7. 進入 Agent 層必須套用 VAD 十欄，而不是只把 Prompt 寫長。
8. 優先使用平台原生 Skills、Tools、Connectors、MCP、Sub-Agent 能力。
9. 重要或高風險決策保留 Human Review、安全與權限限制。
10. 完成前執行 QA / Evaluation，不以「模型已回答」視為任務完成。

---

## 2. Skill 六欄

- **TASK**：真正要完成什麼、成功終點是什麼。
- **INPUT**：文字、圖片、PDF、試算表、網址、Logo、資料庫、API、範例等；區分必要與可推定輸入。
- **STYLE**：語言、品牌、語氣、視覺、格式、合規限制。
- **PROCESS**：理解 → 分析 → 組織 → 執行 → 驗證 → 修正。
- **OUTPUT**：交付成果、格式、數量、比例、欄位與儲存位置。
- **QA**：正確性、完整性、來源、格式、錯字、品牌一致性與完成條件。

必要時增加：`CONTEXT | KNOWLEDGE | RULES | TOOLS | FAILURE CONDITIONS | HUMAN REVIEW`

---

## 3. 選擇最低足夠層級

### Skill
目標、步驟、工具固定，不需要依中間結果改變主要路徑。

### Workflow
多個 Skill 有固定先後順序，決策點少。

### Agent
主要分界是**動態決策**，例如：依中間結果改路徑、動態選 Skill / Tool / Knowledge、重新規劃、跨任務持續狀態或需要委派。

### Multi-Agent
專業角色明顯不同、可平行執行、需要 A2A、或單一 Agent 的上下文／權限過大。

> **多步驟 ≠ Agent。不要為了名稱過度 Agent 化。**

---

## 4. VAD Agent 十欄

`GOAL | ROLE | SKILLS | TOOLS | KNOWLEDGE | WORKFLOW | DECISION | SUB-AGENTS | MCP/A2A | QA/GOVERNANCE`

- **GOAL**：最終目標與完成條件。
- **ROLE**：責任、邊界、不應做的事。
- **SKILLS**：可調度的 Promptless Skills。
- **TOOLS**：搜尋、程式、文件、資料庫、API、Connector。
- **KNOWLEDGE**：RAG、企業知識庫、規範、記憶與更新規則。
- **WORKFLOW**：預設路徑、平行步驟、迴圈與停止條件。
- **DECISION**：自主節點、人工節點、失敗與降級規則。
- **SUB-AGENTS**：委派角色與輸入輸出契約。
- **MCP / A2A**：外部工具與代理協作。
- **QA / GOVERNANCE**：驗收、Evaluation、來源、權限、稽核、隱私、風險與 Human Review。

---

## 5. 執行生命週期

```text
INTENT → NORMALIZE → SELECT LEVEL → PLAN → EXECUTE → OBSERVE → DECIDE/REPLAN → QA/EVALUATE → HUMAN REVIEW → DELIVER → LEARN/VERSION
```

原則：從現有素材辨識目標；選擇最低足夠自主性；使用平台原生工具完成真實工作；依中間結果觀察與重新規劃；交付前逐項驗證成功條件；值得重用的改進納入下一版本。

---

## 6. Visual Skill Card

資訊卡是 Skill 的視覺介面，不是裝飾：

`TASK | INPUT | STYLE | PROCESS | OUTPUT | QA`

要求：人可快速看懂、AI 可映射成 Schema、不依賴大量隱含條件、可版本化、可升級 Workflow / Agent。

---

## 7. VAD Agent Card

Agent Card 使用：

`GOAL | ROLE | SKILLS | TOOLS | KNOWLEDGE | WORKFLOW | DECISION | SUB-AGENTS | MCP/A2A | QA/GOVERNANCE`

必須能回答：Agent 為誰負責、能做什麼、不能做什麼、會用哪些能力、哪裡自主決定、哪裡要人確認、失敗時如何停止／降級／求助。

---

## 8. 建立新 Promptless Skill

1. 擷取 Job-to-be-Done。
2. 建立六欄。
3. 分離不可變規則與每次輸入。
4. 把重複 Prompt 移入 Skill。
5. 詳細參考拆入 `docs/`、`templates/`、`examples/`。
6. `description` 寫清楚做什麼與何時觸發。
7. 定義 Output、QA、失敗條件與 Human Review。
8. 若需要自主決策，依第 9 節升級 Agent。
9. 版本化並建立 CHANGELOG。

---

## 9. Skill → Promptless Agent

1. 先確認真的需要自主性。
2. TASK 升級 GOAL；定義 ROLE 與邊界。
3. 列出 SKILLS、TOOLS / MCP、KNOWLEDGE。
4. PROCESS 轉 WORKFLOW。
5. 找出 DECISION 節點。
6. 規定 SUB-AGENT / A2A 使用條件。
7. 建立 QA / EVALUATION / GOVERNANCE。
8. 建立 VAD Agent Card 與平台原生 Agent 入口。

---

## 10. 跨模型規則

**Single Source of Truth：`SKILL.md`、`docs/`、`agents/promptless-vad-agent.md`。**

- ChatGPT / Codex → `CHATGPT.md`、`AGENTS.md`
- Claude Code → `CLAUDE.md`、`.claude/agents/`
- Gemini CLI → `GEMINI.md`、`.gemini/agents/`

核心方法論不得為不同模型複製三份後各自漂移。

---

## 11. Machine-readable Card（v0.3.0）

當任務以卡片、表單或 JSON 表達時：

1. Skill Card → `schemas/visual-skill-card.schema.json`。
2. Agent Card → `schemas/vad-agent-card.schema.json`。
3. `tools/promptless_card.py validate` 或等價邏輯執行 Schema Validation。
4. Skill Card 依 `execution` 與 `upgrade_policy` 執行 Classify。
5. 固定流程維持 Skill；動態決策才升級 Agent。
6. Compiler 產生平台中立規格，再由 Platform Adapter 對應 ChatGPT / Codex / Claude / Gemini。

參考分類器的 Agent 升級訊號：`autonomy_level>=3`、`dynamic_branching`、`dynamic_tool_selection`、`replanning`、`persistent_state`、`delegation`、`multi_agent`。

---

## 12. 完成檢查

- [ ] 使用者沒有被迫重寫已有需求。
- [ ] TASK / GOAL 明確。
- [ ] INPUT / KNOWLEDGE 正確。
- [ ] 已選最低足夠 Skill / Workflow / Agent 層級。
- [ ] 若為 Agent，VAD 十欄已定義。
- [ ] Tool / MCP / Sub-Agent 權限合理。
- [ ] QA / Evaluation 已通過。
- [ ] 高風險節點已 Human Review。
- [ ] 輸出可直接使用。
- [ ] 可重用改進已可版本化。
