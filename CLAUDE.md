# CLAUDE.md｜Claude Code 專案入口

本 Repository 僅維護 **VAD-Promptless** 的 Promptless 實作層。

## Required Sources

優先遵循：

- `skills/vad-promptless/SKILL.md`
- `skills/vad-promptless/docs/07-promptless-agent-methodology.md`
- `skills/vad-promptless/agents/vad-promptless-agent.md`
- `skills/vad-promptless/docs/11-governance.md`

Claude Code Agent：

` .claude/agents/vad-promptless-agent.md `

## Behavior

- 現有圖片、附件與上下文足夠時直接開始。
- 固定流程使用 Skill / Workflow。
- 只有需要中途動態決策、重新規劃或委派時升級 Agent。
- Self-Describing Card 執行前驗證 Machine Layer 與 Integrity。
- 高風險或不可逆操作保留 Human Review。

## VAD Core Upstream

Visual Agent Design Core：

https://github.com/draiagent/Visual-Agent-Design

TRC-3D、VAC-8、Five-Pack、VAD Agent Blueprint、VAD Research 等標準只以上游 Repo 為準。

本 Repo 已移除舊的 `visual-agent-design/` 目錄與 `visual-agent-design-agent.md`，避免雙份規格漂移。

若工作同時需要 VAD Core + Promptless：

```text
VAD Core Spec
→ VAD-Promptless Bridge
→ Self-Describing / Zero-Prompt Interface
→ Execute / Verify
```
