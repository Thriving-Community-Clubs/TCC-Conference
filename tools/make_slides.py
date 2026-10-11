#!/usr/bin/env python3
"""Turns pages of the master deck PDF into the slide images the page shows.

Usage (from the repository root):
    python3 tools/make_slides.py "/path/to/MASTER content slides.pdf"

Which pages are used is set in SLIDE_PAGES in tools/content.py.
Needs pdftoppm (poppler-utils) and Pillow. Run tools/build.py afterwards.
"""
import glob
import os
import subprocess
import sys
import tempfile

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import content as C  # noqa: E402
from build import slide_name  # noqa: E402


def main():
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    pdf = sys.argv[1]
    out_dir = os.path.join(ROOT, "slides")
    os.makedirs(out_dir, exist_ok=True)
    keep = set()
    with tempfile.TemporaryDirectory() as tmp:
        for key, pages in C.SLIDE_PAGES.items():
            for page in pages:
                prefix = os.path.join(tmp, f"p{page}")
                subprocess.run(
                    ["pdftoppm", "-r", "96", "-f", str(page), "-l", str(page), "-png", pdf, prefix],
                    check=True,
                )
                png = glob.glob(prefix + "*.png")[0]
                name = slide_name(key, page)
                Image.open(png).convert("RGB").save(os.path.join(out_dir, name), quality=78, method=6)
                keep.add(name)
    for old in os.listdir(out_dir):
        if old.endswith(".webp") and old not in keep:
            os.remove(os.path.join(out_dir, old))
    print(f"{len(keep)} slides written to slides/")


if __name__ == "__main__":
    main()
