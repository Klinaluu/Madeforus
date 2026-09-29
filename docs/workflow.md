# Quy trình mỗi khi có khách mới (gói Madeforus.love)

Trang duy nhất cần mở khi có khách mới — làm theo đúng thứ tự bên dưới.
**Bản mẫu:** `customers/thaobe/` (khách đầu tiên làm trọn quy trình này) — khi phân vân
một mục trong `config.js` hay tên file sprite, mở thư mục đó ra xem.
Phần tư vấn/báo giá đã lưu ở Notion. Cách mở khung chat mới và thao tác với Claude Code:
[new-customer-chat.md](new-customer-chat.md).

Nguyên tắc: **không sửa file gốc của repo cho một khách.** Mọi thứ của khách chỉ nằm trong
`customers/<slug>/` (không lên GitHub). Code dùng chung chỉ sửa ở khung chat gốc.

---

## Tổng hợp: cái gì thay cho mỗi khách mới

### A. Khách gửi

| # | Thứ | Quy cách | Vào đâu |
| - | --- | --- | --- |
| 1 | 10 ảnh polaroid (8–12 cũng được) | Ảnh gốc, dọc hay ngang đều được, xếp theo thứ tự thời gian | `assets/photos/` |
| 2 | 1 ảnh màn hình mở đầu (tuỳ chọn) | Nên ảnh dọc kiểu photobooth. Không có → dùng sprite 2 người ôm nhau | `assets/photos/` |
| 3 | 1 video | 15–60 giây, dưới ~25MB, nên quay ngang. `.MOV` cũng được (đổi sang `.mp4` ở Bước 3) | `assets/video/` |
| 4 | Lá thư | Dạng chữ, giữ nguyên văn khách viết | `TEXT.letter` |
| 5 | Tên 5 món quà | + ảnh món quà nếu muốn icon riêng | `GIFTS` |
| 6 | Ảnh 2 người + ảnh chiếc xe máy | Chân dung + toàn thân, trang phục muốn vẽ | làm mẫu vẽ sprite |
| 7 | Tên game + slogan (tuỳ chọn) | Không có → giữ "MADE FOR US / Our love journey" | `GAME_TITLE`, `GAME_SUBTITLE` |
| 8 | Có muốn chữ dưới khung ảnh không | Có → ngày + tên từng mốc. Không → để trống như bản Thảo Bé | `MILESTONES[].date/name` |
| 9 | Tên hai người | Tên/biệt danh muốn in trên thẻ QR bàn giao | `brief.md` → dòng `Tên cặp đôi:` |

### B. Bạn tạo (vẽ theo mặt khách)

Quy cách chung: **PNG nền trong suốt · nhân vật/xe quay mặt sang PHẢI · cắt sát, đáy ảnh
chính là bàn chân / bánh xe** (game neo đáy ảnh xuống mặt đường — thừa khoảng trống ở đáy
thì nhân vật sẽ lơ lửng) · cao khoảng 480–800px · đặt **đúng tên file** vào `assets/characters/`.

| # | Tên file | Dùng ở đâu | Cỡ ở bản Thảo Bé |
| - | --- | --- | --- |
| 1–4 | `Man-Walk-Side-01` … `-04` | Anh đi bộ đoạn mở màn — 4 khung bước chân nối tiếp | 206×480 |
| 5 | `Bike-Idle-01` | Xe dựng chờ ("MY BIKE"), chưa có người | 453×556 |
| 6 | `Man-Bike-Side-01` | Anh chạy xe một mình (chặng solo) | 738×763 |
| 7 | `Woman-Stand-Side-01` | Em đứng chờ ở điểm hẹn | 174×521 |
| 8–9 | `Woman-Cheer-01`, `-02` | Em nhảy mừng khi gặp (2 khung) | 227×574 |
| 10 | `Couple-Pose-Happy-01` | 2 người ôm nhau — màn bầu trời sao (+ làm ảnh mở đầu nếu khách không gửi) | 326×578 |
| 11 | `Couple-Bike-Side-01` | 2 người chở nhau. 1 ảnh là đủ (game tự thêm khói, bụi, vệt gió) — khai báo `COUPLE_FRAMES` | 725×729 |
| 12 | `Portrait-Woman-01` | Ô chân dung trên thanh HUD, gần vuông, cắt mặt | 204×222 |
| 13 | `Scene-Terrace-Sitting-Iso-01` | Tranh minh hoạ trong lá thư | 356×587 |
| 14 | `Scene-Terrace-Bike-Iso-01` | Tranh minh hoạ màn kết thúc | 450×582 |
| + | icon 5 món quà (tuỳ chọn) | Tên tuỳ ý, vd `Item-Coffee-01.png`, khai báo ở `GIFTS[].icon` | 80×116 |

Ảnh gốc khách gửi và bản nháp để trong `assets/characters/_source/` — build bỏ qua.

### C. Cố định — không cần làm gì

Nền Hồ Gươm ban ngày + hoàng hôn (3 lớp), đường, gạch, gai, cây cỏ, mây, trái tim điểm
thưởng, chìa khoá, mũ bảo hiểm, chiếc ô, hòm quà, thanh HUD, nhạc nền, hiệu ứng âm thanh,
hướng dẫn cài app trên điện thoại. (Muốn thay cho riêng một khách: xem cuối Bước 5.)

---

## Bước 0 — Nhận đơn & xin tư liệu

Khách chọn gói trên Notion. Gửi khách tin nhắn dưới đây (copy nguyên), khách gửi tư liệu
vào 1 folder Google Drive:

```
Để làm game cho hai bạn, bạn gửi mình giúp vào 1 folder Google Drive nhé:

1. 10 ảnh kỷ niệm của hai bạn (8–12 ảnh cũng được), xếp theo thứ tự thời gian.
   Ảnh gốc là được, không cần chỉnh.
2. 1 video 15–60 giây (dưới 25MB), nên quay ngang.
3. Lá thư muốn gửi (gõ chữ là được).
4. Tên 5 món quà nhân vật sẽ nhặt trong game (vd: cà phê, máy ảnh, con mèo…).
   Có ảnh món quà thì gửi kèm.
5. Vài ảnh chân dung + toàn thân của hai bạn, và ảnh chiếc xe máy — để mình vẽ nhân vật.
6. Tên (hoặc biệt danh) của hai bạn — để in lên thẻ QR khi giao game.
7. (Tuỳ chọn) 1 ảnh dọc cho màn hình mở đầu, tên game/câu slogan riêng,
   và ngày + tên cho từng ảnh nếu muốn hiện chữ dưới khung ảnh.
```

## Bước 1 — Mở khung chat MỚI cho khách này

**Không làm trong khung chat gốc hay khung khách trước.** Mở khung mới, dán prompt trong
[new-customer-chat.md](new-customer-chat.md), đổi `<slug>` thành tên khách viết liền không
dấu (vd `linh-tung`). Dữ liệu khách sống trên đĩa ở `customers/<slug>/`, không sống trong
chat — khung nào cũng đọc lại được.

## Bước 2 — Tạo khung sườn

```bash
python3 tools/new_customer.py linh-tung
```

Sinh ra `customers/linh-tung/` gồm `brief.md` (checklist tư liệu A + B ở trên),
`config.js` (bản sao cấu hình, đã đặt sẵn chế độ bản khách) và các thư mục `assets/`.

## Bước 3 — Đổ tư liệu khách vào

- Ảnh → `customers/linh-tung/assets/photos/` (script tự thu nhỏ, tự đổi HEIC của iPhone)
- Video → `assets/video/`. Đuôi `.MOV` thì đổi sang `.mp4` (có sẵn trên macOS), xong xoá `.MOV`:

  ```bash
  cd customers/linh-tung/assets/video
  avconvert -s video.MOV -p PresetHighestQuality -o video.mp4 --replace
  ```

- Điền `brief.md`: bảng mốc (thứ tự ảnh), lá thư, ghi chú — để đối chiếu, không ảnh hưởng game.

## Bước 4 — Vẽ sprite (phần B)

1. Mở artifact [Couple Sprite Studio](https://claude.ai/artifact/AtEVsFCuePXKtreWRceo2L),
   điền đơn: tên cặp đôi, ảnh cặp đôi (mục 6 phần A khách gửi), mô tả nhân vật, ảnh + mô tả
   xe máy, props muốn thêm, ghi chú. Bấm **Gửi đơn** — trang tự lưu đơn và hiện sẵn khối
   **Lệnh gửi Claude**.
2. Mở một khung chat **Cowork mới, có kết nối Canva** (khác với khung chat khách đang làm
   ở trên), dán lệnh vừa copy vào đó. Không chạy bước này trong khung chat khách — skill
   `couple-sprite-canva` cần chạy trong Cowork mới dùng được Canva.
3. Skill `couple-sprite-canva` dựng một design Canva mới theo mẫu Thaobe (11 trang 1264×1264,
   8 nếu không có xe), mỗi trang một sprite nền trong suốt, nhân vật/xe quay mặt sang phải.
4. Xuất từng trang thành PNG, đặt **đúng tên file** theo bảng B, bỏ vào
   `customers/<slug>/assets/characters/`. Ảnh gốc khách gửi + bản nháp thì để trong
   `assets/characters/_source/` (build bỏ qua thư mục này).

Kiểm tra từng file trước khi build: quay mặt sang phải, nền trong suốt, đáy ảnh sát chân /
bánh xe.

## Bước 5 — Điền `config.js`

| Mục | Điền gì |
| --- | --- |
| `GAME_TITLE`, `GAME_SUBTITLE`, `WINDOW_NAME` | Tên game / slogan (không có thì giữ mặc định) |
| `TEXT.letter` | Lá thư (bao ngoài bằng dấu `` ` `` để viết nhiều dòng, như bản Thảo Bé) |
| `TEXT.manLine`, `TEXT.meetText` | Câu nói khi gặp / dòng chữ màn bầu trời sao (giữ mặc định nếu khách không đổi) |
| `TITLE_PHOTO` | `"assets/photos/<ảnh mở đầu>"`, hoặc `"assets/characters/Couple-Pose-Happy-01.png"` |
| `VIDEO_SRC` | `"assets/video/video.mp4"` — nhớ có `assets/video/` phía trước |
| `MUSIC_SRC` | Giữ mặc định (nhạc chung). Khách có nhạc riêng → bỏ vào `assets/audio/` rồi trỏ tới |
| `SHOW_EMPTY_PHOTO_FRAMES` | `false` (đã đặt sẵn) |
| `COUPLE_FRAMES` | `["assets/characters/Couple-Bike-Side-01.png"]` nếu chỉ vẽ 1 ảnh xe chở đôi |
| `GIFTS` | Giữ nguyên `id`, đổi `label` (tên món quà) và `icon` (đường dẫn icon riêng nếu có) |
| `MILESTONES` | 1 dòng / ảnh theo thứ tự thời gian: `photo`, `date`, `name` (để `""` nếu không muốn chữ). Ba mốc cuối (mưa / hòm thư / quà) giữ nguyên, chỉ xoá chữ mẫu `DD.MM` / tên mẫu |
| `SCENE_LAYERS` | Để `{}` = nền mặc định |

**Thay ảnh mặc định cho riêng khách (hiếm khi cần):** bỏ file **cùng tên** với file ở gốc
repo vào đúng thư mục của khách — cùng tên thì thay, tên mới thì thêm:

| Thư mục của khách | Thay cho |
| --- | --- |
| `assets/characters/` | nhân vật, xe, icon, tranh minh hoạ (phần B) |
| `assets/elements/` | vật phẩm, khối, đường trong game |
| `assets/props/` | cây cỏ, điểm thưởng |
| `assets/scenes/<id>/` | nền parallax (`L1.png` xa → `L3.png` gần) + khai báo `SCENE_LAYERS` |

## Bước 6 — Build thử

```bash
python3 tools/build_customer.py linh-tung
```

Đọc kỹ phần in ra cuối: **ảnh thiếu** (config trỏ tới file không có), **ảnh thừa** (có ảnh
nhưng config chưa dùng), **video nặng** (>25MB — nên nén lại), danh sách sprite riêng đã
thay (phải đủ 14 file phần B).

## Bước 7 — Test trước khi giao

Chạy thử bằng server cục bộ (`python3 -m http.server` trong `dist/linh-tung/`), ở khung
điện thoại ngang (Chrome DevTools / iPhone Simulator) và desktop. Checklist (cũng có trong
`brief.md`):

- [ ] Màn mở đầu: ảnh, tên game, slogan đúng; nút Start + "Add to Home Screen" thấy rõ
- [ ] Đi bộ: 4 khung bước chân mượt, nhặt chìa khoá + mũ, lên xe
- [ ] Solo: nhặt đủ 5 quà (icon + tên đúng), gai, bục, boss "DOUBT"
- [ ] Gặp nhau: em đứng chờ → nhảy mừng → màn bầu trời sao
- [ ] Đi đôi: xe chở đôi có hiệu ứng chạy, ảnh polaroid đúng thứ tự, chữ dưới ảnh đúng ý khách
- [ ] Đoạn mưa: nhặt được ô, tạnh mưa
- [ ] Lá thư hiện đủ chữ (kể cả dấu tiếng Việt), tranh minh hoạ đúng
- [ ] Video chạy được, nhạc nền tự tắt khi xem video
- [ ] Màn kết thúc: tranh đúng, 3 nút hiện đủ
- [ ] Nhân vật, xe, gai, khối gạch đứng đúng trên vạch kẻ đường (không lơ lửng)
- [ ] Nhạc nền + tiếng nhảy, tắt/mở bằng nút 🔊
- [ ] Điện thoại cầm dọc: thấy màn mở đầu + hộp hướng dẫn; cầm ngang: chơi được

## Bước 8 — Tạo repo & deploy

```bash
gh repo create Klinaluu/linh-tung --public          # repo trống, tên = slug
python3 tools/deploy_customer.py linh-tung https://github.com/Klinaluu/linh-tung.git
gh api -X POST repos/Klinaluu/linh-tung/pages -f "source[branch]=main" -f "source[path]=/"
```

Lệnh `gh api` (bật GitHub Pages) chỉ chạy **lần đầu** của repo đó. Đợi ~1 phút rồi mở
`https://klinaluu.github.io/linh-tung/`. Lần sửa sau chỉ cần chạy lại `deploy_customer.py`.

## Bước 9 — Giao khách

Điền dòng `Tên cặp đôi:` trong `brief.md` (vd `Tên cặp đôi:      Linh & Tùng`), rồi:

```bash
python3 tools/make_qr_card.py linh-tung
```

Script tạo **thẻ QR bàn giao** `customers/linh-tung/qr-card.png` (1080×1350, cùng thiết kế
với artifact [Thẻ QR bàn giao](https://claude.ai/artifact/2atFTscTv31k681V99D3kc), mã QR trỏ
tới `https://klinaluu.github.io/linh-tung/`) và in ra **tin nhắn giao game** (lưu kèm ở
`customers/linh-tung/tin-nhan-giao.txt`). Cần mạng và Google Chrome (chạy ẩn, không mở cửa
sổ). Chưa điền tên trong brief thì truyền thẳng: `--names "Linh" "Tùng"`. Muốn sửa tay
(đổi dòng chữ dưới mã…) thì mở artifact ở trên.

Gửi khách: tin nhắn in ra + ảnh `qr-card.png` (đính kèm ngay sau dòng "Thẻ QR của hai
bạn"). File `dist/linh-tung.zip` (bản offline) **không gửi mặc định** — chỉ gửi khi khách
hỏi, như tin nhắn đã ghi.

Mẫu tin nhắn (script tự điền link; muốn đổi câu chữ thì sửa `MESSAGE` trong
`tools/make_qr_card.py`):

```
Game của hai bạn đã xong rồi nè 💝
🎮 Link game: https://klinaluu.github.io/linh-tung/
Game chơi được ngay trên trình duyệt, cả laptop lẫn điện thoại. Nếu muốn chơi toàn màn hình như một app trên điện thoại:

* iPhone: mở link bằng Safari → bấm nút Chia sẻ (trên iOS mới nằm trong menu ≡ cạnh thanh địa chỉ) → chọn "Thêm vào Màn hình chính"
* Android: mở link bằng Chrome → bấm menu ⋮ → chọn "Cài đặt ứng dụng" hoặc "Thêm vào màn hình chính"

💌 Thẻ QR riêng: chỉ cần quét bằng camera là vào thẳng game. Bạn có thể in ra làm quà hoặc gửi trực tiếp cho người ấy đều xinh nha.
‼️ Một vài lưu ý nhỏ:

* Link và mã QR không có mật khẩu, ai có link đều mở được, nên bạn cân nhắc trước khi chia sẻ công khai nhé.
* Nếu muốn lưu file game để giữ lâu dài hoặc chơi khi không có mạng, cứ nhắn mình nha.
* Bạn có thể gửi yêu cầu chỉnh sửa trong vòng 15 ngày kể từ ngày nhận game ạ.

Chúc hai bạn có thật nhiều khoảnh khắc đáng yêu khi chơi cùng nhau 💖
— Made For Us
```

## Bước 10 — Sau khi giao

```bash
cd dist/linh-tung
git tag delivery/linh-tung-2026-10-05
git push origin delivery/linh-tung-2026-10-05
```

Điền mục "Bàn giao" trong `brief.md` (link, ngày giao, tag; hạn nhận sửa = ngày giao + 15
ngày). Giữ nguyên `customers/linh-tung/` trên máy (không
xoá) — khách xin sửa sau này chỉ cần mở khung chat mới, đọc lại đúng thư mục này.

---

## Khi khách xin sửa

Mở khung chat mới (prompt trong [new-customer-chat.md](new-customer-chat.md)), sửa trong
`customers/<slug>/`, rồi chạy lại Bước 6 → 8 (build + deploy). Link giữ nguyên.

## Khi engine có bug hoặc cải tiến chung

Làm ở **khung chat gốc của repo** (không phải khung khách), vì ảnh hưởng mọi khách. Sau khi
sửa, bản đã giao muốn nhận cải tiến thì chạy lại Bước 6 + 8 cho từng khách. Nếu cải tiến
thêm mục mới vào `config.js`, script build tự điền giá trị mặc định cho config khách cũ.
