
// ===== Theme toggle (persists in localStorage) =====
(function() {
  var body = document.body;
  var stored = localStorage.getItem('ue-theme');
  var prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
  var initial = stored || (prefersDark ? 'dark' : 'light');
  body.setAttribute('data-theme', initial);

  function syncThemeIcons() {
    var suns = document.querySelectorAll('#theme-sun, #ft-sun');
    var moons = document.querySelectorAll('#theme-moon, #ft-moon');
    var isDark = body.getAttribute('data-theme') === 'dark';
    suns.forEach(function(el) { if (el) el.style.display = isDark ? 'none' : 'block'; });
    moons.forEach(function(el) { if (el) el.style.display = isDark ? 'block' : 'none'; });
  }
  syncThemeIcons();

  window.toggleTheme = function() {
    var isDark = body.getAttribute('data-theme') === 'dark';
    var next = isDark ? 'light' : 'dark';
    body.setAttribute('data-theme', next);
    localStorage.setItem('ue-theme', next);
    syncThemeIcons();
  };
})();

// ===== Bilingual toggle =====
function switchLang(tabEl) {
  var block = tabEl.closest('.bilingual-block');
  if (!block) return;
  var tabs = block.querySelectorAll('.lang-tab');
  var contents = block.querySelectorAll('.lang-content');
  var idx = Array.from(tabs).indexOf(tabEl);
  tabs.forEach(function(t, i) { t.classList.toggle('active', i === idx); });
  contents.forEach(function(c, i) { c.classList.toggle('active', i === idx); });
}

var currentLang = 0;
function toggleGlobalLang() {
  currentLang = currentLang === 0 ? 1 : 0;
  var label = document.getElementById('langLabel');
  if (label) label.textContent = currentLang === 0 ? '中文' : 'English';
  document.querySelectorAll('.bilingual-block').forEach(function(block) {
    var tabs = block.querySelectorAll('.lang-tab');
    var contents = block.querySelectorAll('.lang-content');
    tabs.forEach(function(t, i) { t.classList.toggle('active', i === currentLang); });
    contents.forEach(function(c, i) { c.classList.toggle('active', i === currentLang); });
  });
}

// ===== Search / filter =====
function filterItems() {
  var input = document.getElementById('searchInput');
  if (!input) return;
  var query = input.value.toLowerCase().trim();
  document.querySelectorAll('.grid').forEach(function(grid) {
    grid.querySelectorAll('.plugin-card').forEach(function(card) {
      var text = card.textContent.toLowerCase();
      card.style.display = (query === '' || text.indexOf(query) !== -1) ? '' : 'none';
    });
  });
  document.querySelectorAll('.plugin-list').forEach(function(list) {
    list.querySelectorAll('li').forEach(function(li) {
      var text = li.textContent.toLowerCase();
      li.style.display = (query === '' || text.indexOf(query) !== -1) ? '' : 'none';
    });
  });
}

// ===== Sidebar toggle (mobile) =====
(function() {
  var btn = document.getElementById('sidebarToggle');
  var sb = document.getElementById('sidebar');
  if (btn && sb) {
    btn.addEventListener('click', function() { sb.classList.toggle('open'); });
    document.addEventListener('click', function(e) {
      if (sb.classList.contains('open') && !sb.contains(e.target) && e.target !== btn) {
        sb.classList.remove('open');
      }
    });
  }
})();

// ===== Nav highlight (simple: match path) =====
(function() {
  var path = location.pathname;
  document.querySelectorAll('.nav-item').forEach(function(item) {
    var href = item.getAttribute('href');
    if (!href) return;
    if (href === './' && (path === '/' || path === '' || path.endsWith('/index.html'))) {
      item.classList.add('active');
    } else if (href !== './' && path.indexOf(href.replace('./', '/')) !== -1) {
      item.classList.add('active');
    }
  });
})();

window.switchLang = switchLang;
window.toggleGlobalLang = toggleGlobalLang;
window.filterItems = filterItems;
window.toggleTheme = window.toggleTheme || function() {};

document.addEventListener('DOMContentLoaded', function() { filterItems(); });
