# GEMINI.md｜Visual Agent Design

本專案使用 **Visual Agent Design（VAD）**。

複雜任務執行前：

1. 讀取 `AGENT.md`。
2. 使用 `templates/TRC-3D.md` 完成任務診斷。
3. 需要結構化交付時使用 `templates/VAC-8.md`。
4. 若任務符合 `visual-agent-design` Agent Skill 的描述，啟用 `.agents/skills/visual-agent-design/SKILL.md`。

行為原則：

- 圖卡資訊足夠時直接解析與執行，不要求使用者重打一份長提示詞。
- 簡單任務直接完成；固定重複流程使用 Workflow；動態決策才升級 Agent。
- 重要輸出必須驗收，不以「已產生」視為「已完成」。
- 缺少 Critical 素材、涉及不可逆外部行為或高風險決策時，保留 Human Review。

> 詳細規則以 `AGENT.md` 為準。