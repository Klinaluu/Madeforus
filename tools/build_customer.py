#!/usr/bin/env python3
"""Dựng bản game hoàn chỉnh cho một khách.

    python3 tools/build_customer.py linh-tung
    python3 tools/build_customer.py linh-tung --url https://linh-tung.netlify.app

Các bước script tự làm:
    1. Thu nhỏ ảnh trong customers/<slug>/assets/photos (giữ nguyên tỉ lệ, cạnh dài 640px)
    2. Chép video sang bản build, cảnh báo nếu nặng
    3. Chép toàn bộ code hiện tại + config.js của khách
    4. Nếu có customers/<slug>/assets/characters/ (sprite nhân vật đã cá nhân hoá bằng quy
       trình riêng) → đè lên bộ sprite mặc định, cùng tên file thì thay, tên mới thì thêm
    5. Đổi tên game trong manifest / thẻ chia sẻ theo GAME_TITLE của khách
    6. Xuất bản một file (double-click là chơi) và nén dist/<slug>.zip

Kết quả: dist/<slug>/ (đưa lên Netlify / GitHub Pages) và dist/<slug>.zip (gửi khách).
"""
import os
import re
import shutil
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import build_standalone  # noqa: E402

PHOTO_MAX_SIDE = 640
PHOTO_QUALITY = 82
VIDEO_WARN_MB = 25
CODE_DIRS = ["css", "assets/brand", "assets/characters", "assets/elements", "assets/props", "assets/ui", "assets/scenes"]
CODE_FILES = ["index.html", "manifest.webmanifest", "assets/preview.png"]
JS_FILES = ["assets.js", "audio.js", "engine.js", "install.js", "levels.js", "main.js"]


def read_config_value(config, name):
    m = re.search(r'export const %s = "([^"]*)"' % name, config)
    return m.group(1) if m else ""


def copy_photos(src_dir, dst_dir):
    from PIL import Image, ImageOps

    os.makedirs(dst_dir, exist_ok=True)
    done = []
    for name in sorted(os.listdir(src_dir)):
        path = os.path.join(src_dir, name)
        stem, ext = os.path.splitext(name)
        if name.startswith(".") or not os.path.isfile(path):
            continue
        if ext.lower() not in (".jpg", ".jpeg", ".png", ".webp", ".heic"):
            continue
        if ext.lower() == ".heic":  # iPhone: chuyển sang jpg bằng sips của macOS
            tmp = os.path.join(dst_dir, stem + ".tmp.jpg")
            os.system(f'sips -s format jpeg "{path}" --out "{tmp}" >/dev/null 2>&1')
            path = tmp
        im = ImageOps.exif_transpose(Image.open(path)).convert("RGB")
        w, h = im.size
        k = min(1.0, PHOTO_MAX_SIDE / max(w, h))
        if k < 1:
            im = im.resize((round(w * k), round(h * k)), Image.LANCZOS)
        out_name = stem + ".jpg"
        im.save(os.path.join(dst_dir, out_name), quality=PHOTO_QUALITY, optimize=True)
        if path.endswith(".tmp.jpg"):
            os.remove(path)
        done.append((out_name, im.size))
    return done


def main():
    if len(sys.argv) < 2:
        sys.exit("Cach dung: python3 tools/build_customer.py <slug> [--url https://...]")
    slug = sys.argv[1].strip().lower()
    site_url = ""
    if "--url" in sys.argv:
        site_url = sys.argv[sys.argv.index("--url") + 1].rstrip("/") + "/"

    src = os.path.join(ROOT, "customers", slug)
    config_path = os.path.join(src, "config.js")
    if not os.path.isfile(config_path):
        sys.exit(f"Khong thay {config_path} — chay tools/new_customer.py {slug} truoc.")

    dist = os.path.join(ROOT, "dist", slug)
    shutil.rmtree(dist, ignore_errors=True)
    os.makedirs(dist)

    # ---------- code ----------
    for d in CODE_DIRS:
        shutil.copytree(os.path.join(ROOT, d), os.path.join(dist, d), ignore=shutil.ignore_patterns(".*"))
    for f in CODE_FILES:
        os.makedirs(os.path.dirname(os.path.join(dist, f)), exist_ok=True)
        shutil.copy2(os.path.join(ROOT, f), os.path.join(dist, f))
    os.makedirs(os.path.join(dist, "js"))
    for f in JS_FILES:
        shutil.copy2(os.path.join(ROOT, "js", f), os.path.join(dist, "js", f))
    config = open(config_path, encoding="utf-8").read()
    open(os.path.join(dist, "js", "config.js"), "w", encoding="utf-8").write(config)

    # ---------- sprite nhân vật đã cá nhân hoá (quy trình riêng, ngoài script này) ----------
    custom_chars = os.path.join(src, "assets", "characters")
    custom_char_files = []
    if os.path.isdir(custom_chars):
        dst_chars = os.path.join(dist, "assets", "characters")
        for name in sorted(os.listdir(custom_chars)):
            path = os.path.join(custom_chars, name)
            if name.startswith(".") or not os.path.isfile(path):
                continue
            shutil.copy2(path, os.path.join(dst_chars, name))
            custom_char_files.append(name)

    # ---------- ảnh & video của khách ----------
    photos = copy_photos(os.path.join(src, "assets", "photos"), os.path.join(dist, "assets", "photos"))
    videos = []
    vsrc = os.path.join(src, "assets", "video")
    if os.path.isdir(vsrc):
        os.makedirs(os.path.join(dist, "assets", "video"), exist_ok=True)
        for name in sorted(os.listdir(vsrc)):
            if name.startswith("."):
                continue
            path = os.path.join(vsrc, name)
            shutil.copy2(path, os.path.join(dist, "assets", "video", name))
            videos.append((name, os.path.getsize(path) / 1e6))

    # ---------- tên game trong manifest & thẻ chia sẻ ----------
    title = read_config_value(config, "GAME_TITLE") or "Made for Us"
    subtitle = read_config_value(config, "GAME_SUBTITLE")
    pretty = title.title() if title.isupper() else title
    man_path = os.path.join(dist, "manifest.webmanifest")
    man = open(man_path, encoding="utf-8").read()
    man = man.replace('"name": "Made for Us"', f'"name": "{pretty}"').replace('"short_name": "Made for Us"', f'"short_name": "{pretty}"')
    open(man_path, "w", encoding="utf-8").write(man)

    html_path = os.path.join(dist, "index.html")
    html = open(html_path, encoding="utf-8").read()
    html = html.replace("<title>Made for Us</title>", f"<title>{pretty}</title>")
    html = html.replace('content="Made for Us — Our love journey"', f'content="{pretty} — {subtitle}"')
    html = html.replace('content="Made for Us"', f'content="{pretty}"')
    if site_url:
        html = re.sub(r'(property="og:url" content=")[^"]*"', r"\g<1>" + site_url + '"', html)
        html = re.sub(r'((?:property|name)="(?:og:image|twitter:image)" content=")[^"]*"', r"\g<1>" + site_url + 'assets/preview.png"', html)
    open(html_path, "w", encoding="utf-8").write(html)

    # ---------- bản một file + zip ----------
    build_standalone.build(dist, f"{pretty}.html")
    zip_path = os.path.join(ROOT, "dist", f"{slug}.zip")
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for dirpath, dirs, files in os.walk(dist):
            dirs[:] = [d for d in dirs if d != ".git"]
            for f in files:
                full = os.path.join(dirpath, f)
                z.write(full, os.path.join(slug, os.path.relpath(full, dist)))

    # ---------- báo cáo ----------
    print(f"\n{pretty} — {subtitle}")
    print(f"  {len(photos)} anh: " + ", ".join(f"{n} ({w}x{h})" for n, (w, h) in photos[:12]))
    for name, mb in videos:
        flag = "  [NANG - nen giam xuong duoi %dMB]" % VIDEO_WARN_MB if mb > VIDEO_WARN_MB else ""
        print(f"  video: {name} {mb:.1f}MB{flag}")
    if not videos:
        print("  video: chua co (game se hien dong 'Wait for your video')")
    if custom_char_files:
        print("  sprite nhan vat rieng (de len mac dinh): " + ", ".join(custom_char_files))
    missing = [p for p in re.findall(r'photo: "(assets/photos/[^"]+)"', config) if not os.path.isfile(os.path.join(dist, p))]
    if missing:
        print("  THIEU ANH (config tro toi file khong co): " + ", ".join(missing))
    unused = [n for n, _ in photos if n not in config and os.path.splitext(n)[0] not in config]
    if unused:
        print("  ANH CHUA DUNG trong config: " + ", ".join(unused))
    print(f"\n  dist/{slug}/        -> keo tha len Netlify hoac push len repo")
    print(f"  dist/{slug}.zip     -> gui khach ban choi offline")


if __name__ == "__main__":
    main()
