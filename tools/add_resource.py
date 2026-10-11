#!/usr/bin/env python3
"""Prepares a resource (an image or a PDF) for showing on the page.

Usage (from the repository root):
    python3 tools/add_resource.py <short-name> "/path/to/file.png-or-pdf" [--split-spreads] [--keep-whole=2,5]

--split-spreads cuts each double-width PDF page (two pages side by side) into two
single pages, which are far easier to read on a phone. --keep-whole lists PDF pages
to leave uncut, for example artwork that runs across both halves.

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
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = [a for a in sys.argv[1:] if a.startswith("--")]
    if len(args) != 2:
        raise SystemExit(__doc__)
    name, src = args
    split = "--split-spreads" in flags
    keep = set()
    for f in flags:
        if f.startswith("--keep-whole="):
            keep = {int(n) for n in f.split("=", 1)[1].split(",") if n}
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
            out = 0
            for n, png in enumerate(sorted(glob.glob(os.path.join(tmp, "p-*.png"))), 1):
                im = Image.open(png)
                halves = [im]
                if split and n not in keep and im.width > im.height * 1.6:
                    mid = im.width // 2
                    halves = [im.crop((0, 0, mid, im.height)), im.crop((mid, 0, im.width, im.height))]
                for part in halves:
                    out += 1
                    rel = f"resources/{name}/page-{out}.webp"
                    pages.append((rel, save(part, os.path.join(ROOT, rel))))
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
