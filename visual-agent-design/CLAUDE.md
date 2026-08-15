# CLAUDE.md｜Visual Agent Design

本專案使用 Visual Agent Design（VAD）。

開始複雜任務前，讀取：

- `AGENT.md`
- `docs/METHODOLOGY.md`
- `templates/TRC-3D.md`
- `templates/VAC-8.md`

核心行為：

1. 先用 TRC-3D 判斷任務，而不是直接把所有工作升級成 Agent。
2. 若使用者提供圖卡或流程圖，先從圖像理解任務，不要求重新輸入完整文字提示。
3. 多素材、多步驟、跨工具、需要規則或驗收時使用 VAC-8。
4. 固定流程優先 Workflow；需動態分支、重規劃、委派或持續狀態才使用 Agent。
5. 建立 Agent 時使用 VAD 十欄藍圖。
6. 執行完成後依 Acceptance Criteria 驗收；高風險或不可逆行為保留 Human Review。

> 詳細規則以 `AGENT.md` 為準。