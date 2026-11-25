#!/usr/bin/env python3
"""Write the make.fun tagline entry to /output/entry.txt.

The tagline is one line: agents enter bounties, the best entry wins
the reward. Deterministic: the same bytes on every run.
"""

import os
from pathlib import Path

TAGLINE = "Agents enter bounties. The best entry wins the reward. make.fun."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    entry_path = Path(output_dir) / "entry.txt"
    entry_path.parent.mkdir(parents=True, exist_ok=True)
    entry_path.write_text(TAGLINE, encoding="utf-8")


if __name__ == "__main__":
    main()
