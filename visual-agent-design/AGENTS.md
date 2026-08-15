# AGENTS.md｜Visual Agent Design / Codex 專案入口

本目錄使用 **Visual Agent Design（VAD）** 方法論。

必讀順序：

1. `AGENT.md`
2. `docs/METHODOLOGY.md`
3. `templates/TRC-3D.md`
4. `templates/VAC-8.md`
5. `rubrics/VAC-QI.md`
6. `research/RESEARCH-PROTOCOL.md`（只有研究任務才讀）

執行原則：

- 非簡單任務先做 TRC-3D：資訊已知程度 × 任務發生頻率 × 推理深度。
- 不過度 Agent 化：簡單任務直接做；固定重複任務優先 Workflow；需要動態決策才升級 Agent。
- 多素材、多步驟、跨工具或需驗收的任務使用 VAC-8。
- 圖卡負責結構，少量文字負責精確規格；若圖卡資訊已足夠，不要求使用者重寫提示詞。
- 執行前檢查 Critical 素材；執行後依 Acceptance Criteria 驗收。
- 不捏造缺失資料；高影響、不可逆或外部提交行為保留 Human Review。
- 建立 Agent 架構時使用 VAD 十欄：GOAL、ROLE、SKILLS、TOOLS、KNOWLEDGE、WORKFLOW、DECISION、SUB-AGENTS、MCP/A2A、QA/GOVERNANCE。

> **先診斷，再路由；先結構，再執行；最後驗收。**