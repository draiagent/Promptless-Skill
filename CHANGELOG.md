# Changelog

## 0.5.0 - 2026-08-16

### Repo Separation

- 將 **Visual Agent Design Core** 正式拆分至獨立 Repository：`draiagent/Visual-Agent-Design`。
- `Visual-Agent-Design` 成為 TRC-3D、VAC-8、Standard VAC Five-Pack、VAD Agent Blueprint、Routing、QA 與 Research Protocol 的唯一 Source of Truth。
- 自本 Repo 移除重複的 `visual-agent-design/` 目錄，避免雙份規格與版本漂移。
- 移除 Claude / Gemini 中重複的 `visual-agent-design-agent.md`。
- 移除依賴舊 VAD Five-Pack 本地目錄的 CI workflow。
- 重寫 `README.md`、`AGENTS.md`、`CHATGPT.md`、`CLAUDE.md`、`GEMINI.md`，將本 Repo 收斂為 VAD Promptless Companion Project。
- 正式建立 **VAD Promptless Bridge** 定位：VAD Core Spec → Promptless / Self-Describing / Zero-Prompt UX。
- 保留 Promptless Skill、Visual Card Parser、Machine-readable Card、Self-Describing Visual Card、PNG metadata、sidecar JSON 與 SHA-256 等原生能力。

## 0.4.0 - 2026-08-16

- 專案品牌改為 **VAD-Promptless**；機器識別值使用 `vad-promptless`。
- 修正大小寫：`SKILL.md`、`AGENTS.md`、`CLAUDE.md`、`GEMINI.md`、`README.md`、`LICENSE` 保留標準檔名。
- 可安裝技能移至 `skills/vad-promptless/SKILL.md`，使 `name: vad-promptless` 與父資料夾一致。
- 新增 Linux CI 大小寫驗證。
- Agent 定義統一為 `vad-promptless-agent.md`。
- 新增 Self-Describing Visual Card：Human + Machine + Integrity + Binding + Sync。
- 新增 SHA-256、`vadp://` URI、PNG metadata round-trip。
- Schema `$id` 更新為 `draiagent/VAD-Promptless` 與巢狀 schema 路徑。

## 0.3.1 - 2026-08-16
- 新增 Visual Card Parser、Extraction Schema、跨模型視覺 Adapter 與測試。

## 0.3.0 - 2026-08-16
- 新增 Machine-readable Skill / Agent Schema、分類器與 Compiler。

## 0.2.0 - 2026-08-15
- 擴充為 Skill × Agent × VAD 方法論。

## 0.1.0 - 2026-08-15
- 建立 Promptless Skill 初始方法論。
