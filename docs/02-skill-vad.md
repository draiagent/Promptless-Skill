# Skill 與 VAD 的關係

## 1. Skill 是能力封裝

Promptless Skill 將以下內容封裝：

- TASK
- INPUT
- STYLE
- PROCESS
- OUTPUT
- QA
- Context
- Rules
- Knowledge
- Tools（如需要）

Skill 回答：

> **AI 會什麼？**

## 2. Visual Skill Card 是人機入口

Visual Skill Card 可把 Skill 的六欄結構視覺化，使使用者不必閱讀長篇 Prompt。

```text
Visual Skill Card
      ↓
TASK / INPUT / STYLE / PROCESS / OUTPUT / QA
      ↓
Promptless Skill
```

## 3. VAD 是升級橋樑

當 Skill 不再只是固定流程，而需要根據環境與中間結果做選擇，就需要 VAD。

```text
Promptless Skill
      ↓
Workflow
      ↓
VAD
      ↓
Agent
```

## 4. 核心句

> **Promptless Skill 封裝能力，VAD 設計代理如何使用能力。**

> **Skill 是能力，Agent 是大腦，VAD 是藍圖。**
