# Machine-readable Schema｜機器可讀卡片規格

Promptless Skill v0.3.0 將 Visual Skill Card 與 VAD Agent Card 從「給人看的圖卡」提升為「人與 AI/Agent 共用的資料契約」。

## 核心檔案

- `schemas/visual-skill-card.schema.json`：Skill 六欄與執行屬性的 JSON Schema。
- `schemas/vad-agent-card.schema.json`：VAD 十欄與治理屬性的 JSON Schema。
- `schemas/promptless-card.schema.json`：Skill / Agent 聯合入口。

採用 JSON Schema Draft 2020-12。`schema_version` 固定為 `0.3.0`，卡片本身另以 `metadata.version` 管理內容版本。

## 三層視角

1. **Visual Layer**：人看得懂的資訊卡／Agent Card。
2. **Semantic Layer**：TASK、INPUT、PROCESS、GOAL、DECISION 等語意欄位。
3. **Machine Layer**：JSON Schema 驗證、分類、轉換與版本控制。

## 基本管線

```text
Visual Card / Form / UI
        ↓
Normalized JSON
        ↓
JSON Schema Validation
        ↓
Skill-or-Agent Classifier
     ┌──┴──┐
     ↓     ↓
   Skill  Agent
     ↓     ↓
 SKILL.md VAD Agent Card
     └──┬──┘
        ↓
 Platform Adapter
 ChatGPT / Codex / Claude / Gemini
```

## 設計原則

- Schema 是資料契約，不是另一套 Prompt。
- 固定流程即使很多步驟，仍可保持 Skill。
- 只有出現動態決策、動態工具選擇、重新規劃、跨任務狀態或委派等條件才升級 Agent。
- 所有外部寫入、高風險操作與治理要求必須顯式表達。

## 自動驗證

`.github/workflows/schema-validation.yml` 會在 Schema、範例、工具或測試變更時執行驗證，避免卡片規格與 Compiler 漂移。
