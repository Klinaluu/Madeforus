# Ba gói dịch vụ — tư liệu, phạm vi và tình trạng code

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
| 2 ảnh chân dung → nhân vật trong game | sprite trong `assets/characters/` | ⚠️ **chưa có quy trình** — hiện dùng bộ sprite cố định |
| 2 background riêng (gói plus) | `assets/scenes/` + `assets.js` | ⚠️ **làm được nhưng thủ công** — dựng SVG 2 lớp rồi render PNG 3840×1080 |
| 2–3 thử thách/câu hỏi (gói plus) | — | ❌ **chưa có tính năng** trong game |
| Link chơi trên điện thoại/iPad/laptop | GitHub Pages | ✅ xem phần dưới |

## Ba việc cần quyết trước khi nhận đơn đầu tiên

1. **Nhân vật giống khách.** Một bộ sprite gồm 14 hình (nam đi bộ 4 khung, nam đi xe,
   đôi đi xe 4 khung, cô gái đứng, cô gái reo hò 2 khung, ảnh đôi, ảnh chân dung, 2 cảnh
   iso). Ba mức khả thi:
   - *Đổi màu* (rẻ nhất): giữ nguyên hình, đổi màu tóc / áo / da bằng code → hợp gói love.
   - *Vẽ lại đầu & trang phục* trên khung có sẵn → hợp gói plus.
   - *Vẽ mới hoàn toàn* → gói custom.
   Nên ghi rõ trong báo giá để khách không kỳ vọng "giống hệt ảnh" ở gói 499K.
2. **Vật phẩm riêng.** Tương tự: gói love đổi tên gọi, gói plus mới vẽ icon mới.
3. **Thử thách/câu hỏi của gói plus.** Cần thêm tính năng vào engine (hộp thoại câu hỏi
   chặn đường cho tới khi trả lời đúng). Chưa có thì chưa nên bán gói plus.

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
