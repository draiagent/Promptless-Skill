# Skill → Agent 自動升級判斷

## 核心原則

> **多步驟 ≠ Agent。動態決策才是 Agent 的主要分界。**

### 保持 Skill

- 步驟固定。
- 工具固定。
- 中間結果不改變主要路徑。
- 不需要跨任務持續狀態。
- 不需要委派其他 Agent。

### 建議升級 Agent

只要存在一項且 `allow_agent_upgrade=true`，參考分類器可建議升級：

- `autonomy_level >= 3`
- `dynamic_branching = true`
- `dynamic_tool_selection = true`
- `replanning = true`
- `persistent_state = true`
- `delegation = true`
- `multi_agent = true`
- 或 `forced_reasons` 明確指定

若外部副作用同時伴隨動態決策，必須升級成 Agent 並加入 Governance / Human Review。

## Autonomy Level 建議

| 等級 | 定義 | 預設型態 |
|---|---|---|
| 0 | 只轉換／格式化 | Skill |
| 1 | 固定程序執行 | Skill |
| 2 | 有限條件分支但規則固定 | Skill / Workflow |
| 3 | 依結果選路徑或工具 | Agent |
| 4 | 可重新規劃、委派 | Agent |
| 5 | 多代理協作與持續自治 | Governed Multi-Agent |

這個分級用來降低過度 Agent 化，而不是追求最高自治。
