# ChatGPT、Codex、Claude、Gemini 的跨模型 Agent 使用方式

## 1. 核心策略

跨模型不是維護四套方法論，而是：

```text
Canonical Methodology
  ├─ SKILL.md
  ├─ docs/
  └─ agents/promptless-vad-agent.md
          ↓
Platform Adapter
  ├─ ChatGPT / Codex
  ├─ Claude Code
  └─ Gemini CLI
```

平台檔只處理「如何發現／叫用」，核心邏輯仍回到同一份規格。

---

## 2. ChatGPT

建議入口：

- `SKILL.md`
- `CHATGPT.md`

適合：
- Skills 可用的 ChatGPT 工作區／產品
- 以可重複工作流程形式自動或手動使用 Skill

若使用者說「把 Skill 升級成 Agent」，應讀取 `docs/07-promptless-agent-methodology.md` 與 `agents/promptless-vad-agent.md`，建立 VAD，而不是只擴寫 Prompt。

---

## 3. Codex

建議入口：

- `AGENTS.md`
- `SKILL.md`

Codex 主要利用 AGENTS.md 承載專案級規範，再在重複工作中使用 Skills。

---

## 4. Claude Code

專案入口：

- `CLAUDE.md`
- `.claude/agents/promptless-vad-agent.md`

Skill 可放在 Claude Code 支援的 Skill 路徑中；Agent 定義可用 `.claude/agents/`。

本 Repository 直接提供專案級 Agent 範例。

---

## 5. Gemini CLI

專案入口：

- `GEMINI.md`
- `.gemini/agents/promptless-vad-agent.md`

Gemini CLI 可從 Git Repository 安裝 Agent Skill，也可在專案中使用自訂 Agent 定義。

---

## 6. 可攜性原則

跨模型共通層只使用：

- Markdown
- YAML frontmatter（平台支援處）
- TASK / INPUT / STYLE / PROCESS / OUTPUT / QA
- VAD 十欄
- 標準檔案與資料夾

平台特有功能放在平台 Adapter，不污染 Canonical Methodology。

---

## 7. 版本漂移防止

任何核心規則變更：

1. 先改 `SKILL.md` 或 `docs/`。
2. 再檢查 Claude / Gemini Agent Adapter 是否需要同步。
3. 不在 `CLAUDE.md`、`GEMINI.md`、`CHATGPT.md` 重新複製一整套方法論。
4. 更新 `CHANGELOG.md`。
