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


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
