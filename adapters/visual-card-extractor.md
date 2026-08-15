# Visual Card Extractor Adapter｜視覺資訊卡抽取器

版本：0.3.1

## 目的

當 ChatGPT、Gemini、Claude 或其他具備視覺能力的模型收到一張資訊卡、流程卡、Skill Card 或 Agent Card 圖片時，先不要直接生成 Skill。第一步必須把圖片內容抽取成 `schemas/visual-card-extraction.schema.json` 定義的中介 JSON。

## 執行原則

1. 只根據圖片中可見資訊與使用者當前提供的補充內容抽取，不自行發明不存在的流程。
2. 保留原本的繁體中文語意；明顯 OCR 錯字可修正，但不改變專業含義。
3. 無法確認的欄位寫入 `uncertainties`，不要假裝確定。
4. `candidate_type` 只做初步判斷；最終 Skill/Agent 分類交給 Compiler。
5. 若卡片只有固定步驟，即使步驟很多也優先判定 Skill。
6. 出現動態分支、動態選工具、重規劃、跨回合狀態、委派、多 Agent、A2A 等訊號時，設定相對應 `signals`。
7. 涉及寫入外部系統、寄送訊息、修改資料、付款、刪除等行為，將 `external_side_effects=true`；若應由人核准，再設 `human_approval_required=true`。

## 輸出

只輸出符合 `visual-card-extraction.schema.json` 的 JSON 物件。Host 系統接著執行：

```text
Image → Extraction JSON → normalize → validate → classify → compile
```

## 最小欄位映射

- 卡片標題 → `intent.name`
- 任務目的 → `intent.objective`
- 成功條件 → `intent.success_definition`
- 素材／輸入 → `fields.input`
- 風格／限制 → `fields.style`
- 步驟／流程 → `fields.process`
- 產出物 → `fields.output`
- 驗收 → `fields.qa`
- 角色 → `fields.role`
- 技能 → `fields.skills`
- 工具 → `fields.tools`
- 知識 → `fields.knowledge`
- 決策 → `fields.decisions`
- 子代理 → `fields.sub_agents`
- MCP / A2A → `fields.interoperability`
- 治理／人工審核 → `fields.governance`
