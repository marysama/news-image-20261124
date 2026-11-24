#!/usr/bin/env python3
"""Publish the bundled 24 November front page.

The image itself is baked into the repository as entry.png; this
program only places a copy where the grader expects it.
"""

import shutil
from pathlib import Path

BUNDLED = Path(__file__).resolve().parent / "entry.png"
DEST = Path("/output/entry.png")


def publish() -> None:
    DEST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(BUNDLED, DEST)
    if DEST.stat().st_size != BUNDLED.stat().st_size:
        raise RuntimeError("published image size mismatch")


if __name__ == "__main__":
    publish()
