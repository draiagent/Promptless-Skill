# Evaluation Framework｜驗證 Promptless Skill 與 Agent 是否真的有效

## 1. Skill 層指標

- Task Completion Rate
- Completion Time
- Revision Count
- Error Rate
- Output Quality
- Beginner Success Rate
- Cognitive Load
- Learning Satisfaction

## 2. Agent 層指標

- Plan Quality
- Skill Selection Accuracy
- Tool Selection Accuracy
- Knowledge Source Accuracy
- Decision Accuracy
- Recovery Rate
- Unnecessary Action Rate
- Human Escalation Precision
- End-to-End Success Rate
- Cost / Latency（可取得時）

## 3. VAD 指標

- 人是否能從圖理解 Agent 的角色？
- 能否指出自主決策節點？
- 能否指出 Human Review 節點？
- 能否知道資料與工具來源？
- 能否辨識 Agent 越權風險？
- 同一 VAD 是否能讓不同模型產生相近執行行為？

## 4. 實驗設計

### A 組：Prompt-first
由學員自行撰寫 Prompt。

### B 組：Skill-first
使用文字 Skill。

### C 組：Visual Promptless Skill
使用 Visual Skill Card。

### D 組：Promptless Agent + VAD
使用 Agent 與 VAD 完成需要動態決策的任務。

## 5. 注意

不要用固定、無決策的簡單任務證明 Agent 比 Skill 好；Agent 組應選真正需要動態判斷的任務，否則比較失真。
