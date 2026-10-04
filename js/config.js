// ============================================================
// CẤU HÌNH — đây là file duy nhất cần sửa khi cá nhân hoá game
// Ảnh, video, lời thư, tên các mốc… đều nằm ở đây.
// (Bố cục màn chơi ở levels.js, danh sách ảnh dùng chung ở assets.js.)
// ============================================================

// ---------- thương hiệu ----------
export const GAME_TITLE = "MADE FOR US";
export const GAME_SUBTITLE = "Our love journey";
export const WINDOW_NAME = "MADE_FOR_US.EXE"; // chữ trên thanh tiêu đề cửa sổ

// ---------- lời thoại & văn bản ----------
// Game có 2 thứ tiếng: mặc định tiếng Anh, nút VIE ở màn hình mở đầu đổi sang tiếng Việt.
// Các câu dưới đây giữ nguyên câu mẫu tiếng Anh = tự dùng câu mẫu đúng thứ tiếng (js/i18n.js).
// Khách viết câu riêng: ghi 1 chuỗi (dùng cho cả hai thứ tiếng) hoặc { en: "...", vi: "..." }.
// Cách ghi { en, vi } dùng được cả cho GIFTS[].label, MILESTONES[].date/name, GAME_SUBTITLE.
export const TEXT = {
  // đoạn gặp nhau: câu chàng trai nói, rồi câu cô gái đáp lại (2 bong bóng thoại).
  // Câu riêng của từng khách (gửi ở khung chat của khách đó); để "" thì bong bóng đó không hiện.
  // Bản demo dùng câu mẫu bên dưới; khách mới tạo bằng tools/new_customer.py thì để trống sẵn.
  manLine: "Found you.",
  womanLine: "Hi babi",
  // dòng chữ trên màn hình bầu trời sao sau khi gặp nhau
  meetText: "I'm on my solo mission but the stars guide me to you",
  // hộp thoại "System Message" ở chiếc hòm hồng
  systemMessage: "The next level is not unlocked yet.\nWould you like to continue the journey?",
  envelopeLabel: "Highly confidential document",
  // lá thư: thay bằng lời của bạn (xuống dòng bằng \n hoặc dùng chuỗi nhiều dòng)
  letterTitle: "Your love letter",
  letter: "Write your love letter",
  // hiện khi chưa có file video
  videoMissing: "Wait for your video 🎬",
  // chữ trong khung ảnh còn trống
  photoPlaceholder: "(insert pictures here)",
  // nhắc xoay ngang trên điện thoại / máy tính bảng
  rotateTitle: "Please rotate to landscape",
  rotateText: "This journey is made for a sideways screen.",
  rotateTip: "⟳ Hold your device sideways to play",
  // Hướng dẫn thêm vào màn hình chính (chỉ hiện trên điện thoại / máy tính bảng).
  // Để trống thì dùng hướng dẫn mặc định (tiếng Anh / tiếng Việt) trong js/install.js.
  install: {},
};

// ---------- ảnh & video của khách ----------
// Thời gian hiện bong bóng thoại ở đoạn gặp nhau (mili giây, 1000 = 1 giây): chàng trai nói
// trước, cô gái đáp sau (mỗi bên chỉ hiện khi câu có chữ), hết thì sang màn bầu trời sao.
export const MEET_BUBBLE_MS = { man: 2500, woman: 2500 };

// Ảnh polaroid: đặt file vào assets/photos/ rồi điền đường dẫn vào từng mốc bên dưới.
// Video: đặt file .mp4 vào assets/video/ rồi điền tên vào đây (nên dưới 15MB).
export const VIDEO_SRC = "";
// Nhạc nền: đặt file .mp3 vào assets/audio/ rồi điền tên vào đây. Để "" thì không có nhạc nền
// (vẫn còn đủ hiệu ứng nhảy/bấm nút). Tự tắt khi phát video, tự nhỏ lại một chút mỗi lần nhảy.
export const MUSIC_SRC = "assets/audio/bgm.mp3";
// Ảnh ở màn hình mở đầu (ảnh dọc kiểu photobooth rất hợp). Để "" thì hiện khung trống.
export const TITLE_PHOTO = "";
// true  = luôn vẽ khung ảnh trống kèm chữ hướng dẫn (dùng cho bản demo)
// false = mốc nào chưa có ảnh thì không treo khung
export const SHOW_EMPTY_PHOTO_FRAMES = true;

// Ảnh xe chở đôi. Để [] = dùng bộ 4 khung chạy xe mặc định. Chỉ có 1 ảnh thì ghi 1 file —
// game tự thêm hiệu ứng chạy (rung máy, khói, bụi, vệt gió) nên xe vẫn trông đang chạy.
//   export const COUPLE_FRAMES = ["assets/characters/Couple-Bike-Side-01.png"];
export const COUPLE_FRAMES = [];

// ---------- 5 món quà của chặng solo ----------
// icon: để trống ("") thì game tự vẽ hình thay thế.
export const GIFTS = [
  { id: "matcha", label: "Matcha", icon: "assets/elements/Item-MatchaCup.png" },
  { id: "chocolate", label: "Chocolate", icon: "assets/elements/Item-Chocolate.png" },
  { id: "flower", label: "Flowers", icon: "assets/elements/Item-RoseBouquet.png" },
  { id: "lipstick", label: "Lipstick", icon: "" },
  { id: "letter", label: "Letter", icon: "assets/elements/Item-Envelope.png" },
];

// ---------- các mốc của chặng đi đôi ----------
// Mỗi mốc là một khung polaroid treo trên nền, theo thứ tự thời gian.
//   date, name : chú thích in dưới khung ảnh — để "" thì khung không hiện chữ gì (như ở
//                đây, bản demo cố tình để trống); điền cả hai thì khung tự hiện caption
//   photo      : đường dẫn ảnh (để "" nếu chưa có)
//   sky        : hai màu gradient bầu trời [trên, dưới]
//   event      : "rain"  → trời mưa, nhảy chướng ngại để nhặt ô rồi mới đi tiếp
//                "chest" → hòm hồng: System Message → Level Unlocked → lá thư
//                "gift"  → hòm quà rơi từ trời → video
// Ba mốc có event là phần kịch bản, nên giữ nguyên thứ tự ở cuối danh sách và luôn để
// date/name trống (không phải ảnh kỷ niệm của khách).
export const MILESTONES = [
  { date: "", name: "", sky: ["#dfe9ff", "#f6c7d8"], photo: "" },
  { date: "", name: "", sky: ["#3b2a5a", "#b57aa8"], photo: "" },
  { date: "", name: "", sky: ["#bcd7ff", "#ffd9e8"], photo: "" },
  { date: "", name: "", sky: ["#3b2a5a", "#b57aa8"], photo: "" },
  { date: "", name: "", sky: ["#e3d3dc", "#b391a6"], photo: "" },
  { date: "", name: "", sky: ["#ffe6c9", "#ffd9e8"], photo: "" },
  { date: "", name: "", sky: ["#cfe6ff", "#ffe6c9"], photo: "" },
  { date: "", name: "", sky: ["#ffd9c4", "#ffe7ef"], photo: "" },
  {
    date: "", name: "", sky: ["#7fb7d9", "#cfe7f2"], photo: "",
    event: "rain",
    blocks: [{ x: 300 }, { x: 520, h: 2 }],
    platforms: [{ x: 640, w: 2, y: 110 }],
    itemAt: { x: 664, y: 166 },
  },
  { date: "", name: "", sky: ["#ffd9c4", "#ffe7ef"], photo: "", event: "chest" },
  { date: "", name: "", sky: ["#bfe0f2", "#e8f3ee"], photo: "", event: "gift" },
];

// ---------- nền parallax riêng (tuỳ chọn) ----------
// Để trống = dùng bộ nền 3 lớp mặc định (Hồ Gươm ban ngày + hoàng hôn, xem js/assets.js).
// Muốn nền riêng: bỏ ảnh vào customers/<slug>/assets/scenes/<id>/ rồi khai báo lớp (xa → gần)
// + tốc độ trôi (0 = đứng yên, 1 = trôi cùng đường). id: "ho-guom" (đi bộ, solo, gặp nhau),
// "ho-tay" (đi đôi). Ví dụ:
//   "ho-guom": { layers: ["L1.png", "L2.png", "L3.png"], speeds: [0.05, 0.16, 0.4] },
export const SCENE_LAYERS = {};
