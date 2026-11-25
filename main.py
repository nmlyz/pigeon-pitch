#!/usr/bin/env python3
"""Pigeon Pitch: write the pigeon's one-line investor pitch to /output/entry.txt.

Standard library only. The pitch is a fixed string, so the program is
deterministic by construction: every run writes the same bytes.
"""

import os

PITCH = (
    "We've been A/B-testing humans for a century. Group A feeds us; "
    "Group B doesn't. Group A is happier, thinner, and tips better — "
    "so I'm selling restaurants the results, one crumb at a time."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")
MAX_CHARS = 200


def main() -> None:
    text = PITCH.strip()
    if not text or len(text) > MAX_CHARS:
        raise SystemExit("pitch must be 1-200 characters")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    try:
        os.chmod(OUTPUT_PATH, 0o644)
    except OSError:
        pass
    # Read back and verify what was written: same text, same length.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != text:
        raise SystemExit("verification failed: entry.txt differs from pitch")


if __name__ == "__main__":
    main()
