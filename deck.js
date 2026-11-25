/* ============================================================
   AI Agent 時代來臨 · Codex 打造超級小幫手 · 橘子老師
   互動展示與演講引擎核心腳本 (deck.js)
   ============================================================ */

(function () {
  'use strict';

  // Constants & Config
  var AUTH_STORAGE_KEY = 'codex_deck_auth';
  var THEME_STORAGE_KEY = 'codex_deck_theme';
  var FONT_STORAGE_KEY = 'codex_deck_font';
  var MODE_STORAGE_KEY = 'codex_deck_mode';
  
  // SHA-256 for 'nato'
  var NATO_HASH = '5cae49b1fea5b5b969cdc931b8338968940c92309aa2339360cdd5c77be4a4ff';
  
  var currentSlide = 1;
  var totalSlides = 50;
  var currentUnitFilter = 'all';
  var isAutoPlaying = false;
  var autoPlayTimer = null;
  
  // Whiteboard State
  var isWhiteboardActive = false;
  var isDrawing = false;
  var currentPenColor = '#38bdf8';
  var currentPenSize = 4;
  var isEraser = false;

  // DOM Elements
  var passwordGate = document.getElementById('passwordGate');
  var gateForm = document.getElementById('gateForm');
  var gatePasswordInput = document.getElementById('gatePassword');
  var gateError = document.getElementById('gateError');
  var relockBtn = document.getElementById('relockBtn');

  var themeBtns = document.querySelectorAll('[data-set-theme]');
  var fontBtns = document.querySelectorAll('[data-set-font]');
  var modeBtns = document.querySelectorAll('[data-set-mode]');
  var tabBtns = document.querySelectorAll('.tab-item');

  var presentationMode = document.getElementById('presentationMode');
  var readingMode = document.getElementById('readingMode');

  var slideScreen = document.getElementById('slideScreen');
  var slideIndicator = document.getElementById('slideIndicator');
  var stageBadge = document.getElementById('stageBadge');
  var stageSlideTitle = document.getElementById('stageSlideTitle');
  var prevSlideBtn = document.getElementById('prevSlideBtn');
  var nextSlideBtn = document.getElementById('nextSlideBtn');
  var autoPlayBtn = document.getElementById('autoPlayBtn');
  var fullscreenBtn = document.getElementById('fullscreenBtn');
  var stageWrapper = document.getElementById('stageWrapper');
  var thumbnailsStrip = document.getElementById('thumbnailsStrip');

  var whiteboardCanvas = document.getElementById('whiteboardCanvas');
  var togglePenBtn = document.getElementById('togglePenBtn');
  var toggleEraserBtn = document.getElementById('toggleEraserBtn');
  var clearPenBtn = document.getElementById('clearPenBtn');
  var penColorPicker = document.getElementById('penColorPicker');

  var lightboxModal = document.getElementById('lightboxModal');
  var lightboxImg = document.getElementById('lightboxImg');
  var lightboxCaption = document.getElementById('lightboxCaption');
  var lightboxCloseBtn = document.getElementById('lightboxCloseBtn');

  // Slides Data from Global Object
  var slidesData = window.SLIDES_DATA || [];
  totalSlides = slidesData.length || 50;

  // --- 1. Password Gate (NATO) ---
  async function sha256(message) {
    var msgBuffer = new TextEncoder().encode(message);
    var hashBuffer = await crypto.subtle.digest('SHA-256', msgBuffer);
    var hashArray = Array.from(new Uint8Array(hashBuffer));
    return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
  }

  async function checkAuth() {
    var stored = localStorage.getItem(AUTH_STORAGE_KEY);
    if (stored === 'nato' || stored === NATO_HASH) {
      unlockGate();
    } else {
      lockGate();
    }
  }

  function unlockGate() {
    passwordGate.classList.add('hidden');
    document.body.style.overflow = '';
  }

  function lockGate() {
    passwordGate.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
    gatePasswordInput.value = '';
    gateError.textContent = '';
    setTimeout(() => gatePasswordInput.focus(), 100);
  }

  if (gateForm) {
    gateForm.addEventListener('submit', async function (e) {
      e.preventDefault();
      var input = gatePasswordInput.value.trim();
      var hash = await sha256(input);
      if (input === 'nato' || hash === NATO_HASH) {
        localStorage.setItem(AUTH_STORAGE_KEY, 'nato');
        unlockGate();
      } else {
        gateError.textContent = '密碼錯誤，請輸入正確通行碼 (nato)';
        gatePasswordInput.focus();
        gatePasswordInput.select();
      }
    });
  }

  if (relockBtn) {
    relockBtn.addEventListener('click', function () {
      localStorage.removeItem(AUTH_STORAGE_KEY);
      lockGate();
    });
  }

  // --- 2. Themes (Light, Dark, Green, Blue) ---
  function initTheme() {
    var savedTheme = localStorage.getItem(THEME_STORAGE_KEY) || 'dark';
    setTheme(savedTheme);
  }

  function setTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem(THEME_STORAGE_KEY, theme);
    themeBtns.forEach(btn => {
      btn.classList.toggle('active', btn.getAttribute('data-set-theme') === theme);
    });
  }

  themeBtns.forEach(btn => {
    btn.addEventListener('click', function () {
      setTheme(this.getAttribute('data-set-theme'));
    });
  });

  // --- 3. Font Size (Medium, Large, XLarge) ---
  function initFont() {
    var savedFont = localStorage.getItem(FONT_STORAGE_KEY) || 'medium';
    setFont(savedFont);
  }

  function setFont(font) {
    document.documentElement.setAttribute('data-font', font);
    localStorage.setItem(FONT_STORAGE_KEY, font);
    fontBtns.forEach(btn => {
      btn.classList.toggle('active', btn.getAttribute('data-set-font') === font);
    });
  }

  fontBtns.forEach(btn => {
    btn.addEventListener('click', function () {
      setFont(this.getAttribute('data-set-font'));
    });
  });

  // --- 4. Presentation vs Reading Mode ---
  function initMode() {
    var savedMode = localStorage.getItem(MODE_STORAGE_KEY) || 'present';
    setMode(savedMode);
  }

  function setMode(mode) {
    localStorage.setItem(MODE_STORAGE_KEY, mode);
    modeBtns.forEach(btn => {
      btn.classList.toggle('active', btn.getAttribute('data-set-mode') === mode);
    });

    if (mode === 'present') {
      presentationMode.style.display = 'flex';
      readingMode.style.display = 'none';
      resizeCanvas();
    } else {
      presentationMode.style.display = 'none';
      readingMode.style.display = 'block';
    }
  }

  modeBtns.forEach(btn => {
    btn.addEventListener('click', function () {
      setMode(this.getAttribute('data-set-mode'));
    });
  });

  // --- 5. Tabs Filtering ---
  tabBtns.forEach(tab => {
    tab.addEventListener('click', function () {
      tabBtns.forEach(t => t.classList.remove('active'));
      this.classList.add('active');

      currentUnitFilter = this.getAttribute('data-unit');
      filterCards(currentUnitFilter);

      // If in present mode, jump to the first slide of that unit
      if (currentUnitFilter !== 'all') {
        var unitNum = parseInt(currentUnitFilter, 10);
        var targetSlide = slidesData.find(s => s.unit === unitNum);
        if (targetSlide) {
          goToSlide(targetSlide.page);
        }
      }
    });
  });

  function filterCards(unit) {
    var cards = document.querySelectorAll('.slide-card');
    cards.forEach(card => {
      if (unit === 'all' || card.getAttribute('data-card-unit') === unit) {
        card.style.display = 'flex';
      } else {
        card.style.display = 'none';
      }
    });
  }

  // --- 6. 16:9 Presentation Controls ---
  function goToSlide(page) {
    if (page < 1) page = 1;
    if (page > totalSlides) page = totalSlides;
    currentSlide = page;

    var s = slidesData[currentSlide - 1] || {};
    var padded = String(currentSlide).padStart(2, '0');
    slideScreen.src = s.image || `assets/slides/slide_${padded}.png`;

    slideIndicator.textContent = `${currentSlide} / ${totalSlides}`;
    if (stageBadge) stageBadge.textContent = s.badge || `單元 ${s.unit}`;
    if (stageSlideTitle) stageSlideTitle.textContent = s.title || `投影片第 ${currentSlide} 頁`;

    prevSlideBtn.disabled = (currentSlide === 1);
    nextSlideBtn.disabled = (currentSlide === totalSlides);

    // Update thumbnail highlights & scroll
    var thumbs = document.querySelectorAll('.thumb-card');
    thumbs.forEach(t => {
      var p = parseInt(t.getAttribute('data-thumb-page'), 10);
      t.classList.toggle('active', p === currentSlide);
      if (p === currentSlide) {
        t.scrollIntoView({ behavior: 'smooth', inline: 'center', block: 'nearest' });
      }
    });

    // Clear whiteboard per slide if user navigates
    clearWhiteboard();
  }

  prevSlideBtn.addEventListener('click', () => goToSlide(currentSlide - 1));
  nextSlideBtn.addEventListener('click', () => goToSlide(currentSlide + 1));

  // Auto-play Toggle
  if (autoPlayBtn) {
    autoPlayBtn.addEventListener('click', function () {
      isAutoPlaying = !isAutoPlaying;
      if (isAutoPlaying) {
        this.classList.add('primary');
        this.innerHTML = '<span>⏸ 暫停播放</span>';
        autoPlayTimer = setInterval(() => {
          if (currentSlide >= totalSlides) {
            goToSlide(1);
          } else {
            goToSlide(currentSlide + 1);
          }
        }, 4000);
      } else {
        this.classList.remove('primary');
        this.innerHTML = '<span>▶ 自動播放</span>';
        clearInterval(autoPlayTimer);
      }
    });
  }

  // Fullscreen
  if (fullscreenBtn && stageWrapper) {
    fullscreenBtn.addEventListener('click', function () {
      if (!document.fullscreenElement) {
        stageWrapper.requestFullscreen().catch(err => {
          alert(`無法進入全螢幕：${err.message}`);
        });
      } else {
        document.exitFullscreen();
      }
    });
  }

  // Keyboard Navigation
  window.addEventListener('keydown', function (e) {
    if (passwordGate && !passwordGate.classList.contains('hidden')) return;

    if (e.key === 'ArrowRight' || e.key === 'PageDown' || e.key === ' ') {
      if (document.activeElement.tagName !== 'INPUT') {
        e.preventDefault();
        goToSlide(currentSlide + 1);
      }
    } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
      if (document.activeElement.tagName !== 'INPUT') {
        e.preventDefault();
        goToSlide(currentSlide - 1);
      }
    } else if (e.key === 'Escape') {
      closeLightbox();
    }
  });

  // Thumbnail clicks
  document.addEventListener('click', function (e) {
    var thumb = e.target.closest('.thumb-card');
    if (thumb) {
      var p = parseInt(thumb.getAttribute('data-thumb-page'), 10);
      goToSlide(p);
    }
  });

  // --- 7. Whiteboard Canvas ---
  var ctx = whiteboardCanvas ? whiteboardCanvas.getContext('2d') : null;

  function resizeCanvas() {
    if (!whiteboardCanvas || !stageWrapper) return;
    var rect = stageWrapper.getBoundingClientRect();
    whiteboardCanvas.width = rect.width;
    whiteboardCanvas.height = rect.height;
  }
  window.addEventListener('resize', resizeCanvas);

  function clearWhiteboard() {
    if (ctx && whiteboardCanvas) {
      ctx.clearRect(0, 0, whiteboardCanvas.width, whiteboardCanvas.height);
    }
  }

  if (togglePenBtn) {
    togglePenBtn.addEventListener('click', function () {
      isWhiteboardActive = !isWhiteboardActive;
      isEraser = false;
      this.classList.toggle('active', isWhiteboardActive);
      if (toggleEraserBtn) toggleEraserBtn.classList.remove('active');
      whiteboardCanvas.classList.toggle('inactive', !isWhiteboardActive);
    });
  }

  if (toggleEraserBtn) {
    toggleEraserBtn.addEventListener('click', function () {
      isEraser = !isEraser;
      if (isEraser) {
        isWhiteboardActive = true;
        this.classList.add('active');
        if (togglePenBtn) togglePenBtn.classList.remove('active');
        whiteboardCanvas.classList.remove('inactive');
      } else {
        this.classList.remove('active');
      }
    });
  }

  if (clearPenBtn) {
    clearPenBtn.addEventListener('click', clearWhiteboard);
  }

  if (penColorPicker) {
    penColorPicker.addEventListener('input', function (e) {
      currentPenColor = e.target.value;
      isEraser = false;
      if (toggleEraserBtn) toggleEraserBtn.classList.remove('active');
      if (togglePenBtn) togglePenBtn.classList.add('active');
      isWhiteboardActive = true;
      whiteboardCanvas.classList.remove('inactive');
    });
  }

  if (whiteboardCanvas) {
    function getCanvasCoords(e) {
      var rect = whiteboardCanvas.getBoundingClientRect();
      var clientX = e.clientX || (e.touches && e.touches[0].clientX);
      var clientY = e.clientY || (e.touches && e.touches[0].clientY);
      return {
        x: clientX - rect.left,
        y: clientY - rect.top
      };
    }

    function startDraw(e) {
      if (!isWhiteboardActive) return;
      isDrawing = true;
      var pos = getCanvasCoords(e);
      ctx.beginPath();
      ctx.moveTo(pos.x, pos.y);
      ctx.lineCap = 'round';
      ctx.lineJoin = 'round';
      if (isEraser) {
        ctx.globalCompositeOperation = 'destination-out';
        ctx.lineWidth = 24;
      } else {
        ctx.globalCompositeOperation = 'source-over';
        ctx.strokeStyle = currentPenColor;
        ctx.lineWidth = currentPenSize;
      }
    }

    function draw(e) {
      if (!isDrawing || !isWhiteboardActive) return;
      var pos = getCanvasCoords(e);
      ctx.lineTo(pos.x, pos.y);
      ctx.stroke();
    }

    function stopDraw() {
      if (isDrawing) {
        ctx.closePath();
        isDrawing = false;
      }
    }

    whiteboardCanvas.addEventListener('mousedown', startDraw);
    whiteboardCanvas.addEventListener('mousemove', draw);
    window.addEventListener('mouseup', stopDraw);

    whiteboardCanvas.addEventListener('touchstart', function (e) {
      if (isWhiteboardActive) e.preventDefault();
      startDraw(e);
    }, { passive: false });
    whiteboardCanvas.addEventListener('touchmove', function (e) {
      if (isWhiteboardActive) e.preventDefault();
      draw(e);
    }, { passive: false });
    window.addEventListener('touchend', stopDraw);
  }

  // --- 8. Lightbox Zoom ---
  function openLightbox(src, title) {
    lightboxImg.src = src;
    lightboxCaption.textContent = title || '';
    lightboxModal.classList.add('active');
  }

  function closeLightbox() {
    lightboxModal.classList.remove('active');
  }

  if (lightboxCloseBtn) {
    lightboxCloseBtn.addEventListener('click', closeLightbox);
  }
  if (lightboxModal) {
    lightboxModal.addEventListener('click', function (e) {
      if (e.target === lightboxModal) closeLightbox();
    });
  }

  document.addEventListener('click', function (e) {
    var mediaBox = e.target.closest('.card-media-box');
    if (mediaBox) {
      var img = mediaBox.querySelector('img');
      var card = mediaBox.closest('.slide-card');
      var title = card ? card.querySelector('.card-title').textContent : '';
      if (img) openLightbox(img.src, title);
    }
  });

  // --- Initializer ---
  function init() {
    checkAuth();
    initTheme();
    initFont();
    initMode();
    goToSlide(1);
    setTimeout(resizeCanvas, 300);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
