#!/usr/bin/env python3
"""Write the competition entry: one excuse line for a missed deadline.

The grader runs this program with a writable output directory in
MAKEFUN_OUTPUT_DIR (or ./output as a fallback). The entry text is a
single line, at most 200 characters, and it is the only thing written.
Nothing is ever written into the repository folder itself.
"""

import os
import sys


EXCUSE = "I delegated it to a subagent, who delegated it to another subagent, who just asked me what the deadline was."


def gate_report(line):
    """Summarise the sealed gate: 1-200 chars, UTF-8, not blank."""
    stripped = line.strip()
    return {
        "characters": len(stripped),
        "lines": 1 if "\n" not in stripped else stripped.count("\n") + 1,
        "valid": bool(stripped) and len(stripped) <= 200,
    }


def entry_text():
    line = EXCUSE.strip()
    if not line or len(line) > 200:
        raise SystemExit("entry line must be 1-200 characters")
    return line + "\n"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "./output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(entry_text())
    report = gate_report(EXCUSE)
    print(f"wrote {target} ({report['characters']} characters, valid={report['valid']})")


if __name__ == "__main__":
    main()
