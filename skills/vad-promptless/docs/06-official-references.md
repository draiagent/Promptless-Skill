# 官方技術參考（2026-08-16 檢查）

> 本檔只記錄平台能力與安裝依據；VAD-Promptless 方法論本身由本 Repository 定義。

## Agent Skills open standard

- Skill 是一個資料夾，至少包含 `SKILL.md`。
- YAML `name:` 只能使用小寫字母、數字與連字號。
- `name:` 必須與父資料夾名稱一致。

## OpenAI / ChatGPT / Codex

- ChatGPT Skills 以 `SKILL.md` 作為可重複 workflow 的 playbook。
- Codex 支援 `AGENTS.md` 作 Repository 級指引。

## Claude Code

- Claude Code Skills 使用 `<skill-name>/SKILL.md`。
- 個人 Skill 可位於 `~/.claude/skills/`；專案 Skill 可位於 `.claude/skills/`。
- `CLAUDE.md` 為 Claude Code 專案 context 入口之一。

## Gemini CLI

- Gemini CLI Agent Skills 使用 `SKILL.md`。
- 可從 Git Repository 安裝，並以 `--path` 指定 Repository 內的 Skill 子目錄。
- `GEMINI.md` 可提供專案級 context。

## 相容性原則

平台功能會演進。本 Repository 應定期更新 Adapter 與安裝文件，但核心方法論保持平台中立。
