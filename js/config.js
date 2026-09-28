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
export const TEXT = {
  // câu nhân vật nam nói khi tìm thấy cô ấy
  manLine: "Found you.",
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
  // Để trống thì dùng chuỗi mặc định tiếng Anh trong js/install.js.
  install: {},
};

// ---------- ảnh & video của khách ----------
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
//   date, name : chú thích in dưới khung ảnh
//   photo      : đường dẫn ảnh (để "" nếu chưa có)
//   sky        : hai màu gradient bầu trời [trên, dưới]
//   event      : "rain"  → trời mưa, nhảy chướng ngại để nhặt ô rồi mới đi tiếp
//                "chest" → hòm hồng: System Message → Level Unlocked → lá thư
//                "gift"  → hòm quà rơi từ trời → video
// Ba mốc có event là phần kịch bản, nên giữ nguyên thứ tự ở cuối danh sách.
export const MILESTONES = [
  { date: "DD.MM", name: "Your milestone 1", sky: ["#dfe9ff", "#f6c7d8"], photo: "" },
  { date: "DD.MM", name: "Your milestone 2", sky: ["#3b2a5a", "#b57aa8"], photo: "" },
  { date: "DD.MM", name: "Your milestone 3", sky: ["#bcd7ff", "#ffd9e8"], photo: "" },
  { date: "DD.MM", name: "Your milestone 4", sky: ["#3b2a5a", "#b57aa8"], photo: "" },
  { date: "DD.MM", name: "Your milestone 5", sky: ["#e3d3dc", "#b391a6"], photo: "" },
  { date: "DD.MM", name: "Your milestone 6", sky: ["#ffe6c9", "#ffd9e8"], photo: "" },
  { date: "DD.MM", name: "Your milestone 7", sky: ["#cfe6ff", "#ffe6c9"], photo: "" },
  { date: "DD.MM", name: "Your milestone 8", sky: ["#ffd9c4", "#ffe7ef"], photo: "" },
  {
    date: "DD.MM", name: "Rainy stop", sky: ["#7fb7d9", "#cfe7f2"], photo: "",
    event: "rain",
    blocks: [{ x: 300 }, { x: 520, h: 2 }],
    platforms: [{ x: 640, w: 2, y: 110 }],
    itemAt: { x: 664, y: 166 },
  },
  { date: "DD.MM", name: "Letter stop", sky: ["#ffd9c4", "#ffe7ef"], photo: "", event: "chest" },
  { date: "DD.MM", name: "Final stop", sky: ["#bfe0f2", "#e8f3ee"], photo: "", event: "gift" },
];

// ---------- nền parallax riêng (tuỳ chọn) ----------
// Để trống = dùng bộ nền 2 lớp mặc định. Muốn nền riêng: bỏ ảnh vào
// customers/<slug>/assets/scenes/<id>/ rồi khai báo lớp (xa → gần) + tốc độ trôi (0 = đứng yên,
// 1 = trôi cùng tốc độ đường). id: "ho-guom" (đi bộ, solo, gặp nhau), "ho-tay" (đi đôi).
//   "ho-guom": { layers: ["L1.png", "L2.png", "L3.png"], speeds: [0.06, 0.18, 0.45] },
export const SCENE_LAYERS = {
  // Hồ Gươm: trời + mây → dãy nhà + hàng cây (sau tháp) → mặt hồ + Tháp Rùa
  "ho-guom": { layers: ["L1.png", "L2.png", "L3.png"], speeds: [0.05, 0.16, 0.4] },
  // Hoàng hôn: trời + mặt trời → skyline + mặt nước → vệt nắng (khoá theo mặt trời)
  "ho-tay": { layers: ["L1.png", "L2.png", "L3.png"], speeds: [0.02, 0.3, 0.02] },
};
