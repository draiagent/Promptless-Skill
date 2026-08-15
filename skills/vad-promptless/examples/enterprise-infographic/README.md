# 範例：企業資訊圖卡 Promptless Skill

## 使用者體驗

使用者只提供：

- 原始文字／文件
- Logo（選用）
- 參考圖片（選用）

不要求使用者寫完整設計 Prompt。

## Skill Schema

### TASK
建立企業專業資訊圖卡。

### INPUT
文字、圖片、Logo、文件。

### STYLE
繁體中文、企業專業、清楚易讀、品牌一致。

### PROCESS
理解內容 → 萃取重點 → 建立資訊階層 → 視覺化 → 文字校對 → QA。

### OUTPUT
指定比例的資訊圖卡。

### QA
- 繁體中文
- 無明顯錯字
- 重點完整
- 品牌一致
- 排版清楚

## 若升級成 Agent

當需要自動搜尋資料、比對來源、建立文案、產生視覺、審稿與發布時，改以 VAD 方式設計：

```text
Content Agent
  ├─ Research Skill → Search / MCP
  ├─ Writing Skill
  ├─ Design Skill
  └─ QA Skill
```
