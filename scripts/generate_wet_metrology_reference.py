#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from energy_lab.wet_metrology import reference_snapshot

DEFAULT = Path("lab/experiments/EXP-WET-001/reference/R077-metrology-gate.json")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    text = json.dumps(reference_snapshot(), indent=2, sort_keys=True) + "\n"
    if args.check:
        if not args.output.exists() or args.output.read_text(encoding="utf-8") != text:
            raise SystemExit(f"stale deterministic artifact: {args.output}")
        print(f"reference artifact OK: {args.output}")
        return 0
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(text, encoding="utf-8")
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
