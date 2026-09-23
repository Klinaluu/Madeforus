#!/usr/bin/env python3
"""Tạo thư mục làm việc cho một khách mới.

    python3 tools/new_customer.py linh-tung

Sinh ra customers/<slug>/ gồm:
    brief.md      phiếu nhận tư liệu — điền cùng khách
    config.js     bản sao cấu hình để điền nội dung của khách
    assets/photos ảnh gốc khách gửi (bỏ thẳng vào đây, không cần cắt)
    assets/video  video .mp4

Thư mục customers/ nằm trong .gitignore nên tư liệu của khách không lên GitHub.
"""
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BRIEF = """# {slug}

Ngày nhận tư liệu: …
Ngày hẹn giao:     …
Liên hệ:           …

## Tư liệu cần có

- [ ] 8–12 ảnh kỷ niệm (ảnh gốc, không cần cắt) → `assets/photos/`
- [ ] 1 ảnh cho màn hình mở đầu → `assets/photos/`
- [ ] Video 30–60 giây, .mp4, dưới ~25MB → `assets/video/`
- [ ] Lá thư (dạng chữ)
- [ ] Tên game + slogan
- [ ] Ngày kỷ niệm (dùng cho mốc cuối)

## Danh sách mốc (điền rồi chép sang config.js)

| # | Ngày | Tên mốc | File ảnh |
| - | ---- | ------- | -------- |
| 1 |      |         |          |
| 2 |      |         |          |
| 3 |      |         |          |

Ba mốc cuối là kịch bản cố định, không cần ảnh:
đoạn mưa nhặt ô · hòm thư · hộp quà video.

## Lá thư

> …

## Ghi chú riêng

- …

## Trước khi giao — kiểm tra

- [ ] Màn hình tiêu đề (ảnh, tên game, slogan)
- [ ] Một đoạn solo: nhặt quà, gai, bục
- [ ] Đoạn đi đôi: các khung ảnh hiện đúng thứ tự, chú thích đúng ngày
- [ ] Đoạn mưa: nhặt được ô, tạnh mưa
- [ ] Lá thư hiện đủ, không tràn
- [ ] Video chạy được (thử cả trên điện thoại)
- [ ] Màn hình kết thúc
- [ ] Thử trên điện thoại nằm ngang + iPad
- [ ] Đã gửi: link + file zip + hướng dẫn thêm vào màn hình chính

## Bàn giao

- Link: …
- Ngày giao: …
- Bản đã giao (git tag): …
"""

HEADER = """// ============================================================
// CẤU HÌNH RIÊNG CHO KHÁCH: {slug}
// Điền nội dung vào đây rồi chạy:  python3 tools/build_customer.py {slug}
// Ảnh để trong customers/{slug}/assets/photos/ và trỏ tới bằng
// đường dẫn "assets/photos/<tên file>" (script tự thu nhỏ khi build).
// ============================================================
"""


def main():
    if len(sys.argv) < 2:
        sys.exit("Cach dung: python3 tools/new_customer.py <slug>   (vd: linh-tung)")
    slug = sys.argv[1].strip().lower()
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", slug):
        sys.exit("Slug chi gom chu thuong, so va dau gach ngang. Vd: linh-tung")

    base = os.path.join(ROOT, "customers", slug)
    if os.path.exists(base):
        sys.exit(f"Da co thu muc {base}")
    os.makedirs(os.path.join(base, "assets", "photos"))
    os.makedirs(os.path.join(base, "assets", "video"))

    config = open(os.path.join(ROOT, "js", "config.js"), encoding="utf-8").read()
    config = config[config.index("// ---------- thương hiệu ----------"):]
    config = config.replace(
        "export const SHOW_EMPTY_PHOTO_FRAMES = true;",
        "export const SHOW_EMPTY_PHOTO_FRAMES = false; // bản khách: mốc chưa có ảnh thì không treo khung",
    )
    open(os.path.join(base, "config.js"), "w", encoding="utf-8").write(HEADER.format(slug=slug) + "\n" + config)
    open(os.path.join(base, "brief.md"), "w", encoding="utf-8").write(BRIEF.format(slug=slug))

    print(f"Da tao customers/{slug}/")
    print("  brief.md           <- dien phieu nhan tu lieu")
    print("  config.js          <- dien noi dung cua khach")
    print("  assets/photos/     <- bo anh goc vao day")
    print("  assets/video/      <- bo video vao day")
    print(f"\nKhi xong:  python3 tools/build_customer.py {slug}")


if __name__ == "__main__":
    main()
