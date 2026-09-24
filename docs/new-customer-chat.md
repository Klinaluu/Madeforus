# Mở khung chat mới cho mỗi khách

**Nguyên tắc: 1 khách = 1 khung chat mới.** Đừng làm nhiều khách trong cùng một khung —
chat sẽ phình dần, tốn token, và khó lần lại dữ liệu ban đầu.

Điều làm cho việc này an toàn: **dữ liệu không nằm trong chat, nó nằm trên đĩa.** Toàn bộ
"trí nhớ" cần cho một khách là những thứ có sẵn trong repo, không phụ thuộc lịch sử hội thoại:

- `README.md`, `docs/workflow.md` — cách repo hoạt động và quy trình từng bước
- `js/config.js` ở gốc repo — bản mẫu gốc, luôn là nguồn đúng mới nhất
- `customers/<slug>/` — dữ liệu riêng của khách đó (ảnh, config đã điền, brief)

Nên khung chat mới **không cần "nhớ" gì từ khung cũ** — chỉ cần đọc những thứ trên. Việc
đó giữ mỗi chat ngắn, rẻ, và không lẫn dữ liệu khách này sang khách khác.

## Bảng thao tác: từ mở khung chat mới đến giao khách

| # | Thao tác trên Claude Code | Bạn làm / gõ gì |
| - | --- | --- |
| 1 | Mở app Claude Code | Vào project `madeforus` (nếu chưa mở sẵn) |
| 2 | Tạo phiên (chat) mới | Không dùng lại chat của khách trước hay chat sửa engine. Nếu app hỏi thư mục dự án, chọn đúng `Documents/madeforus` |
| 3 | Đặt tên phiên | Đổi tên chat thành tên khách, vd "Made for Us — Linh Tùng", để lần sau tìm lại đúng chat khi khách quay lại xin sửa |
| 4 | Dán prompt mở đầu | Copy khối prompt ở mục dưới, đổi `<slug>`, dán vào ô chat, Enter |
| 5 | Cho phép chạy lệnh | Claude sẽ chạy `tools/new_customer.py`. Nếu app hỏi "cho phép chạy lệnh này?", bấm cho phép |
| 6 | Gửi tư liệu khách | Kéo-thả ảnh/video thẳng vào ô chat, hoặc dán link Google Drive để Claude tải xuống; kèm ngày + tên từng mốc, lá thư, tên game/slogan |
| 7 | Yêu cầu điền config | Nói rõ nội dung (không cần biết cú pháp) — Claude tự sửa `customers/<slug>/config.js` |
| 8 | Yêu cầu build thử | Gõ "build thử cho tôi xem" — Claude chạy `tools/build_customer.py`, đọc phần cảnh báo nó in ra (ảnh thiếu/thừa, video nặng) |
| 9 | Xem trước kết quả | Gõ "cho xem thử trên trình duyệt" — Claude mở bằng Browser pane hoặc chỉ đường mở file cho bạn |
| 10 | Duyệt & sửa | Xem checklist ở `docs/workflow.md` Bước 5, phản hồi trực tiếp trong chat (vd "ảnh mốc 3 để mờ quá"), Claude sửa lại và build lại |
| 11 | Deploy | Gõ "deploy lên `https://github.com/Klinaluu/<slug>.git`" (tạo sẵn repo trống trên GitHub trước) — Claude chạy `tools/deploy_customer.py` |
| 12 | Bật GitHub Pages (chỉ lần đầu của repo đó) | Claude sẽ nhắc; bạn vào Settings → Pages → Branch main / (root) → Save |
| 13 | Nhận link & file giao khách | Claude báo link + đường dẫn `dist/<slug>.zip`; gửi cả hai cho khách |
| 14 | Kết thúc | Không cần đóng chat thủ công — cứ để đó hoặc archive; dữ liệu đã nằm ở `customers/<slug>/` trên đĩa, không mất khi đóng chat |

## Prompt mở đầu (copy-paste)

Dán nguyên văn vào khung chat mới, đổi `<slug>`:

```
Làm bản Made for Us cho khách <slug>.

Đọc trước: README.md, docs/workflow.md.
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

Chỉ khi việc cần làm là sửa **code dùng chung** — engine, giao diện, quy trình build —
vì việc đó ảnh hưởng mọi khách và nên có lịch sử ở một chỗ. Ví dụ: sửa lỗi hiển thị, thêm
cảnh nền, đổi HUD. Xong việc, khách nào build lại cũng tự có bản mới.

## Mẹo giữ khung chat của một khách gọn nhẹ

- Không yêu cầu Claude đọc `js/engine.js` (mấy nghìn dòng) trừ khi thật sự cần sửa engine
  ở đúng khung đó — việc của khung khách chỉ là điền `config.js` + chạy script.
- Ảnh/video gửi qua chat: nếu Claude không lưu được file trực tiếp, gửi link Google Drive
  để tải xuống, hoặc kéo thả file thẳng vào `customers/<slug>/assets/`.
- Xong một khách, không cần giữ khung chat mở — mọi thứ cần giữ đã nằm ở
  `customers/<slug>/` và tag git `delivery/<slug>-<ngày>` trong `dist/<slug>`.
