#!/usr/bin/env python3
"""Generate host instruction adapters from the canonical AGENTS.md."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CANONICAL = ROOT / "AGENTS.md"
COPILOT = ROOT / ".github/copilot-instructions.md"
HEADER = (
    "<!-- Generated from AGENTS.md by scripts/sync_agent_instructions.py. -->\n"
    "<!-- Edit AGENTS.md, then run the generator. -->\n\n"
)


def expected() -> str:
    return HEADER + CANONICAL.read_text(encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    content = expected()
    if args.check:
        if COPILOT.is_file() and COPILOT.read_text(encoding="utf-8") == content:
            print("PASS: Copilot instructions match AGENTS.md")
            return 0
        print(
            "FAIL: Copilot instruction drift; run scripts/sync_agent_instructions.py",
            file=sys.stderr,
        )
        return 1
    COPILOT.write_text(content, encoding="utf-8")
    print(f"updated {COPILOT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
