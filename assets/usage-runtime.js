/*
 * usage-runtime.js — progressive enhancement (方案1).
 * Keeps the static baked usage card as fallback, then overrides it from
 * assets/usage.fb at runtime on plugin/module detail pages.
 */
(function () {
  'use strict';

  function inline(s) {
    return String(s == null ? '' : s)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
      .replace(/`([^`]+)`/g, function (_, c) { return '<code class="usage-code">' + c + '</code>'; });
  }

  function renderSteps(steps, note) {
    var ol = '<ol class="usage-steps">' +
      (steps || []).map(function (s) { return '<li>' + inline(s) + '</li>'; }).join('') +
      '</ol>';
    var nt = note ? '<p class="usage-note">' + inline(note) + '</p>' : '';
    return ol + nt;
  }

  function detectTarget() {
    var m = location.pathname.match(/\/(plugins|modules)\/([^\/]+?)\.html?$/);
    if (!m) return null;
    return { kind: m[1] === 'plugins' ? 'plugin' : 'module', slug: decodeURIComponent(m[2]) };
  }

  function applyDoc(doc) {
    var card = document.getElementById('usage');
    if (!card) return false;
    var block = card.querySelector('.bilingual-block');
    if (block) {
      var panes = block.querySelectorAll('.lang-content');
      if (panes[0]) panes[0].innerHTML = renderSteps(doc.cn_steps, doc.note_cn);
      if (panes[1]) panes[1].innerHTML = renderSteps(doc.en_steps, doc.note_en);
    } else {
      var body = card.querySelector('.desc-body');
      if (body) body.innerHTML = renderSteps(doc.cn_steps, doc.note_cn);
    }
    card.setAttribute('data-usage-source', 'fb');
    return true;
  }

  function run() {
    var t = detectTarget();
    if (!t) return;                       // not a detail page -> no fetch
    if (typeof UEUsage === 'undefined' || !UEUsage.load) return;
    var url = window.__USAGE_FB_URL__ || '/assets/usage.fb';
    UEUsage.load(url).then(function () {
      var doc = UEUsage.get(t.kind, t.slug);
      if (doc) applyDoc(doc);
    }).catch(function (e) {
      // Silent: keep the static fallback card.
      console.warn('[usage-runtime] fb load failed, keeping static card:', e && e.message);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', run);
  } else {
    run();
  }
})();
