# Machine-readable Schema｜機器可讀卡片規格

VAD-Promptless v0.4.0 將 Visual Skill Card 與 VAD Agent Card 提升為人與 AI/Agent 共用的資料契約。

核心檔案：
- `schemas/visual-skill-card.schema.json`
- `schemas/vad-agent-card.schema.json`
- `schemas/promptless-card.schema.json`
- `schemas/self-describing-visual-card.schema.json`

管線：
`Visual Card → Normalized JSON → Schema Validation → Skill/Agent Classifier → SKILL.md / VAD Agent → Platform Adapter`

原則：固定流程保持 Skill；動態決策才升級 Agent；外部寫入與高風險操作必須顯式治理。
