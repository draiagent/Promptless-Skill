import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOL = ROOT / "tools" / "vac_self_describing.py"

spec = importlib.util.spec_from_file_location("vac_self_describing", TOOL)
assert spec and spec.loader
bridge = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bridge)


class SelfDescribingBridgeTest(unittest.TestCase):
    def setUp(self):
        self.cards = [
            "VAC-VIDEO-001",
            "VAC-SLIDE-001",
            "VAC-WEB-001",
            "VAC-DATA-001",
            "VAC-REPORT-001",
        ]

    def test_all_five_cards_convert_to_promptless_skill(self):
        for card_id in self.cards:
            with self.subTest(card_id=card_id):
                _, vac = bridge.resolve_vac(card_id)
                payload = bridge.vac_to_skill(vac)
                self.assertEqual(payload["card_type"], "skill")
                self.assertEqual(payload["id"], card_id)
                self.assertTrue(payload["process"])
                self.assertTrue(payload["qa"]["checks"])
                bridge.promptless_card.validate(payload)

    def test_all_five_cards_wrap_as_self_describing_envelope(self):
        for card_id in self.cards:
            with self.subTest(card_id=card_id):
                _, vac = bridge.resolve_vac(card_id)
                payload = bridge.vac_to_skill(vac)
                envelope = bridge.sdc.wrap(payload, mode="hybrid")
                self.assertEqual(envelope["id"], card_id)
                self.assertEqual(envelope["binding"]["metadata_key"], "vad-promptless")
                self.assertIn("png-metadata", envelope["binding"]["carriers"])
                bridge.sdc.validate_envelope(envelope)

    def test_embed_and_extract_round_trip(self):
        try:
            from PIL import Image
        except ImportError:
            self.skipTest("Pillow not installed")

        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            source = tmp / "source.png"
            output = tmp / "self.png"
            Image.new("RGB", (64, 64), "white").save(source)

            _, vac = bridge.resolve_vac("VAC-VIDEO-001")
            payload = bridge.vac_to_skill(vac)
            envelope = bridge.sdc.wrap(payload, mode="hybrid")
            bridge.embed_png(source, envelope, output)

            extracted = bridge.extract_png(output)
            self.assertEqual(extracted["id"], "VAC-VIDEO-001")
            self.assertEqual(
                extracted["integrity"]["payload_sha256"],
                envelope["integrity"]["payload_sha256"],
            )

    def test_converted_payload_is_serializable(self):
        _, vac = bridge.resolve_vac("VAC-DATA-001")
        payload = bridge.vac_to_skill(vac)
        rendered = json.dumps(payload, ensure_ascii=False)
        self.assertIn("VAC-DATA-001", rendered)


if __name__ == "__main__":
    unittest.main()
