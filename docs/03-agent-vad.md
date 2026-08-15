# Agent 與 VAD 的關係

## 1. Agent 不等於大型 Skill

Skill 通常描述「如何做一件事」。

Agent 則要根據目標、情境與中間結果決定：

- 下一步做什麼
- 要呼叫哪個 Skill
- 要使用哪個 Tool
- 是否需要 MCP
- 是否委派 Sub-Agent
- 是否啟動 A2A
- 何時要求 Human Review

## 2. VAD Agent 九欄

### GOAL
最終目標。

### ROLE
Agent 的責任與邊界。

### SKILLS
可以使用哪些能力。

### TOOLS
搜尋、資料庫、程式、文件、API 等。

### KNOWLEDGE
知識庫、RAG、企業規則與記憶。

### WORKFLOW
預設工作流程。

### DECISION
哪些節點允許 Agent 自主判斷。

### SUB-AGENTS / MCP / A2A
外部工具、服務與代理協作。

### QA
完成條件、評估、風險與人工審核。

## 3. Promptless Skill × VAD Agent

```text
Human
  ↓
Visual / Natural Intent Interface
  ↓
Promptless Skill
  ↓
Workflow
  ↓
VAD Agent
  ├─ Skill A
  ├─ Skill B
  ├─ Tool
  ├─ MCP
  └─ A2A → Sub-Agent
  ↓
QA / Human Review
  ↓
Output
```

## 4. 企業教學語言

- 初階：不用先學 Prompt，先會使用 Skill。
- 中階：把 Skill 串成 Workflow。
- 進階：讓 Agent 自己選擇與調度 Skill。
- 高階：用 VAD 把 Agent、Skill、Tool、MCP、A2A 與治理機制視覺化。
