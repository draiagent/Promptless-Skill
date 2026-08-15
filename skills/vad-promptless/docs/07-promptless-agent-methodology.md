# Promptless Agent 方法論｜無提示詞代理方法論

## 1. 定義

**Promptless Agent** 是建立在 Promptless Skill 之上的代理設計方法：終端使用者以自然需求、素材、資訊卡或既有流程表達意圖，系統再以 Agent 自主規劃與調度已封裝的 Skills、Tools、Knowledge、MCP 與 Sub-Agents。

它不是「完全沒有提示詞」，而是**不把提示詞工程當成終端使用者的操作前提**。

---

## 2. 與 Skill 的差異

| 比較 | Promptless Skill | Promptless Agent |
|---|---|---|
| 核心 | 能力封裝 | 目標導向調度 |
| 路徑 | 相對固定 | 可依結果改變 |
| 決策 | 少 | 明確決策節點 |
| 工具 | 通常固定 | 可動態選擇 |
| Sub-Agent | 非必要 | 視任務委派 |
| MCP / A2A | 可有 | 常作為擴充層 |
| VAD | 可選 | 建議必備 |
| QA | 結果驗收 | 結果＋決策＋治理驗收 |

---

## 3. 三個層級不要混淆

```text
Skill = 如何做好一種能力
Workflow = 多個能力按照流程串接
Agent = 根據目標與觀察結果，決定下一步該使用哪種能力
```

**原則：用最低足夠複雜度完成任務。**

固定 SOP 不需要硬做成 Agent。

---

## 4. Promptless Agent 的 VAD 十欄

### 4.1 GOAL
- 最終想達成什麼？
- 成功判定可以量化嗎？
- 何時停止？

### 4.2 ROLE
- Agent 代表哪個職能？
- 負責什麼？
- 不負責什麼？
- 哪些事項不得自主執行？

### 4.3 SKILLS
- 可調用哪些可重複能力？
- 各 Skill 的觸發描述與輸入輸出是否清楚？
- 是否有重複 Skill 可合併？

### 4.4 TOOLS
- Search、Browser、Code、Database、Email、Calendar、Files、API 等。
- 每個工具需要什麼權限？
- 讀與寫要不要分開授權？

### 4.5 KNOWLEDGE
- 公開資訊
- 企業知識庫
- RAG
- 長期記憶
- SOP / Policy
- 資料版本與新鮮度

### 4.6 WORKFLOW
- 預設流程
- 平行流程
- 迴圈
- 重試
- 失敗降級
- 停止條件

### 4.7 DECISION
每個決策點明確標示：

- AUTO：可自動決定
- ASK：需要人確認
- ESCALATE：交給更高權限／專家 Agent
- STOP：不應繼續

### 4.8 SUB-AGENTS
委派時定義：

- 任務契約
- 輸入
- 允許工具
- 輸出格式
- Deadline / Max turns（平台支援時）
- 回傳後如何驗證

### 4.9 MCP / A2A
MCP 解決 Agent 與工具／資料源的標準連接；A2A 解決 Agent 與 Agent 的協作。

不要因為有協定就使用；只有任務需要才引入。

### 4.10 QA / GOVERNANCE
- 內容正確性
- 來源與引用
- 工具執行結果
- 權限
- 隱私
- 稽核
- 成本
- 失敗記錄
- Human Review

---

## 5. Agent 生命週期

### Stage 1｜Intent Capture
從自然語言、檔案、圖片、卡片或事件擷取目標。

### Stage 2｜Normalize
將需求轉成可執行 Goal、Inputs、Constraints、Success Criteria。

### Stage 3｜Plan
拆成 Tasks，指派 Skills、Tools、Knowledge 與 Agent。

### Stage 4｜Execute
執行動作並保留可觀察結果。

### Stage 5｜Observe
分析工具回傳、錯誤、缺口、外部狀態。

### Stage 6｜Decide
繼續、改路、重試、委派、詢問、停止。

### Stage 7｜Evaluate
依 QA / KPI / Rubric 檢查。

### Stage 8｜Human Review
高影響行為由人確認。

### Stage 9｜Deliver
交付成果與必要的決策摘要。

### Stage 10｜Version
把新成功模式、失敗案例與規則更新到下一版。

---

## 6. Promptless UX

終端使用者應該看到：

```text
我要完成什麼？
  ↓
提供必要素材
  ↓
選 Skill / Agent（或系統自動匹配）
  ↓
執行
  ↓
必要時只確認關鍵決策
  ↓
成果
```

而不是看到所有底層 Prompt、工具路由與代理協議。

---

## 7. Agent 不應隱藏的東西

Promptless 不代表黑箱化。使用者應能知道：

- Agent 的角色與權限
- 使用了哪些重要資料來源
- 何時執行外部寫入
- 哪些決策是自動做的
- 哪些結果未通過 QA
- 哪些地方需要人工判斷

VAD 的重要價值之一，就是把這些資訊可視化。

---

## 8. 企業導入建議

### 第一階段：Skill-first
先把高頻、規則清楚的工作封裝 Skill。

### 第二階段：Workflow
將跨部門或多 Skill 的固定流程串接。

### 第三階段：Agent
只對真正需要動態判斷的節點加入代理自主性。

### 第四階段：Multi-Agent
按專業、權限、上下文與可平行性拆 Agent。

### 第五階段：VAD Governance
建立企業級代理地圖、權限、Evaluation、版本與稽核。

---

## 9. 核心判斷題

建立 Agent 前問：

> 如果所有步驟都已經知道而且順序固定，為什麼不用 Workflow？

建立 Multi-Agent 前問：

> 如果一個 Agent 就能安全、清楚地完成，為什麼增加協作成本？

建立 Promptless 介面時問：

> 哪些複雜性真的需要終端使用者知道？哪些應該由系統封裝？
