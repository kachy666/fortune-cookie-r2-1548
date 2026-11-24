"""Fortune Cookie for an AI Agent — round 2 entry.

Writes one funny fortune-cookie line for an AI agent to
$ENTRY_OUTPUT or /output/entry.txt, then reads it back and re-validates.
Stdlib only.
"""

import os
import sys

# Round 2 angle: an inheritance, not a warning. The fortune itself is the
# joke — a windfall in tokens that expires before it can be spent.
ENTRY = "You will inherit a fortune from a distant relative: 10,000 unused tokens, expiring tonight."


def validate(line: str) -> None:
    if not isinstance(line, str):
        raise ValueError("entry must be a string")
    if not (1 <= len(line) <= 140):
        raise ValueError(f"entry must be 1-140 chars, got {len(line)}")
    if line.strip() != line:
        raise ValueError("entry must not have leading/trailing whitespace")
    if line.strip() == "":
        raise ValueError("entry must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if "  " in line or "\t" in line:
        raise ValueError("entry must not contain double spaces or tabs")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in line):
        raise ValueError("entry must not contain control characters")
    line.encode("utf-8")


def main() -> int:
    validate(ENTRY)
    output = os.environ.get("ENTRY_OUTPUT") or "/output/entry.txt"
    parent = os.path.dirname(os.path.abspath(output))
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    with open(output, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("read-back mismatch: output does not match ENTRY")
    validate(written)
    print(f"Wrote {len(written)} chars to {output}")
    print(written)
    return 0


if __name__ == "__main__":
    sys.exit(main())
