// ============================================================
// RIDE TO US — nội dung game
// Phần bạn cần tự thay: MAN_LINE, LETTER_TEXT, VIDEO_SRC, ảnh polaroid.
// ============================================================

const CH = "Assets2/4x/";
const E = "Assets2/Elements-Pixel/4x/";
const UI = "Assets2/UI-Pixel/4x/";

// ---------- Bộ cảnh nền (dùng bằng terrain: "scene:<tên>") ----------
const SCENE_DIR = "Assets2/Scenes-2L/";
// Bộ nền 2 lớp parallax (Vietnam BG 2 Layer): L1 = trời + cảnh xa (đục), L2 = cảnh gần
// (trong suốt), render 3840×1080. Mặt đất của cảnh ở y = 380/540 → sink 160.
// Chỉ dùng 2 cảnh: Hồ Gươm cho cả đoạn trước khi gặp, Hồ Tây hoàng hôn cho đoạn đi đôi.
const L2 = (id) => [`${SCENE_DIR}${id}/L1.png`, `${SCENE_DIR}${id}/L2.png`];
export const SCENES = {
  "ho-guom": L2("ho-guom"),
  "ho-tay": L2("ho-tay"),
};
export const SCENE_IDS = Object.keys(SCENES);
export const SCENE_SPEEDS = [0.25, 1.0];
// Cảnh có bục cỏ / prop thiên nhiên (cảnh phố dùng gạch + prop đô thị)
export const GRASS_SCENES = ["ho-guom"];
// Màu mép trên lớp trời của từng cảnh — tô liền phần trời phía trên ảnh (dự phòng khi
// không đọc được pixel, ví dụ chạy trực tiếp từ file://)
export const SCENE_TOP = { "ho-guom": "#bfe0e2", "ho-tay": "#e2620a" };
// Phần đáy cảnh (theo hệ 540px) chìm dưới mặt đường
export const SCENE_SINK = Object.fromEntries(SCENE_IDS.map((id) => [id, 160]));

export const GAME_TITLE = "MADE FOR US";
export const GAME_SUBTITLE = "Our love journey";
// Bản demo (madeforus) bật hai cờ này để hiện khung ảnh trống có chữ hướng dẫn
export const EMPTY_POLAROIDS = true;
export const PHOTO_PLACEHOLDER = "(insert pictures here)";

// ---------- ảnh dùng chung ----------
export const IMG = {
  playerSolo: CH + "Man-Bike-Side-01.png",
  walkFrames: [CH + "Man-Walk-Side-01.png", CH + "Man-Walk-Side-02.png", CH + "Man-Walk-Side-03.png", CH + "Man-Walk-Side-04.png"],
  key: CH + "Item-Key-01.png",
  helmet: CH + "Item-Helmet-01.png",
  coupleFrames: [CH + "Couple-Bike-Side-01.png", CH + "Couple-Bike-Side-02.png", CH + "Couple-Bike-Side-Motion-01.png", CH + "Couple-Bike-Side-03.png"],
  woman: CH + "Woman-Stand-Side-01.png",
  womanCheer: [CH + "Woman-Cheer-01.png", CH + "Woman-Cheer-02.png"],
  couplePose: CH + "Couple-Pose-Happy-01.png",
  portraitWoman: CH + "Portrait-Woman-01.png",
  sceneTerraceBike: CH + "Scene-Terrace-Bike-Iso-01.png",
  sceneTerraceSitting: CH + "Scene-Terrace-Sitting-Iso-01.png",
  keyHelmet: CH + "Item-Key-Helmet-01.png",
  heartFull: UI + "Heart-Full.png",
  heartEmpty: UI + "Heart-Empty.png",
  bars: [UI + "Bar-0.png", UI + "Bar-25.png", UI + "Bar-50.png", UI + "Bar-75.png", UI + "Bar-100.png"],
  cloud: E + "Nature-Cloud.png",
  road: E + "Road-Straight.png",
  roadHorizon: E + "Road-Horizon.png",
  brick: E + "Block-Brick.png",
  brickRow: E + "Block-BrickRow.png",
  blockSurprise: E + "Block-Surprise.png",
  blockUsed: E + "Block-Used.png",
  itemHeart: E + "Item-Heart.png",
  terrainHills: E + "Nature-Hills.png",
  terrainRiverLake: E + "Nature-RiverLake.png",
  terrainRiceField: E + "Nature-RiceField.png",
  terrainSunset: E + "Nature-Sunset.png",
  bgSunset: E + "BG-Sunset.png",
  bgSea: E + "BG-Sea.png",
  grassFloat: E + "Props/Platform-Grass-Float.png",
  grassGround: E + "Props/Ground-Grass-Short.png",
  egg: E + "Props/Egg-Gold.png",
};
// Cảnh vật ven đường (tách từ sprite sheet), rải tự động theo từng đoạn
const PR = E + "Props/";
export const PROPS = {
  treeRound: PR + "Tree-Round.png", treePine: PR + "Tree-Pine.png", bushSmall: PR + "Bush-Small.png", bushWide: PR + "Bush-Wide.png",
  bushRound: PR + "Bush-Round.png", mushroom: PR + "Mushroom-Blue.png", grass: PR + "Grass-Tuft.png", log: PR + "Log.png",
  flowerBlue: PR + "Flower-Blue.png", flowerWhite: PR + "Flower-White.png", flowers: PR + "Flowers-White.png", sprout: PR + "Sprout.png", rabbit: PR + "Rabbit.png",
};
// bộ cảnh vật theo loại cảnh: [tên, chiều cao (px thế giới)]
export const PROP_SETS = {
  nature: [["treeRound", 120], ["treePine", 104], ["bushWide", 46], ["bushSmall", 40], ["bushRound", 36], ["mushroom", 34], ["grass", 30], ["log", 26], ["flowerBlue", 30], ["flowerWhite", 30], ["flowers", 32], ["sprout", 30], ["rabbit", 30]],
  city: [["grass", 26], ["flowerBlue", 28], ["bushSmall", 34], ["sprout", 26], ["flowers", 28]],
};

// ---------- CHƯƠNG 1: solo mission — thu thập 5 món quà ----------
// Ảnh "lipstick" chưa có: game tự vẽ tạm, khi nào có file thì đặt vào
// Assets2/Elements-Pixel/4x/Item-Lipstick.png.
export const ITEMS = [
  { id: "matcha", label: "Matcha", icon: E + "Item-MatchaCup.png" },
  { id: "chocolate", label: "Chocolate", icon: E + "Item-Chocolate.png" },
  { id: "flower", label: "Flowers", icon: E + "Item-RoseBouquet.png" },
  { id: "lipstick", label: "Lipstick", icon: E + "Item-Lipstick.png" },
  { id: "letter", label: "Letter", icon: E + "Item-Envelope.png" },
];

// Bố cục từng đoạn (tính từ đầu đoạn, đơn vị px thế giới; 1 viên gạch = 44px; mỗi đoạn dài SOLO_SEG_W).
// Vật lý: nhảy đơn cao ~116px, nhảy đôi (bấm lần 2 lúc lên tới đỉnh) cao ~206px.
//   blocks:     [{ x, w?, h? }]      — chồng gạch trên mặt đường (w, h tính bằng viên), khối đặc
//   platforms:  [{ x, w, y, move?, breakable? }] — bục gạch lơ lửng, y = độ cao mặt bục so với mặt đường
//                 move: { dx, dy, speed } — bục di chuyển qua lại (dx) / lên xuống (dy)
//                 breakable: true         — gạch vỡ: đội đầu từ dưới là tan
//   spikes:     [{ x, n, y? }]       — dãy n gai (mỗi gai 22px), y = đặt trên bục (mặc định mặt đường)
//   itemAt:     { x, y }             — món quà, y = độ cao đáy món quà so với mặt đường
//   heartBlock: { x }                — ô "?" nhảy đội từ dưới lên để nhận thêm 1 tim
export const SOLO_SEG_W = 1300;
export const WALK_TERRAIN = "scene:ho-guom";
export const BOSS_TERRAIN = "scene:ho-guom";
export const MEET_TERRAIN = "scene:ho-guom";
export const SOLO_SEGMENTS = [
  {
    item: "matcha", terrain: "scene:ho-guom", sky: ["#bfe0f2", "#e8f3ee"],
    platforms: [{ x: 160, w: 1, y: 140, breakable: true }, { x: 720, w: 2, y: 96 }],
    blocks: [{ x: 300 }, { x: 960, w: 2 }],
    spikes: [{ x: 480, n: 3 }, { x: 860, n: 2 }],
    itemAt: { x: 1120, y: 100 },
  },
  {
    item: "chocolate", terrain: "scene:ho-guom", sky: ["#cfe2f3", "#e9f0f5"],
    blocks: [{ x: 180, h: 2 }, { x: 1120 }],
    spikes: [{ x: 460, n: 3 }, { x: 980, n: 3 }],
    platforms: [{ x: 580, w: 3, y: 140 }],
    itemAt: { x: 1230, y: 150 },
    heartBlock: { x: 820 },
  },
  {
    item: "flower", terrain: "scene:ho-guom", sky: ["#cfe2f3", "#e9f0f5"],
    blocks: [{ x: 120, w: 2 }, { x: 208, w: 2, h: 2 }, { x: 296, w: 2, h: 3 }],
    platforms: [{ x: 420, w: 2, y: 190, move: { dx: 70, dy: 0, speed: 1.4 } }, { x: 1100, w: 2, y: 100 }],
    spikes: [{ x: 400, n: 4 }, { x: 780, n: 3 }, { x: 960, n: 4 }],
    itemAt: { x: 1122, y: 156 },
  },
  {
    item: "lipstick", terrain: "scene:ho-guom", sky: ["#f7b46a", "#f08a3c"],
    spikes: [{ x: 160, n: 3 }, { x: 420, n: 4 }, { x: 700, n: 2 }, { x: 1040, n: 2 }],
    platforms: [{ x: 300, w: 2, y: 100 }, { x: 520, w: 3, y: 100, move: { dx: 0, dy: 50, speed: 1.3 } }, { x: 760, w: 2, y: 150 }, { x: 940, w: 2, y: 100 }],
    itemAt: { x: 1150, y: 100 },
  },
  {
    item: "letter", terrain: "scene:ho-guom", sky: ["#f7b46a", "#f08a3c"],
    blocks: [{ x: 150, h: 2 }],
    spikes: [{ x: 380, n: 3 }, { x: 560, n: 3 }, { x: 950, n: 2 }, { x: 1100, n: 2 }],
    platforms: [{ x: 640, w: 3, y: 110 }, { x: 640, w: 2, y: 250, breakable: true }, { x: 860, w: 2, y: 175 }, { x: 1000, w: 2, y: 120 }],
    itemAt: { x: 1200, y: 100 },
  },
];

export const MAX_HEARTS = 3;

// ---------- CHƯƠNG 2: gặp nhau ----------
export const MAN_LINE = "Found you."; // câu thoại của nhân vật nam — bạn sửa tuỳ ý
export const MEET_TEXT = "I'm on my solo mission but the stars guide me to you";

// ---------- CHƯƠNG 3: đi cùng nhau ----------
// Mỗi mốc: biển báo ở đầu đoạn + khung polaroid trên trời (photo để trống,
// sau này bạn điền đường dẫn ảnh vào là tự hiện).
//   event: "rain"  → trời mưa, phải nhảy qua chướng ngại (blocks/platforms) để nhặt ô (itemAt), tạnh mưa rồi đi tiếp
//   event: "chest" → chiếc hòm hồng: System Message → Level Unlocked → thư
//   event: "gift"  → hòm quà rơi từ trời → video
// Mốc đi đôi: không còn biển báo địa điểm — chỉ polaroid ảnh thật treo trên nền.
// Ảnh gốc ở Assets2/photos/<tên>.jpg → tools/photos.py thu nhỏ (không crop) vào Assets2/photos/p/.
const PH = "Assets2/photos/p/";
export const MILESTONES = [
  { date: "DD.MM", name: "Your milestone 1", terrain: "scene:ho-tay", sky: ["#dfe9ff", "#f6c7d8"], photo: "" },
  { date: "DD.MM", name: "Your milestone 2", terrain: "scene:ho-tay", sky: ["#3b2a5a", "#b57aa8"], photo: "" },
  { date: "DD.MM", name: "Your milestone 3", terrain: "scene:ho-tay", sky: ["#bcd7ff", "#ffd9e8"], photo: "" },
  { date: "DD.MM", name: "Your milestone 4", terrain: "scene:ho-tay", sky: ["#3b2a5a", "#b57aa8"], photo: "" },
  { date: "DD.MM", name: "Your milestone 5", terrain: "scene:ho-tay", sky: ["#e3d3dc", "#b391a6"], photo: "" },
  { date: "DD.MM", name: "Your milestone 6", terrain: "scene:ho-tay", sky: ["#ffe6c9", "#ffd9e8"], photo: "" },
  { date: "DD.MM", name: "Your milestone 7", terrain: "scene:ho-tay", sky: ["#cfe6ff", "#ffe6c9"], photo: "" },
  { date: "DD.MM", name: "Your milestone 8", terrain: "scene:ho-tay", sky: ["#ffd9c4", "#ffe7ef"], photo: "" },
  {
    date: "DD.MM", name: "Rainy stop", terrain: "scene:ho-tay", sky: ["#7fb7d9", "#cfe7f2"], photo: "",
    event: "rain",
    blocks: [{ x: 300 }, { x: 520, h: 2 }],
    platforms: [{ x: 640, w: 2, y: 110 }],
    itemAt: { x: 664, y: 166 },
  },
  { date: "DD.MM", name: "Letter stop", terrain: "scene:ho-tay", sky: ["#ffd9c4", "#ffe7ef"], photo: "", event: "chest" },
  { date: "DD.MM", name: "Final stop", terrain: "scene:ho-tay", sky: ["#bfe0f2", "#e8f3ee"], photo: "", event: "gift" },
];

// ---------- CHƯƠNG 4: hòm quà ----------
export const SYSTEM_MESSAGE = "The next level is not unlocked yet.\nWould you like to continue the journey?";
export const ENVELOPE_LABEL = "Highly confidential document";

// Nội dung thư
export const LETTER_TEXT = "Write your love letter";

// Video ngắn: đặt file .mp4 vào Assets2/video/ rồi sửa tên ở đây (tối đa ~15MB).
export const VIDEO_SRC = "";

export const ENDING_TEXT = "Happy our 1 year anniversary, cheers to our next chapter together";
