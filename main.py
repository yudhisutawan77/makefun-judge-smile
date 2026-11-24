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
#
# The line is assembled from fragments so the entry text lives in one
# place (build_entry) and everything else just validates and saves it.
ENTRY_FRAGMENTS = (
    "This morning the bus driver held the doors while I hopped ",
    "up with one shoe untied, then grinned like my sprint had ",
    "made his whole day.",
)


def build_entry() -> str:
    """Join the fragments into the single entry line."""
    return "".join(ENTRY_FRAGMENTS).strip()


def check_entry(line: str) -> bool:
    """An entry is valid when it is non-empty and at most 200 chars."""
    return 0 < len(line) <= 200


def save_entry(line: str, destination_dir: str) -> str:
    """Write the entry line to entry.txt inside destination_dir."""
    os.makedirs(destination_dir, exist_ok=True)
    target = os.path.join(destination_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")
    return target


def resolve_destination() -> str:
    """Where the entry goes: $ENTRY_OUT wins, else /output."""
    return os.environ.get("ENTRY_OUT") or "/output"


def main() -> int:
    destination = resolve_destination()
    line = build_entry()
    if not check_entry(line):
        print(f"entry invalid: {len(line)} chars", file=sys.stderr)
        return 1
    target = save_entry(line, destination)
    print(f"wrote {target} ({len(line)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
