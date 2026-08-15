# Agent × VAD｜視覺代理設計

## 1. Agent 不等於大型 Skill

Skill 回答「如何做好一種能力」。

Agent 回答「為了達成目標，現在應該做什麼、用哪個 Skill、哪個 Tool、哪個 Knowledge，是否需要委派或詢問人」。

> **Skill 是能力，Agent 是大腦，VAD 是藍圖。**

---

## 2. VAD 十欄

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
QA / GOVERNANCE
```

VAD 的目的不是畫漂亮架構圖，而是把 Agent 的**責任、能力、工具、資料、決策、協作、風險與完成條件**視覺化。

---

## 3. Skill → Workflow → Agent → Multi-Agent

```text
Promptless Skill
      ↓
Workflow
      ↓
VAD Agent
  ├─ Skill A
  ├─ Skill B
  ├─ Tool
  ├─ Knowledge
  └─ MCP
      ↓
Sub-Agent / A2A
      ↓
QA / Human Review
      ↓
Output
```

---

## 4. VAD 的治理價值

一張好的 VAD 應讓非工程主管也能指出：

- Agent 的 Goal
- 哪些 Skill 可用
- 哪些資料可讀
- 哪些工具可寫
- 哪裡 Agent 可以自主決定
- 哪裡一定要 Human Review
- 哪個 Sub-Agent 負責什麼
- 失敗時怎麼降級或停止

---

## 5. 教學語言

- 初階：先會用 Skill。
- 中階：把 Skill 串成 Workflow。
- 進階：讓 Agent 根據結果做決策。
- 高階：用 VAD 管理 Skill、Tool、Knowledge、MCP、A2A、Evaluation 與治理。

完整方法見 `07-promptless-agent-methodology.md`。
