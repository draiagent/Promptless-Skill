# Changelog

## 0.3.1 - 2026-08-16

- 新增 Visual Card Parser：圖片資訊卡先抽取為可稽核的 Extraction JSON。
- 新增 `visual-card-extraction.schema.json`。
- 新增跨模型視覺抽取 Adapter。
- 新增 `visual_card_parser.py`，支援 validate-extraction / normalize / pipeline。
- 新增 Skill 與 Agent 視覺抽取測試案例。
- 新增 Perception Layer → Specification Layer 分層，降低圖片直接生成 Skill 的幻覺風險。
- 中文卡片名稱使用穩定雜湊 ID，避免不同卡片發生機器名稱衝突。

## 0.3.0 - 2026-08-16

- 新增 Visual Skill Card JSON Schema。
- 新增 VAD Agent Card JSON Schema。
- 新增 Skill / Agent 聯合 Card Schema。
- 新增 `tools/promptless_card.py`：validate / classify / compile 參考實作。
- 建立 Skill → Agent 可機器判斷的升級條件與 Autonomy Level。
- 新增 Machine-readable Skill 與 Agent JSON 範例。
- 新增 Card → Skill / Agent Compiler 方法。

## 0.2.0 - 2026-08-15

- 將 Promptless Skill 擴充為 Skill × Agent × VAD 完整方法論。
- 新增 Promptless Agent 方法論與 VAD 十欄。
- 新增 Claude / Gemini / ChatGPT 跨模型入口。
- 新增 Evaluation、Governance、Roadmap 與 Agent 模板。

## 0.1.0 - 2026-08-15

- 建立 Promptless Skill 初始方法論。
- 建立 Skill 六欄、Visual Skill Card、VAD 關係與跨模型說明。
