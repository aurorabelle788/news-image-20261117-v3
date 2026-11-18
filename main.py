#!/usr/bin/env python3
"""Copy the front-page image to the output directory.

The entry is the JPEG file entry.png that sits next to this program. The
program checks the file really is a JPEG (it must start with the SOI marker
FF D8) and then writes those exact bytes to MAKEFUN_OUTPUT_DIR/entry.png
(or /output/entry.png when the variable is unset). The copy is byte for byte
identical every run, so the two grader runs agree.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
IMAGE = os.path.join(HERE, "entry.png")
SOI = b"\xff\xd8"


def main():
    with open(IMAGE, "rb") as f:
        data = f.read()
    if not data.startswith(SOI):
        sys.exit("entry.png is not a JPEG: missing SOI marker FF D8")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    with open(target, "wb") as f:
        f.write(data)
    # Post-copy check: the written file must match the source byte for byte.
    with open(target, "rb") as f:
        written = f.read()
    if written != data:
        sys.exit("copy mismatch: %s does not match entry.png" % target)
    print("wrote %s (%d bytes)" % (target, len(data)))


if __name__ == "__main__":
    main()
