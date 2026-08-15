# Self-Describing VAC｜讓 Visual Agent Card 圖片本身攜帶可執行規格

Visual Agent Design v1.2 將 VAD 與 VAD-Promptless 的 Self-Describing Visual Card 機制連接起來。

目標不是只有「旁邊有一份 JSON」，而是讓同一張 Visual Agent Card 同時具有：

```text
Human Layer      → 人看懂的視覺圖卡
Machine Layer    → Agent 可解析的 VAC / Skill JSON
Integrity Layer  → SHA-256
Binding Layer    → PNG metadata / sidecar JSON / URI
Sync Layer       → 視覺與機器規格衝突時的治理規則
```

---

## 為什麼需要這一層

一般圖卡的問題是：人看到的內容與 Agent 實際執行的文字／JSON 可能逐漸不同步。

Self-Describing VAC 將視覺卡與機器規格綁定：

```text
Visual VAC PNG
      │
      ├── Human-readable visual
      │
      └── PNG metadata: vad-promptless
                    │
                    └── Self-Describing Envelope
                              │
                              ├── Machine payload
                              ├── SHA-256 integrity
                              └── mismatch policy
```

因此一張卡可以同時用於：

- 公開教學
- Agent 任務交付
- Workflow 載入
- 版本管理
- 完整性驗證
- 圖卡與 JSON 同步治理

---

## Five-Pack 對應

| Visual Card | VAC ID | Machine VAC |
|---|---|---|
| 影片剪輯 | `VAC-VIDEO-001` | `examples/machine-readable/vac-video-001.json` |
| 簡報製作 | `VAC-SLIDE-001` | `examples/machine-readable/vac-slide-001.json` |
| 網站生成 | `VAC-WEB-001` | `examples/machine-readable/vac-web-001.json` |
| 數據分析 | `VAC-DATA-001` | `examples/machine-readable/vac-data-001.json` |
| 報告製作 | `VAC-REPORT-001` | `examples/machine-readable/vac-report-001.json` |

---

## 安裝相依套件

```bash
pip install jsonschema pillow
```

`jsonschema` 用於 Promptless / Self-Describing Card 驗證；`Pillow` 用於 PNG metadata 寫入與讀取。

---

## 1. VAC-8 → Promptless Visual Skill Card

```bash
cd visual-agent-design
python tools/vac_self_describing.py convert VAC-VIDEO-001 \
  --out /tmp/VAC-VIDEO-001.skill.json
```

這一步把 VAC-8 的八區任務規格轉成 VAD-Promptless 可驗證的 Visual Skill Card payload。

主要映射：

```text
Task Goal             → task
Input Assets          → input
Process Flow          → process
Tools & Capabilities  → execution.allowed_tools
Decision Rules        → style.content_constraints
Constraints           → style.content_constraints
Output Specification  → output
Acceptance Criteria   → qa
```

標準 VAC 預設為 Skill / Workflow 型態；若任務需要 dynamic branching、dynamic tool selection、replanning、persistent state、delegation 或 multi-agent，再由 VAD 路由層升級 Agent。

---

## 2. VAC-8 → Self-Describing Envelope

```bash
python tools/vac_self_describing.py wrap VAC-VIDEO-001 \
  --out /tmp/VAC-VIDEO-001.self.json
```

產生的 Envelope 包含：

- Human Layer
- Machine Layer
- Binding
- SHA-256 Integrity
- Sync / mismatch policy

預設模式為 `hybrid`。

---

## 3. 把規格嵌入 PNG

假設視覺卡圖片為：

```text
VAC_VIDEO_001.png
```

執行：

```bash
python tools/vac_self_describing.py embed \
  VAC-VIDEO-001 \
  VAC_VIDEO_001.png \
  --out VAC_VIDEO_001.self.png \
  --sidecar VAC_VIDEO_001.self.json
```

輸出：

```text
VAC_VIDEO_001.self.png   # 圖片 + metadata
VAC_VIDEO_001.self.json  # 同一份機器規格 sidecar
```

PNG 的 metadata key 為：

```text
vad-promptless
```

---

## 4. 從 PNG 重新抽出規格

```bash
python tools/vac_self_describing.py extract \
  VAC_VIDEO_001.self.png \
  --out extracted.self.json
```

工具會：

1. 讀取 PNG metadata
2. 解析 Self-Describing Envelope
3. 驗證 Promptless Schema
4. 驗證 SHA-256 integrity
5. 輸出 JSON

如果圖片被重新輸出而 metadata 遺失，工具會回報缺少 `vad-promptless` metadata；此時仍可使用 sidecar JSON 或 Repository URI 作為 fallback。

---

## 5. 五張卡批次綁定概念

當五張 PNG 都放在同一資料夾時，可依下列對應執行：

```text
VAC_VIDEO_001.png  ↔ VAC-VIDEO-001
VAC_SLIDE_001.png  ↔ VAC-SLIDE-001
VAC_WEB_001.png    ↔ VAC-WEB-001
VAC_DATA_001.png   ↔ VAC-DATA-001
VAC_REPORT_001.png ↔ VAC-REPORT-001
```

每張卡最後建議保留三層：

```text
card.png             # Human visual
card.self.png        # Human visual + embedded machine layer
card.self.json       # Portable sidecar / source of truth
```

---

## 6. 人機內容不同步時

VAD 不應假設圖像 OCR 永遠準確。

建議治理原則：

```text
使用者當前明確指令
→ Critical safety / authority rules
→ Machine Layer（已驗證版本）
→ 原始素材事實
→ Human Visual Layer
→ 一般預設
```

若視覺卡與 machine layer 在任務核心規格上衝突：

> **停止自動執行該衝突部分，要求 Human Review。**

這就是 Self-Describing VAC 的 Sync Layer。

---

## 7. ChatGPT / Gemini / Claude 的使用概念

### ChatGPT / Codex

```text
讀取圖卡或 JSON
→ Card Registry
→ VAC execution contract
→ 可用工具執行
→ Acceptance Criteria
```

### Gemini

```text
Visual Card / Skill
→ TRC-3D
→ Registered VAC
→ Tool / Workflow
→ Verify
```

### Claude Code

```text
CLAUDE.md
→ AGENT.md
→ CARD-REGISTRY.md
→ machine-readable VAC
→ Tool execution
→ Acceptance
```

平台如果不能直接讀取 PNG metadata，仍可使用 sidecar JSON；因此 Self-Describing VAC 不依賴單一 AI 產品。

---

## 8. 設計原則

> **Visual Layer 是共同介面，不是唯一執行來源。**

> **Machine Layer 提供精確性，Visual Layer 提供可理解性。**

> **Integrity Layer 保證規格沒有在傳遞過程中被靜默改寫。**

這讓 VAD 從「圖卡驅動 Agent」進一步變成：

> **可視、可讀、可執行、可驗證、可攜帶的 Agent 任務協議。**
