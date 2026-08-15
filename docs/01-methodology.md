# Promptless Skill 方法論

## 1. 問題背景

生成式 AI 的早期教學大量集中於「如何寫好 Prompt」。這有其價值，但也容易把「提示詞能力」誤當成「使用 AI 的先決條件」。

Promptless Skill 提出另一種教學順序：

> **先讓人完成任務，再讓人理解底層。**

## 2. 核心定義

**Promptless Skill**：將可重複的專業工作方法封裝成 Skill，使終端使用者可直接選擇與使用能力，而不必每次從零撰寫完整提示詞。

Promptless 並不是消滅 Prompt，而是把 Prompt 從「終端使用者操作介面」移到「系統與 Skill 設計層」。

## 3. Skill-first Learning

```text
Level 1 USE       選 Skill、放資料、取得成果
Level 2 COMPOSE   多 Skill 組成 Workflow
Level 3 ORCHESTRATE Agent 調度 Skill / Tool / MCP
Level 4 BUILD     理解 Prompt / Context / RAG / Rules / Evaluation
Level 5 DESIGN    使用 VAD 設計 Multi-Agent / A2A / Governance
```

## 4. 研究假設

可用 A/B/C 驗證：

- A：Prompt-first
- B：文字 Skill
- C：Promptless Skill + Visual Skill Card

評估：

- 任務完成率
- 完成時間
- 修改次數
- 錯誤率
- 認知負荷
- 初學者成功率
- 成果品質
- 滿意度

## 5. 方法論邊界

Promptless Skill 不主張：

- Prompt Engineering 沒有價值
- 所有任務都能零確認完成
- Agent 可以取代所有人工決策
- 視覺卡片是唯一介面

它主張：

- 一般使用 AI 不應以會寫長 Prompt 為必要條件
- 重複任務應封裝成 Skill
- 複雜決策應升級到 Agent
- Agent 設計應以 VAD 讓結構可理解、可溝通、可驗證
