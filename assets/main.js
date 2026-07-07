// Language tab switching for individual blocks
function switchLang(tabEl) {
  const block = tabEl.closest('.bilingual-block');
  if (!block) return;
  const tabs = block.querySelectorAll('.lang-tab');
  const contents = block.querySelectorAll('.lang-content');
  const idx = Array.from(tabs).indexOf(tabEl);
  tabs.forEach((t, i) => t.classList.toggle('active', i === idx));
  contents.forEach((c, i) => c.classList.toggle('active', i === idx));
}

// Global language toggle - switches ALL bilingual blocks on the page
let currentLang = 0; // 0 = Chinese, 1 = English
function toggleGlobalLang() {
  currentLang = currentLang === 0 ? 1 : 0;
  const btn = document.getElementById('langSwitch');
  if (btn) {
    btn.textContent = currentLang === 0 ? '中文' : 'English';
  }
  document.querySelectorAll('.bilingual-block').forEach(block => {
    const tabs = block.querySelectorAll('.lang-tab');
    const contents = block.querySelectorAll('.lang-content');
    tabs.forEach((t, i) => t.classList.toggle('active', i === currentLang));
    contents.forEach((c, i) => c.classList.toggle('active', i === currentLang));
  });
}

// Search/filter functionality for plugin/module lists
function filterItems() {
  const input = document.getElementById('searchInput');
  if (!input) return;
  const query = input.value.toLowerCase().trim();
  const lists = document.querySelectorAll('.plugin-list');
  lists.forEach(list => {
    const items = list.querySelectorAll('li');
    items.forEach(item => {
      const name = item.querySelector('.plugin-name');
      const desc = item.querySelector('.plugin-desc');
      const text = (name ? name.textContent : '') + ' ' + (desc ? desc.textContent : '');
      if (query === '' || text.toLowerCase().includes(query)) {
        item.style.display = 'block';
      } else {
        item.style.display = 'none';
      }
    });
  });
}

// Initialize
document.addEventListener('DOMContentLoaded', () => {
  filterItems();
});

// Expose globally
window.switchLang = switchLang;
window.toggleGlobalLang = toggleGlobalLang;
window.filterItems = filterItems;
