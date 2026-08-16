# ChatGPT / Codex｜VAD-Promptless 使用入口

本 Repository 專注於 **VAD-Promptless**。

## Core Skill

`skills/vad-promptless/SKILL.md`

## 可直接使用的任務

- 將自然需求封裝成 Promptless Skill。
- 將重複工作改造成 Workflow。
- 在需要動態決策時升級為 Promptless Agent。
- 從資訊卡／流程圖擷取結構化任務。
- 建立 Machine-readable Card。
- 建立 Self-Describing Visual Card。
- 進行 SHA-256、PNG metadata、sidecar JSON 綁定與驗證。

## Codex

在 Repository 工作時先遵循根目錄 `AGENTS.md`，再讀取：

- `skills/vad-promptless/SKILL.md`
- `skills/vad-promptless/agents/vad-promptless-agent.md`
- `skills/vad-promptless/docs/11-governance.md`

## Visual-first Rule

若使用者已提供圖片、資訊卡、附件或範例，先利用現有內容，不要求重新撰寫相同需求。

## Visual Agent Design Core

完整 VAD 的 TRC-3D、VAC-8、Five-Pack、Agent Blueprint、Routing、Research Protocol 位於：

https://github.com/draiagent/Visual-Agent-Design

本 Repo 不再包含 `visual-agent-design/` 複本。

若任務是「使用完整 Visual Agent Design」，應以該 Repo 為上游標準；VAD-Promptless 可在其後提供 Promptless Bridge、Self-Describing Card 或 Zero-Prompt UX。

> **VAD 定義任務；VAD-Promptless 降低終端使用者反覆撰寫 Prompt 的負擔。**
