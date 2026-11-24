#!/usr/bin/env python3
"""news-image-20261124 entry for make.fun.

Writes one 1024x1024 PNG summarising the world news of Tuesday
24 November 2026 to /output/entry.png.

The image is held in this repository as entry.png (generated at build
time from the day's reporting — see README.md for the stories and
sources). The brief allows the simplest program to copy an image the
repository holds, and copying keeps the run fully deterministic: no
network, no clock, no randomness, so two runs write identical bytes.

Standard library only; Python 3.13.
"""
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
DST = Path("/output/entry.png")


def main() -> None:
    DST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
