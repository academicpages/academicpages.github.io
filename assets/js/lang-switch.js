(function () {
  var STORAGE_KEY = 'preferred-lang';
  var DEFAULT_LANG = 'zh';

  function applyLang(lang) {
    document.documentElement.setAttribute('data-lang', lang);
    localStorage.setItem(STORAGE_KEY, lang);
  }

  function toggleLang() {
    var current = document.documentElement.getAttribute('data-lang') || DEFAULT_LANG;
    applyLang(current === 'zh' ? 'en' : 'zh');
  }

  document.addEventListener('DOMContentLoaded', function () {
    var btn = document.getElementById('lang-toggle-btn');
    if (btn) btn.addEventListener('click', toggleLang);
  });
})();
