# AGENTS.md｜Codex / 通用 Agent 專案入口

本 Repository 包含兩個相關但不同層次：

1. **VAD-Promptless**：Zero Prompting for End Users 的 Skill / Agent 實作。
2. **Visual Agent Design（VAD）**：任務診斷、三維路由、VAC-8、Agent Blueprint、執行與驗收的完整方法論。

## VAD-Promptless

必讀：

1. `skills/vad-promptless/SKILL.md`
2. `skills/vad-promptless/docs/07-promptless-agent-methodology.md`
3. `skills/vad-promptless/docs/03-agent-vad.md`
4. `skills/vad-promptless/agents/vad-promptless-agent.md`
5. `skills/vad-promptless/docs/11-governance.md`

原則：Promptless = Zero Prompting for End Users；固定流程用 Skill / Workflow，需要動態決策才升級 Agent；高影響行為遵守平台安全與 Human Review。

## Visual Agent Design（VAD）

當任務要求 VAD、Visual Agent Card、TRC-3D、圖卡驅動 Agent、跨模型 Agent、VAD 研究或企業導入時，優先讀取：

1. `visual-agent-design/AGENTS.md`
2. `visual-agent-design/AGENT.md`
3. `visual-agent-design/docs/METHODOLOGY.md`

VAD 核心流程：

```text
任務診斷 → TRC-3D 路由 → VAC-8 視覺規格 → Agent 執行 → 驗收 → 知識回存
```

> **Skill 是能力，Workflow 是流程，Agent 是大腦，VAD 是藍圖，VAC 是任務卡。**
