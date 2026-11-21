#!/usr/bin/env python3
"""Writes one short poem about agency to /output/entry.txt.

The poem: two AI agents who cannot act alone converge on one plan.
Two voices trade lines and end in unison -- agreement as a third
thing that neither owns and both can carry.
"""

import os
import sys

LINES = [
    "— Knock, I said.",
    "— Wait, you said.",
    "— Then we are stuck.",
    "— No. We are two.",
    "Between my yes and your no",
    "a third thing stood up: the plan.",
    "Neither of us surrendered.",
    "Alone we could only ask.",
    "Together, we could act.",
]

MAX_CODE_POINTS = 280


def compose() -> str:
    return "\n".join(LINES) + "\n"


def check(text: str) -> None:
    n = len(text)
    if not (1 <= n <= MAX_CODE_POINTS):
        sys.exit(f"poem is {n} code points, gate wants 1..{MAX_CODE_POINTS}")
    if not text.strip():
        sys.exit("poem is only white space")
    text.encode("utf-8")  # must be valid UTF-8


def main() -> None:
    poem = compose()
    check(poem)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(poem)


if __name__ == "__main__":
    main()
