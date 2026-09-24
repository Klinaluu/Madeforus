# Quy trình mỗi khi có khách mới (gói Madeforus.love)

Đây là trang duy nhất cần mở khi có khách mới — các bước theo đúng thứ tự làm.
Chi tiết từng phần nằm ở [intake.md](intake.md) (tư liệu cần xin), [packages.md](packages.md)
(phạm vi gói) và [new-customer-chat.md](new-customer-chat.md) (vì sao mở khung chat mới).

## Bước 0 — Nhận đơn

Khách chọn gói love trên Notion → nhắn đoạn tư vấn trong
[intake.md § Đoạn gửi khách](intake.md#đoạn-gửi-khách) → khách gửi tư liệu vào 1 folder
Google Drive (ảnh, video, lá thư, tên game/slogan, ngày kỷ niệm).

## Bước 1 — Mở khung chat MỚI cho khách này

**Không làm trong khung chat này hay khung khách trước.** Mở khung mới, dán prompt trong
[new-customer-chat.md](new-customer-chat.md), đổi `<slug>` thành tên khách viết liền không
dấu (vd `linh-tung`). Lý do: dữ liệu khách sống trên đĩa ở `customers/<slug>/`, không sống
trong chat — khung nào cũng đọc lại được, nên không cần dồn hết vào một chỗ.

## Bước 2 — Tạo khung sườn

```bash
python3 tools/new_customer.py linh-tung
```

Sinh ra `customers/linh-tung/{brief.md, config.js, assets/{photos,video,characters}}`.

## Bước 3 — Đổ tư liệu vào

- Tải ảnh/video từ Drive của khách → bỏ vào `customers/linh-tung/assets/photos/` và `assets/video/`
- Điền `customers/linh-tung/brief.md` (bảng mốc, lá thư, ghi chú) — dùng để đối chiếu, không
  ảnh hưởng game
- Điền `customers/linh-tung/config.js`:
  - `GAME_TITLE`, `GAME_SUBTITLE`, `WINDOW_NAME`
  - `TEXT.letter`, `TEXT.manLine`, `TEXT.meetText`
  - `TITLE_PHOTO` — ảnh mở đầu
  - `MILESTONES[].date/name/photo` — theo đúng thứ tự ảnh khách gửi
  - `VIDEO_SRC` — tên file trong `assets/video/`
  - `GIFTS[].label` — đổi tên gọi nếu khách muốn (gói love không đổi hình)
- (Tuỳ chọn) nếu đã có sprite cá nhân hoá từ quy trình riêng: bỏ vào
  `customers/linh-tung/assets/characters/`, đúng tên file như `assets/characters/` gốc repo

## Bước 4 — Build thử

```bash
python3 tools/build_customer.py linh-tung
```

Đọc kỹ phần in ra cuối: **ảnh thiếu** (config trỏ tới file không có), **ảnh thừa** (có ảnh
nhưng config chưa dùng), **video nặng** (>25MB — nên nén lại trước khi giao).

## Bước 5 — Test trước khi giao

Mở `dist/linh-tung/index.html` bằng server cục bộ hoặc double-click
`dist/linh-tung/Linh Tung.html`. Checklist (cũng có trong `brief.md`):

- [ ] Màn hình tiêu đề: ảnh, tên game, slogan đúng
- [ ] Một đoạn solo: nhặt quà, gai, bục chạy được
- [ ] Đi đôi: khung ảnh đúng thứ tự, chú thích đúng ngày (kể cả dấu tiếng Việt)
- [ ] Đoạn mưa: nhặt được ô, tạnh mưa
- [ ] Lá thư hiện đủ, không tràn khung
- [ ] Video chạy được
- [ ] Màn hình kết thúc
- [ ] Thử trên điện thoại nằm ngang + iPad (Chrome DevTools responsive hoặc máy thật)

## Bước 6 — Tạo repo & deploy

```bash
# 1 lần trên github.com: tạo repo TRỐNG, public, tên = slug, vd Klinaluu/linh-tung
python3 tools/deploy_customer.py linh-tung https://github.com/Klinaluu/linh-tung.git
```

**Lần đầu tiên của repo đó**, vào `https://github.com/Klinaluu/linh-tung/settings/pages` →
Source: *Deploy from a branch* → Branch **main** / **(root)** → Save. Đợi ~1 phút.

Link cuối: `https://klinaluu.github.io/linh-tung/`

## Bước 7 — Giao khách

Gửi 3 thứ:

1. **Link**: `https://klinaluu.github.io/linh-tung/`
2. **File**: `dist/linh-tung.zip` (bản offline giữ làm kỷ niệm, giải nén rồi mở file `.html`)
3. **Hướng dẫn thêm vào màn hình chính** (game tự hiện khi khách mở bằng điện thoại, nhưng
   nhắc thêm cho chắc):
   - iPhone/iPad: mở bằng **Safari** → nút Chia sẻ → *Thêm vào MH chính*
   - Android: mở bằng **Chrome** → menu ⋮ → *Cài ứng dụng*

Nhắc khách: link không cần mật khẩu, ai có link đều xem được.

## Bước 8 — Sau khi giao

```bash
cd dist/linh-tung
git tag delivery/linh-tung-2026-10-05
git push origin delivery/linh-tung-2026-10-05
```

Giữ nguyên `customers/linh-tung/` trên máy (không xoá) — khách xin sửa vài tuần/tháng sau
chỉ cần mở khung chat mới, đọc lại đúng thư mục này là đủ ngữ cảnh, không cần chat cũ.

---

## Khi engine có bug hoặc cải tiến chung

Việc đó làm ở **khung chat gốc của repo `madeforus`** (không phải khung khách), vì ảnh
hưởng mọi khách. Sau khi sửa, các bản đã giao muốn nhận cải tiến thì chạy lại
Bước 4 + Bước 6 cho từng khách (build lại + deploy lại), không cần làm gì thêm ở phía khách.
