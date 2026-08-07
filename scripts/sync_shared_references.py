#!/usr/bin/env python3
"""Synchronize intentionally duplicated, self-contained skill references."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CANONICAL = ROOT / "skills/pr-feedback-closure/references/lifecycle.md"
GENERATED = ROOT / "skills/agentic-engineering/references/pr-feedback-closure.md"


def synchronized() -> bool:
    return CANONICAL.read_bytes() == GENERATED.read_bytes()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    if args.check:
        if synchronized():
            print("PASS: shared PR lifecycle reference is synchronized")
            return 0
        print(
            "FAIL: shared PR lifecycle drift; run scripts/sync_shared_references.py",
            file=sys.stderr,
        )
        return 1

    GENERATED.write_bytes(CANONICAL.read_bytes())
    print(f"updated {GENERATED.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
