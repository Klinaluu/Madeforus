#!/usr/bin/env python3
"""Tạo thẻ QR bàn giao cho một khách + in sẵn tin nhắn giao game để copy.

    python3 tools/make_qr_card.py linh-tung
    python3 tools/make_qr_card.py linh-tung --names "Linh" "Tùng"
    python3 tools/make_qr_card.py linh-tung --link https://klinaluu.github.io/linh-tung/

Tên hai người lấy từ dòng "Tên cặp đôi:" trong customers/<slug>/brief.md (vd
"Tên cặp đôi:      Linh & Tùng"), hoặc truyền bằng --names. Link mặc định là
https://klinaluu.github.io/<slug>/.

Thẻ vẽ bằng tools/qr_card.html (cùng thiết kế với artifact "Thẻ QR bàn giao") qua Chrome
headless, lưu ở customers/<slug>/qr-card.png (1080×1350). Tin nhắn giao lưu ở
customers/<slug>/tin-nhan-giao.txt. Cần mạng (font Google + thư viện QR từ jsdelivr).
"""
import base64
import os
import re
import shutil
import subprocess
import sys
import urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARD_HTML = os.path.join(ROOT, "tools", "qr_card.html")
CHROME_PATHS = [
    os.environ.get("CHROME", ""),
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    shutil.which("google-chrome") or "",
    shutil.which("chromium") or "",
]

MESSAGE = """Game của hai bạn đã xong rồi nè 💝
🎮 Link game: {link}
Game chơi được ngay trên trình duyệt, cả laptop lẫn điện thoại. Nếu muốn chơi toàn màn hình như một app trên điện thoại:

* iPhone: mở link bằng Safari → bấm nút Chia sẻ (trên iOS mới nằm trong menu ≡ cạnh thanh địa chỉ) → chọn "Thêm vào Màn hình chính"
* Android: mở link bằng Chrome → bấm menu ⋮ → chọn "Cài đặt ứng dụng" hoặc "Thêm vào màn hình chính"

💌 Thẻ QR riêng: chỉ cần quét bằng camera là vào thẳng game. Bạn có thể in ra làm quà hoặc gửi trực tiếp cho người ấy đều xinh nha.
‼️ Một vài lưu ý nhỏ:

* Link và mã QR không có mật khẩu, ai có link đều mở được, nên bạn cân nhắc trước khi chia sẻ công khai nhé.
* Nếu muốn lưu file game để giữ lâu dài hoặc chơi khi không có mạng, cứ nhắn mình nha.
* Bạn có thể gửi yêu cầu chỉnh sửa trong vòng 15 ngày kể từ ngày nhận game ạ.

Chúc hai bạn có thật nhiều khoảnh khắc đáng yêu khi chơi cùng nhau 💖
— Made For Us"""


def names_from_brief(path):
    if not os.path.isfile(path):
        return None
    for line in open(path, encoding="utf-8"):
        m = re.match(r"\s*Tên cặp đôi:\s*(.+?)\s*$", line)
        value = re.sub(r"\(.*\)\s*$", "", m.group(1)).strip() if m else ""  # bỏ chú thích (…) cuối dòng
        if value and "…" not in value:
            parts = [p.strip() for p in re.split(r"\s*(?:&|♥|\+)\s*", value) if p.strip()]
            if len(parts) == 2:
                return parts
    return None


def find_chrome():
    for p in CHROME_PATHS:
        if p and os.path.isfile(p):
            return p
    sys.exit("Khong tim thay Google Chrome. Cai Chrome hoac dat bien CHROME=<duong dan>.")


def main():
    args = sys.argv[1:]
    if not args or args[0].startswith("-"):
        sys.exit('Cach dung: python3 tools/make_qr_card.py <slug> [--names "Ten 1" "Ten 2"] [--link URL]')
    slug = args[0].strip().lower()
    base = os.path.join(ROOT, "customers", slug)
    if not os.path.isdir(base):
        sys.exit(f"Chua co customers/{slug}/")

    names = None
    if "--names" in args:
        i = args.index("--names")
        names = args[i + 1:i + 3]
        if len(names) != 2:
            sys.exit('--names can 2 ten, vd: --names "Linh" "Tung"')
    names = names or names_from_brief(os.path.join(base, "brief.md"))
    if not names:
        sys.exit(f'Chua co ten cap doi: dien dong "Tên cặp đôi: A & B" trong customers/{slug}/brief.md '
                 'hoac truyen --names "A" "B"')
    link = args[args.index("--link") + 1] if "--link" in args else f"https://klinaluu.github.io/{slug}/"

    frag = urllib.parse.urlencode({"n1": names[0], "n2": names[1], "link": link}, quote_via=urllib.parse.quote)
    url = "file://" + urllib.parse.quote(CARD_HTML) + "#" + frag
    r = subprocess.run(
        [find_chrome(), "--headless=new", "--disable-gpu", "--no-first-run", "--no-default-browser-check",
         "--virtual-time-budget=20000", "--dump-dom", url],
        capture_output=True, text=True, timeout=120,
    )
    found = re.findall(r'<pre id="out">(.*?)</pre>', r.stdout, re.S)
    body = found[-1].strip() if found else ""
    if not body.startswith("data:image/png;base64,"):
        sys.exit("Khong ve duoc the QR: " + (body or r.stderr.strip()[-400:] or "khong co ket qua"))

    png = os.path.join(base, "qr-card.png")
    with open(png, "wb") as f:
        f.write(base64.b64decode(body.split(",", 1)[1]))
    msg = MESSAGE.format(link=link)
    with open(os.path.join(base, "tin-nhan-giao.txt"), "w", encoding="utf-8") as f:
        f.write(msg + "\n")

    print(f"The QR: customers/{slug}/qr-card.png  ({names[0]} ♥ {names[1]} -> {link})")
    print(f"Tin nhan: customers/{slug}/tin-nhan-giao.txt — copy doan duoi, gui kem anh qr-card.png\n")
    print(msg)


if __name__ == "__main__":
    main()
