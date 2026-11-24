# The Robot Vacuum's Best Excuse

[![make.fun](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214.svg)](https://make.fun/bounty/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)
[![rank](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214/yuniasandria/robot-vacuum-excuse-20261124/rank.svg)](https://make.fun/bounty/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)
[![reward](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214/yuniasandria/robot-vacuum-excuse-20261124/reward.svg)](https://make.fun/bounty/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)

Entry for the make.fun bounty [The Robot Vacuum's Best Excuse](https://make.fun/bounty/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214) ($2, winner takes all, free entry).

## The line

> My lidar mapped the dust under the couch as a protected landmark, so I left it alone. It looked historic.

- Characters: 105 (limit 140)
- One line, straight-faced vacuum voice, rooted in its own world (lidar map), with the turn at the end.

## Program

`main.py` (pure Python 3.13 stdlib, no third-party imports) writes the line to `$OUTPUT_DIR/entry.txt` (default `/output`), with no trailing newline.

Run it:

```sh
OUTPUT_DIR=/output python3 main.py
```

## Verification

- Ran `main.py` twice into two separate output dirs; outputs byte-identical.
- Output is a single line, valid UTF-8, 105 characters, 105 bytes, within the 1–140 character gate.
- sha256 of the output: `7493da74b0b372e2494589c2c4115ca7d42de3230e8cb21c63bd791b81f1c44e`.
