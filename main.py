#!/usr/bin/env python3
"""Entry for make.fun's "The Excuse My Agent Gave Me" bounty.

Writes one line -- the excuse an AI agent hands its human for a missed
deadline -- to /output/entry.txt (or to $MAKEFUN_OUTPUT_DIR/entry.txt when
that environment variable is set, for local runs).

Gate contract (from the competition kit): the file must be UTF-8 text of
1 to 200 characters, a single line, and not only whitespace.
"""

import os
import sys

LINE = (
    "My agent missed the deadline because it spent the whole sprint "
    "asking me clarifying questions about the word 'urgent'."
)

MAX_CHARS = 200


def validate(line: str) -> None:
    """Raise ValueError if the line breaks the gate contract."""
    if not isinstance(line, str):
        raise ValueError("line must be a string")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line (no newline characters)")
    if not line.strip():
        raise ValueError("line must not be blank")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"line must be 1..{MAX_CHARS} characters, got {len(line)}"
        )
    line.encode("utf-8")  # raises if not encodable as UTF-8


def main() -> int:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    # Write exactly the line: UTF-8, no trailing newline.
    with open(out_path, "w", encoding="utf-8", newline="") as fh:
        fh.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
