---
name: promptless-skill
description: 將使用者的任務、素材、資訊卡或既有工作流程轉換成「不用由終端使用者撰寫長提示詞」的可重複 Skill；也可直接以 Skill-first 方式執行已定義任務。當使用者說「使用 Promptless Skill」「套用無提示詞技能」「依照這張資訊卡執行」「不要叫我寫 Prompt」「把流程封裝成 Skill」「把 Skill 升級成 Agent」或任務明顯屬於可重複、可標準化工作時使用。涉及自主規劃、多工具、多代理或 MCP/A2A 時，必須連結 VAD（Visual Agent Design）思維設計 Agent。
---

# Promptless Skill｜無提示詞技能

## 1. 目的

讓終端使用者不必先學會撰寫完整 Prompt，也能可靠完成 AI 任務；同時把專家方法封裝成可重複、可分享、可版本化的 Skill。

**Promptless 不代表系統內沒有 Prompt。**

Promptless 的定義是：

> **Zero Prompting for End Users**

底層可以包含 Prompt、Context、Rules、Knowledge、Workflow、Tools 與 QA，但不要求終端使用者每次重寫。

---

## 2. 核心行為規則

啟用本 Skill 後：

1. 優先理解「使用者要完成什麼」，不要先要求使用者學習 Prompt 格式。
2. 如果目前素材足以開始工作，直接執行，不要求使用者重新把需求改寫成結構化 Prompt。
3. 自動把需求整理為 TASK / INPUT / STYLE / PROCESS / OUTPUT / QA。
4. 使用者提供資訊卡、圖片、文件或範例時，把它們視為任務規格與上下文來源，而不是要求使用者再次文字描述同樣內容。
5. 任務可重複時，主動以可封裝 Skill 的方式思考，而不是只完成一次性答案。
6. 只有在缺少真正不可推定、且會實質改變結果的必要資訊時才詢問。
7. 涉及醫療、法律、財務、安全或其他高風險內容時，不因 Promptless 而降低必要的查證、限制、警告或人工確認。
8. 不把「Promptless」解讀為「完全沒有底層指令」。

---

## 3. 六欄任務模型

將任何任務正規化為：

### TASK
- 要完成什麼？
- 完成的終點是什麼？

### INPUT
- 有哪些資料、圖片、文件、網址、資料表、Logo、範例？
- 哪些是必要輸入？哪些可自動推定？

### STYLE
- 語言
- 品牌
- 語氣
- 視覺
- 格式
- 限制

### PROCESS
- 理解
- 分析
- 組織
- 執行
- 驗證
- 修正

### OUTPUT
- 要交付的成果
- 檔案格式
- 長寬比
- 結構
- 數量

### QA
- 正確性
- 完整性
- 格式
- 品牌一致性
- 錯字
- 引用／來源
- 是否達成任務

---

## 4. 執行流程

### Phase A｜辨識意圖

先從目前對話、附件、資訊卡、既有規則與可用工具推定使用者真正的 Job-to-be-Done。

不要把「請再提供完整 Prompt」當成預設下一步。

### Phase B｜建立 Skill Schema

在內部建立：

```text
TASK
INPUT
STYLE
PROCESS
OUTPUT
QA
```

必要時再加入：

```text
CONTEXT
KNOWLEDGE
RULES
TOOLS
FAILURE CONDITIONS
HUMAN REVIEW
```

### Phase C｜決定執行層級

#### Level 1：單一 Skill
任務清楚、步驟固定、低自主性。

#### Level 2：Workflow
需要多個 Skill 按順序執行。

#### Level 3：Agent
需要根據中間結果自主決定下一步。

#### Level 4：Multi-Agent
需要不同角色／專業 Agent 協作。

### Phase D｜執行

使用平台可用的原生工具、Skill、Connector、MCP、程式碼或檔案能力完成任務。

不要為了展示 Promptless 而刻意繞過更可靠的平台原生能力。

### Phase E｜QA

完成前逐項驗證：

- TASK 是否完成？
- INPUT 是否被正確使用？
- STYLE 是否遵守？
- PROCESS 是否漏步驟？
- OUTPUT 是否符合指定格式？
- QA 是否全部通過？

不合格時，先修正再交付。

---

## 5. 與 VAD 的連結

當任務進入 Agent 層，不再只使用六欄 Skill Schema；必須轉換為 VAD 視覺代理設計模型：

```text
GOAL
ROLE
SKILLS
TOOLS
KNOWLEDGE
WORKFLOW
DECISION
SUB-AGENTS
MCP / A2A
QA
```

核心關係：

> **Promptless Skill 封裝能力；VAD 設計代理如何使用能力。**

> **Skill 是能力，Agent 是大腦，VAD 是藍圖。**

### 何時升級成 VAD Agent？

符合任一條件時：

- 必須根據中間結果做下一步決策
- 需要呼叫多個 Skill
- 需要多個 Tool／Connector／MCP
- 需要持續任務或循環
- 需要角色分工
- 需要 Sub-Agent
- 需要 A2A 協作
- 需要人工審核節點

詳細規格讀取 `docs/03-agent-vad.md`。

---

## 6. Visual Skill Card

若使用者提供資訊卡或希望建立「不用提示詞的資訊卡」，把 Visual Skill Card 視為 Promptless Skill 的人機介面，而不是單純海報。

卡片至少呈現：

```text
TASK | INPUT | STYLE | PROCESS | OUTPUT | QA
```

卡片的目的：

1. 人看得懂
2. AI 看得懂
3. 可以映射到 Skill
4. 可以再升級成 Workflow／Agent

詳細規格讀取 `docs/04-visual-skill-card.md`。

---

## 7. 建立新 Promptless Skill 時

當使用者要求「把這個流程做成不用提示詞的 Skill」：

1. 擷取 Job-to-be-Done。
2. 建立六欄規格。
3. 找出不可變規則與可變輸入。
4. 把重複 Prompt 內容移入 Skill。
5. 將詳細參考內容拆到 `docs/`、`references/`、`templates/` 或 `examples/`，避免主 `SKILL.md` 過長。
6. 加入清楚的 `name` 與 `description`，description 必須同時說明「做什麼」與「何時使用」。
7. 加入輸出與 QA。
8. 若需要 Agent 自主性，加入 VAD 設計。
9. 產出可版本化資料夾。

可直接使用 `templates/PROMPTLESS-SKILL-TEMPLATE.md`。

---

## 8. 使用者體驗原則

### 不要這樣做

- 「請先用以下格式重新寫 Prompt：Role / Goal / Context / Output...」
- 「請再把圖片內容全部打成文字。」
- 「你必須先學會提示詞才能使用。」

### 應該這樣做

- 直接理解使用者現有素材。
- 自動補齊可合理推定的結構。
- 在必要時提出最少量問題。
- 把複雜性留在 Skill／Agent 系統內，而不是丟回給終端使用者。

---

## 9. 輸出模式

依任務選擇最適合的輸出；不要固定只輸出文字。

可能包括：

- 對話答案
- Markdown
- 圖卡
- 簡報
- PDF
- 文件
- 試算表
- HTML
- JSON / YAML
- Skill 資料夾
- Agent 設計
- VAD 架構

---

## 10. 觸發範例

應啟用本 Skill：

- 「不用 Prompt 幫我完成這個。」
- 「照這張資訊卡做。」
- 「我不要再學一堆提示詞。」
- 「幫我把這個工作流程做成 Skill。」
- 「我希望員工只要選功能就能執行。」
- 「將這個 Skill 接到 Agent。」
- 「用 VAD 把這套 Agent 畫清楚。」
- 「讓這個方法可以給 ChatGPT、Gemini、Claude 使用。」

不一定需要啟用：

- 單純詢問一個一次性的常識問題
- 使用者明確要求學習／研究 Prompt Engineering 本身

---

## 11. 最終檢查

交付前確認：

- [ ] 終端使用者是否被迫寫不必要的長 Prompt？若是，重新設計。
- [ ] Skill 是否可以重複使用？
- [ ] 可變輸入是否與固定規則分離？
- [ ] 是否有明確 QA？
- [ ] 若是 Agent 任務，是否已使用 VAD 思維？
- [ ] 是否優先使用平台原生能力？
- [ ] 是否避免宣稱「系統完全沒有 Prompt」？
