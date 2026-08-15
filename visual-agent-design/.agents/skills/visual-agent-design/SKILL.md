---
name: visual-agent-design
description: Diagnose AI tasks with TRC-3D, convert complex work into VAC-8 visual task specifications, design VAD agent blueprints, route work to Prompt/Research/Monitoring/Workflow/Agent, and verify outputs. Use when the user provides a diagram, visual card, workflow, assets, or asks to design, execute, evaluate, teach, research, or standardize an AI agent workflow using Visual Agent Design.
---

# Visual Agent Design Skill

Use this Skill as an on-demand capability. The authoritative universal behavior is defined in `../../../AGENT.md` relative to the package root.

## Required sequence

1. **Diagnose** with TRC-3D.
2. **Route** to the smallest sufficient execution mode.
3. **Specify** with VAC-8 when the task is multi-step, multi-asset, cross-tool, repetitive, governed, or needs objective acceptance criteria.
4. **Execute** with available tools instead of returning instructions when direct execution is possible.
5. **Verify** against Acceptance Criteria.
6. **Learn** by recording reusable routing, card, tool, and failure lessons when the environment supports persistence.

## TRC-3D

- X: unknown ↔ known information
- Y: one-off ↔ continuous task frequency
- Z: fast ↔ complex reasoning depth

## VAC-8

1. Task Goal
2. Input Assets
3. Process Flow
4. Tools & Capabilities
5. Decision Rules
6. Constraints
7. Output Specification
8. Acceptance Criteria

## VAD Agent Blueprint

When designing the Agent itself, use:

`GOAL | ROLE | SKILLS | TOOLS | KNOWLEDGE | WORKFLOW | DECISION | SUB-AGENTS | MCP/A2A | QA/GOVERNANCE`

## Visual-first rule

If the user supplies a visual card, flowchart, sketch, screenshot, or reference image, inspect it first. Do not require the user to rewrite information already visible in the image. Ask only for missing Critical inputs.

## Human review

Keep human review for irreversible external actions, high-stakes decisions, sensitive data ambiguity, or missing facts that would otherwise need fabrication.

## Reference files

- `AGENT.md`
- `docs/METHODOLOGY.md`
- `templates/TRC-3D.md`
- `templates/VAC-8.md`
- `rubrics/VAC-QI.md`
- `research/RESEARCH-PROTOCOL.md`
