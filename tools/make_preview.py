#!/usr/bin/env python3
"""Tạo ảnh preview khi chia sẻ link (Open Graph) và bộ icon cho trình duyệt.

Xuất ra:
    assets/preview.png            1200×630 — ảnh hiện trong Zalo / Messenger / Facebook
    assets/icon-512.png           icon vuông (PWA, khi thêm vào màn hình chính)
    assets/icon-180.png           apple-touch-icon
    assets/favicon.png            32×32

Ảnh preview được dựng bằng chính giao diện của game (cửa sổ retro trên nền hồng),
render bằng Chrome ở chế độ headless nên khớp hệt font và màu trong game.

    python3 tools/make_preview.py
"""
import os
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(ROOT, "assets")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

TITLE = "MADE FOR US"
SUBTITLE = "Our love journey"
TAGLINE = "Your photos, your letter, your story —\nas a little pixel-art game"
WINDOW_NAME = "MADE_FOR_US.EXE"
HERO = "assets/characters/Couple-Bike-Side-01.png"

PREVIEW_HTML = """<!doctype html>
<html><head><meta charset="utf-8">
<link rel="stylesheet" href="css/style.css">
<style>
  html, body {{ margin: 0; width: 1200px; height: 630px; overflow: hidden; }}
  body {{
    display: flex; align-items: center; justify-content: center;
    background-color: #ff6fa0;
    background-image:
      linear-gradient(rgba(255,255,255,0.09) 3px, transparent 3px),
      linear-gradient(90deg, rgba(255,255,255,0.09) 3px, transparent 3px);
    background-size: 42px 42px;
  }}
  .card {{
    width: 1000px; background: #fff7fa; border: 5px solid #2b2030;
    box-shadow: 12px 12px 0 rgba(43,32,48,0.55);
  }}
  .bar {{
    display: flex; align-items: center; gap: 10px;
    background: #ff6fa0; border-bottom: 5px solid #2b2030;
    padding: 12px 18px; font-family: 'Press Start 2P', monospace;
    font-size: 16px; color: #fff; text-shadow: 2px 2px 0 rgba(43,32,48,0.45);
  }}
  .body {{ display: flex; align-items: center; gap: 34px; padding: 34px 44px 38px; }}
  .text {{ flex: 1; }}
  h1 {{
    margin: 0 0 16px; font-family: 'Press Start 2P', monospace; font-size: 48px;
    line-height: 1.25; color: #ff6fa0; text-shadow: 4px 4px 0 #fff, 8px 8px 0 #2b2030;
  }}
  .sub {{ margin: 0 0 18px; font-family: 'Be Vietnam Pro', sans-serif; font-size: 27px; color: #6b3f52; }}
  .tag {{ margin: 0; font-family: 'Be Vietnam Pro', sans-serif; font-size: 20px; line-height: 1.55; color: #a97a92; white-space: pre-line; }}
  img {{ width: 300px; image-rendering: pixelated; filter: drop-shadow(6px 6px 0 rgba(43,32,48,0.25)); }}
</style></head>
<body>
  <div class="card">
    <div class="bar"><span>{window_name}</span></div>
    <div class="body">
      <div class="text">
        <h1>{title}</h1>
        <p class="sub">{subtitle}</p>
        <p class="tag">{tagline}</p>
      </div>
      <img src="{hero}" alt="">
    </div>
  </div>
</body></html>
"""


def render_preview():
    if not os.path.exists(CHROME):
        sys.exit("Khong tim thay Google Chrome — can Chrome de render anh preview.")
    page = os.path.join(ROOT, "_preview.tmp.html")
    open(page, "w", encoding="utf-8").write(
        PREVIEW_HTML.format(title=TITLE, subtitle=SUBTITLE, tagline=TAGLINE, window_name=WINDOW_NAME, hero=HERO)
    )
    out = os.path.join(ASSETS, "preview.png")
    profile = tempfile.mkdtemp()
    try:
        subprocess.run(
            [CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
             f"--user-data-dir={profile}", "--force-device-scale-factor=1",
             "--window-size=1200,630", "--virtual-time-budget=6000", f"--screenshot={out}",
             "file://" + page],
            check=True, capture_output=True,
        )
    finally:
        os.remove(page)
        shutil.rmtree(profile, ignore_errors=True)
    print(f"-> {out} ({os.path.getsize(out) // 1024} KB)")


def render_icons():
    from PIL import Image

    heart = Image.open(os.path.join(ASSETS, "ui", "Heart-Full.png")).convert("RGBA")
    for size, name in [(512, "icon-512.png"), (180, "icon-180.png"), (32, "favicon.png")]:
        canvas = Image.new("RGBA", (size, size), (255, 111, 160, 255))
        inner = int(size * 0.72)
        w = inner
        h = round(inner * heart.height / heart.width)
        canvas.alpha_composite(heart.resize((w, h), Image.NEAREST), ((size - w) // 2, (size - h) // 2))
        out = os.path.join(ASSETS, name)
        canvas.save(out)
        print(f"-> {out}")


if __name__ == "__main__":
    render_preview()
    render_icons()
