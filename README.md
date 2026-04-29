# 📚 ExamPrep — 開源互動式題庫練習系統

[English](./README.en.md) | **繁體中文**

一個純前端、零依賴的題庫練習框架。準備好 JSON 格式的題目與詳解，就能擁有完整的互動練習介面——進度追蹤、筆記、重考模式、自訂模擬考試計時器與 AI 個人化詳解。

> 框架本身不限考試種類，適用於任何可整理成 JSON 格式的題庫。

---

## 🎯 作者的備考故事

這套系統是我備考 **GCP Associate Cloud Engineer（ACE）** 認證時，因為找不到順手的刷題工具而自己動手做的。

GCP ACE 的備考材料散落各處——官方文件、ExamTopics 社群討論、YouTube 解說影片——但沒有一個地方可以讓我「刷題 + 做筆記 + 標記難題 + 模擬考試 + AI 個人化分析」全部整合在一起。

所以我就做了一個。

**實際的備考流程長這樣：**

1. **刷題練習**：逐題作答，翻開詳解確認觀念
2. **標記難題**：遇到搞不清楚的 IAM 或 VPC 題目，按 ⭐ 書籤
3. **做筆記**：在每題下方記下「為什麼選 C 不選 B」這種思考
4. **AI 詳解**：答錯之後請 AI 解釋錯誤原因，或自由提問「這個 Service Account 的情境實際上怎麼用？」
5. **模擬考試**：設定 60 題 / 2 小時，模擬真實考試壓力
6. **重考模式**：考前一天只刷「標記題」與「答錯題」

這套框架把以上流程全部自動化了。你只需要換上自己的題庫 JSON，就能用同樣的系統備考任何考試。

---

## 📸 功能截圖

### 題目練習介面 — 含進度統計、選項作答、答案揭曉
每道題目可展開查看選項，作答後顯示正確答案、詳解、社群討論、筆記欄與 AI 詳解入口。頂部統計列即時顯示完成數與書籤數。
![題目詳解](screenshots/02_question_detail.png)

### 詳解區 — 正確答案分析 + 筆記
![詳解區](screenshots/03_explanation.png)

### AI 進階詳解 — 錯誤分析
![AI 詳解](screenshots/04_ai_explanation.png)

### AI 多輪對話 — 持續追問
AI 詳解支援**多輪對話**——不只是看一段分析，你可以針對任何細節繼續追問，對話記錄會自動儲存，下次開啟同一題時直接從中斷處繼續。
![AI 對話](screenshots/05_ai_chat.png)

### 模擬考試 — 場次選擇 + 計時
![模擬考試](screenshots/06_exam_mode.png)

---

## ⚠️ 使用前提

在開始之前，請確認你了解以下兩點：

### 1. 詳解需要自己撰寫

`explanations.json` 中的每題詳解**需要你自己準備**。

這套框架不會幫你生成詳解內容——它只負責把你準備好的詳解漂亮地呈現出來。

**建議做法：**
- 手動整理每題的正解分析與錯誤選項原因
- 利用 ChatGPT / Claude 等工具批量生成初稿，再人工校對
- 參考本 repo 的 `explanations.json` 格式作為範本

詳解格式說明見下方「替換成自己的題庫」章節。

---

### 2. AI 進階詳解需要自己的 AI API（安全設計）

「🤖 AI 進階詳解」功能會呼叫 **OpenAI 相容 API**。

**重要安全提示：**
- ❌ **API Key / Endpoint / Model 完全不會硬碼在任何 HTML / 程式碼中**
- ✅ **首次使用時系統會提示你輸入 Endpoint / Model / API Key**
- ✅ **設定安全儲存在你的本機瀏覽器（localStorage）**
- ✅ **即使程式碼上傳 GitHub，也完全不會洩露任何敏感資訊**

**你需要：**
- 一個本地或雲端 AI API 服務（例如：[OpenAI](https://platform.openai.com/)、[Anthropic](https://claude.ai/)、[Google Gemini](https://ai.google.dev/)、[OpenCode](https://opencode.ai) 等）
- 該服務的 API Key（首次使用時輸入，只需輸入一次）

**首次使用 AI 功能時的設定流程：**

系統會依序提示你輸入：
1. **API Endpoint**（例如 `https://api.openai.com/v1/chat/completions`）
2. **Model**（例如 `gpt-4o-mini`、`gemini-3-flash-preview`）
3. **API Key**（例如 `sk-xxxx...`）

這些設定會存進 `localStorage`，同一台裝置/同一瀏覽器只需輸入一次。

**想更新設定？**
清除瀏覽器 localStorage（或使用開發者工具），下次使用 AI 會重新提示輸入。

> ℹ️ 不設定 AI API 也完全沒關係，其他所有功能（練習、模擬考、筆記、重考等）均可正常使用，AI 詳解只是附加功能。

> ⚠️ **嵌入式版本（index-embedded.html）** 是以 `file://` 方式開啟，是否能使用 AI 取決於你的 API Endpoint 與瀏覽器限制。
> 一般來說：若 Endpoint 是本機（如 `http://localhost:4142`），多數情況可用；若是雲端 API，可能會被瀏覽器擋掉。
> 若遇到限制，請改用 GitHub Pages 或本地伺服器方式開啟。

---

## ✨ 功能一覽

| 功能 | 說明 |
|------|------|
| 📖 **互動練習** | 選答案、顯示詳解、自動儲存進度 |
| ⭐ **書籤 / 標記** | 標記重要或易錯題目 |
| 📝 **每題筆記** | 記錄答題思路，包含於進度備份 |
| 🔍 **弱點練習** | 點「🔍 弱點練習」按鈕，勾選標記題 / 答錯題，隱藏答案重新作答（不計時） |
| 🎯 **模擬考試** | 自訂每場題數與考試時間；支援🎲隨機出題與📂來源多選篩選（可同時選已標記＋答錯取聯集） |
| 🤖 **AI 進階詳解** | 錯誤分析 + 多輪自由提問對話（需自備 AI API）；內建「AI 路由資訊（驗證用）」面板可查看 endpoint / request model / response model / 狀態 |
| 💬 **社群討論** | 格式化顯示 ExamTopics 原始討論 |
| 💾 **進度管理** | localStorage 自動儲存，單一 JSON 匯出／匯入（含答題、筆記、AI 快取、考試歷史） |
| 🔍 **搜尋 / 篩選** | 依內容、主題、完成狀態篩選 |

---

## 🚀 快速開始

### 方案 A：GitHub Pages（推薦，無需本地伺服器）⭐

這個 repo 已啟用 GitHub Pages，你可以直接在網頁上使用：

**電腦版本：** https://jack880311.github.io/examprep/index-embedded.html

**iPhone/Mobile 版本：** https://jack880311.github.io/examprep/index-mobile.html

> 🔐 **安全提示**：首次使用 AI 功能時，系統會提示你輸入 **API Endpoint + Model + API Key**。這些設定會**安全儲存在你的本機瀏覽器**，不會上傳到 GitHub。

---

## ✅ 適用情境整理（請先看這段）

### 你只是要「直接刷題」（不在乎 AI）
✅ **用 `index-embedded.html`**（雙擊開啟即可，不需要伺服器）

### 你要「公開展示 / 讓別人直接用」
✅ **用 GitHub Pages（index-mobile.html / index-embedded.html）**
⚠️ 注意：GitHub Pages 上**不會有你的私人題庫**（questions.json 被 .gitignore 排除）

### 你要「用自己的題庫 + AI」
✅ **方案 C（本機伺服器 + Tailscale）** 最穩定
✅ 或是把你的題庫上傳到你自己的私有網站

---

## 🔧 方案 C：用自己的題庫 + AI（Tailscale / 本機伺服器）

這個方式可以讓你：
- ✅ iPhone 使用你自己的題庫
- ✅ AI 功能可用
- ✅ 不需要上傳題庫到 GitHub

### Step 1：Mac 啟動本機伺服器（提供題庫檔案）

在專案目錄執行：

```bash
cd "/Users/jack/Desktop/Courses/GCP ACE"
python3 -m http.server 8000
```

保持這個終端不要關閉（它就是你的「題庫伺服器」）。

### Step 2：確認你的 Mac 有 Tailscale IP

打開 Terminal，執行：

```bash
tailscale status
```

找到你的 **macbook** 對應的 IP（例如：`100.115.60.107`）。

### Step 3：iPhone 連上 Tailscale VPN

1. 打開 iPhone 的 Tailscale App
2. 確認狀態為「Connected」

### Step 4：在 iPhone Safari 開啟你的題庫頁面

```
http://<你的Tailscale IP>:8000/index.html
```

例如：
```
http://100.115.60.107:8000/index.html
```

### Step 5：首次使用 AI

系統會提示你輸入：
1. API Endpoint
2. Model
3. API Key

只需要輸入一次，之後會自動記住。

### 方案 B：嵌入式版本（零設定）

直接**雙擊** `index-embedded.html`，無需伺服器、無需安裝任何東西。

### 方案 C：伺服器模式（可動態更新 JSON）

```bash
# macOS / Linux
python3 -m http.server 8000

# Windows
python -m http.server 8000
```

瀏覽器開啟 `http://localhost:8000`

---

## 📁 檔案結構

```
.
├── index.html              # 主程式（開發修改這裡）
├── index-embedded.html     # 嵌入式版本（直接使用）
├── index-mobile.html       # 行動版本（iPhone 最佳化）
├── questions.json          # 題庫資料（不上傳 GitHub）
├── explanations.json       # 題目詳解（不上傳 GitHub）
├── generate_embedded.py    # 重新生成嵌入式版本
├── generate_mobile.py      # 重新生成行動版本
├── parse.py                # 原始資料解析腳本（範例）
├── start-server.command    # macOS 一鍵啟動伺服器
├── start-server.bat        # Windows 一鍵啟動伺服器
└── README.md
```

---

## 🔧 替換成自己的題庫

這套框架可以拿來練習**任何考試**，只需要替換兩個 JSON 檔案。

### `questions.json` 格式

```json
[
  {
    "id": "T1-Q1",
    "topic": 1,
    "idx": 1,
    "question": "題目內容",
    "options": {
      "A": "選項 A 內容",
      "B": "選項 B 內容",
      "C": "選項 C 內容",
      "D": "選項 D 內容"
    },
    "answer": "A",
    "comments_raw": "[username1] Selected Answer: A 理由說明... [username2] Selected Answer: B 另一種看法...",
    "link": "https://example.com/question/1",
    "timestamp": "2024-01"
  }
]
```

| 欄位 | 必填 | 說明 |
|------|------|------|
| `id` | ✅ | 唯一識別碼，建議 `TopicX-QY` 格式 |
| `topic` | ✅ | 主題編號（數字），介面顯示為「Topic N」，用於篩選器 |
| `idx` | ✅ | 題目顯示序號（數字），介面右上角顯示用 |
| `question` | ✅ | 題目內容 |
| `options` | ✅ | 選項物件（A/B/C/D，可多於或少於四個） |
| `answer` | ✅ | 正確答案；多選題用逗號分隔，如 `"A,C"` |
| `comments_raw` | — | 社群討論原始文字，系統自動解析 `[username]` 格式；可留空字串 |
| `link` | — | 題目來源連結 |
| `timestamp` | — | 題目時間戳記 |

### `explanations.json` 格式

```json
{
  "T1-Q1": {
    "correct": "正確答案的詳細說明（建議填寫）",
    "wrong": {
      "B": "B 選項錯誤的原因",
      "C": "C 選項錯誤的原因",
      "D": "D 選項錯誤的原因"
    },
    "knowledge": ["關鍵字1", "關鍵字2"],
    "best_practice": "相關最佳實踐建議",
    "gcloud": "gcloud example command",
    "docs": "https://官方文件連結"
  }
}
```

- key 對應 `questions.json` 的 `id`
- 只有 `correct` 是建議填寫的，其他欄位皆選填
- 沒有對應詳解的題目仍可正常顯示，僅略過詳解區塊

> 💡 **建議做法**：用 ChatGPT / Claude 批量生成 `explanations.json` 初稿（餵入題目與正解），再人工審核調整，效率最高。

### 更新嵌入式版本

修改 JSON 後，執行以下指令重新生成 `index-embedded.html`：

```bash
python3 generate_embedded.py
```

---

## 🤖 AI 進階詳解設定

### 修改 API 設定

開啟 `index.html`，找到以下三行並修改：

```javascript
const AI_ENDPOINT = 'http://localhost:4142/v1/chat/completions';  // API 端點
const AI_MODEL    = 'gemini-3-flash-preview';                      // 模型名稱
const AI_KEY      = 'your-api-key-here';                           // API 金鑰
```

修改後執行 `python3 generate_embedded.py` 重新生成嵌入式版本。

### 常見相容服務

| 服務 | 說明 |
|------|------|
| [LM Studio](https://lmstudio.ai/) | 本地運行開源模型，預設 `localhost:1234` |
| [Ollama](https://ollama.ai/) | 輕量本地模型，預設 `localhost:11434` |
| [OpenAI API](https://platform.openai.com/) | 雲端 GPT 系列，需替換 endpoint 與 key |
| [OpenCode](https://opencode.ai) | 開發者工具，本地 proxy `localhost:4142` |

### 自訂考試情境

介面控制列有「**🤖 AI 考試情境**」欄位，預設為 `GCP Associate Cloud Engineer (ACE)`。換成自己的題庫時修改此欄位，AI prompt 即自動帶入對應情境。設定存於 `localStorage`。

---

## 🎯 模擬考試

點「🎯 模擬考試」後，可自訂：
- **考試時間**（分鐘，預設 120）
- **每場題數**（題，預設 60）
- **🎲 隨機出題**：開啟後每場從候選池隨機抽取題目，不依場次固定範圍
- **📂 題目來源**：全部題目 / ⭐ 已標記題 / ❌ 答錯題（搭配隨機出題使用效果最佳）

套用後系統自動切分場次，點場次卡片即可開考（若開啟隨機出題，直接從選定來源抽題）。計時結束自動交卷，顯示各主題正確率分析與歷史記錄。

---

## 📝 筆記 & 弱點練習

**筆記**：每題展開「📝 我的筆記」，輸入後 500ms 自動儲存，包含於進度 JSON 備份。設計用途是在**考試或練習當下**記錄答題思路——例如「為什麼選 C 不選 B」「這個概念還不確定，要再查」——日後弱點練習時回頭看筆記，就能還原當初為何打書籤的原因。

**弱點練習**：點控制列的「🔍 弱點練習」按鈕，在 Modal 中勾選題目來源（⭐ 已標記題 / ❌ 答錯題，可複選取聯集），按「開始練習」進入弱點練習模式——答案自動隱藏，不計時，適合考前針對弱點複習。題目照原始題號排序，點「顯示答案」只在當次 session 揭曉，**不修改已儲存進度**。

---

## 💾 進度管理

- **📥 下載進度**：匯出為 JSON（含所有答題、書籤、筆記、AI 快取、考試歷史）
- **📤 匯入進度**：選擇備份 JSON 恢復（完整覆蓋）

> ⚠️ 清除瀏覽器快取會導致進度遺失，建議定期匯出備份。

---

## 🌐 環境需求

| 功能 | 需求 |
|------|------|
| 嵌入式版本 | 任何現代瀏覽器，無其他依賴 |
| 伺服器模式 | Python 3.6+ |
| AI 詳解 | 本地或雲端 OpenAI 相容 API |
| 重新生成嵌入式 | Python 3.6+ |

---

## ⚙️ 故障排除

**「無法載入題庫資料」**：使用 `index-embedded.html` 即可避免；伺服器模式請確認 JSON 檔案在同一目錄。

**進度遺失**：請使用一般瀏覽器視窗（非無痕），並定期匯出備份。

**AI 詳解失敗**：確認 API endpoint 是否正確且服務在線。

---

## 📜 關於預設題庫

預設搭載的 GCP ACE 題庫來自 [ExamTopics](https://www.examtopics.com/) 社群討論，詳解由 AI 輔助整理並人工校對。如需替換，請參考上方「替換成自己的題庫」章節。

---

## 🤖 用 AI Agent 快速客製化

把以下 prompt 丟給任何 AI Agent（Claude、ChatGPT、Cursor 等），讓它直接幫你完成題庫轉換或詳解生成：

```
請參考這個專案的架構與 JSON 格式（questions.json / explanations.json），
幫我將以下題目資料轉換成相容的格式，並生成對應的詳解。
[貼上你的題目來源]
```

---

## 📅 版本資訊

**版本：2.14** | 最後更新：2026-04-27

| 版本 | 日期 | 內容 |
|------|------|------|
| 2.14 | 2026-04-27 | AI 區塊新增「AI 路由資訊（驗證用）」面板（含 endpoint / request model / response model / 狀態 / 來源），同時支援「❓ 分析我的錯誤」與「💬 自由提問」 |
| 2.13 | 2026-04-23 | 🔄重考改名為🔍弱點練習（按鈕/Banner/Modal全面更新）；模擬考題目來源改為多選 checkboxes（全部/已標記/答錯可複選取聯集） |
| 2.12 | 2026-04-23 | 修復🔄重考按鈕無反應（modal class 錯誤）；篩選器已標記加上⭐icon；模擬考新增🎲隨機出題與📂題目來源篩選（全部/已標記/答錯） |
| 2.11 | 2026-04-23 | 重考模式重設計：新增「🔄 重考」按鈕與 Modal，可自由勾選「⭐ 已標記題」/「❌ 答錯題」組合進入重考；篩選器移除舊重考選項，加入純「❌ 答錯」篩選 |
| 2.10 | 2026-04-23 | 修復重考模式點選選項後藍底不顯示（新增 retestTouched 追蹤本次互動） |
| 2.9 | 2026-04-23 | 修復模擬考模式選項點擊後藍底不顯示（retestMode 誤清空 selected）；頁碼跳轉移至獨立新行 |
| 2.8 | 2026-04-23 | 還原控制列按鈕文字標籤（重置/匯出/匯入），並維持單行佈局的緊湊度 |
| 2.7 | 2026-04-23 | 優化上方控制列佈局，縮減間距與邊距，將所有按鈕與選項盡可能收納至同一排 |
| 2.6 | 2026-04-23 | 修復模擬考模式答題藍底選取樣式；跳至題號改以 # 題序為準並支援數字輸入；分頁加入手動輸入頁碼 |
| 2.5 | 2026-04-23 | 修復匯入進度後 AI 對話歷史不顯示的問題；匯入後自動重新套用篩選器 |
| 2.4 | 2026-04-23 | 模擬考試模式：答題不顯示選取狀態、隱藏詳解／討論／AI 區塊，僅保留筆記欄 |
| 2.3 | 2026-04-23 | AI 自由提問升級為多輪對話（氣泡介面、對話歷史儲存與還原、清除對話） |
| 2.2 | 2026-04-23 | 模擬考試場次卡片顯示真實最佳分數＋嘗試次數＋最近日期；進度匯出合併為單一 JSON（含 AI 快取、考試歷史） |
| 2.1 | 2026-04-22 | AI 兩按鈕、AI 考試情境自訂、模擬考試時間 / 題數自訂、社群討論格式化、README 雙語 |
| 2.0 | 2026-04-22 | 筆記欄、重考模式、AI 進階詳解、模擬考試（6 場次）|
| 1.1 | 2026-04-22 | 擴充題庫，修復 HTML 注入 bug |
| 1.0 | 2026-04-21 | 初始版本 |
