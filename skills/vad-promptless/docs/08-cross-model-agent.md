# ChatGPT、Codex、Claude、Gemini 的跨模型 Agent 使用方式

## 核心策略

```text
Canonical Methodology
  ├─ SKILL.md
  ├─ docs/
  └─ agents/vad-promptless-agent.md
          ↓
Platform Adapter
  ├─ ChatGPT / Codex
  ├─ Claude Code
  └─ Gemini CLI
```

平台檔只處理發現／叫用，核心邏輯回到同一份規格。

## ChatGPT
- `SKILL.md`
- Repository 根目錄 `CHATGPT.md`

## Codex
- Repository 根目錄 `AGENTS.md`
- `SKILL.md`

## Claude Code
- Repository 根目錄 `CLAUDE.md`
- `.claude/agents/vad-promptless-agent.md`

## Gemini CLI
- Repository 根目錄 `GEMINI.md`
- `.gemini/agents/vad-promptless-agent.md`

## 版本漂移防止
1. 先改 `skills/vad-promptless/SKILL.md` 或 Skill 內的 `docs/`。
2. 再檢查 Claude / Gemini Agent Adapter。
3. 不在平台入口重新複製一整套方法論。
4. 更新 `CHANGELOG.md`。
