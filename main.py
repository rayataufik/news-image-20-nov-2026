#!/usr/bin/env python3
"""Copy the 20 November 2026 news image to the output directory.

The entry is a single pre-rendered image (entry.png, 1024x1024, under
1 MiB) held in this repository. This program copies it, byte for byte,
to $MAKEFUN_OUTPUT_DIR/entry.png (or /output when the variable is
unset). It reads no network, writes nothing else, and is fully
deterministic: two runs produce identical bytes.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def main() -> int:
    if not os.path.isfile(SOURCE):
        print("entry.png not found next to main.py", file=sys.stderr)
        return 1
    with open(SOURCE, "rb") as f:
        if f.read(8) != b"\x89PNG\r\n\x1a\n":
            print("entry.png is not a PNG", file=sys.stderr)
            return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, target)
    return 0


if __name__ == "__main__":
    sys.exit(main())
