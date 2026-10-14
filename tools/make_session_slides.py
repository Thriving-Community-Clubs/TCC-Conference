#!/usr/bin/env python3
"""Turns a session's own final slide deck into the slide images the page shows.

Usage (from the repository root):
    python3 tools/make_session_slides.py d1-teamwork "/path/to/Teamwork slides.pdf" [d2-lmd "/path/to/LMD.pdf" ...]

Which pages are used is set in SLIDE_PAGES in tools/content.py, written as "f1", "f2"...
(page numbers of the session's own deck). Plain numbers there still refer to the old
master deck and are left alone. Keep the deck PDFs outside this repository.
Run tools/build.py afterwards.
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

WIDTH = 1280


def main():
    args = sys.argv[1:]
    if not args or len(args) % 2:
        raise SystemExit(__doc__)
    out_dir = os.path.join(ROOT, "slides")
    for key, pdf in zip(args[::2], args[1::2]):
        pages = [p for p in C.SLIDE_PAGES.get(key, []) if isinstance(p, str) and p.startswith("f")]
        if not pages:
            raise SystemExit(f"No final-deck pages for {key} in SLIDE_PAGES")
        with tempfile.TemporaryDirectory() as tmp:
            for p in pages:
                n = int(p[1:])
                prefix = os.path.join(tmp, f"p{n}")
                subprocess.run(["pdftoppm", "-r", "150", "-f", str(n), "-l", str(n), "-png", pdf, prefix], check=True)
                im = Image.open(glob.glob(prefix + "*.png")[0]).convert("RGB")
                im = im.resize((WIDTH, round(im.height * WIDTH / im.width)), Image.LANCZOS)
                im.save(os.path.join(out_dir, slide_name(key, p)), quality=80, method=6)
        print(f"{key}: {len(pages)} slides")
    # Remove slide files no longer listed anywhere.
    keep = {slide_name(k, p) for k, ps in C.SLIDE_PAGES.items() for p in ps}
    gone = [f for f in os.listdir(out_dir) if f.endswith(".webp") and f not in keep]
    for f in gone:
        os.remove(os.path.join(out_dir, f))
    print(f"removed {len(gone)} old slide files")


if __name__ == "__main__":
    main()
