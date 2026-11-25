/**
 * Codex 超級小幫手 · AI Agent 時代來臨
 * 前端互動核心邏輯 (app.js)
 */

(function () {
  "use strict";

  // 1. Password Configuration
  const ACCESS_PASSWORD = "nato";
  const AUTH_STORAGE_KEY = "codex_agent_nato_unlocked";
  const THEME_STORAGE_KEY = "codex_site_theme";
  const FONT_STORAGE_KEY = "codex_site_fontsize";

  // Elements
  const gateOverlay = document.getElementById("passwordGateOverlay");
  const gateCard = document.getElementById("passwordCard");
  const gateInput = document.getElementById("passwordInput");
  const gateBtn = document.getElementById("passwordSubmitBtn");
  const gateError = document.getElementById("passwordErrorMsg");
  const btnLock = document.getElementById("btnLockSite");

  // State
  let currentTheme = localStorage.getItem(THEME_STORAGE_KEY) || "dark";
  let currentFontSize = localStorage.getItem(FONT_STORAGE_KEY) || "font-md";
  let currentTab = "tab-all";
  let currentUnitFilter = "all";
  let searchQuery = "";
  let currentModalSlideIndex = 0;

  // Initialize
  function init() {
    setupAuth();
    setupThemeAndFont();
    setupTabs();
    setupFilterAndSearch();
    renderAllViews();
    setupModalEvents();
    setupKeyboardShortcuts();
  }

  // ==========================================
  // 密碼閘門系統 (Password Gate)
  // ==========================================
  function setupAuth() {
    const isUnlocked = sessionStorage.getItem(AUTH_STORAGE_KEY) === "true" || localStorage.getItem(AUTH_STORAGE_KEY) === "true";
    if (isUnlocked) {
      gateOverlay.classList.add("hidden");
    } else {
      gateOverlay.classList.remove("hidden");
      setTimeout(() => gateInput.focus(), 200);
    }

    gateBtn.addEventListener("click", verifyPassword);
    gateInput.addEventListener("keydown", (e) => {
      if (e.key === "Enter") verifyPassword();
    });

    if (btnLock) {
      btnLock.addEventListener("click", () => {
        sessionStorage.removeItem(AUTH_STORAGE_KEY);
        localStorage.removeItem(AUTH_STORAGE_KEY);
        gateInput.value = "";
        gateError.textContent = "";
        gateOverlay.classList.remove("hidden");
        gateInput.focus();
      });
    }
  }

  function verifyPassword() {
    const entered = gateInput.value.trim();
    if (entered.toLowerCase() === ACCESS_PASSWORD.toLowerCase()) {
      sessionStorage.setItem(AUTH_STORAGE_KEY, "true");
      localStorage.setItem(AUTH_STORAGE_KEY, "true");
      gateError.textContent = "";
      gateOverlay.classList.add("hidden");
    } else {
      gateError.textContent = "密碼錯誤，請輸入正確通關密碼 (nato)";
      gateCard.classList.remove("shake");
      void gateCard.offsetWidth; // trigger reflow
      gateCard.classList.add("shake");
      gateInput.select();
    }
  }

  // ==========================================
  // 主題與字型切換控制 (Theme & Font Size)
  // ==========================================
  function setupThemeAndFont() {
    applyTheme(currentTheme);
    applyFontSize(currentFontSize);

    // Theme buttons
    const themeButtons = document.querySelectorAll("[data-theme-btn]");
    themeButtons.forEach((btn) => {
      btn.addEventListener("click", () => {
        const theme = btn.getAttribute("data-theme-btn");
        applyTheme(theme);
      });
    });

    // Font size buttons
    const fontButtons = document.querySelectorAll("[data-font-btn]");
    fontButtons.forEach((btn) => {
      btn.addEventListener("click", () => {
        const sizeClass = btn.getAttribute("data-font-btn");
        applyFontSize(sizeClass);
      });
    });
  }

  function applyTheme(theme) {
    currentTheme = theme;
    document.body.setAttribute("data-theme", theme);
    localStorage.setItem(THEME_STORAGE_KEY, theme);

    document.querySelectorAll("[data-theme-btn]").forEach((btn) => {
      if (btn.getAttribute("data-theme-btn") === theme) {
        btn.classList.add("active");
      } else {
        btn.classList.remove("active");
      }
    });
  }

  function applyFontSize(sizeClass) {
    currentFontSize = sizeClass;
    document.body.classList.remove("font-md", "font-lg", "font-xl");
    document.body.classList.add(sizeClass);
    localStorage.setItem(FONT_STORAGE_KEY, sizeClass);

    document.querySelectorAll("[data-font-btn]").forEach((btn) => {
      if (btn.getAttribute("data-font-btn") === sizeClass) {
        btn.classList.add("active");
      } else {
        btn.classList.remove("active");
      }
    });
  }

  // ==========================================
  // 分頁標籤切換 (Tabs)
  // ==========================================
  function setupTabs() {
    const tabButtons = document.querySelectorAll(".nav-tab-btn");
    const tabPanels = document.querySelectorAll(".tab-panel");

    tabButtons.forEach((btn) => {
      btn.addEventListener("click", () => {
        const targetId = btn.getAttribute("data-tab-target");
        currentTab = targetId;

        tabButtons.forEach((b) => b.classList.remove("active"));
        tabPanels.forEach((p) => p.classList.remove("active"));

        btn.classList.add("active");
        const panel = document.getElementById(targetId);
        if (panel) panel.classList.add("active");
      });
    });
  }

  // ==========================================
  // 篩選與搜尋 (Filter & Search)
  // ==========================================
  function setupFilterAndSearch() {
    const filterChips = document.querySelectorAll("[data-unit-filter]");
    const searchInput = document.getElementById("slideSearchInput");

    filterChips.forEach((chip) => {
      chip.addEventListener("click", () => {
        filterChips.forEach((c) => c.classList.remove("active"));
        chip.classList.add("active");
        currentUnitFilter = chip.getAttribute("data-unit-filter");
        renderSlidesGrid();
      });
    });

    if (searchInput) {
      searchInput.addEventListener("input", (e) => {
        searchQuery = e.target.value.trim().toLowerCase();
        renderSlidesGrid();
      });
    }
  }

  // ==========================================
  // 資料渲染 (Render Views)
  // ==========================================
  function renderAllViews() {
    renderSlidesGrid();
    renderUnitsGuide();
    renderPromptStudio();
    renderArchitecture();
    renderResources();
  }

  function getFilteredSlides() {
    const slides = window.SLIDES_DATA || [];
    return slides.filter((slide) => {
      // Unit filter
      if (currentUnitFilter !== "all" && String(slide.unit) !== String(currentUnitFilter)) {
        return false;
      }
      // Search filter
      if (searchQuery) {
        const matchTitle = slide.title.toLowerCase().includes(searchQuery);
        const matchSubtitle = slide.subtitle && slide.subtitle.toLowerCase().includes(searchQuery);
        const matchSummary = slide.summary && slide.summary.toLowerCase().includes(searchQuery);
        const matchText = slide.texts && slide.texts.some((t) => t.toLowerCase().includes(searchQuery));
        const matchPrompt = slide.prompts && slide.prompts.some((p) => p.toLowerCase().includes(searchQuery));
        if (!matchTitle && !matchSubtitle && !matchSummary && !matchText && !matchPrompt) {
          return false;
        }
      }
      return true;
    });
  }

  // 1. 全部投影片網格
  function renderSlidesGrid() {
    const container = document.getElementById("slidesGridContainer");
    if (!container) return;

    const filtered = getFilteredSlides();
    if (filtered.length === 0) {
      container.innerHTML = `
        <div style="grid-column: 1 / -1; text-align: center; padding: 4rem 1rem; color: var(--text-muted);">
          <div style="font-size: 3rem; margin-bottom: 1rem;">🔍</div>
          <h3>找不到相符的投影片</h3>
          <p>請嘗試其他關鍵字或清除篩選條件</p>
        </div>
      `;
      return;
    }

    container.innerHTML = filtered
      .map((slide) => {
        const imgWebp = `assets/slides_webp/slide_${String(slide.page).padStart(2, "0")}.webp`;
        const imgPng = `assets/slides/slide_${String(slide.page).padStart(2, "0")}.png`;

        const hasPrompt = slide.prompts && slide.prompts.length > 0;
        const hasLinks = slide.links && slide.links.length > 0;

        return `
          <div class="slide-card" onclick="window.openSlideModal(${slide.page - 1})">
            <div class="slide-thumb-wrap">
              <img src="${imgWebp}" onerror="this.onerror=null;this.src='${imgPng}'" alt="Slide ${slide.page}" class="slide-img" loading="lazy">
              <div class="slide-page-badge">第 ${slide.page} 頁</div>
              <div class="slide-unit-badge">${slide.badge || `單元 ${slide.unit}`}</div>
            </div>
            <div class="slide-content-wrap">
              <h4 class="slide-card-title">${slide.title}</h4>
              <div class="slide-card-subtitle">${slide.subtitle || ""}</div>
              <p class="slide-card-desc">${slide.summary || ""}</p>
              <div class="slide-card-footer">
                <span>單元 ${slide.unit} · ${slide.unit_name}</span>
                <span>
                  ${hasPrompt ? "💡 含提示詞 " : ""}
                  ${hasLinks ? "🔗 含連結 " : ""}
                  ➔
                </span>
              </div>
            </div>
          </div>
        `;
      })
      .join("");
  }

  // 2. 單元結構導讀
  function renderUnitsGuide() {
    const container = document.getElementById("unitsGuideContainer");
    if (!container) return;

    const slides = window.SLIDES_DATA || [];
    const unitsMap = {};

    slides.forEach((s) => {
      if (!unitsMap[s.unit]) {
        unitsMap[s.unit] = {
          unit: s.unit,
          name: s.unit_name,
          slides: [],
        };
      }
      unitsMap[s.unit].slides.push(s);
    });

    const unitKeys = Object.keys(unitsMap).sort((a, b) => Number(a) - Number(b));

    container.innerHTML = unitKeys
      .map((key) => {
        const u = unitsMap[key];
        const startPage = u.slides[0].page;
        const endPage = u.slides[u.slides.length - 1].page;

        return `
          <div class="unit-section-block">
            <div class="unit-header-bar">
              <div class="unit-header-left">
                <div class="unit-num-pill">${u.unit}</div>
                <div>
                  <h3>${u.name}</h3>
                  <p>涵蓋第 ${startPage} ~ ${endPage} 頁 · 共 ${u.slides.length} 張投影片</p>
                </div>
              </div>
              <div>
                <button class="filter-chip" onclick="window.filterByUnit(${u.unit})">在總覽中查看本單元</button>
              </div>
            </div>
            <div class="unit-body-grid">
              ${u.slides
                .map((s) => {
                  return `
                    <div class="slide-card" style="cursor: pointer;" onclick="window.openSlideModal(${s.page - 1})">
                      <div class="slide-content-wrap" style="padding: 1rem;">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
                          <span style="font-weight: 800; color: var(--accent-color); font-size: 0.85rem;">P.${s.page}</span>
                          <span class="tab-badge">${s.badge || "重點"}</span>
                        </div>
                        <h5 style="font-size: 0.95rem; font-weight: 700; margin-bottom: 0.3rem;">${s.title}</h5>
                        <p style="font-size: 0.8rem; color: var(--text-muted); line-height: 1.4;">${s.summary.substring(0, 75)}...</p>
                      </div>
                    </div>
                  `;
                })
                .join("")}
            </div>
          </div>
        `;
      })
      .join("");
  }

  // 3. 核心提示詞指令庫
  function renderPromptStudio() {
    const container = document.getElementById("promptStudioContainer");
    if (!container) return;

    const slides = window.SLIDES_DATA || [];
    const allPrompts = [];

    slides.forEach((s) => {
      if (s.prompts && s.prompts.length > 0) {
        s.prompts.forEach((p, idx) => {
          allPrompts.push({
            slidePage: s.page,
            slideTitle: s.title,
            unit: s.unit,
            unitName: s.unit_name,
            badge: s.badge,
            summary: s.summary,
            prompt: p,
          });
        });
      }
    });

    container.innerHTML = allPrompts
      .map((item, idx) => {
        const codeId = `prompt_code_${idx}`;
        return `
          <div class="prompt-card">
            <div class="prompt-card-header">
              <h3>
                <span>💡</span>
                <span>P.${item.slidePage} · ${item.slideTitle}</span>
              </h3>
              <div style="display: flex; gap: 0.5rem; align-items: center;">
                <span class="prompt-badge">${item.badge || `單元 ${item.unit}`}</span>
                <span class="tab-badge">${item.unitName}</span>
              </div>
            </div>
            <p class="prompt-desc">${item.summary}</p>
            <div class="prompt-code-wrap">
              <button class="btn-copy-prompt" onclick="window.copyText('${codeId}')">
                <span>📋</span>
                <span>複製指令</span>
              </button>
              <pre id="${codeId}">${escapeHtml(item.prompt)}</pre>
            </div>
          </div>
        `;
      })
      .join("");
  }

  // 4. Codex 五層金字塔架構
  function renderArchitecture() {
    const container = document.getElementById("architectureContainer");
    if (!container) return;

    container.innerHTML = `
      <div class="pyramid-card-stack">
        <div style="text-align: center; margin-bottom: 1.5rem;">
          <h3 style="font-size: 1.6rem; font-weight: 800; margin-bottom: 0.5rem;">Codex 專案五大層級金字塔</h3>
          <p style="color: var(--text-muted); font-size: 1rem;">
            橘子老師歸納之標準 Agent 工程規範：讓人讀懂專案，更讓 Agent 具備獨立開發與永續維護能力。
          </p>
        </div>

        <div class="pyramid-level">
          <div class="pyramid-level-num">L1</div>
          <div class="pyramid-icon">🧠</div>
          <div class="pyramid-info">
            <h4>Agent 規則 · AGENTS.md</h4>
            <p>告訴 Codex「怎麼工作」——包含開發原則、增量更新策略、驗證規範與人機審核機制。</p>
          </div>
          <div class="pyramid-tag">AGENTS.md</div>
        </div>

        <div class="pyramid-level">
          <div class="pyramid-level-num">L2</div>
          <div class="pyramid-icon">🧩</div>
          <div class="pyramid-info">
            <h4>Agent 能力 · .agents/skills/</h4>
            <p>告訴 Codex「有哪些專業技能」——每個技能以 SKILL.md 定義標準流程與觸發條件。</p>
          </div>
          <div class="pyramid-tag">.agents/skills/</div>
        </div>

        <div class="pyramid-level">
          <div class="pyramid-level-num">L3</div>
          <div class="pyramid-icon">📚</div>
          <div class="pyramid-info">
            <h4>Agent 知識 · references/</h4>
            <p>告訴 Codex「需要知道什麼」——放置 API 文件、資料庫 Schema、題型規格與業務知識。</p>
          </div>
          <div class="pyramid-tag">references/</div>
        </div>

        <div class="pyramid-level">
          <div class="pyramid-level-num">L4</div>
          <div class="pyramid-icon">⚙️</div>
          <div class="pyramid-info">
            <h4>Agent 工具 · scripts/</h4>
            <p>告訴 Codex「可以執行什麼」——可重複執行的 Python、Bash、Node.js 專案自動化腳本。</p>
          </div>
          <div class="pyramid-tag">scripts/</div>
        </div>

        <div class="pyramid-level">
          <div class="pyramid-level-num">L5</div>
          <div class="pyramid-icon">💻</div>
          <div class="pyramid-info">
            <h4>實際產品 · src/</h4>
            <p>真正的應用程式代碼——包含網站前端、後端服務、資料庫與產出之各項教學與行政成果。</p>
          </div>
          <div class="pyramid-tag">src/</div>
        </div>
      </div>
    `;
  }

  // 5. 實戰教材與雲端資源包
  function renderResources() {
    const container = document.getElementById("resourcesContainer");
    if (!container) return;

    const resources = [
      {
        icon: "📝",
        title: "財產報廢申請單 (Google Docs)",
        desc: "橘子老師提供之財產報廢標準套表格式，支援自動套入設備序號與報廢理由。",
        link: "https://docs.google.com/document/d/1ycXsCTt2Q-PgNkp6wz-OUnCMr-0ByBpL/edit?usp=drive_link&ouid=114425903125895498189&rtpof=true&sd=true",
        label: "開啟 Google 文件",
      },
      {
        icon: "🖼️",
        title: "範例照片 (Google Drive)",
        desc: "供多模態 AI 辨識之報廢財產實體照片，用於訓練 Agent 讀取設備銘牌與損壞狀態。",
        link: "https://drive.google.com/file/d/1Ur8aPxQ8N5ccepBKg439qcljlbMBDYyn/view?usp=drive_link",
        label: "檢視雲端照片",
      },
      {
        icon: "📊",
        title: "範例財產清冊檔案 (Google Sheets)",
        desc: "標準財產編號、購置年份、品名與保管人資料庫，供 Agent 進行欄位核對與除帳。",
        link: "https://docs.google.com/spreadsheets/d/1hllWwzfOnPZ3Vbfnm5qgS90Vd1uTIc2g/edit?usp=drive_link&ouid=114425903125895498189&rtpof=true&sd=true",
        label: "開啟試算表清冊",
      },
      {
        icon: "💡",
        title: "實戰提示詞文件 (Google Drive)",
        desc: "財產報廢申請自動化全流程提示詞，包含照片解析、清冊核對與文件生成完整指引。",
        link: "https://drive.google.com/file/d/1G253bCwUvQN80D7Y_bRCZiGyOTZSr8XW/view?usp=drive_link",
        label: "下載提示詞文件",
      },
      {
        icon: "🌐",
        title: "OpenAI Codex 繁體中文官網",
        desc: "OpenAI Codex 官方入口，提供環境下載、開發者說明文件與 API 規格參考。",
        link: "https://openai.com/zh-Hant/codex/",
        label: "前往 OpenAI Codex",
      },
      {
        icon: "💬",
        title: "「每天開心玩Ai」LINE 共學社群",
        desc: "教育科技教師共學圈，隨時交流 AI 提問、Prompt 與最新小幫手技巧（入群密碼：happyai）。",
        link: "https://line.me/ti/g2/WcNwA_0Zf-ciDHCVodeEpFFBLd0PmGwKlhRprg?utm_source=invitation&utm_medium=link_copy&utm_campaign=default",
        label: "加入 LINE 社群",
      },
      {
        icon: "📘",
        title: "橘子老師 Facebook 個人專頁",
        desc: "橘子老師個人 FB，歡迎教育夥伴一同交流 AI 跨域教學與工作流創新。",
        link: "https://www.facebook.com/ju.laoshi",
        label: "追蹤個人 FB",
      },
      {
        icon: "🏫",
        title: "橘子老師教室 粉絲專頁",
        desc: "定期分享最新 AI 工具教學、提示詞包與教育科技實例的官方粉絲專頁。",
        link: "https://www.facebook.com/profile.php?id=61580433065847",
        label: "造訪粉專",
      },
    ];

    container.innerHTML = `
      <div class="resources-grid">
        ${resources
          .map(
            (r) => `
          <div class="resource-card">
            <div class="resource-icon">${r.icon}</div>
            <h3>${r.title}</h3>
            <p>${r.desc}</p>
            <a href="${r.link}" target="_blank" rel="noopener noreferrer" class="resource-link-btn">
              <span>${r.label}</span>
              <span>➔</span>
            </a>
          </div>
        `
          )
          .join("")}
      </div>
    `;
  }

  // ==========================================
  // 投影片播放器燈箱 (Slide Modal)
  // ==========================================
  function setupModalEvents() {
    const modal = document.getElementById("slideModal");
    const closeBtn = document.getElementById("btnCloseModal");
    const prevBtn = document.getElementById("btnModalPrev");
    const nextBtn = document.getElementById("btnModalNext");

    if (closeBtn) closeBtn.addEventListener("click", closeModal);
    if (prevBtn) prevBtn.addEventListener("click", () => navigateModal(-1));
    if (nextBtn) nextBtn.addEventListener("click", () => navigateModal(1));

    if (modal) {
      modal.addEventListener("click", (e) => {
        if (e.target === modal) closeModal();
      });
    }
  }

  window.openSlideModal = function (slideIndex) {
    const slides = window.SLIDES_DATA || [];
    if (slideIndex < 0 || slideIndex >= slides.length) return;

    currentModalSlideIndex = slideIndex;
    updateModalContent();

    const modal = document.getElementById("slideModal");
    if (modal) modal.classList.add("active");
    document.body.style.overflow = "hidden";
  };

  function closeModal() {
    const modal = document.getElementById("slideModal");
    if (modal) modal.classList.remove("active");
    document.body.style.overflow = "";
  }

  function navigateModal(delta) {
    const slides = window.SLIDES_DATA || [];
    let newIndex = currentModalSlideIndex + delta;
    if (newIndex < 0) newIndex = slides.length - 1;
    if (newIndex >= slides.length) newIndex = 0;
    currentModalSlideIndex = newIndex;
    updateModalContent();
  }

  function updateModalContent() {
    const slides = window.SLIDES_DATA || [];
    const slide = slides[currentModalSlideIndex];
    if (!slide) return;

    const pageNumEl = document.getElementById("modalPageNum");
    const titleEl = document.getElementById("modalTitle");
    const imgEl = document.getElementById("modalSlideImg");
    const summaryEl = document.getElementById("modalSummary");
    const promptsEl = document.getElementById("modalPromptsList");
    const linksEl = document.getElementById("modalLinksList");

    if (pageNumEl) pageNumEl.textContent = `第 ${slide.page} / ${slides.length} 頁 · 單元 ${slide.unit}`;
    if (titleEl) titleEl.textContent = slide.title;

    const imgWebp = `assets/slides_webp/slide_${String(slide.page).padStart(2, "0")}.webp`;
    const imgPng = `assets/slides/slide_${String(slide.page).padStart(2, "0")}.png`;
    if (imgEl) {
      imgEl.src = imgWebp;
      imgEl.onerror = () => {
        imgEl.onerror = null;
        imgEl.src = imgPng;
      };
    }

    if (summaryEl) {
      summaryEl.innerHTML = `
        <div style="font-weight: 700; margin-bottom: 0.35rem; color: var(--accent-color);">核心重點摘要：</div>
        <div>${slide.summary}</div>
      `;
    }

    if (promptsEl) {
      if (slide.prompts && slide.prompts.length > 0) {
        promptsEl.innerHTML = `
          <h4 style="font-size: 0.95rem; font-weight: 700; margin-bottom: 0.5rem;">💡 實用提示詞指令：</h4>
          ${slide.prompts
            .map(
              (p, idx) => `
            <div class="prompt-code-wrap" style="margin-bottom: 0.75rem;">
              <button class="btn-copy-prompt" onclick="window.copyText('modal_prompt_${idx}')">
                <span>📋</span>
                <span>複製指令</span>
              </button>
              <pre id="modal_prompt_${idx}">${escapeHtml(p)}</pre>
            </div>
          `
            )
            .join("")}
        `;
      } else {
        promptsEl.innerHTML = "";
      }
    }

    if (linksEl) {
      if (slide.links && slide.links.length > 0) {
        linksEl.innerHTML = `
          <h4 style="font-size: 0.95rem; font-weight: 700; width: 100%; margin-bottom: 0.25rem;">🔗 相關資源連結：</h4>
          ${slide.links
            .map(
              (l) => `
            <a href="${l.href}" target="_blank" rel="noopener noreferrer" class="resource-link-btn" style="padding: 0.4rem 0.9rem; font-size: 0.825rem;">
              <span>${l.text}</span>
              <span>➔</span>
            </a>
          `
            )
            .join("")}
        `;
      } else {
        linksEl.innerHTML = "";
      }
    }
  }

  // ==========================================
  // 全域輔助函數 (Helpers)
  // ==========================================
  window.filterByUnit = function (unitNumber) {
    const tabBtn = document.querySelector('[data-tab-target="tab-all"]');
    if (tabBtn) tabBtn.click();

    const chip = document.querySelector(`[data-unit-filter="${unitNumber}"]`);
    if (chip) chip.click();
    window.scrollTo({ top: 400, behavior: "smooth" });
  };

  window.copyText = function (elementId) {
    const el = document.getElementById(elementId);
    if (!el) return;
    const text = el.innerText || el.textContent;

    navigator.clipboard
      .writeText(text)
      .then(() => {
        showToast("已成功複製指令至剪貼簿！");
      })
      .catch((err) => {
        console.error("Copy failed", err);
        showToast("複製失敗，請手動複製");
      });
  };

  function showToast(msg) {
    let toast = document.getElementById("siteToast");
    if (!toast) {
      toast = document.createElement("div");
      toast.id = "siteToast";
      toast.style.position = "fixed";
      toast.style.bottom = "2rem";
      toast.style.left = "50%";
      toast.style.transform = "translateX(-50%) translateY(100px)";
      toast.style.background = "var(--accent-color)";
      toast.style.color = "#ffffff";
      toast.style.padding = "0.75rem 1.5rem";
      toast.style.borderRadius = "var(--radius-full)";
      toast.style.boxShadow = "var(--shadow-lg)";
      toast.style.zIndex = "999999";
      toast.style.fontWeight = "600";
      toast.style.fontSize = "0.95rem";
      toast.style.transition = "transform 0.3s cubic-bezier(0.16, 1, 0.3, 1)";
      document.body.appendChild(toast);
    }
    toast.textContent = msg;
    toast.style.transform = "translateX(-50%) translateY(0)";

    setTimeout(() => {
      toast.style.transform = "translateX(-50%) translateY(100px)";
    }, 2500);
  }

  function setupKeyboardShortcuts() {
    document.addEventListener("keydown", (e) => {
      const modal = document.getElementById("slideModal");
      const isModalOpen = modal && modal.classList.contains("active");

      if (e.key === "Escape" && isModalOpen) {
        closeModal();
      } else if (e.key === "ArrowLeft" && isModalOpen) {
        navigateModal(-1);
      } else if (e.key === "ArrowRight" && isModalOpen) {
        navigateModal(1);
      }
    });
  }

  function escapeHtml(str) {
    return str
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
  }

  // Run on DOM Ready
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
