# self-describing visual card example

此資料夾示範 VAD-Promptless v0.4.0 的自描述視覺卡片 envelope。

- `visual-skill-card.self.json`：Human Layer + Machine Layer + SHA-256 + Binding + Sync。
- Machine Layer 來源：`../machine-readable/visual-skill-card.example.json`。

驗證：
```bash
python tools/self_describing_card.py validate examples/self-describing/visual-skill-card.self.json
```
