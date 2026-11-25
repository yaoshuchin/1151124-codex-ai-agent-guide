import json
import html
import os

project_dir = r"C:\antigravity\1151124Al Agent時代來臨-codex小幫手-橘子老師"
slides_file = os.path.join(project_dir, "enriched_slides.json")

with open(slides_file, "r", encoding="utf-8") as f:
    slides = json.load(f)

# Count slides per unit
unit_counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
for s in slides:
    u = s.get("unit", 1)
    unit_counts[u] = unit_counts.get(u, 0) + 1

# Generate Cards HTML for Reading Mode
cards_html_list = []
for s in slides:
    p = s["page"]
    u = s.get("unit", 1)
    uname = html.escape(s.get("unit_name", f"單元 {u}"))
    badge = html.escape(s.get("badge", "投影片"))
    title = html.escape(s.get("title", f"投影片第 {p} 頁"))
    sub = html.escape(s.get("subtitle", ""))
    desc = html.escape(s.get("desc", ""))
    img = html.escape(s.get("image", f"assets/slides/slide_{p:02d}.png"))
    
    # Key points HTML
    kp_items = []
    for kp in s.get("key_points", []):
        kp_items.append(f'<li class="key-point-item">{html.escape(kp)}</li>')
    kp_html = f'<ul class="key-points-list">{"".join(kp_items)}</ul>' if kp_items else ''
    
    # Links HTML
    link_items = []
    for lnk in s.get("links", []):
        lbl = html.escape(lnk.get("label") or lnk.get("text") or "開啟連結")
        url = html.escape(lnk.get("url") or lnk.get("href") or "#")
        link_items.append(f'<a href="{url}" target="_blank" rel="noopener noreferrer" class="card-link-btn">🔗 {lbl}</a>')
    links_html = f'<div class="card-links-box">{"".join(link_items)}</div>' if link_items else ''
    
    card_html = f'''
    <article class="slide-card" data-card-unit="{u}">
      <div class="card-media-box">
        <img class="card-img" src="{img}" alt="{title}" loading="lazy" />
        <span class="card-page-badge">P.{p:02d}</span>
        <span class="card-zoom-hint">🔍 點擊放大</span>
      </div>
      <div class="card-body">
        <div class="card-header-line">
          <span class="card-unit-badge">{uname}</span>
          <span class="card-type-badge">{badge}</span>
        </div>
        <h3 class="card-title">{title}</h3>
        {f'<p class="card-sub">{sub}</p>' if sub else ''}
        {f'<p class="card-desc">{desc}</p>' if desc else ''}
        {kp_html}
        {links_html}
      </div>
    </article>
    '''
    cards_html_list.append(card_html)

# Generate Thumbnails HTML for Presentation Mode
thumbs_html_list = []
for s in slides:
    p = s["page"]
    img = html.escape(s.get("image", f"assets/slides/slide_{p:02d}.png"))
    thumbs_html_list.append(f'''
    <div class="thumb-card" data-thumb-page="{p}">
      <img src="{img}" alt="Slide {p}" loading="lazy" />
      <span class="thumb-num">{p:02d}</span>
    </div>
    ''')

# Slides data JSON string for client-side JS
slides_json_str = json.dumps(slides, ensure_ascii=False)

index_html_content = f'''<!DOCTYPE html>
<html lang="zh-Hant" data-theme="dark" data-font="medium">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>AI Agent 時代來臨 · Codex 打造超級小幫手 | 橘子老師實戰研習簡報</title>
  <meta name="description" content="AI Agent 時代來臨，Codex 打造超級小幫手！橘子老師 2026 最新實戰研習簡報，涵蓋 Context Engineering、Skill 五層架構、試算表自動發信、財產報廢申請單與雲端自動排程出題。" />
  
  <!-- Favicon -->
  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🍊</text></svg>">
  
  <!-- Stylesheet -->
  <link rel="stylesheet" href="deck.css" />
</head>
<body>

  <!-- 門禁驗證防護 (Password Gate - 密碼 nato) -->
  <div id="passwordGate">
    <div class="gate-card">
      <div class="gate-icon">🔒</div>
      <h2 class="gate-title">專屬研習簡報門禁</h2>
      <p class="gate-subtitle">AI Agent 時代來臨 · Codex 打造超級小幫手<br>請輸入通關密碼解鎖內容</p>
      <form id="gateForm" class="gate-form">
        <input type="password" id="gatePassword" class="gate-input" placeholder="請輸入通行碼" autofocus autocomplete="current-password" />
        <button type="submit" class="gate-btn">立即驗證進入 ➔</button>
      </form>
      <div id="gateError" class="gate-error"></div>
      <p class="gate-hint">💡 提示：本研習站點通行碼為 <strong>nato</strong></p>
    </div>
  </div>

  <!-- 頂部吸頂控制列 (Sticky App Header) -->
  <header class="app-header">
    <div class="brand-group">
      <span class="brand-badge">AGENT 2026</span>
      <h1 class="brand-title">AI Agent 時代來臨 · Codex 打造超級小幫手</h1>
      <span class="brand-sub">| 橘子老師實戰研習 (共 50 頁)</span>
    </div>

    <div class="toolbar-group">
      <!-- 模式切換 -->
      <div class="pill-group" title="模式切換">
        <button class="pill-btn active" data-set-mode="present">📺 簡報投影</button>
        <button class="pill-btn" data-set-mode="read">📖 卡片閱讀</button>
      </div>

      <!-- 字級縮放 (中、大、特大) -->
      <div class="pill-group" title="字型大小切換">
        <button class="pill-btn active" data-set-font="medium">中</button>
        <button class="pill-btn" data-set-font="large">大</button>
        <button class="pill-btn" data-set-font="xlarge">特大</button>
      </div>

      <!-- 四色布景主題 (淺、深、綠、藍) -->
      <div class="pill-group" title="四色布景切換">
        <button class="pill-btn" data-set-theme="light">淺</button>
        <button class="pill-btn active" data-set-theme="dark">深</button>
        <button class="pill-btn" data-set-theme="green">綠</button>
        <button class="pill-btn" data-set-theme="blue">藍</button>
      </div>

      <!-- 重新上鎖 -->
      <button id="relockBtn" class="action-btn" title="鎖定網站">🔒 上鎖</button>
    </div>
  </header>

  <!-- 單元分頁標籤導航列 (Category Tabs) -->
  <nav class="tabs-nav-bar">
    <button class="tab-item active" data-unit="all">
      📌 全部投影片 <span class="tab-count">{len(slides)}</span>
    </button>
    <button class="tab-item" data-unit="1">
      🚀 1. 講師與社群前言 <span class="tab-count">{unit_counts[1]}</span>
    </button>
    <button class="tab-item" data-unit="2">
      🛠️ 2. Codex基礎與指令工具 <span class="tab-count">{unit_counts[2]}</span>
    </button>
    <button class="tab-item" data-unit="3">
      📐 3. Context工程與Skill架構 <span class="tab-count">{unit_counts[3]}</span>
    </button>
    <button class="tab-item" data-unit="4">
      📊 4. 實戰一 · 試算表與郵件通知 <span class="tab-count">{unit_counts[4]}</span>
    </button>
    <button class="tab-item" data-unit="5">
      ⚡ 5. 實戰二與三 · 報廢單與排程出題 <span class="tab-count">{unit_counts[5]}</span>
    </button>
  </nav>

  <!-- 主內容區 (Main Container) -->
  <main class="app-main">
    
    <!-- 模式 1：16:9 簡報投影模式 -->
    <section id="presentationMode">
      <div id="stageWrapper" class="stage-wrapper">
        <img id="slideScreen" class="slide-screen" src="assets/slides/slide_01.png" alt="Slide 1" />
        <canvas id="whiteboardCanvas" class="inactive"></canvas>
        <div class="stage-info-overlay">
          <span id="stageBadge" class="stage-badge">首頁封面</span>
          <span id="stageSlideTitle" class="stage-slide-title">AI Agent 時代來臨 · Codex 打造超級小幫手</span>
        </div>
      </div>

      <!-- 簡報底部控制列 -->
      <div class="deck-controls">
        <div class="nav-arrow-group">
          <button id="prevSlideBtn" class="deck-btn" title="上一頁 (← / PageUp)">◀ 上一頁</button>
          <span id="slideIndicator" class="slide-indicator">1 / {len(slides)}</span>
          <button id="nextSlideBtn" class="deck-btn" title="下一頁 (→ / PageDown / Space)">下一頁 ▶</button>
        </div>

        <!-- 白板畫筆工具列 -->
        <div class="whiteboard-bar">
          <button id="togglePenBtn" class="tool-icon-btn" title="啟用白板畫筆">✏️ 畫筆</button>
          <input type="color" id="penColorPicker" class="color-picker-input" value="#38bdf8" title="畫筆顏色" />
          <button id="toggleEraserBtn" class="tool-icon-btn" title="橡皮擦">🧹 擦拭</button>
          <button id="clearPenBtn" class="tool-icon-btn" title="清除所有塗鴉">🗑️ 清空</button>
        </div>

        <!-- 播放與全螢幕 -->
        <div class="nav-arrow-group">
          <button id="autoPlayBtn" class="deck-btn"><span>▶ 自動播放</span></button>
          <button id="fullscreenBtn" class="deck-btn"><span>⛶ 全螢幕</span></button>
        </div>
      </div>

      <!-- 縮圖導覽列 -->
      <div id="thumbnailsStrip" class="thumbnails-strip">
        {"".join(thumbs_html_list)}
      </div>
    </section>

    <!-- 模式 2：卡片式圖文閱讀模式 -->
    <section id="readingMode" style="display: none;">
      <div class="cards-grid">
        {"".join(cards_html_list)}
      </div>
    </section>

  </main>

  <!-- 燈箱大圖預覽 (Lightbox Modal) -->
  <div id="lightboxModal">
    <div class="lightbox-content">
      <button id="lightboxCloseBtn" class="lightbox-close-btn" title="關閉 (Esc)">✕</button>
      <img id="lightboxImg" class="lightbox-img" src="" alt="Zoom Slide" />
      <p id="lightboxCaption" class="lightbox-caption"></p>
    </div>
  </div>

  <!-- 頁腳 (Footer) -->
  <footer class="app-footer">
    <div class="footer-links">
      <a href="https://www.facebook.com/ju.laoshi" target="_blank" rel="noopener noreferrer">🍊 橘子老師 FB 專頁</a>
      <a href="https://www.facebook.com/profile.php?id=61580433065847" target="_blank" rel="noopener noreferrer">📚 橘子老師教室粉專</a>
      <a href="https://line.me/ti/g2/WcNwA_0Zf-ciDHCVodeEpFFBLd0PmGwKlhRprg?utm_source=invitation&utm_medium=link_copy&utm_campaign=default" target="_blank" rel="noopener noreferrer">💬 每天開心玩Ai 社群 (密碼: happyai)</a>
      <a href="https://openai.com/zh-Hant/codex/" target="_blank" rel="noopener noreferrer">🤖 OpenAI Codex 官方</a>
    </div>
    <p>AI Agent 時代來臨 · Codex 打造超級小幫手 研習簡報成果展示系統 · 支援響應式 RWD、白板畫筆、無障礙縮放與 GitHub Pages</p>
  </footer>

  <!-- 注入投影片資料 -->
  <script>
    window.SLIDES_DATA = {slides_json_str};
  </script>
  <!-- 主互動腳本 -->
  <script src="deck.js"></script>
</body>
</html>
'''

output_html_file = os.path.join(project_dir, "index.html")
with open(output_html_file, "w", encoding="utf-8") as f:
    f.write(index_html_content)

print(f"Successfully generated {output_html_file} ({len(index_html_content)} bytes)")
