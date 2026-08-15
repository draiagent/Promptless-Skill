# 官方技術參考

> 查核日期：2026-08-15。平台功能會持續更新，安裝方式以官方最新文件為準。

## OpenAI / ChatGPT

- OpenAI Academy — Using skills  
  https://openai.com/academy/skills/
- OpenAI Help Center — Skills in ChatGPT  
  https://help.openai.com/en/articles/20001066

重點：Skills 是可重複、可分享的工作流程；`SKILL.md` 是主要操作手冊格式，可包含指示、範例、程式碼與支援資源。

## Anthropic / Claude

- Claude Platform — Agent Skills overview  
  https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- Claude Platform — Skill authoring best practices  
  https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices

重點：自訂 Skill 是包含 `SKILL.md` 的目錄；Claude Code 可從 `~/.claude/skills/` 或 `.claude/skills/` 發現 Skills。

## Google / Gemini CLI

- Gemini CLI — Agent Skills  
  https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/skills.md
- Gemini CLI — Managing Agent Skills  
  https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/using-agent-skills.md
- Gemini CLI — GEMINI.md context  
  https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/gemini-md.md

重點：Gemini CLI 支援 Agent Skills open standard，可從 Git Repository 安裝，並支援 `.gemini/skills/`、`.agents/skills/` 等目錄。
