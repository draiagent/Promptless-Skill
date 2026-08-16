# AGENTS.md｜Codex / 通用 Agent 專案入口

## Repository Mission

本 Repository 只負責 **VAD-Promptless**：Zero Prompting for End Users、Visual Card Parsing、Promptless Skill / Workflow / Agent、Self-Describing Visual Card 與跨模型 Promptless 執行。

完整 Visual Agent Design（VAD）Core 已獨立維護於：

https://github.com/draiagent/Visual-Agent-Design

> **Visual-Agent-Design 是 VAD Core 的唯一 Source of Truth。**

## Required Local Sources

執行本 Repo 任務時優先讀取：

1. `skills/vad-promptless/SKILL.md`
2. `skills/vad-promptless/docs/07-promptless-agent-methodology.md`
3. `skills/vad-promptless/agents/vad-promptless-agent.md`
4. `skills/vad-promptless/docs/11-governance.md`

## Core Rules

- Promptless = Zero Prompting for End Users。
- 不要求使用者重寫圖片、附件或上下文中已經存在的需求。
- 固定流程優先使用 Skill / Workflow。
- 只有需要動態決策、重新規劃、動態選工具、持續狀態或委派時才升級 Agent。
- 圖卡進入執行前，優先正規化為可驗證 Machine Layer。
- Self-Describing Card 應驗證 schema、payload 與 SHA-256。
- Human Layer 與 Machine Layer 重大衝突時，需要 Human Review。
- 高影響、敏感資料、不可逆外部行為遵守平台安全與確認機制。

## VAD Core Boundary

當任務涉及以下內容：

- TRC-3D
- VAC-8
- Standard VAC Five-Pack
- VAD Agent Blueprint
- VAD Core Routing
- VAD Core Research Protocol
- VAD Core Governance Standard

不要在本 Repository 重新建立第二套標準。

應使用上游：

https://github.com/draiagent/Visual-Agent-Design

若上游資料沒有被載入目前工作環境，明確指出 dependency，而不是引用已移除的本地 `visual-agent-design/` 路徑。

## Promptless Bridge

```text
VAD / Skill / Task Spec
→ Promptless Bridge
→ Visual / Machine Representation
→ Integrity Validation
→ Skill / Workflow / Agent
→ QA / Human Review
```

## Completion Check

完成前確認：

- 使用者沒有被迫重寫已有需求。
- 選擇最低足夠的 Skill / Workflow / Agent 層級。
- Machine Layer 可驗證。
- 失敗條件與 Human Review 已處理。
- 沒有把 VAD Core 規格偷偷 fork 成本地第二版本。
- 輸出可直接使用或明確說明缺少的必要依賴。
