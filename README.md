# Made for Us

Game pixel-art chạy trên trình duyệt, làm quà kỷ niệm cho một cặp đôi: chàng trai đi
thu thập quà, vượt chướng ngại, gặp cô gái, rồi cả hai cùng đi qua từng cột mốc của
chuyện tình — kết thúc bằng một lá thư và một đoạn video của riêng họ.

Bản trong repo này là **bản mẫu (demo)**: khung ảnh, video và lá thư để trống cho khách
xem cấu trúc trước khi đặt làm bản cá nhân hoá. **Không sửa nội dung demo này để tạo bản
cho khách** — xem [Làm bản riêng cho từng khách](#làm-bản-riêng-cho-từng-khách) bên dưới.

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

## Nội dung cấu hình (`config.js`)

Toàn bộ nội dung có thể cá nhân hoá nằm trong file `js/config.js` của mỗi bản:

| Sửa gì | Ở đâu trong `config.js` |
| --- | --- |
| Tên game, slogan | `GAME_TITLE`, `GAME_SUBTITLE`, `WINDOW_NAME` |
| Lời thoại, lá thư, các dòng chữ | `TEXT` |
| Ảnh từng mốc, ngày, tên mốc | `MILESTONES` |
| Ảnh màn hình mở đầu | `TITLE_PHOTO` |
| Video | `VIDEO_SRC` |
| Tên 5 món quà | `GIFTS` |
| Khung ảnh trống hiện hay ẩn khi mốc chưa có ảnh | `SHOW_EMPTY_PHOTO_FRAMES` |

Ở bản demo (repo gốc) file này giữ nguyên placeholder trống — **đây là thứ hiển thị công
khai ở link demo**, không sửa trực tiếp. Muốn tạo bản có nội dung thật cho một khách, làm
theo mục dưới.

## Làm bản riêng cho từng khách

**→ [docs/workflow.md](docs/workflow.md) — quy trình đầy đủ, mở file này mỗi khi có khách mới.**
**→ [docs/new-customer-chat.md](docs/new-customer-chat.md) — cách mở khung chat mới và thao tác với Claude Code.**

Tóm tắt: không nhân bản code cho mỗi khách, chỉ nhân bản **nội dung**. Mỗi khách là một
thư mục trong `customers/` (nằm trong `.gitignore`, không lên GitHub). Ba lệnh chính:

```bash
python3 tools/new_customer.py linh-tung      # tạo customers/linh-tung/{brief.md, config.js, assets/}
python3 tools/build_customer.py linh-tung    # thu nhỏ ảnh, build, đóng gói, cảnh báo thiếu/thừa
python3 tools/deploy_customer.py linh-tung https://github.com/Klinaluu/linh-tung.git
```

Khi build, script lấy code mới nhất trong repo + nội dung riêng của khách, nên mọi cải
tiến chung về sau đều đến được với các bản đã giao chỉ bằng cách build và deploy lại.

## Cấu trúc thư mục

```
index.html          khung giao diện (các màn hình + hộp thoại)
css/style.css       giao diện retro, bố cục cho laptop / iPad / điện thoại
js/config.js        nội dung của bản demo — bản khách có config.js riêng trong customers/
js/assets.js        đường dẫn ảnh dùng chung
js/levels.js        bố cục màn chơi (gai, bục, gạch, vị trí quà)
js/engine.js        vòng lặp game: vật lý, va chạm, camera, vẽ canvas
js/main.js          điều phối màn hình, HUD, điều khiển, cắt cảnh
js/audio.js         hiệu ứng âm thanh chiptune sinh bằng WebAudio (không cần file)
assets/             brand (logo, favicon), characters, elements, props, ui, scenes, photos, video
assets/preview.png  ảnh hiện khi gửi link — dựng lại bằng tools/make_preview.py
tools/new_customer.py     tạo thư mục tư liệu cho một khách mới
tools/build_customer.py   build bản riêng từ customers/<slug>/
tools/deploy_customer.py  push bản riêng lên GitHub Pages
tools/build_standalone.py gộp các module JS thành một file HTML chạy qua file://
tools/package.py          đóng gói LẠI bản demo hiện tại (không phải bản khách) thành zip
tools/make_preview.py     dựng lại assets/preview.png khi đổi nội dung ảnh preview
customers/          tư liệu từng khách — KHÔNG đưa lên GitHub
docs/workflow.md              quy trình đầy đủ mỗi khi có khách mới — mở file này trước
docs/new-customer-chat.md     cách mở khung chat mới + thao tác với Claude Code
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

## Nhân vật cá nhân hoá

Sprite nhân vật giống ảnh khách gửi được tạo bằng một quy trình riêng, ngoài codebase
này. Kết quả bỏ vào `customers/<slug>/assets/characters/`, đặt **đúng tên file** như
trong `assets/characters/` ở gốc repo (vd `Man-Walk-Side-01.png`) — `build_customer.py`
tự đè các file trùng tên lên bộ mặc định, file nào không cung cấp thì giữ nguyên sprite
gốc, nên có thể chỉ thay một vài file thay vì làm lại cả bộ.

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
