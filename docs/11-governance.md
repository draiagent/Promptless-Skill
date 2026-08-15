# Governance｜Promptless Agent 治理原則

## 1. Promptless 不能等於取消控制

介面可以簡單，但底層治理必須更清楚。

## 2. 四種行為層級

### READ
搜尋、讀檔、讀資料庫。通常風險較低，但仍需資料權限。

### DRAFT
生成草稿、不對外發布。適合預設自動化。

### WRITE
修改檔案、資料、系統狀態。需要更嚴格權限與驗證。

### COMMIT / SEND / PUBLISH / DELETE
不可逆或高影響行為。預設應有明確 Human Review 或平台原生確認。

## 3. VAD 治理標記

每個 DECISION 節點標示：

- AUTO
- ASK
- ESCALATE
- STOP

每個 Tool 標示：

- READ
- WRITE
- EXTERNAL
- SENSITIVE

## 4. 資料治理

- 來源
- 更新日期
- 版本
- 存取權
- 個資／機密等級
- 保留政策

## 5. 可觀測性

能記錄時應保留：

- 使用的 Skill
- 使用的 Tool
- 關鍵資料來源
- 重要決策
- Human Review
- 失敗與重試
- 最終版本

## 6. 失敗策略

Agent 不知道時不應假裝知道。

優先順序：

```text
Retry → Alternate Tool → Ask Human → Escalate → Stop
```
