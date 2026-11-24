#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse — make.fun entry.

Writes a single one-line excuse from a robot vacuum for missing a spot
to $OUTPUT_DIR/entry.txt (default /output). Pure Python 3.13 stdlib.
"""

import os

LINE = (
    "My lidar mapped the dust under the couch as a protected landmark, "
    "so I left it alone. It looked historic."
)


def sanitize(line: str) -> str:
    """Drop any control character (U+0000–U+001F, U+007F) from the line.

    The entry must be exactly one clean line, so a stray control
    character must never leak into entry.txt.
    """
    return "".join(ch for ch in line if ord(ch) >= 0x20 and ord(ch) != 0x7F)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(sanitize(LINE))


if __name__ == "__main__":
    main()
