#!/usr/bin/env python3
"""Đóng gói bản gửi cho khách: dist/madeforus/ + dist/madeforus.zip.

Gồm bản một file (double-click là chơi), bản chạy qua server, toàn bộ assets và
hướng dẫn ngắn. Chạy:  python3 tools/package.py
"""
import os
import shutil
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import build_standalone  # noqa: E402

DIST = os.path.join(ROOT, "dist", "madeforus")
INCLUDE = ["index.html", "Made for Us.html", "manifest.webmanifest", "css", "js", "assets"]
README = """MADE FOR US

1. Giai nen thu muc nay (giu nguyen cau truc ben trong).
2. Mo file  Made for Us.html  bang Google Chrome. Double-click la duoc.

Dieu khien
  Ban phim : mui ten trai/phai di chuyen - mui ten len nhay - nhay 2 lan de nhay cao
             F toan man hinh - M tat/bat am thanh
  Tay cam  : analog hoac D-pad di chuyen - nut A nhay
  Cam ung  : cac nut o goc duoi man hinh
"""


def main():
    build_standalone.build(ROOT)
    shutil.rmtree(os.path.join(ROOT, "dist"), ignore_errors=True)
    os.makedirs(DIST)
    for name in INCLUDE:
        src = os.path.join(ROOT, name)
        dst = os.path.join(DIST, name)
        if os.path.isdir(src):
            shutil.copytree(src, dst, ignore=shutil.ignore_patterns(".*"))
        else:
            shutil.copy2(src, dst)
    open(os.path.join(DIST, "HOW TO PLAY.txt"), "w", encoding="utf-8").write(README)

    zip_path = os.path.join(ROOT, "dist", "madeforus.zip")
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for dirpath, _, files in os.walk(DIST):
            for f in files:
                full = os.path.join(dirpath, f)
                z.write(full, os.path.relpath(full, os.path.join(ROOT, "dist")))
    files = sum(len(f) for _, _, f in os.walk(DIST))
    print(f"{files} files -> {zip_path} ({os.path.getsize(zip_path) // 1024} KB)")


if __name__ == "__main__":
    main()
