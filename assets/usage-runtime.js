/*
 * usage-runtime.js — 方案 1：静态用法卡兜底，详情页运行时用 usage.fb 覆盖。
 *
 * 只在插件/模块详情页加载（由 _layouts/default.html 注入 __USAGE_PAGE__）。
 * fetch 失败或查不到记录时保持页面上已烤好的卡片。
 * 若 CI 重生成导致页面没有 #usage 卡，则插入一张空卡再填 fb 内容。
 */
(function () {
  'use strict';

  function inline(s) {
    return String(s == null ? '' : s)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
      .replace(/`([^`]+)`/g, function (_, c) {
        return '<code class="usage-code">' + c + '</code>';
      });
  }

  function renderSteps(steps, note) {
    var ol = '<ol class="usage-steps">' +
      (steps || []).map(function (s) { return '<li>' + inline(s) + '</li>'; }).join('') +
      '</ol>';
    var nt = note ? '<p class="usage-note">' + inline(note) + '</p>' : '';
    return ol + nt;
  }

  function detectTarget() {
    var p = window.__USAGE_PAGE__;
    if (p && p.kind && p.slug) {
      return { kind: p.kind, slug: String(p.slug).toLowerCase() };
    }
    var path = (location.pathname || '').replace(/\/+$/, '');
    var m = path.match(/\/(plugins|modules)\/([^\/]+?)(?:\.html?)?$/);
    if (!m) return null;
    return {
      kind: m[1] === 'plugins' ? 'plugin' : 'module',
      slug: decodeURIComponent(m[2]).toLowerCase()
    };
  }

  function ensureCard() {
    var card = document.getElementById('usage');
    if (card) return card;
    var html =
      '<div class="card usage-card" id="usage" data-usage-source="fb">' +
      '<style>' +
      '.usage-steps{margin:0;padding-left:22px}' +
      '.usage-steps li{margin-bottom:12px;line-height:1.7}' +
      '.usage-steps li:last-child{margin-bottom:0}' +
      '.usage-code{font-family:\'JetBrains Mono\',ui-monospace,monospace;font-size:12.5px;' +
      'background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}' +
      '.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}' +
      '.usage-card .desc-body .bilingual-block{margin-bottom:0}' +
      '</style>' +
      '<div class="card-title"><span class="card-title-sep"></span>How to use' +
      '<span class="card-title-cn">使用方法</span></div>' +
      '<div class="desc-body"><div class="bilingual-block">' +
      '<div class="lang-tabs">' +
      '<button class="lang-tab active" onclick="switchLang(this)">中文</button>' +
      '<button class="lang-tab" onclick="switchLang(this)">English</button>' +
      '</div>' +
      '<div class="lang-content active"></div>' +
      '<div class="lang-content"></div>' +
      '</div></div></div>';
    var wrap = document.createElement('div');
    wrap.innerHTML = html;
    card = wrap.firstElementChild;
    var host = document.querySelector('.info-card');
    if (host && host.parentNode) {
      host.parentNode.insertBefore(card, host.nextSibling);
    } else {
      var main = document.getElementById('content');
      if (main) main.appendChild(card);
    }
    return card;
  }

  function applyDoc(doc) {
    var card = ensureCard();
    if (!card) return false;
    var block = card.querySelector('.bilingual-block');
    if (block) {
      var panes = block.querySelectorAll('.lang-content');
      if (panes[0]) panes[0].innerHTML = renderSteps(doc.cn_steps, doc.note_cn);
      if (panes[1]) panes[1].innerHTML = renderSteps(doc.en_steps, doc.note_en);
      if (typeof currentLang === 'number') {
        var tabs = block.querySelectorAll('.lang-tab');
        tabs.forEach(function (t, i) { t.classList.toggle('active', i === currentLang); });
        panes.forEach(function (c, i) { c.classList.toggle('active', i === currentLang); });
      }
    } else {
      var body = card.querySelector('.desc-body');
      if (body) body.innerHTML = renderSteps(doc.cn_steps, doc.note_cn);
    }
    card.setAttribute('data-usage-source', 'fb');
    return true;
  }

  function run() {
    var t = detectTarget();
    if (!t) return;
    if (typeof UEUsage === 'undefined' || !UEUsage.load) return;
    var url = window.__USAGE_FB_URL__ || '/assets/usage.bin';
    UEUsage.load(url).catch(function () {
      return UEUsage.load('/assets/usage.fb');
    }).then(function () {
      var doc = UEUsage.get(t.kind, t.slug) || UEUsage.getBySlug(t.slug);
      if (doc) applyDoc(doc);
    }).catch(function (e) {
      console.warn('[usage-runtime] fb load failed, keeping static card:', e && e.message);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', run);
  } else {
    run();
  }
})();
