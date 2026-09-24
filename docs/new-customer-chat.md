# Mở khung chat mới cho mỗi khách

**Nguyên tắc: 1 khách = 1 khung chat mới.** Đừng làm nhiều khách trong cùng một khung —
chat sẽ phình dần, tốn token, và khó lần lại dữ liệu ban đầu.

Điều làm cho việc này an toàn: **dữ liệu không nằm trong chat, nó nằm trên đĩa.** Toàn bộ
"trí nhớ" cần cho một khách là 3 thứ có sẵn trong repo, không phụ thuộc lịch sử hội thoại:

- `js/config.js` ở gốc repo — bản mẫu gốc, luôn là nguồn đúng mới nhất
- `docs/intake.md`, `docs/packages.md` — quy tắc cá nhân hoá & phạm vi gói
- `customers/<slug>/` — dữ liệu riêng của khách đó (ảnh, config đã điền, brief)

Nên khung chat mới **không cần "nhớ" gì từ khung cũ** — chỉ cần đọc 3 thứ trên. Việc đó
giữ mỗi chat ngắn, rẻ, và không lẫn dữ liệu khách này sang khách khác.

## Prompt mở đầu (copy-paste)

Dán nguyên văn vào khung chat mới, đổi `<slug>`:

```
Làm bản Made for Us cho khách <slug>.

Đọc trước: README.md, docs/intake.md, docs/packages.md — phạm vi chat này CHỈ gói love.
Đừng đụng js/engine.js, js/main.js, js/assets.js, js/levels.js hay bất cứ file dùng chung
nào khác trừ khi tôi nói rõ là sửa lỗi chung (việc đó làm ở khung chat gốc, không phải đây).

python3 tools/new_customer.py <slug>   # nếu customers/<slug>/ chưa có
Tôi sẽ gửi ảnh + thông tin qua chat này. Việc của bạn: điền customers/<slug>/config.js,
bỏ ảnh vào customers/<slug>/assets/photos, video vào assets/video, rồi:

python3 tools/build_customer.py <slug>

Xem cảnh báo (ảnh thiếu, ảnh thừa, video nặng) rồi báo tôi trước khi deploy.
```

## Khi khách xin sửa lại (vài tuần/tháng sau)

Mở khung chat mới, dán:

```
Sửa lại bản Made for Us cho khách <slug>. Đọc customers/<slug>/brief.md và config.js
hiện tại trước. Không đụng file dùng chung.
```

`customers/<slug>/` vẫn còn nguyên trên đĩa nên khung chat mới đọc lại là có đủ ngữ cảnh,
không cần chat cũ.

## Khi nào MỚI dùng chung 1 khung với chat gốc (repo `madeforus`)

Chỉ khi việc cần làm là sửa **code dùng chung** — engine, giao diện, quy trình build,
bảng giá — vì việc đó ảnh hưởng mọi khách và nên có lịch sử ở một chỗ. Ví dụ: sửa lỗi
hiển thị, thêm cảnh nền, đổi HUD. Xong việc, khách nào build lại cũng tự có bản mới.

## Mẹo giữ khung chat của một khách gọn nhẹ

- Không yêu cầu Claude đọc `js/engine.js` (mấy nghìn dòng) trừ khi thật sự cần sửa engine
  ở đúng khung đó — việc của khung khách chỉ là điền `config.js` + chạy script.
- Ảnh/video gửi qua chat: nếu Claude không lưu được file trực tiếp (thường gặp), lưu ra
  Google Drive rồi tải xuống, hoặc kéo thả file thẳng vào `customers/<slug>/assets/`.
- Xong một khách, không cần giữ khung chat mở — mọi thứ cần giữ đã nằm ở
  `customers/<slug>/` và tag git `delivery/<slug>-<ngày>` trong `dist/<slug>`.
