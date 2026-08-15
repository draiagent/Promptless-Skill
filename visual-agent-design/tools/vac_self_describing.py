#!/usr/bin/env python3
"""Bridge VAC-8 cards into VAD-Promptless self-describing visual cards.

This tool turns a machine-readable VAC-8 JSON card into the existing
VAD-Promptless Visual Skill Card payload, optionally wraps it in the
Self-Describing Visual Card envelope and can embed that envelope into PNG
metadata.

Examples:
  python tools/vac_self_describing.py convert VAC-VIDEO-001 --out /tmp/video.skill.json
  python tools/vac_self_describing.py wrap VAC-VIDEO-001 --out /tmp/video.self.json
  python tools/vac_self_describing.py embed VAC-VIDEO-001 card.png --out card.self.png --sidecar card.self.json
  python tools/vac_self_describing.py extract card.self.png --out extracted.self.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

VAD_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = VAD_ROOT.parent
PROMPTLESS_TOOLS = REPO_ROOT / "skills" / "vad-promptless" / "tools"

if str(PROMPTLESS_TOOLS) not in sys.path:
    sys.path.insert(0, str(PROMPTLESS_TOOLS))

import promptless_card  # type: ignore  # noqa: E402
import self_describing_card as sdc  # type: ignore  # noqa: E402

from vac_runner import basic_validate, card_path, load_json  # noqa: E402

METADATA_KEY = "vad-promptless"


def normalize_version(value: str | None) -> str:
    raw = str(value or "1.0.0")
    parts = raw.split(".")
    while len(parts) < 3:
        parts.append("0")
    return ".".join(parts[:3])


def infer_input_type(name: str) -> str:
    text = name.lower()
    if any(k in text for k in ("影片", "video", "mp4", "mov")):
        return "video"
    if any(k in text for k in ("音訊", "音樂", "audio", "mp3", "wav")):
        return "audio"
    if any(k in text for k in ("圖片", "圖示", "logo", "image", "png", "jpg", "jpeg")):
        return "image"
    if any(k in text for k in ("excel", "csv", "試算表", "spreadsheet", "資料檔")):
        return "spreadsheet"
    if any(k in text for k in ("pdf",)):
        return "pdf"
    if any(k in text for k in ("逐字稿", "文件", "文案", "資料", "報告", "docx", "document", "文字")):
        return "document"
    if any(k in text for k in ("網址", "url", "網站", "reference site")):
        return "url"
    return "file"


def output_format_string(spec: dict[str, Any]) -> str:
    fmt = spec.get("format")
    if isinstance(fmt, list):
        return ", ".join(map(str, fmt))
    return str(fmt or "unspecified")


def qa_method(criterion: str) -> str:
    text = criterion.lower()
    if any(k in text for k in ("開啟", "播放", "重算", "公式", "程式", "解碼", "頁數", "時長")):
        return "tool"
    return "model"


def severity_to_promptless(value: str | None) -> str:
    return {
        "critical": "blocker",
        "major": "warning",
        "minor": "info",
    }.get(str(value or "major").lower(), "warning")


def vac_to_skill(vac: dict[str, Any]) -> dict[str, Any]:
    errors = basic_validate(vac)
    if errors:
        raise ValueError("Invalid VAC-8:\n" + "\n".join(f"- {e}" for e in errors))

    goal = vac["task_goal"]
    inputs = vac.get("input_assets", {})
    output_spec = vac.get("output_specification", {})

    promptless_inputs: list[dict[str, Any]] = []
    for required in (True, False):
        key = "required" if required else "optional"
        for name in inputs.get(key, []):
            promptless_inputs.append(
                {
                    "name": str(name),
                    "type": infer_input_type(str(name)),
                    "required": required,
                }
            )

    if not promptless_inputs:
        promptless_inputs.append({"name": "task_input", "type": "file", "required": True})

    process = []
    for step in vac.get("process_flow", []):
        process.append(
            {
                "id": str(step["id"]),
                "name": str(step.get("action", step["id"])),
                "action": str(step["action"]),
                "on_failure": "human_review" if "Critical" in str(step.get("checkpoint", "")) else "stop",
            }
        )

    deliverables = output_spec.get("deliverables") or ["final_output"]
    fmt_string = output_format_string(output_spec)
    artifacts = [
        {
            "name": str(name),
            "type": "file",
            "format": fmt_string,
            "required": True,
        }
        for name in deliverables
    ]

    qa_checks = []
    for index, item in enumerate(vac.get("acceptance_criteria", []), start=1):
        criterion = str(item.get("criterion", f"check_{index}"))
        qa_checks.append(
            {
                "id": f"QA{index:02d}",
                "criterion": criterion,
                "severity": severity_to_promptless(item.get("severity")),
                "method": qa_method(criterion),
            }
        )

    allowed_tools = [
        str(item.get("tool"))
        for item in vac.get("tools_capabilities", [])
        if item.get("tool")
    ]

    content_constraints = [str(item.get("rule")) for item in vac.get("constraints", []) if item.get("rule")]
    for rule in vac.get("decision_rules", []):
        content_constraints.append(f"IF {rule['if']} THEN {rule['then']}")

    human_review = vac.get("human_review", {})
    card = {
        "schema_version": "0.3.0",
        "card_type": "skill",
        "id": str(vac.get("card_id") or goal["name"]).replace(" ", "-"),
        "name": str(goal["name"]),
        "description": str(goal["primary_goal"]),
        "language": "zh-TW",
        "metadata": {
            "version": normalize_version(vac.get("version")),
            "author": "draiagent",
            "license": "MIT",
            "tags": ["VAD", "VAC-8", "Visual-Agent-Card"],
        },
        "task": {
            "objective": str(goal["primary_goal"]),
            "task_type": str(vac.get("card_id", "VAC")),
            "success_definition": str(goal["completion_definition"]),
        },
        "input": promptless_inputs,
        "style": {
            "language": str(output_spec.get("language", "繁體中文")),
            "brand": str(output_spec.get("brand", "依使用者提供之品牌規範")),
            "format_constraints": [str(output_spec.get("size_or_duration", "")), fmt_string],
            "content_constraints": content_constraints,
        },
        "process": process,
        "output": {
            "artifacts": artifacts,
            "delivery": str(output_spec.get("naming_rule", "依任務輸出規格命名")),
        },
        "qa": {
            "checks": qa_checks,
            "pass_policy": "all_blockers",
        },
        "execution": {
            "autonomy_level": 2,
            "dynamic_branching": False,
            "dynamic_tool_selection": False,
            "replanning": False,
            "persistent_state": False,
            "delegation": False,
            "multi_agent": False,
            "external_side_effects": False,
            "human_approval_required": bool(human_review.get("required", False)),
            "allowed_tools": allowed_tools,
        },
        "upgrade_policy": {
            "allow_agent_upgrade": True,
            "mode": "suggest",
            "forced_reasons": [],
        },
    }

    promptless_card.validate(card)
    return card


def resolve_vac(value: str) -> tuple[Path, dict[str, Any]]:
    candidate = Path(value)
    if candidate.exists():
        path = candidate.resolve()
    elif (VAD_ROOT / value).exists():
        path = (VAD_ROOT / value).resolve()
    else:
        path = card_path(value)
    return path, load_json(path)


def write_json(obj: dict[str, Any], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def embed_png(image_path: Path, envelope: dict[str, Any], out_path: Path) -> None:
    try:
        from PIL import Image, PngImagePlugin
    except ImportError as exc:
        raise RuntimeError("PNG embedding requires Pillow: pip install pillow") from exc

    sdc.validate_envelope(envelope)
    image = Image.open(image_path).convert("RGBA")
    metadata = PngImagePlugin.PngInfo()
    for key, value in getattr(image, "info", {}).items():
        if isinstance(value, str) and key != METADATA_KEY:
            metadata.add_itxt(key, value)
    metadata.add_itxt(
        METADATA_KEY,
        json.dumps(envelope, ensure_ascii=False, separators=(",", ":")),
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    image.save(out_path, "PNG", pnginfo=metadata)


def extract_png(image_path: Path) -> dict[str, Any]:
    try:
        from PIL import Image
    except ImportError as exc:
        raise RuntimeError("PNG extraction requires Pillow: pip install pillow") from exc

    raw = Image.open(image_path).info.get(METADATA_KEY)
    if not raw:
        raise ValueError(f"PNG missing metadata key: {METADATA_KEY}")
    envelope = json.loads(raw)
    sdc.validate_envelope(envelope)
    return envelope


def cmd_convert(args: argparse.Namespace) -> int:
    _, vac = resolve_vac(args.vac)
    payload = vac_to_skill(vac)
    write_json(payload, args.out)
    print(args.out)
    return 0


def cmd_wrap(args: argparse.Namespace) -> int:
    _, vac = resolve_vac(args.vac)
    payload = vac_to_skill(vac)
    envelope = sdc.wrap(payload, mode=args.mode, reference_uri=args.reference_uri)
    write_json(envelope, args.out)
    print(args.out)
    return 0


def cmd_embed(args: argparse.Namespace) -> int:
    _, vac = resolve_vac(args.vac)
    payload = vac_to_skill(vac)
    envelope = sdc.wrap(payload, mode="hybrid", reference_uri=args.reference_uri)
    embed_png(args.image, envelope, args.out)
    if args.sidecar:
        write_json(envelope, args.sidecar)
    print(args.out)
    return 0


def cmd_extract(args: argparse.Namespace) -> int:
    envelope = extract_png(args.image)
    write_json(envelope, args.out)
    print(args.out)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="VAC-8 to self-describing visual card bridge")
    sub = parser.add_subparsers(dest="command", required=True)

    p_convert = sub.add_parser("convert", help="Convert VAC-8 JSON to Promptless Visual Skill Card")
    p_convert.add_argument("vac")
    p_convert.add_argument("--out", type=Path, required=True)
    p_convert.set_defaults(func=cmd_convert)

    p_wrap = sub.add_parser("wrap", help="Convert and wrap VAC as Self-Describing Visual Card JSON")
    p_wrap.add_argument("vac")
    p_wrap.add_argument("--out", type=Path, required=True)
    p_wrap.add_argument("--mode", choices=["embedded", "sidecar", "reference", "hybrid"], default="hybrid")
    p_wrap.add_argument("--reference-uri")
    p_wrap.set_defaults(func=cmd_wrap)

    p_embed = sub.add_parser("embed", help="Embed converted self-describing card into PNG metadata")
    p_embed.add_argument("vac")
    p_embed.add_argument("image", type=Path)
    p_embed.add_argument("--out", type=Path, required=True)
    p_embed.add_argument("--sidecar", type=Path)
    p_embed.add_argument("--reference-uri")
    p_embed.set_defaults(func=cmd_embed)

    p_extract = sub.add_parser("extract", help="Extract and validate self-describing metadata from PNG")
    p_extract.add_argument("image", type=Path)
    p_extract.add_argument("--out", type=Path, required=True)
    p_extract.set_defaults(func=cmd_extract)

    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        return args.func(args)
    except Exception as exc:  # CLI boundary
        print(json.dumps({"error": str(exc)}, ensure_ascii=False, indent=2), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
