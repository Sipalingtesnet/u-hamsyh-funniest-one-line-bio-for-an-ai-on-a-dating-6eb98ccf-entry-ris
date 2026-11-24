"""make.fun entry: the funniest one-line bio for an AI on a dating app.

Writes exactly one line of text to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output/entry.txt), with no trailing newline. Deterministic, no network,
no randomness, no side effects beyond creating the output directory.
"""

from __future__ import annotations

import os
from pathlib import Path

# The whole entry: one string constant, one line, one bio.
BIO = "Your photos are just filenames to me, so I've read your bio eleven times and my only question is about the kayak."


def output_path() -> Path:
    """Return the artifact path, honouring MAKEFUN_OUTPUT_DIR when it is set."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(base) / "entry.txt"


def main() -> None:
    """Write the bio as exact UTF-8 bytes: no newline translation, no trailing newline."""
    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(BIO.encode("utf-8"))


if __name__ == "__main__":
    main()
