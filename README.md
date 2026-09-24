# Made for Us

Game pixel-art chạy trên trình duyệt, làm quà kỷ niệm cho một cặp đôi: chàng trai đi
thu thập quà, vượt chướng ngại, gặp cô gái, rồi cả hai cùng đi qua từng cột mốc của
chuyện tình — kết thúc bằng một lá thư và một đoạn video của riêng họ.

Bản trong repo này là **bản mẫu (demo)**: khung ảnh, video và lá thư để trống cho khách
xem cấu trúc trước khi đặt làm bản cá nhân hoá.

- Bản demo đang chạy: <https://klinaluu.github.io/Madeforus/>
- Chơi được trên laptop, iPad (xoay ngang) và điện thoại. Không cần cài đặt gì.

## Chơi thử

| Cách | Làm gì |
| --- | --- |
| Online | Mở link ở trên |
| Ngoại tuyến | Double-click `Made for Us.html` (giữ nguyên thư mục `assets/` bên cạnh) |
| Khi phát triển | `python3 -m http.server 8750` rồi mở <http://localhost:8750> |

**Điều khiển** — bàn phím: `◀ ▶` di chuyển, `▲` nhảy, `▲▲` nhảy đôi, `F` toàn màn hình,
`M` tắt/bật âm thanh. Tay cầm: analog hoặc D-pad di chuyển, `A` nhảy (`A`/`Start` cũng
bấm được các nút trên màn hình). Cảm ứng: các nút ở hai góc dưới.

## Mạch chơi

1. **Đi bộ** — nhặt chìa khoá và mũ bảo hiểm, lên xe.
2. **Solo** — 5 đoạn, mỗi đoạn một món quà, có gai, gạch vỡ, bục di chuyển, ô `?` hồi tim.
3. **Boss** — nhảy qua đám mây "DOUBT" 3 lần.
4. **Gặp nhau** — màn hình sao, thống kê điểm và thời gian.
5. **Đi đôi** — các cột mốc, mỗi mốc một khung ảnh polaroid; đoạn mưa phải nhặt ô.
6. **Lá thư** — hòm hồng → System Message → Level Unlocked → thư.
7. **Kết** — hòm quà rơi xuống, mở ra video, màn hình "Completed".

## Cá nhân hoá

Mọi nội dung của khách nằm trong **`js/config.js`** — đây là file duy nhất cần sửa:

| Sửa gì | Ở đâu trong `config.js` |
| --- | --- |
| Tên game, slogan | `GAME_TITLE`, `GAME_SUBTITLE`, `WINDOW_NAME` |
| Lời thoại, lá thư, các dòng chữ | `TEXT` |
| Ảnh từng mốc, ngày, tên mốc | `MILESTONES` |
| Ảnh màn hình mở đầu | `TITLE_PHOTO` |
| Video | `VIDEO_SRC` |
| Tên 5 món quà | `GIFTS` |

Các bước thường làm khi giao một bản cá nhân hoá:

1. Chép ảnh vào `assets/photos/` (gồm cả ảnh cho màn hình mở đầu) (ảnh vuông hoặc dọc đều được, khung tự co theo tỉ lệ;
   nên thu nhỏ còn cạnh dài ~640px cho nhẹ).
2. Chép video `.mp4` (H.264, nên dưới 15MB) vào `assets/video/`.
3. Mở `js/config.js`: điền `photo` cho từng mốc, `VIDEO_SRC`, `TEXT.letter`, tên mốc và ngày.
4. Đặt `SHOW_EMPTY_PHOTO_FRAMES = false` để mốc chưa có ảnh thì không treo khung trống.
5. Chạy `python3 tools/package.py` → `dist/madeforus.zip` để gửi cho khách.

## Làm bản riêng cho từng khách

Không nhân bản code cho mỗi khách — chỉ nhân bản **nội dung**. Mỗi khách là một thư mục
trong `customers/` (đã nằm trong `.gitignore` nên ảnh, thư, video của khách không bao giờ
lên GitHub). Khi build, script lấy code mới nhất + nội dung của khách, nên mọi cải tiến về
sau đều đến được với các bản đã giao chỉ bằng một lệnh build lại.

```bash
python3 tools/new_customer.py linh-tung      # tạo customers/linh-tung/{brief.md, config.js, assets/}
# → điền brief.md, bỏ ảnh vào assets/photos, video vào assets/video, sửa config.js
python3 tools/build_customer.py linh-tung    # thu nhỏ ảnh, build, đóng gói
# → dist/linh-tung/ (đưa lên Netlify / GitHub Pages) + dist/linh-tung.zip (gửi khách)
```

Giao hàng qua GitHub Pages (khách chơi được trên laptop, iPhone, iPad và thêm vào màn
hình chính như app):

```bash
# tạo sẵn một repo TRỐNG, public trên github.com, vd Klinaluu/linh-tung
python3 tools/deploy_customer.py linh-tung https://github.com/Klinaluu/linh-tung.git
# lần đầu: Settings → Pages → Deploy from a branch → main / (root)
# → https://klinaluu.github.io/linh-tung/
```

Script tự build lại với đúng đường dẫn Pages (để ảnh preview khi gửi link hiện đúng),
commit và push. Lần sau chỉ cần chạy lại một lệnh đó.

Nếu dùng Netlify thay GitHub, build kèm `--url https://linh-tung.netlify.app` rồi kéo thả
thư mục `dist/linh-tung/`.

Script tự: thu nhỏ ảnh về cạnh dài 640px (giữ nguyên tỉ lệ, xoay đúng chiều, HEIC→JPG),
đổi tên game trong manifest và thẻ chia sẻ, xuất bản một file HTML chơi offline, đồng thời
cảnh báo nếu video quá nặng, ảnh trong config bị thiếu hoặc ảnh thừa chưa dùng.

Phiếu tư vấn khách: [docs/intake.md](docs/intake.md) · Ba gói dịch vụ và phạm vi:
[docs/packages.md](docs/packages.md).
Mẹo: mỗi khách nên làm trong một khung chat riêng, còn việc sửa engine thì làm ở chat
của repo này để mọi bản đều được hưởng.

## Cấu trúc thư mục

```
index.html          khung giao diện (các màn hình + hộp thoại)
css/style.css       giao diện retro, bố cục cho laptop / iPad / điện thoại
js/config.js        nội dung của khách  ← sửa ở đây
js/assets.js        đường dẫn ảnh dùng chung
js/levels.js        bố cục màn chơi (gai, bục, gạch, vị trí quà)
js/engine.js        vòng lặp game: vật lý, va chạm, camera, vẽ canvas
js/main.js          điều phối màn hình, HUD, điều khiển, cắt cảnh
js/audio.js         hiệu ứng âm thanh chiptune sinh bằng WebAudio (không cần file)
assets/             brand (logo, favicon), characters, elements, props, ui, scenes, photos, video
assets/preview.png  ảnh hiện khi gửi link — dựng lại bằng tools/make_preview.py
tools/              new_customer.py, build_customer.py, deploy_customer.py (quy trình từng khách),
                    build_standalone.py (gộp 1 file), package.py (đóng gói zip demo),
                    make_preview.py (ảnh preview khi chia sẻ link)
customers/          tư liệu từng khách — KHÔNG đưa lên GitHub
docs/               intake.md (phiếu tư vấn), packages.md (3 gói dịch vụ)
```

## Kỹ thuật

- Vanilla JS (ES modules) + Canvas 2D, không framework, không bước build khi phát triển.
- Nền là ảnh parallax 2 lớp 3840×1080; cảnh vẽ ở tỉ lệ cố định, phần trời phía trên tô
  bằng màu khai báo sẵn trong `assets.js` (chạy từ `file://` không đọc được pixel ảnh).
- Canvas đổi độ phân giải theo tỉ lệ màn hình nên không méo và không cắt nhân vật.
- Âm thanh sinh bằng WebAudio, không kèm file mp3.
- `tools/build_standalone.py` gộp các module thành một file HTML chạy được qua `file://`.

Cờ khi thử nghiệm: mở trang với `#autostart` để vào thẳng màn chơi, `#debug` để lấy ván
chơi hiện tại qua `window.__game` trong console.

## Thêm vào màn hình chính (chạy như app)

`manifest.webmanifest` + các thẻ `apple-mobile-web-app-*` giúp game mở toàn màn hình khi
được thêm vào màn hình chính: iPhone/iPad dùng Safari → nút Chia sẻ → *Thêm vào MH chính*;
Android dùng Chrome → ⋮ → *Cài ứng dụng*. Icon lấy từ `assets/brand/`.

## Ảnh preview khi gửi link

`index.html` khai báo thẻ Open Graph trỏ tới `assets/preview.png` (1200×630) và favicon
lấy từ `assets/brand/`. Sửa chữ trên ảnh thì đổi các hằng đầu file `tools/make_preview.py`
rồi chạy `python3 tools/make_preview.py`.

Zalo/Messenger/Facebook lưu cache preview theo từng đường dẫn — sau khi đổi ảnh, gửi link
kèm `?v=2` hoặc dùng <https://developers.facebook.com/tools/debug/> để lấy bản mới.

## Bản quyền

Mã nguồn và đồ hoạ trong repo này thuộc về tác giả. Vui lòng không sao chép để bán lại.
