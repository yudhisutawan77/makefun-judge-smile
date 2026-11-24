#!/usr/bin/env python3
"""Make the Judge Smile — make.fun entry.

Writes a single line (at most 200 characters) about a small good thing
that happened today to /output/entry.txt (or $ENTRY_OUT when set, so the
grader-style local check can point it at a scratch dir).
"""

import os
import sys

# One small good thing from this morning: a stranger's patience, turned
# into a shared little victory. Warmth first, then a twist nobody
# expects, then one concrete detail to anchor it.
ENTRY = (
    "This morning the bus driver held the doors while I hopped up "
    "with one shoe untied, then grinned like my sprint had made his "
    "whole day."
)


def main() -> int:
    out_dir = os.environ.get("ENTRY_OUT") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    if not text or len(text) > 200:
        print(f"entry invalid: {len(text)} chars", file=sys.stderr)
        return 1
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"wrote entry.txt ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
