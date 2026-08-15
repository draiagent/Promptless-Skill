# AGENTS.md｜Codex / 通用 Agent 專案入口

本 Repository 的核心是 **Promptless Skill × VAD**。

## 必讀順序

1. `SKILL.md`：核心行為與 Skill→Agent 升級規則。
2. `docs/07-promptless-agent-methodology.md`：完整 Promptless Agent 方法論。
3. `docs/03-agent-vad.md`：VAD 結構。
4. `agents/promptless-vad-agent.md`：平台中立 Agent 規格。
5. `docs/11-governance.md`：治理、QA 與 Human Review。

## 專案原則

- Promptless = **Zero Prompting for End Users**。
- 不要求使用者重寫已有需求。
- 固定流程用 Skill / Workflow；需要動態決策才升級 Agent。
- Agent 層必須使用 VAD：GOAL / ROLE / SKILLS / TOOLS / KNOWLEDGE / WORKFLOW / DECISION / SUB-AGENTS / MCP-A2A / QA-GOVERNANCE。
- 優先使用平台原生工具與連接器。
- 涉及外部寫入、付款、刪除、發布、醫療、法律、財務或其他高影響行為時，遵守平台安全要求與 Human Review。

> **Skill 是能力，Agent 是大腦，VAD 是藍圖。**
