# 跨模型安裝與召喚

## 1. 原則

本 Repository 的核心規格是 `SKILL.md`，不是為每個模型重寫一份 Prompt。

---

## 2. ChatGPT

若 ChatGPT 帳號／工作區提供 Skills：

1. 從 GitHub 下載 ZIP。
2. 在 Skills 建立／上傳功能中匯入。
3. 確認 Skill 可用後，以符合 description 的自然任務觸發，或直接說「使用 Promptless Skill」。
4. 需要 Agent 時說：「把這個 Skill 升級成 Agent，使用 VAD。」

> 不同 ChatGPT 方案與介面支援狀態可能不同，以當下產品介面為準。

---

## 3. Claude Code

### Skill

可將 Skill 放到 Claude Code 支援的個人或專案 Skills 路徑。

### Agent

本 Repository 已提供：

```text
.claude/agents/promptless-vad-agent.md
```

專案中啟動 Claude Code 後，可在 Agent 管理／委派流程中使用。

---

## 4. Gemini CLI

Gemini CLI 支援從 Git Repository 安裝 Agent Skill：

```bash
gemini skills install https://github.com/draiagent/Promptless-Skill
```

專案 Agent 定義：

```text
.gemini/agents/promptless-vad-agent.md
```

可依 Gemini CLI 當前 Agent / Skills 指令重新載入。

---

## 5. Codex

在 Repository 中使用：

```text
AGENTS.md
SKILL.md
agents/promptless-vad-agent.md
```

Codex 可把 `AGENTS.md` 當專案行為與工作規格入口；重複流程則使用 Skill。

---

## 6. 驗證安裝

安裝後測試以下任務：

> 「我有一份資料與參考圖，請直接依 Promptless Skill 完成，不要叫我改寫 Prompt。」

再測：

> 「這個工作需要中途決策，請升級成 Promptless Agent，並輸出 VAD 十欄。」

應能看出 Skill 與 Agent 的層級差異。
