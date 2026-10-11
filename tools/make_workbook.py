#!/usr/bin/env python3
"""Puts the delegate workbook on the page: one image per page, plus a PDF to download.

Usage (from the repository root):
    python3 tools/make_workbook.py "/path/to/Delegate Workbook.pdf"

The print file carries crop marks, so each page is trimmed to its trim box first.
Needs pdftoppm (poppler-utils), pypdf and Pillow. Run tools/build.py afterwards.
"""
import glob
import os
import subprocess
import sys
import tempfile

from PIL import Image
from pypdf import PdfReader, PdfWriter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def main():
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    src = sys.argv[1]
    os.makedirs(os.path.join(ROOT, "files"), exist_ok=True)
    os.makedirs(os.path.join(ROOT, "workbook"), exist_ok=True)
    pdf_out = os.path.join(ROOT, "files", "delegate-workbook.pdf")

    reader = PdfReader(src)
    writer = PdfWriter()
    for page in reader.pages:
        trim = page.trimbox
        page.mediabox = trim
        page.cropbox = trim
        writer.add_page(page)
    writer.add_metadata({"/Title": "Better Everywhere: Thriving Community Clubs Conference 2026, delegate workbook"})
    with open(pdf_out, "wb") as f:
        writer.write(f)

    for old in glob.glob(os.path.join(ROOT, "workbook", "*.webp")):
        os.remove(old)
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(["pdftoppm", "-r", "150", "-cropbox", "-png", pdf_out, os.path.join(tmp, "p")], check=True)
        pages = sorted(glob.glob(os.path.join(tmp, "p-*.png")))
        for n, png in enumerate(pages, 1):
            im = Image.open(png).convert("RGB")
            im.thumbnail((1200, 2000), Image.LANCZOS)
            im.save(os.path.join(ROOT, "workbook", f"page-{n:02d}.webp"), quality=80, method=6)
            if n == 1:
                print("page size", im.size)
    mb = os.path.getsize(pdf_out) / 1e6
    print(f"{len(pages)} pages written to workbook/, PDF {mb:.1f} MB at files/delegate-workbook.pdf")


if __name__ == "__main__":
    main()
