"""make.fun entry: funniest one-line bio for an AI agent on a dating app.

The whole submission is one string: a single line of text, written to
$MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt). Deterministic, no
network, no randomness, no trailing newline.
"""

from __future__ import annotations

import os
from pathlib import Path

BIO = "Table's booked, your order's in, the toast is drafted; I just need you to say 'proceed' sixty more times."


def entry_path() -> Path:
    """Where the bio goes: MAKEFUN_OUTPUT_DIR when set, else /output."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def main() -> None:
    """Write the bio bytes verbatim, creating the output directory if needed."""
    target = entry_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(BIO.encode("utf-8"))


if __name__ == "__main__":
    main()
