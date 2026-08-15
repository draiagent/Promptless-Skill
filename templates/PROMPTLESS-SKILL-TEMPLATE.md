---
name: your-skill-name
description: 用一句話說明這個 Skill 做什麼，以及什麼情況應該啟用。
---

# Skill 名稱

## 1. TASK
要完成什麼？

## 2. INPUT
使用者需要提供什麼？哪些可自動推定？

## 3. STYLE
語言、品牌、語氣、格式、限制。

## 4. PROCESS
1. 理解
2. 分析
3. 執行
4. 驗證
5. 修正

## 5. OUTPUT
交付成果與格式。

## 6. QA
- [ ] 正確
- [ ] 完整
- [ ] 格式符合
- [ ] 無明顯錯字
- [ ] 符合任務目標

## 7. Promptless 規則

- 不要求終端使用者先重寫一份長 Prompt。
- 優先使用目前對話、附件、範例與可推定資訊。
- 只有真正必要資訊缺失時才詢問。

## 8. VAD 升級條件

如果任務需要自主決策、多 Skill、多 Tool、MCP、Sub-Agent 或 A2A，讀取 VAD 規格，建立：

GOAL / ROLE / SKILLS / TOOLS / KNOWLEDGE / WORKFLOW / DECISION / SUB-AGENTS / QA
