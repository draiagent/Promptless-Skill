# file naming compatibility｜檔名大小寫相容規範

VAD-Promptless 的機器識別值採小寫，但平台約定入口檔名保留標準大小寫。

## 必須小寫
- `SKILL.md` YAML `name: vad-promptless`
- 技能資料夾 `vad-promptless/`
- `schemas/*.json`
- 一般非保留檔名

## 保留標準大小寫
`SKILL.md`、`AGENTS.md`、`CLAUDE.md`、`GEMINI.md`、`README.md`、`LICENSE`、`CITATION.cff`、`CONTRIBUTING.md`、`SECURITY.md`、`CHANGELOG.md`。

macOS 預設常不區分檔名大小寫，Linux / GitHub / CI 會暴露 `skill.md` vs `SKILL.md` 錯誤。因此 CI 驗證入口檔存在、錯誤小寫不存在、`name:` 與父資料夾一致、schema `$id` 指向 `draiagent/VAD-Promptless`。

Agent 定義檔不是固定入口，可小寫：
`agents/vad-promptless-agent.md`、`.claude/agents/vad-promptless-agent.md`、`.gemini/agents/vad-promptless-agent.md`。
