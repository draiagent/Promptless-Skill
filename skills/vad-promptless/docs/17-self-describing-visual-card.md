# self-describing visual card｜自描述視覺卡片

VAD-Promptless v0.4.0 將一張視覺卡片拆成四層：

1. **human layer**：給人閱讀與教學。
2. **machine layer**：完整 skill card 或 vad agent card JSON，給 AI / Agent 執行。
3. **integrity layer**：以 sha256 綁定 machine payload。
4. **binding layer**：png metadata、sidecar JSON、URI 或 QR reference。

執行時以 machine layer 為機器規格來源；human / machine 不一致時依 sync policy 拒絕或要求 human review。

```bash
python tools/self_describing_card.py wrap examples/machine-readable/visual-skill-card.example.json --out card.self.json
python tools/self_describing_card.py validate card.self.json
python tools/png_card_metadata.py embed card.png card.self.json --out card.self.png
```
