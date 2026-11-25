import json

# Define enriched metadata for all 50 slides
slides_data = [
    # Unit 1
    {
        "page": 1,
        "title": "Codex打造超級小幫手 · AI Agent時代來臨",
        "subtitle": "橘子老師 · 20261124 實戰研習簡報",
        "unit": 1,
        "unit_name": "講師簡介與社群交流",
        "badge": "研習開場",
        "summary": "本次研習核心聚焦於 OpenAI Codex 打造超級 AI Agent 助理，介紹從 Prompt、Context 到 Loop Engineering 的進化，以及試算表自動化、財產報廢 SKILL 與課前出題排程等三大落地實務。",
        "texts": [
            "Codex打造超級小幫手",
            "AI Agent時代來臨",
            "研習短網址：https://reurl.cc/1lp4K8",
            "主講人：橘子老師"
        ],
        "links": [
            {"text": "研習講義短網址", "href": "https://reurl.cc/1lp4K8"}
        ],
        "prompts": []
    },
    {
        "page": 2,
        "title": "講師個人專頁 · 橘子老師",
        "subtitle": "專注於 AI 教育創新、自動化工作流與 Agent 實戰",
        "unit": 1,
        "unit_name": "講師簡介與社群交流",
        "badge": "講師介紹",
        "summary": "橘子老師個人 Facebook 專頁交流，持續分享最新 AI 教育工具、Codex 與 Agent 教學應用經驗。",
        "texts": [
            "橘子老師 個人 Facebook 專頁",
            "https://www.facebook.com/ju.laoshi",
            "歡迎教育夥伴交流討論 AI 與自動化教學"
        ],
        "links": [
            {"text": "Facebook：橘子老師", "href": "https://www.facebook.com/ju.laoshi"}
        ],
        "prompts": []
    },
    {
        "page": 3,
        "title": "橘子老師教室 · 官方粉絲專頁",
        "subtitle": "第一手 AI 工具教學、提示詞包與教育科技實例分享",
        "unit": 1,
        "unit_name": "講師簡介與社群交流",
        "badge": "社群專頁",
        "summary": "追蹤「橘子老師教室」，定期獲取最新 AI 教學提示詞、SKILL 技能包與實務自動化工作流教材。",
        "texts": [
            "橘子老師教室 粉專",
            "https://www.facebook.com/profile.php?id=61580433065847",
            "掌握最新 AI 教育前沿科技與落地教學案例"
        ],
        "links": [
            {"text": "FB 粉專：橘子老師教室", "href": "https://www.facebook.com/profile.php?id=61580433065847"}
        ],
        "prompts": []
    },
    {
        "page": 4,
        "title": "社群交流 · 加入「每天開心玩Ai」LINE社群",
        "subtitle": "教育科技共學圈，隨時交流 AI 提問與最新技巧",
        "unit": 1,
        "unit_name": "講師簡介與社群交流",
        "badge": "LINE社群",
        "summary": "加入「每天開心玩Ai」LINE 社群，今日入群密碼為「happyai」，歡迎大家一起共學與交流實戰心得。",
        "texts": [
            "加入「每天開心玩Ai」LINE社群",
            "今日密碼: happyai",
            "與各級教師夥伴即時互動、解決問題"
        ],
        "links": [
            {"text": "加入「每天開心玩Ai」LINE社群 (密碼: happyai)", "href": "https://line.me/ti/g2/WcNwA_0Zf-ciDHCVodeEpFFBLd0PmGwKlhRprg?utm_source=invitation&utm_medium=link_copy&utm_campaign=default"}
        ],
        "prompts": []
    },
    {
        "page": 5,
        "title": "進入主題 · AI Agent 時代來臨",
        "subtitle": "從單純對話走向自主任務執行的全新典範",
        "unit": 1,
        "unit_name": "講師簡介與社群交流",
        "badge": "主題導入",
        "summary": "AI 不再只是回答問題的聊天機器人，而是能自主規劃、調用工具、讀取環境與完成複雜工作流的超級小幫手（AI Agent）。",
        "texts": [
            "Codex",
            "AI Agent",
            "次世代 AI 助手正深刻改變教育與行政工作流程"
        ],
        "links": [],
        "prompts": []
    },

    # Unit 2
    {
        "page": 6,
        "title": "認識 OpenAI Codex",
        "subtitle": "專為程式碼理解、工作流建置與自動化打造的 AI Agent",
        "unit": 2,
        "unit_name": "Codex 環境建置與工程架構",
        "badge": "環境概觀",
        "summary": "介紹 Codex 的核心定位，它能理解整個專案目錄脈絡，並具備自動讀寫檔案、調用終端指令與執行腳本的強大能力。",
        "texts": [
            "Codex",
            "AI Agent",
            "專為開發與自動化量身打造的智能助理"
        ],
        "links": [],
        "prompts": []
    },
    {
        "page": 7,
        "title": "Codex 官方入口與資源導覽",
        "subtitle": "前往 OpenAI Codex 繁體中文官方頁面",
        "unit": 2,
        "unit_name": "Codex 環境建置與工程架構",
        "badge": "官方入口",
        "summary": "介紹 OpenAI Codex 官方頁面與產品架構，了解其支援的平台與各項企業級/教育級功能。",
        "texts": [
            "官方網站：https://openai.com/zh-Hant/codex/",
            "Codex AI Agent 核心介紹與功能規範"
        ],
        "links": [
            {"text": "OpenAI Codex 官方頁面", "href": "https://openai.com/zh-Hant/codex/"}
        ],
        "prompts": []
    },
    {
        "page": 8,
        "title": "Codex 下載與環境準備",
        "subtitle": "安裝與設定 Codex 運行環境",
        "unit": 2,
        "unit_name": "Codex 環境建置與工程架構",
        "badge": "軟體安裝",
        "summary": "示範如何下載與安裝 Codex 用戶端或外掛，完成初次啟動與系統前置檢查。",
        "texts": [
            "Codex 下載與環境安裝",
            "登入帳號並配置運算核心環境"
        ],
        "links": [
            {"text": "OpenAI Codex 官網下載", "href": "https://openai.com/zh-Hant/codex/"}
        ],
        "prompts": []
    },
    {
        "page": 9,
        "title": "外掛工具安裝 · 擴充功能生態系",
        "subtitle": "把需要用到的外掛工具都裝上去",
        "unit": 2,
        "unit_name": "Codex 環境建置與工程架構",
        "badge": "外掛擴充",
        "summary": "安裝必要的擴充套件（Extensions / Plugins），包含 Google Workspace 整合、試算表工具、Gmail 發信模組等，賦予 Codex 操作真實軟體的能力。",
        "texts": [
            "把需要用到的外掛工具都裝上去",
            "Google Drive / Sheets / Gmail 外掛套件整合"
        ],
        "links": [],
        "prompts": []
    },
    {
        "page": 10,
        "title": "權限設定 · 系統操作與安全存取授權",
        "subtitle": "設定終端機執行、檔案讀寫與雲端服務權限",
        "unit": 2,
        "unit_name": "Codex 環境建置與工程架構",
        "badge": "權限設定",
        "summary": "詳細解說 Codex 執行所需的安全權限設定，包含檔案存取範圍、終端命令核准機制與雲端授權安全邊界。",
        "texts": [
            "權限設定 (Permissions)",
            "確保 Agent 在受控與安全邊界內執行檔案存取與命令"
        ],
        "links": [],
        "prompts": []
    },
    {
        "page": 11,
        "title": "指令呼叫技巧 · 輸入「/」斜線指令",
        "subtitle": "快速觸發內建功能、Skill 與自訂工作流",
        "unit": 2,
        "unit_name": "Codex 環境建置與工程架構",
        "badge": "指令技巧",
        "summary": "在對話框中輸入「/」即可開啟指令選單（Slash Commands），快速叫出各類技能、工作流或預設自動化工具。",
        "texts": [
            "輸入: /",
            "叫出 Slash Commands 與 SKILL 快捷選單"
        ],
        "links": [],
        "prompts": ["/"]
    },
    {
        "page": 12,
        "title": "選擇模型 · 運算引擎最佳化配置",
        "subtitle": "依據任務複雜度選擇最合適的 AI 模型",
        "unit": 2,
        "unit_name": "Codex 環境建置與工程架構",
        "badge": "模型選擇",
        "summary": "示範如何在 Codex 中切換不同的 AI 模型（如速度優先的輕量模型或深度推理的大模型），兼顧產出速度與分析精度。",
        "texts": [
            "選擇模型 (Model Selection)",
            "依任務難度切換推理大模型或輕量高敏模型"
        ],
        "links": [],
        "prompts": []
    },
    {
        "page": 13,
        "title": "AI 工程三大演化階段",
        "subtitle": "從 Prompt ➔ Context ➔ Loop Engineering",
        "unit": 2,
        "unit_name": "Codex 環境建置與工程架構",
        "badge": "工程演進",
        "summary": "闡述 AI 應用開發的三個歷史階段：第一階段是單純寫好問題的 Prompt Engineering；第二階段是注入外部資料與記憶的 Context Engineering；第三階段則是讓 Agent 具備自我檢測與閉環修正的 Loop Engineering。",
        "texts": [
            "第一階段：Prompt Engineering (提示工程)",
            "第二階段：Context Engineering (脈絡工程)",
            "第三階段：Loop Engineering (迴圈工程)"
        ],
        "links": [],
        "prompts": []
    },
    {
        "page": 14,
        "title": "Codex 特別關注的核心文件體系",
        "subtitle": "AGENTS.md、.agents/skills/ 與 SKILL.md",
        "unit": 2,
        "unit_name": "Codex 環境建置與工程架構",
        "badge": "核心架構",
        "summary": "剖析專案目錄中真正屬於 Codex Agent 特別關注的核心規範文件，包含引導 Agent 行為的 AGENTS.md 以及標準技能存放庫 .agents/skills/。",
        "texts": [
            "真正屬於 Codex 特別關注的是：",
            "• AGENTS.md",
            "• .agents/skills/",
            "• SKILL.md",
            "而 README.md、GOALS.md、PLANS.md、PROMPTS.md、harness/ 等屬於實用的專案說明文件"
        ],
        "links": [],
        "prompts": []
    },

    # Unit 3
    {
        "page": 15,
        "title": "專案四大說明書職責分工",
        "subtitle": "README.md、GOALS.md、PLANS.md、PROMPTS.md",
        "unit": 3,
        "unit_name": "專案記憶盤點與 SKILL 技能規格體系",
        "badge": "文件分工",
        "summary": "清晰劃分專案四大核心文件：README.md 給人看、GOALS.md 明確願景、PLANS.md 鋪設步驟路線圖、PROMPTS.md 典藏重複任務指令庫。",
        "texts": [
            "README.md：給「人」看的專案說明書",
            "GOALS.md：「我們到底要做出什麼？」(願景與驗收標準)",
            "PLANS.md：「我要怎麼走？」(路線圖與里程碑)",
            "PROMPTS.md：「這個專案常用的 Agent 任務指令庫」"
        ],
        "links": [],
        "prompts": []
    },
    {
        "page": 16,
        "title": "文件職責對照清單",
        "subtitle": "讓人與 Agent 各司其職的現代軟體工程心法",
        "unit": 3,
        "unit_name": "專案記憶盤點與 SKILL 技能規格體系",
        "badge": "文件職責",
        "summary": "將專案文件標準化，確保未來重啟專案或不同協作者加入時，人能看懂專案、Agent 也能立即接手開發。",
        "texts": [
            "README.md 給「人」看的專案說明書",
            "GOALS.md「我們到底要做出什麼？」",
            "PLANS.md 我要怎麼走？",
            "PROMPTS.md「這個專案常用的 Agent 任務指令庫」"
        ],
        "links": [],
        "prompts": []
    },
    {
        "page": 17,
        "title": "完整專案知識盤點與 Agent 記憶整理 Prompt",
        "subtitle": "讓 Agent 深入掃描目前專案代碼、設定與工作流程",
        "unit": 3,
        "unit_name": "專案記憶盤點與 SKILL 技能規格體系",
        "badge": "核心提示詞",
        "summary": "橘子老師研發的經典記憶整理提示詞，要求 Agent 完整讀取專案既有代碼與脈絡，將知識提煉保存，讓未來重啟時可無縫延續。",
        "texts": [
            "請對目前這個 Codex 專案進行一次「完整專案知識盤點與 Agent 記憶整理」。",
            "你的目標不是單純建立幾個空白文件，而是要「讀取目前專案的實際程式、設定、文件、工作流程、既有 Skills 與開發脈絡」，將這個專案目前已經形成的知識完整整理並保存，使未來重新開啟本專案時，另一個 Codex Agent 可以快速理解專案並延續開發。"
        ],
        "links": [],
        "prompts": [
            "請對目前這個 Codex 專案進行一次「完整專案知識盤點與 Agent 記憶整理」。你的目標不是單純建立幾個空白文件，而是要「讀取目前專案的實際程式、設定、文件、工作流程、既有 Skills 與開發脈絡」，將這個專案目前已經形成的知識完整整理並保存，使未來重新開啟本專案時，另一個 Codex Agent 可以快速理解專案並延續開發。"
        ]
    },
    {
        "page": 18,
        "title": "AGENTS.md 增量規則整合策略",
        "subtitle": "先讀取原內容，不直接覆蓋既有開發智慧",
        "unit": 3,
        "unit_name": "專案記憶盤點與 SKILL 技能規格體系",
        "badge": "規則維護",
        "summary": "建立或更新 AGENTS.md 時的重要原則：若檔案已存在，切勿粗暴覆蓋，應先讀取分析舊內容，再將最新確認的規則與架構增量合併進去。",
        "texts": [
            "建立：AGENTS.md",
            "如果目前已經存在 AGENTS.md，不要直接覆蓋。",
            "請先讀取原內容，再將目前專案中已經確認的規則、架構與開發知識整合進去。"
        ],
        "links": [],
        "prompts": [
            "如果目前已經存在 AGENTS.md，不要直接覆蓋。請先讀取原內容，再將目前專案中已經確認的規則、架構與開發知識整合進去。"
        ]
    },
    {
        "page": 19,
        "title": "Skill 盤點機制與職責邊界",
        "subtitle": "分析可被重複執行、具有明確流程的工作",
        "unit": 3,
        "unit_name": "專案記憶盤點與 SKILL 技能規格體系",
        "badge": "技能抽象",
        "summary": "如何判斷什麼任務適合做成 Skill？檢視專案中是否有「高頻重複、流程固定、需要專用知識或調用工具」的作業，將其封裝為獨立 Skill。",
        "texts": [
            "檢查：.agents/skills/",
            "如果目前不存在，建立它。",
            "請分析目前專案有哪些「可以被重複執行、具有明確流程、需要特定知識或工具」的工作，判斷哪些適合抽象成 Skill。"
        ],
        "links": [],
        "prompts": [
            "請分析目前專案有哪些「可以被重複執行、具有明確流程、需要特定知識或工具」的工作，判斷哪些適合抽象成 Skill。"
        ]
    },
    {
        "page": 20,
        "title": "每個 Skill 的標準規範路徑",
        "subtitle": ".agents/skills/<skill-name>/SKILL.md",
        "unit": 3,
        "unit_name": "專案記憶盤點與 SKILL 技能規格體系",
        "badge": "規範路徑",
        "summary": "規範 Skill 的統一命名與目錄標準，以 SKILL.md 作為核心進入點，包含 YAML Frontmatter 描述、觸發條件與逐步流程說明。",
        "texts": [
            "每個 Skill 必須建立：",
            ".agents/skills/<skill-name>/SKILL.md",
            "SKILL.md 必須包含 YAML 描述、觸發詞與作業流程"
        ],
        "links": [],
        "prompts": []
    },
    {
        "page": 21,
        "title": "Skill 資料夾標準四層架構",
        "subtitle": "SKILL.md + scripts/ + references/ + assets/",
        "unit": 3,
        "unit_name": "專案記憶盤點與 SKILL 技能規格體系",
        "badge": "資料夾架構",
        "summary": "展示標準 Skill 資料夾結構：SKILL.md 說明 SOP、scripts/ 存放腳本、references/ 放置規格文件、assets/ 保存模板素材。",
        "texts": [
            ".agents/skills/<skill-name>/",
            "├── SKILL.md      (告訴 Agent 怎麼做)",
            "├── scripts/          (真正執行工作的工具)",
            "├── references/   (Agent 工作時查閱的知識)",
            "└── assets/           (Skill 執行時需要的素材)"
        ],
        "links": [],
        "prompts": []
    },
    {
        "page": 22,
        "title": "模組化職責解耦原則",
        "subtitle": "不要把所有內容全部塞進 SKILL.md",
        "unit": 3,
        "unit_name": "專案記憶盤點與 SKILL 技能規格體系",
        "badge": "設計心法",
        "summary": "SKILL.md 應保持精簡俐落，專注於流程決策與調度，將冗長的 API 規範移入 references/、可執行腳本移入 scripts/，避免 Context 爆量與維護災難。",
        "texts": [
            "其中：",
            "• SKILL.md = Agent 的操作說明",
            "• scripts/ = 可以實際執行的工具",
            "• references/ = Agent 執行任務時需要查閱的知識",
            "• assets/ = 範本、圖片、JSON、設定檔或其他必要素材",
            "不要把所有內容全部塞進 SKILL.md！"
        ],
        "links": [],
        "prompts": []
    },
    {
        "page": 23,
        "title": "Codex 專案五大層級金字塔",
        "subtitle": "規則 ➔ 能力 ➔ 知識 ➔ 工具 ➔ 實際產品",
        "unit": 3,
        "unit_name": "專案記憶盤點與 SKILL 技能規格體系",
        "badge": "五層金字塔",
        "summary": "橘子老師整理的 Codex 專案五層架構全景圖：AGENTS.md (規則) ➔ skills (能力) ➔ references (知識) ➔ scripts (工具) ➔ src (產品)。",
        "texts": [
            "🧠 Agent 規則：AGENTS.md ➔ 告訴 Codex「怎麼工作」",
            "🧩 Agent 能力：.agents/skills/ ➔ 告訴 Codex「有哪些專業技能」",
            "📚 Agent 知識：references/ ➔ 告訴 Codex「需要知道什麼」",
            "⚙️ Agent 工具：scripts/ ➔ 告訴 Codex「可以執行什麼」",
            "💻 實際產品：src/ ➔ 真正的應用程式"
        ],
        "links": [],
        "prompts": []
    },
    {
        "page": 24,
        "title": "讓 Codex 記住目前專案 · 提示詞範本與下載",
        "subtitle": "專案知識持久化與長期記憶整理指令",
        "unit": 3,
        "unit_name": "專案記憶盤點與 SKILL 技能規格體系",
        "badge": "實務提示詞",
        "summary": "提供可直接下載與複製的提示詞模板，一鍵讓 Codex 整理架構、代碼規則、UI規範、資料流向與測試部署手冊。",
        "texts": [
            "想「讓 Codex 記住目前這個專案」",
            "請分析目前整個專案，將目前已經存在的功能、架構、程式規則、開發流程、UI 規範、資料流程、測試方式、部署方式與重要注意事項整理成 Codex Agent 可以長期使用的專案知識。"
        ],
        "links": [],
        "prompts": [
            "想「讓 Codex 記住目前這個專案」：請分析目前整個專案，將目前已經存在的功能、架構、程式規則、開發流程、UI 規範、資料流程、測試方式、部署方式與重要注意事項整理成 Codex Agent 可以長期使用的專案知識。請完成以下工作：建立或更新 AGENTS.md、整理 .agents/skills/ 技能架構、確認 references/ 知識庫，使任何未來的 Agent 都能立即理解並延續開發。"
        ]
    },

    # Unit 4
    {
        "page": 25,
        "title": "實戰應用一：試算表自動化處理",
        "subtitle": "整合 Google Sheets 進行批次清洗、篩選與運算",
        "unit": 4,
        "unit_name": "實戰應用一：試算表自動化與個人化通知信小幫手",
        "badge": "實戰開場",
        "summary": "開啟第一個實戰應用案例：利用 Codex 自動化讀取試算表、條件式篩選教師資料並產生客製化信件。",
        "texts": [
            "試算表處理",
            "Codex AI Agent 實戰篇：自動化處理試算表資料"
        ],
        "links": [],
        "prompts": []
    },
    {
        "page": 26,
        "title": "建立填報表單與工作表結構",
        "subtitle": "設計線上資料收集表單",
        "unit": 4,
        "unit_name": "實戰應用一：試算表自動化與個人化通知信小幫手",
        "badge": "表單設計",
        "summary": "規劃資料收集流程，建立包含姓名、身分別、帳號與到期日等關鍵欄位的 Google 填報表單。",
        "texts": [
            "建立填報表單",
            "規劃表單題目與對應之資料欄位格式"
        ],
        "links": [],
        "prompts": []
    },
    {
        "page": 27,
        "title": "表單線上連結與資料收集",
        "subtitle": "公開表單供成員填報資料",
        "unit": 4,
        "unit_name": "實戰應用一：實戰應用一：試算表自動化與個人化通知信小幫手",
        "badge": "表單連結",
        "summary": "發布線上填報表單，讓測試成員或教師填寫，自動匯流至 Google Sheets 試算表中。",
        "texts": [
            "建立填報表單",
            "提供表單公開連結以收集實際資料"
        ],
        "links": [],
        "prompts": []
    },
    {
        "page": 28,
        "title": "填報表單結構驗證",
        "subtitle": "檢查各欄位填寫正確性",
        "unit": 4,
        "unit_name": "實戰應用一：試算表自動化與個人化通知信小幫手",
        "badge": "結構驗證",
        "summary": "驗證表單所產生的試算表結構，確認欄位名稱、資料型態與空值防呆規則。",
        "texts": [
            "建立填報表單",
            "確認資料正確同步至後端試算表"
        ],
        "links": [],
        "prompts": []
    },
    {
        "page": 29,
        "title": "表單回應試算表彙整",
        "subtitle": "檢視收集到的身分與信箱名冊",
        "unit": 4,
        "unit_name": "實戰應用一：試算表自動化與個人化通知信小幫手",
        "badge": "資料彙整",
        "summary": "檢視累積之試算表資料，包含各類身分別（如 1, 2, 3, 4）以及需要通知的帳號群組。",
        "texts": [
            "建立填報表單",
            "形成完整的帳號重置通知名單資料庫"
        ],
        "links": [],
        "prompts": []
    },
    {
        "page": 30,
        "title": "上下文標記技巧 · 輸入「@」提及檔案",
        "subtitle": "直接在對話中載入指定試算表或文件脈絡",
        "unit": 4,
        "unit_name": "實戰應用一：試算表自動化與個人化通知信小幫手",
        "badge": "指令技巧",
        "summary": "輸入「@」符號可直接呼叫檔案選擇清單（At Mention），將指定 Google 試算表直接作為對話上下文輸入給 Codex。",
        "texts": [
            "輸入: @",
            "直接提及並載入特定試算表、文檔或資料庫上下文"
        ],
        "links": [],
        "prompts": ["@"]
    },
    {
        "page": 31,
        "title": "試算表資料結構解析",
        "subtitle": "身分別、帳號與到期日欄位對齊",
        "unit": 4,
        "unit_name": "實戰應用一：試算表自動化與個人化通知信小幫手",
        "badge": "欄位分析",
        "summary": "分析試算表中每一列紀錄，確認篩選條件（例如身分別為 3 或 4 者），為自動化發信做好準備。",
        "texts": [
            "試算表資料欄位解析",
            "定位篩選鍵值與個人化信件模板代入欄位"
        ],
        "links": [],
        "prompts": []
    },
    {
        "page": 32,
        "title": "試算表篩選、假名脫敏與信件草稿提示詞",
        "subtitle": "實戰高階提示詞：批次篩選 + 資料脫敏 + 個人化郵件草稿",
        "unit": 4,
        "unit_name": "實戰應用一：試算表自動化與個人化通知信小幫手",
        "badge": "核心提示詞",
        "summary": "包含兩大核心任務：第一是篩選身分別3或4者寄送重置警告信（需經確認才發送）；第二是教學去識別化脫敏（替換為明星姓名與假信箱另存新檔）。",
        "texts": [
            "提示詞 1 (篩選發信)：從這個試算表中篩選出身分別為3或4的資料，並以jam@fyjh.ntpc.edu.tw帳號寄發帳號重置通知信件，信件標題: google ai帳號重置通知，內容: (使用者名稱)老師好，這個帳號(顯示帳號名稱)，將於7/15重置，請先備份該帳號相關重要資料以免重置後資料遺失，請先給我信件草稿，不要直接寄出，由我決定使否寄出信件",
            "提示詞 2 (資料脫敏)：把使用人欄位姓名換成明星的中文名字，email: 則改成隨意編排帳號名稱@gmail.com，重新另存一個試算表檔案給我，存在同一個資料夾中"
        ],
        "links": [],
        "prompts": [
            "從這個試算表中篩選出身分別為3或4的資料，並以jam@fyjh.ntpc.edu.tw帳號寄發帳號重置通知信件，信件標題: google ai帳號重置通知，內容: (使用者名稱)老師好，這個帳號(顯示帳號名稱)，將於7/15重置，請先備份該帳號相關重要資料以免重置後資料遺失，請先給我信件草稿，不要直接寄出，由我決定使否寄出信件",
            "把使用人欄位姓名換成明星的中文名字，email: 則改成隨意編排帳號名稱@gmail.com，重新另存一個試算表檔案給我，存在同一個資料夾中"
        ]
    },
    {
        "page": 33,
        "title": "設定 Codex 寄信使用的帳號",
        "subtitle": "在 ChatGPT 網頁版中進行認證與設定",
        "unit": 4,
        "unit_name": "實戰應用一：試算表自動化與個人化通知信小幫手",
        "badge": "信箱設定",
        "summary": "指導如何在 ChatGPT 網頁版或 Codex 設定中綁定 Gmail 發信帳號，確保寄發郵件的發信人身分合規與安全。",
        "texts": [
            "設定codex寄信使用的帳號",
            "在Chatgpt網頁版中配置郵件帳號連線"
        ],
        "links": [],
        "prompts": []
    },
    {
        "page": 34,
        "title": "郵件外掛授權連線設定",
        "subtitle": "完成 Google Workspace OAuth 授權",
        "unit": 4,
        "unit_name": "實戰應用一：試算表自動化與個人化通知信小幫手",
        "badge": "OAuth授權",
        "summary": "點擊同意授權畫面，讓 Agent 獲得以使用者身分建立 Gmail 草稿或寄送郵件的安全存取憑證。",
        "texts": [
            "設定codex寄信使用的帳號",
            "完成 OAuth 2.0 授權登入流程"
        ],
        "links": [],
        "prompts": []
    },
    {
        "page": 35,
        "title": "綁定發信信箱與預設設定",
        "subtitle": "指定專用公務或學校信箱帳號",
        "unit": 4,
        "unit_name": "實戰應用一：試算表自動化與個人化通知信小幫手",
        "badge": "發信身分",
        "summary": "確認已成功綁定發信郵件地址，例如 jam@fyjh.ntpc.edu.tw，並確認預設寄件身分。",
        "texts": [
            "設定codex寄信使用的帳號",
            "確認發信信箱綁定成功"
        ],
        "links": [],
        "prompts": []
    },
    {
        "page": 36,
        "title": "郵件草稿產生與格式審核",
        "subtitle": "先出草稿由使用者核准，落實人機協同防呆",
        "unit": 4,
        "unit_name": "實戰應用一：試算表自動化與個人化通知信小幫手",
        "badge": "草稿審核",
        "summary": "Codex 產生每一位受通知教師的郵件草稿與代入內容，使用者逐一確認無誤後，方才下達寄送指令。",
        "texts": [
            "郵件草稿預覽",
            "確認每一封郵件的受託人、帳號名稱與到期時間無誤"
        ],
        "links": [],
        "prompts": []
    },
    {
        "page": 37,
        "title": "自動發信執行完成與成果報表",
        "subtitle": "完成批次寄發並回傳寄送統計報表",
        "unit": 4,
        "unit_name": "實戰應用一：試算表自動化與個人化通知信小幫手",
        "badge": "寄送完成",
        "summary": "顯示所有符合條件名單之寄發成功狀態，並在原試算表標記寄發時間與狀態欄位，達成完美自動化。",
        "texts": [
            "發信執行成果回報",
            "批次通知完成，無漏發與誤發"
        ],
        "links": [],
        "prompts": []
    },

    # Unit 5
    {
        "page": 38,
        "title": "實戰應用二：建立財產報廢申請單全域 SKILL",
        "subtitle": "行政繁瑣流程自動化：照片識別 ➔ 財產核對 ➔ 表單產出",
        "unit": 5,
        "unit_name": "實戰應用二：建立財產報廢申請單全域 SKILL",
        "badge": "實戰開場",
        "summary": "開啟第二個實戰應用：行政人員經常需要辦理財產報廢，透過多模態照片辨識、財產清冊核對與 Google 文件套表，建立一鍵完成的全域 SKILL。",
        "texts": [
            "建立財產報廢申請單",
            "將傳統耗時的行政表單作業轉化為標準自動化技能"
        ],
        "links": [],
        "prompts": []
    },
    {
        "page": 39,
        "title": "建立專案資料夾與工作環境",
        "subtitle": "專案 --> + --> 指定專案名稱與指定資料夾",
        "unit": 5,
        "unit_name": "實戰應用二：建立財產報廢申請單全域 SKILL",
        "badge": "專案建立",
        "summary": "在介面中點選專案（Projects）並點擊「+」，建立專案資料夾以存放所有相關的申請單範本與清冊資料。",
        "texts": [
            "建立專案資料夾",
            "專案 --> + --> 指定專案名稱，指定資料夾"
        ],
        "links": [],
        "prompts": []
    },
    {
        "page": 40,
        "title": "財產報廢實例素材包與資源連結",
        "subtitle": "申請單範本、照片素材、財產清冊與提示詞全套資源",
        "unit": 5,
        "unit_name": "實戰應用二：建立財產報廢申請單全域 SKILL",
        "badge": "素材資源",
        "summary": "橘子老師提供的實戰教材包，包含申請單 Google 文件範本、報廢設備範例照片、財產 Excel/Sheets 檔案與標準提示詞。",
        "texts": [
            "財產報廢申請單 實戰素材：",
            "1. 財產報廢申請單 (Google Docs)",
            "2. 範例照片 (Google Drive)",
            "3. 範例財產檔案 (Google Sheets)",
            "4. 提示詞文件 (Google Drive)"
        ],
        "links": [
            {"text": "財產報廢申請單 (Google Docs)", "href": "https://docs.google.com/document/d/1ycXsCTt2Q-PgNkp6wz-OUnCMr-0ByBpL/edit?usp=drive_link&ouid=114425903125895498189&rtpof=true&sd=true"},
            {"text": "範例照片 (Google Drive)", "href": "https://drive.google.com/file/d/1Ur8aPxQ8N5ccepBKg439qcljlbMBDYyn/view?usp=drive_link"},
            {"text": "範例財產檔案 (Google Sheets)", "href": "https://docs.google.com/spreadsheets/d/1hllWwzfOnPZ3Vbfnm5qgS90Vd1uTIc2g/edit?usp=drive_link&ouid=114425903125895498189&rtpof=true&sd=true"},
            {"text": "提示詞文件 (Google Drive)", "href": "https://drive.google.com/file/d/1G253bCwUvQN80D7Y_bRCZiGyOTZSr8XW/view?usp=drive_link"}
        ],
        "prompts": []
    },
    {
        "page": 41,
        "title": "將工作流程封裝為全域 SKILL",
        "subtitle": "很好，將這個工作流程建立全域SKILL",
        "unit": 5,
        "unit_name": "實戰應用二：建立財產報廢申請單全域 SKILL",
        "badge": "全域SKILL",
        "summary": "測試單次執行成功後，下達關鍵指令「很好，將這個工作流程建立全域SKILL」，讓 Agent 自動產生 SKILL.md、定義觸發指令與自動化腳本。",
        "texts": [
            "很好，將這個工作流程建立全域SKILL",
            "建立SKILL：將測試成功的工作流沉澱為跨專案隨時可用的全域能力"
        ],
        "links": [],
        "prompts": [
            "很好，將這個工作流程建立全域SKILL"
        ]
    },

    # Unit 6
    {
        "page": 42,
        "title": "實戰應用三：AI 自動課前複習題生成",
        "subtitle": "結合課堂紀錄、教材文本與自動出題演算法",
        "unit": 6,
        "unit_name": "實戰應用三：AI 課前複習題生成與雲端自動排程",
        "badge": "實戰開場",
        "summary": "開啟第三個實戰案例：讀取教師課堂筆記與教科書內容，自動出題、存檔並排程寄信給授課老師，大幅減輕備課負擔。",
        "texts": [
            "AI自動課前複習題生成",
            "教務與教學實踐：課前複習題目智能生成"
        ],
        "links": [],
        "prompts": []
    },
    {
        "page": 43,
        "title": "設計課前複習題生成全域 SKILL 提示詞",
        "subtitle": "幫我把以下提示詞轉成正確的SKILL格式（4大標準流程）",
        "unit": 6,
        "unit_name": "實戰應用三：AI 課前複習題生成與雲端自動排程",
        "badge": "核心提示詞",
        "summary": "定義完整的 4 步出題流程：1. 讀取雲端課堂紀錄試算表 2. 獲取最近課程紀錄 3. 參考課本出 5 題複習題 + 5 題延伸題 4. 存檔至 Google 文件並透過 Gmail 發送。",
        "texts": [
            "設計複習題生成SKILL：幫我把以下提示詞轉成正確的SKILL格式",
            "課前複習題生成全域SKILL",
            "1. 讀取 jaremy.tw@gmail.com 帳號雲端硬碟「教師課堂紀錄系統」資料夾中試算表檔案資料，列出班級科目資料",
            "2. 讀取各班級科目最近一次的課程內容紀錄",
            "3. 參考「教師課堂紀錄系統」資料夾中課本資料，生成5題與最近一次課程有關的複習題，另外5題則為前5題類似的延伸題",
            "4. 將生成題目以 Google 文件儲存在「教師課堂紀錄系統」資料夾中的複習題資料夾裡的當日資料夾中(如果沒有則建立這個資料夾)，並且以 Gmail 程式 mail 給 jaremy.tw@gmail.com，信件直接寄出不用使用者確認"
        ],
        "links": [],
        "prompts": [
            "幫我把以下提示詞轉成正確的SKILL格式\n\n課前複習題生成全域SKILL：\n1. 讀取 jaremy.tw@gmail.com 帳號雲端硬碟「教師課堂紀錄系統」資料夾中試算表檔案資料，列出班級科目資料\n2. 讀取各班級科目最近一次的課程內容紀錄\n3. 參考「教師課堂紀錄系統」資料夾中課本資料，生成5題與最近一次課程有關的複習題，另外5題則為前5題類似的延伸題\n4. 將生成題目以 Google 文件儲存在「教師課堂紀錄系統」資料夾中的複習題資料夾裡的當日資料夾中(如果沒有則建立這個資料夾)，並且以 Gmail 程式 mail 給 jaremy.tw@gmail.com，信件直接寄出不用使用者確認"
        ]
    },
    {
        "page": 44,
        "title": "課前複習題生成流程檢視與執行測試",
        "subtitle": "檢視產出的題庫文件與格式正確性",
        "unit": 6,
        "unit_name": "實戰應用三：AI 課前複習題生成與雲端自動排程",
        "badge": "執行檢核",
        "summary": "執行 Skill 測試，驗證從試算表讀取紀錄、文本關聯出題到 Google 文件格式排版與寄送的流暢度。",
        "texts": [
            "AI自動課前複習題生成",
            "驗證出題邏輯與自動建立當日資料夾"
        ],
        "links": [],
        "prompts": []
    },
    {
        "page": 45,
        "title": "雲端自動排程指令語意結構",
        "subtitle": "雲端排程，每週重複，每週日上午9:00 /pre-class.....",
        "unit": 6,
        "unit_name": "實戰應用三：AI 課前複習題生成與雲端自動排程",
        "badge": "核心提示詞",
        "summary": "橘子老師示範的經典定時排程提示詞：設定每週日上午 9:00 定時觸發出題 Skill，自主執行至學期結束（2027-01-17）。",
        "texts": [
            "雲端排程",
            "雲端排程，每週重複，每週日上午9:00  /pre-class..... 生成課前複習題，執行到2027-01-17 為止"
        ],
        "links": [],
        "prompts": [
            "雲端排程，每週重複，每週日上午9:00  /pre-class..... 生成課前複習題，執行到2027-01-17 為止"
        ]
    },
    {
        "page": 46,
        "title": "雲端排程週期與自動觸發原理",
        "subtitle": "無需本機開機，雲端 Agent 定時自主喚醒運行",
        "unit": 6,
        "unit_name": "實戰應用三：AI 課前複習題生成與雲端自動排程",
        "badge": "排程原理",
        "summary": "解釋雲端排程（Cloud Scheduled Tasks）與傳統本機腳本的差異：即使電腦關機，伺服器端的 Agent 仍會準時在每週日喚醒、出題並寄信。",
        "texts": [
            "雲端排程 (Cloud Scheduling)",
            "雲端自主喚醒，免本機電腦開機"
        ],
        "links": [],
        "prompts": []
    },
    {
        "page": 47,
        "title": "在 ChatGPT 網頁版中配置雲端排程",
        "subtitle": "進入排程任務管理介面",
        "unit": 6,
        "unit_name": "實戰應用三：AI 課前複習題生成與雲端自動排程",
        "badge": "網頁排程",
        "summary": "展示在 ChatGPT 網頁版中如何檢視、啟用與管理已設定的定時自動化任務。",
        "texts": [
            "雲端排程 : 在ChatGPT 網頁版中",
            "檢視排程清單與觸發規則設定"
        ],
        "links": [],
        "prompts": []
    },
    {
        "page": 48,
        "title": "排程執行權限與參數微調",
        "subtitle": "確認雲端排程之存取權限與終止期限",
        "unit": 6,
        "unit_name": "實戰應用三：AI 課前複習題生成與雲端自動排程",
        "badge": "參數配置",
        "summary": "檢查排程的重複頻率、每次執行的提示詞指令參數，以及有效期限設定。",
        "texts": [
            "雲端排程 : 在ChatGPT 網頁版中",
            "設定執行週期：每週日上午 9:00"
        ],
        "links": [],
        "prompts": []
    },
    {
        "page": 49,
        "title": "雲端排程執行紀錄與日誌監控",
        "subtitle": "檢查定時出題之成功日誌與發信狀態",
        "unit": 6,
        "unit_name": "實戰應用三：AI 課前複習題生成與雲端自動排程",
        "badge": "日誌監控",
        "summary": "查看排程歷史日誌（Execution Logs），確認每次出題皆如期完成並成功送達教師信箱。",
        "texts": [
            "雲端排程 : 在ChatGPT 網頁版中",
            "監控排程日誌，確保出題流程順暢無中斷"
        ],
        "links": [],
        "prompts": []
    },
    {
        "page": 50,
        "title": "自動化閉環大成 · 迎接 AI Agent 智慧校園",
        "subtitle": "從備課到行政，由 Agent 打造自主教育科技工作流",
        "unit": 6,
        "unit_name": "實戰應用三：AI 課前複習題生成與雲端自動排程",
        "badge": "總結閉環",
        "summary": "總結全課：透過 Codex 結合 Google Workspace、自訂全域 SKILL 與雲端排程，成功打造全自動自主閉環小幫手，全面賦能教學與行政！",
        "texts": [
            "AI自動課前複習題生成 總結",
            "雲端排程 : 在ChatGPT 網頁版中",
            "實現真正的校園 AI Agent 自動化閉環"
        ],
        "links": [],
        "prompts": []
    }
]

# Write enriched_slides.json
with open("enriched_slides.json", "w", encoding="utf-8") as f:
    json.dump(slides_data, f, ensure_ascii=False, indent=2)

print(f"Generated enriched_slides.json with {len(slides_data)} slides.")
