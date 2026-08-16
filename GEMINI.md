# GEMINI.md｜Gemini CLI 專案入口

本 Repository 僅維護 **VAD-Promptless**。

## Local Promptless Sources

@./skills/vad-promptless/SKILL.md
@./skills/vad-promptless/docs/07-promptless-agent-methodology.md
@./skills/vad-promptless/agents/vad-promptless-agent.md
@./skills/vad-promptless/docs/11-governance.md

Gemini Agent：`.gemini/agents/vad-promptless-agent.md`。

## Behavior

- 先利用現有圖片、附件、上下文與規則。
- 固定任務維持 Skill / Workflow。
- 需要依觀察結果動態改變執行路徑時才升級 Agent。
- 圖卡先結構化與驗證，再進入執行。
- Human / Machine Layer 衝突時不得靜默猜測。

## Visual Agent Design Core

完整 VAD 上游：

https://github.com/draiagent/Visual-Agent-Design

TRC-3D、VAC-8、Standard VAC、Agent Blueprint、VAD Research 與 Core Governance 以上游為準。

本 Repo 不再提供第二份 `visual-agent-design/`。

整合順序：

```text
VAD Core
→ VAC / Spec
→ Promptless Bridge
→ Self-Describing Card
→ Gemini Skill / Workflow / Agent
```
