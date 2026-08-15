# ChatGPT、Claude、Gemini 跨模型安裝與召喚

> 本文件提供實務安裝方向。不同產品方案與介面可能更新，請以各平台當期官方文件為準。

## 1. 共通原則

本 Repository 的主要可執行規格是：

```text
SKILL.md
```

`AGENTS.md`、`CLAUDE.md`、`GEMINI.md` 是平台／專案入口，不應複製另一套不同的核心規則。

---

## 2. ChatGPT

支援 Skills 的 ChatGPT 工作區／產品，可將 Skill 從電腦上傳或透過 Skills 介面建立。安裝後，ChatGPT 可以在任務相關時自動使用 Skill，也可以由使用者明確選擇／召喚。

建議：

1. 將 `Promptless-Skill` 資料夾壓縮為 ZIP。
2. 在支援 Skills 的 ChatGPT 介面選擇建立／上傳 Skill。
3. 上傳 ZIP。
4. 確認 Skill 名稱 `promptless-skill` 與 description 已被辨識。
5. 測試：「把這個工作流程封裝成不用提示詞的 Skill。」

若目前帳號／工作區沒有 Skills 上傳功能，可把 Repository 作為專案／工作區參考資料使用；但這不等於原生 Skill 安裝。

---

## 3. Claude / Claude Code

### claude.ai

可用自訂 Skills 的方案，可將 Skill 資料夾以 ZIP 上傳至自訂 Skills 功能。

### Claude Code

個人 Skill：

```text
~/.claude/skills/promptless-skill/
```

專案 Skill：

```text
.claude/skills/promptless-skill/
```

其中必須存在：

```text
SKILL.md
```

Claude 會依 `name` 與 `description` 判斷何時需要使用。

---

## 4. Gemini CLI

Gemini CLI 支援 Agent Skills。

可從 Git Repository 安裝：

```bash
gemini skills install https://github.com/<owner>/Promptless-Skill
```

也可放入：

```text
~/.gemini/skills/
~/.agents/skills/
.gemini/skills/
.agents/skills/
```

開發時可 link：

```bash
gemini skills link ./Promptless-Skill
```

重新載入：

```text
/skills reload
```

`GEMINI.md` 可作為專案持續性 Context，但 Promptless Skill 本身應使用 Agent Skill 機制按需啟用。

---

## 5. 建議測試句

安裝後測試：

1. 「使用 Promptless Skill，把這份資料做成可重複工作流程。」
2. 「照這張資訊卡直接完成，不要叫我先寫 Prompt。」
3. 「把這個流程變成 Skill，並建立 TASK / INPUT / STYLE / PROCESS / OUTPUT / QA。」
4. 「這個任務需要自主決策，請升級成 Agent 並用 VAD 表示。」

---

## 6. 安全提醒

從 GitHub 安裝第三方 Skill 前，應閱讀 `SKILL.md` 與任何 scripts。Skill 可能具有檔案、程式碼或工具存取能力；不要只因 Repository 公開就直接信任執行。
