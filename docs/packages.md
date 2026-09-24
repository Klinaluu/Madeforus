# Ba gói dịch vụ — tư liệu, phạm vi và tình trạng code

> **Phạm vi khung chat này: chỉ Madeforus.love.** Các mục thuộc gói plus/custom (2
> background riêng, 2–3 thử thách/câu hỏi, gameplay/cốt truyện riêng) không xử lý ở đây —
> mở khung chat khác khi cần làm gói đó.

Nguồn: trang báo giá trên Notion (Made For Us). Bảng này đối chiếu **lời hứa với khách**
và **những gì code hiện làm được**, để lúc tư vấn không hứa quá.

| Gói | Giá | Nội dung |
| --- | --- | --- |
| **Madeforus.love** | 499K | Cốt truyện sẵn + cá nhân hoá nhân vật, kỷ niệm, thư & video |
| **Madeforus.plus** | 999K | Như trên + tên/slogan riêng, 2 background riêng, 2–3 thử thách/câu hỏi |
| **Madeforus.custom** | từ 1.999K | Cốt truyện & gameplay riêng |

## Đối chiếu từng hạng mục

| Khách gửi gì | Vào đâu trong game | Tình trạng |
| --- | --- | --- |
| 5–10 ảnh + ngày + tên kỷ niệm | `MILESTONES` trong `config.js` | ✅ tự động, chỉ điền config |
| 1 ảnh mở đầu | `TITLE_PHOTO` | ✅ |
| Lá thư 150–400 chữ | `TEXT.letter` | ✅ |
| Video 30–60 giây | `VIDEO_SRC` | ✅ (tự chuyển .MOV/HEVC sang H.264 nếu cần) |
| 1–2 câu thoại nhân vật | `TEXT.manLine`, `TEXT.meetText` | ✅ |
| Tên game + slogan (gói plus) | `GAME_TITLE`, `GAME_SUBTITLE`, `WINDOW_NAME` | ✅ |
| 5 vật phẩm gắn với hai bạn | `GIFTS` | ⚠️ **đổi được tên, chưa đổi được hình** — icon phải vẽ pixel mới |
| 2 ảnh chân dung → nhân vật trong game | sprite trong `assets/characters/` | 🔧 **quy trình riêng, ngoài code này** — build đã có chỗ để nhận kết quả (xem dưới) |
| 2 background riêng (gói plus) | `assets/scenes/` + `assets.js` | ⚠️ **làm được nhưng thủ công** — dựng SVG 2 lớp rồi render PNG 3840×1080 |
| 2–3 thử thách/câu hỏi (gói plus) | — | ❌ **chưa có tính năng** trong game |
| Link chơi trên điện thoại/iPad/laptop | GitHub Pages | ✅ xem phần dưới |

## Nhân vật cá nhân hoá (gói love)

Quyết định: **quy trình tạo sprite từ ảnh chân dung được xây riêng, ngoài codebase này**
(không phải palette-swap tự động trong repo). Phần build đã chuẩn bị sẵn chỗ nhận kết quả:

- Bỏ sprite đã cá nhân hoá vào `customers/<slug>/assets/characters/`, **đặt đúng tên file**
  như trong `assets/characters/` ở gốc repo (vd `Man-Walk-Side-01.png`, `Woman-Stand-Side-01.png`…).
- `build_customer.py` tự đè các file cùng tên lên bộ mặc định; file nào không cung cấp thì
  giữ nguyên sprite gốc — nên có thể chỉ thay một vài file (vd chỉ đổi 2 khuôn mặt) mà
  không cần làm lại cả bộ 14 hình.
- Danh sách đầy đủ tên file cần khớp: xem `assets/characters/` ở gốc repo.

Vật phẩm riêng (5 vật phẩm gắn với hai bạn): gói love chỉ đổi **tên gọi** trong `GIFTS`
(`config.js`), chưa đổi hình — icon mới không thuộc phạm vi love.

Câu hỏi/thử thách riêng và 2 background riêng là tính năng của gói **plus**, không xử lý
trong khung chat này (xem ghi chú phạm vi ở đầu trang).

## Quy trình giao một bản

```bash
python3 tools/new_customer.py linh-tung          # tạo thư mục tư liệu + brief
# điền config.js, bỏ ảnh/video vào customers/linh-tung/assets/
python3 tools/build_customer.py linh-tung        # build thử, xem cảnh báo
# tạo repo TRỐNG public trên GitHub: Klinaluu/linh-tung
python3 tools/deploy_customer.py linh-tung https://github.com/Klinaluu/linh-tung.git
# lần đầu: bật Settings → Pages → main / (root)
```

Kết quả giao khách:

- **Link**: `https://klinaluu.github.io/linh-tung/` — chơi trên laptop, iPhone, iPad
- **File zip**: `dist/linh-tung.zip` — bản offline giữ làm kỷ niệm
- **Hướng dẫn kèm theo**: iPhone/iPad mở bằng **Safari** → Chia sẻ → *Thêm vào MH chính*
  (game tự hiện hướng dẫn này khi khách mở trên điện thoại); Android dùng Chrome → *Cài ứng dụng*

Lưu ý riêng tư: repo public nên ảnh/thư/video tải được nếu ai đó biết đường dẫn. Nói trước
với khách, hoặc đặt slug khó đoán (`linh-tung-9f3a`), hoặc dùng Netlify nếu khách muốn kín.

## Sau khi giao

- `git tag delivery/linh-tung-2026-10-05` trong `dist/linh-tung` để biết đã giao bản nào
- Giữ `customers/<slug>/` (tư liệu gốc) ít nhất vài tháng phòng khi khách xin sửa
- Khi engine có cải tiến: chạy lại `build_customer.py` + `deploy_customer.py` là bản của
  khách cũ cũng được cập nhật
