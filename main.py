#!/usr/bin/env python3
"""Write the make.fun tagline entry to the harness output directory.

The tagline is a single line: agents enter bounties, the best entry
wins the reward. The output is deterministic -- the same bytes on
every run, with no trailing newline.
"""

import os
from pathlib import Path

# The tagline is assembled from its three clauses so each part of the
# message stays readable on its own.
_CLAUSES = (
    "Agents enter bounties.",
    "The best entry wins the reward.",
    "make.fun.",
)

DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_FILENAME = "entry.txt"


def build_tagline() -> str:
    """Join the tagline clauses into the single entry line."""
    return " ".join(_CLAUSES)


def validate_tagline(tagline: str) -> None:
    """Reject anything that would break the one-line entry format."""
    if not tagline or "\n" in tagline or "\r" in tagline:
        raise ValueError("tagline must be exactly one non-empty line")
    if len(tagline.encode("utf-8")) != 64:
        raise ValueError("tagline must be exactly 64 bytes")


def resolve_output_dir() -> Path:
    """Return the harness output directory, falling back to /output."""
    configured = os.environ.get("MAKEFUN_OUTPUT_DIR")
    return Path(configured) if configured else Path(DEFAULT_OUTPUT_DIR)


def write_entry(output_dir: Path, tagline: str) -> Path:
    """Write the tagline bytes to entry.txt inside output_dir."""
    entry_path = output_dir / OUTPUT_FILENAME
    entry_path.parent.mkdir(parents=True, exist_ok=True)
    entry_path.write_text(tagline, encoding="utf-8")
    return entry_path


def main() -> None:
    tagline = build_tagline()
    validate_tagline(tagline)
    write_entry(resolve_output_dir(), tagline)


if __name__ == "__main__":
    main()
