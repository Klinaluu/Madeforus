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
| Video | `VIDEO_SRC` |
| Tên 5 món quà | `GIFTS` |

Các bước thường làm khi giao một bản cá nhân hoá:

1. Chép ảnh vào `assets/photos/` (ảnh vuông hoặc dọc đều được, khung tự co theo tỉ lệ;
   nên thu nhỏ còn cạnh dài ~640px cho nhẹ).
2. Chép video `.mp4` (H.264, nên dưới 15MB) vào `assets/video/`.
3. Mở `js/config.js`: điền `photo` cho từng mốc, `VIDEO_SRC`, `TEXT.letter`, tên mốc và ngày.
4. Đặt `SHOW_EMPTY_PHOTO_FRAMES = false` để mốc chưa có ảnh thì không treo khung trống.
5. Chạy `python3 tools/package.py` → `dist/madeforus.zip` để gửi cho khách.

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
assets/             characters, elements, props, ui, scenes, photos, video
tools/              build_standalone.py (gộp 1 file), package.py (đóng gói zip)
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

## Bản quyền

Mã nguồn và đồ hoạ trong repo này thuộc về tác giả. Vui lòng không sao chép để bán lại.
