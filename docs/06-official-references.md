# 官方技術參考（2026-08-15 檢查）

> 本檔只記錄平台能力與安裝依據；Promptless Skill × VAD 方法論本身由本 Repository 定義。

## OpenAI / ChatGPT

- Skills 是可重複、可分享的工作流程，可包含指示、範例與程式碼；安裝後可在有幫助時被使用。
- OpenAI Skills 遵循 Agent Skills open standard。
- Codex 亦支援 Skills。

官方：OpenAI Help Center「Skills in ChatGPT」。

## Claude Code

- Claude Code Skills 使用 `SKILL.md`。
- 可自動載入相關 Skill，也可直接以 Skill 名稱叫用。
- 專案／個人 Skills 有對應目錄。
- Claude Code 自訂 Subagents 使用 Markdown + YAML frontmatter；專案 Agent 可放 `.claude/agents/`。

官方：Claude Code Docs「Skills」「Sub-agents」。

## Gemini CLI

- Gemini CLI 支援 Agent Skills，核心檔為 `SKILL.md`。
- 可從 Git Repository 安裝 Skill。
- 專案自訂 Agent 定義可放 `.gemini/agents/*.md`。
- `GEMINI.md` 可提供專案級 context。

官方：Gemini CLI Docs「Agent Skills」「Subagents」「GEMINI.md」。

## 相容性原則

平台功能會演進。本 Repository 應定期更新 Adapter 與安裝文件，但核心方法論保持平台中立。
