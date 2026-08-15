# Promptless Skill × VAD｜無提示詞技能與視覺代理設計方法論

> **讓使用 AI 不再以「先學會寫 Prompt」為前提，並把 Skill 進一步升級為可設計、可治理、可協作的 Agent。**

**版本：0.3.1**  
**語言：繁體中文（zh-TW）**  
**定位：開源教學／企業導入／AI Skill／Agent／VAD 方法論**

---

## v0.3.1｜圖片資訊卡直接進入機器流程

```text
圖片資訊卡 → Vision Extraction JSON → Schema 驗證 → Card 正規化 → Skill / Agent → 編譯輸出
```

- 視覺抽取規格：`schemas/visual-card-extraction.schema.json`
- 跨模型抽取器：`adapters/visual-card-extractor.md`
- Parser：`tools/visual_card_parser.py`
- 詳細說明：`docs/16-visual-card-parser.md`

> 圖片不是直接執行碼。先抽取、保留信心與不確定性，再進入可驗證規格。
