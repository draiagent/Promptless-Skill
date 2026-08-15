# cross-model install｜跨模型安裝

VAD-Promptless 的可安裝 Agent Skill 位於：

```text
skills/vad-promptless/
└── SKILL.md
```

其 YAML frontmatter：

```yaml
name: vad-promptless
```

`name:` 與父資料夾 `vad-promptless` 一致，`SKILL.md` 保留標準大寫。

## Claude Code

```bash
mkdir -p ~/.claude/skills/vad-promptless
cp -R skills/vad-promptless/. ~/.claude/skills/vad-promptless/
```

## Gemini CLI

```bash
gemini skills install https://github.com/draiagent/VAD-Promptless.git --path skills/vad-promptless
```

或：

```bash
gemini skills link ./skills/vad-promptless
```

## ChatGPT / Codex

- ChatGPT Skills 使用 `SKILL.md` 作為工作流程 playbook。
- 可將 `skills/vad-promptless/` 封裝後匯入支援 Skills 的環境。
- Codex 可另外使用 Repository 根目錄 `AGENTS.md` 作專案級指引。

## 專案 Context 檔

`AGENTS.md`、`CLAUDE.md`、`GEMINI.md`、`CHATGPT.md` 為專案層入口，不取代 `skills/vad-promptless/SKILL.md`。
