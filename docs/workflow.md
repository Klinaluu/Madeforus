# Quy trình mỗi khi có khách mới (gói Madeforus.love)

Đây là trang duy nhất cần mở khi có khách mới — các bước theo đúng thứ tự làm.
Phần tư vấn/báo giá khách đã lưu ở Notion, không lặp lại ở đây. Cách mở khung chat mới
và thao tác với Claude Code: [new-customer-chat.md](new-customer-chat.md).

## Bước 0 — Nhận đơn

Khách chọn gói love trên Notion, gửi tư liệu vào 1 folder Google Drive theo checklist đã
lưu ngoài (ảnh, video, lá thư, tên game/slogan, ngày kỷ niệm).

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

Mọi thứ của khách chỉ nằm trong `customers/linh-tung/` — **không sửa file gốc của repo**.
Mẫu tham khảo đầy đủ: `customers/thaobe/` (khách đầu tiên làm theo quy trình này).

- Tải ảnh/video từ Drive của khách → bỏ vào `customers/linh-tung/assets/photos/` và `assets/video/`
  - Video iPhone đuôi `.MOV` → đổi sang `.mp4` cho mọi trình duyệt phát được (có sẵn trên macOS):
    `avconvert -s video.MOV -p PresetHighestQuality -o video.mp4 --replace`
- Điền `customers/linh-tung/brief.md` (bảng mốc, lá thư, ghi chú) — dùng để đối chiếu, không
  ảnh hưởng game
- Điền `customers/linh-tung/config.js`:
  - `GAME_TITLE`, `GAME_SUBTITLE`, `WINDOW_NAME`
  - `TEXT.letter`, `TEXT.manLine`, `TEXT.meetText`
  - `TITLE_PHOTO` — ảnh mở đầu (ảnh chụp, hoặc sprite 2 nhân vật nếu có)
  - `MILESTONES[].date/name/photo` — theo đúng thứ tự ảnh khách gửi. Khách không muốn chữ dưới
    khung ảnh thì để `date: "", name: ""` (kể cả 3 mốc mưa / hòm thư / quà cuối)
  - `SHOW_EMPTY_PHOTO_FRAMES = false` — bản khách không treo khung trống
  - `VIDEO_SRC` — `"assets/video/<tên file>.mp4"` (nhớ có `assets/video/` phía trước)
  - `MUSIC_SRC` — để mặc định = nhạc nền chung; khách có nhạc riêng thì bỏ vào `assets/audio/`
  - `GIFTS[].label` / `icon` — tên và hình 5 món quà (giữ nguyên `id`)
  - `COUPLE_FRAMES` — chỉ có 1 ảnh xe chở đôi thì ghi 1 file; để `[]` = bộ 4 khung mặc định
- (Tuỳ chọn) ảnh riêng thay ảnh mặc định: bỏ vào đúng thư mục, **đúng tên file** như gốc repo
  (cùng tên thì thay, tên mới thì thêm):

  | Thư mục của khách | Thay cho | Ví dụ ở bản Thảo Bé |
  | --- | --- | --- |
  | `assets/characters/` | nhân vật, xe, icon quà, ảnh minh hoạ | `Man-Walk-Side-01..04`, `Man-Bike-Side-01`, `Couple-Bike-Side-01` |
  | `assets/elements/` | vật phẩm, khối, UI trong game | — |
  | `assets/props/` | vật trang trí / điểm thưởng | — |
  | `assets/scenes/<id>/` | nền parallax (`L1.png` xa → `L3.png` gần) + khai báo `SCENE_LAYERS` | — (nền mới đã thành mặc định) |

  - Ảnh gốc/nháp để trong thư mục con `_source/` — script build bỏ qua, không chép vào bản giao
  - Sprite nhân vật/xe phải **quay mặt sang phải** (game tự lật khi đi sang trái)

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
- [ ] Xe, cây, gai, khối gạch đứng đúng trên vạch kẻ đường (không lơ lửng)
- [ ] Nhạc nền + tiếng nhảy, tắt/mở bằng nút 🔊
- [ ] Điện thoại cầm dọc: thấy màn mở đầu + hộp "Add to Home Screen"; cầm ngang: chơi được
- [ ] Thử trên điện thoại nằm ngang + iPad (Chrome DevTools responsive, iPhone Simulator hoặc máy thật)

## Bước 6 — Tạo repo & deploy

```bash
# 1 lần trên github.com: tạo repo TRỐNG, public, tên = slug, vd Klinaluu/linh-tung
python3 tools/deploy_customer.py linh-tung https://github.com/Klinaluu/linh-tung.git
```

**Lần đầu tiên của repo đó**, bật GitHub Pages (hoặc làm tay trong Settings → Pages →
*Deploy from a branch* → **main** / **(root)**):

```bash
gh api -X POST repos/Klinaluu/linh-tung/pages -f "source[branch]=main" -f "source[path]=/"
```

Đợi ~1 phút.

Link cuối: `https://klinaluu.github.io/linh-tung/`

## Bước 7 — Giao khách

Gửi 3 thứ:

1. **Link**: `https://klinaluu.github.io/linh-tung/`
2. **File**: `dist/linh-tung.zip` (bản offline giữ làm kỷ niệm, giải nén rồi mở file `.html`)
3. **Hướng dẫn thêm vào màn hình chính** (game tự hiện khi khách mở bằng điện thoại, nhưng
   nhắc thêm cho chắc):
   - iPhone/iPad: mở bằng **Safari** → nút Chia sẻ (iPhone đời mới: nằm trong menu ≡ / •••
     cạnh thanh địa chỉ) → *Thêm vào MH chính*
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
