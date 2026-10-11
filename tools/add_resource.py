#!/usr/bin/env python3
"""Prepares a resource (an image or a PDF) for showing on the page.

Usage (from the repository root):
    python3 tools/add_resource.py <short-name> "/path/to/file.png-or-pdf"

Writes resources/<short-name>/page-1.webp (one image per page for a PDF) and,
for a PDF, a copy at files/<short-name>.pdf for download. It prints the lines
to paste into PILLAR_RESOURCES in tools/content.py. Run tools/build.py afterwards.
Needs pdftoppm (poppler-utils) and Pillow.
"""
import glob
import os
import shutil
import subprocess
import sys
import tempfile

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
MAX_WIDTH = 1400


def save(im, out):
    im = im.convert("RGB")
    if im.width > MAX_WIDTH:
        im = im.resize((MAX_WIDTH, round(im.height * MAX_WIDTH / im.width)), Image.LANCZOS)
    im.save(out, quality=82, method=6)
    return im.size


def main():
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    name, src = sys.argv[1], sys.argv[2]
    out_dir = os.path.join(ROOT, "resources", name)
    os.makedirs(out_dir, exist_ok=True)
    for old in glob.glob(os.path.join(out_dir, "*.webp")):
        os.remove(old)
    pages = []
    pdf = None
    if src.lower().endswith(".pdf"):
        os.makedirs(os.path.join(ROOT, "files"), exist_ok=True)
        pdf = f"files/{name}.pdf"
        shutil.copyfile(src, os.path.join(ROOT, pdf))
        with tempfile.TemporaryDirectory() as tmp:
            subprocess.run(["pdftoppm", "-r", "150", "-png", src, os.path.join(tmp, "p")], check=True)
            for n, png in enumerate(sorted(glob.glob(os.path.join(tmp, "p-*.png"))), 1):
                rel = f"resources/{name}/page-{n}.webp"
                pages.append((rel, save(Image.open(png), os.path.join(ROOT, rel))))
    else:
        rel = f"resources/{name}/page-1.webp"
        pages.append((rel, save(Image.open(src), os.path.join(ROOT, rel))))

    print("Add to PILLAR_RESOURCES in tools/content.py:")
    print("    {")
    print('        "title": "",')
    if pdf:
        print(f'        "pdf": "{pdf}",')
    print('        "pages": [')
    for rel, (w, h) in pages:
        print(f'            ("{rel}", {w}, {h}, "describe this page"),')
    print("        ],")
    print("    },")


if __name__ == "__main__":
    main()
