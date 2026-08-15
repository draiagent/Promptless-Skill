# Visual Skill Card｜視覺技能卡規格

## 1. 定位

Visual Skill Card 不是單純資訊海報，而是 **Promptless Skill 的可視化人機介面**。

它應同時滿足：

1. Human-readable
2. AI-readable
3. Skill-mappable
4. Agent-upgradable

## 2. 六欄標準

| 欄位 | 問題 |
|---|---|
| TASK | 要完成什麼？ |
| INPUT | 要提供什麼？ |
| STYLE | 有哪些語言、品牌、格式或限制？ |
| PROCESS | 系統要怎麼做？ |
| OUTPUT | 要交付什麼？ |
| QA | 如何判定合格？ |

## 3. 建議卡片結構

```text
┌────────────────────────────┐
│ Skill 名稱 / Skill ID      │
├──────────────┬─────────────┤
│ TASK         │ INPUT       │
├──────────────┼─────────────┤
│ STYLE        │ PROCESS     │
├──────────────┼─────────────┤
│ OUTPUT       │ QA          │
└──────────────┴─────────────┘
```

## 4. Machine Metadata（選用）

```yaml
skill_id: ps-info-001
version: 1.0
language: zh-TW
task: infographic
input: auto-detect
output: png
qa:
  - content-accuracy
  - typo-check
  - layout-check
```

## 5. 升級為 Agent Card

如果卡片涉及自主決策，增加：

```text
GOAL
ROLE
SKILLS
TOOLS
KNOWLEDGE
DECISION
SUB-AGENTS
MCP / A2A
QA
```

此時卡片已從 Visual Skill Card 進入 VAD Agent Card。
