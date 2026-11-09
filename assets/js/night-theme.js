/**
 * Night theme toggle with localStorage persistence.
 */
(function () {
  "use strict";

  var STORAGE_KEY = "site-theme";
  var THEME_NIGHT = "night";
  var THEME_DAY = "day";

  /**
   * Read the preferred theme from storage or system preference.
   *
   * @returns {string} Theme id (`night` or `day`).
   */
  function preferredTheme() {
    try {
      var stored = window.localStorage.getItem(STORAGE_KEY);
      if (stored === THEME_NIGHT || stored === THEME_DAY) {
        return stored;
      }
    } catch (err) {
      // Ignore storage access errors (private mode, etc.).
    }

    if (
      window.matchMedia &&
      window.matchMedia("(prefers-color-scheme: dark)").matches
    ) {
      return THEME_NIGHT;
    }

    return THEME_DAY;
  }

  /**
   * Apply a theme to the document and remember it.
   *
   * @param {string} theme Theme id (`night` or `day`).
   * @returns {void}
   */
  function applyTheme(theme) {
    var root = document.documentElement;
    var isNight = theme === THEME_NIGHT;

    if (isNight) {
      root.setAttribute("data-theme", THEME_NIGHT);
    } else {
      root.removeAttribute("data-theme");
    }

    var meta = document.querySelector('meta[name="theme-color"]');
    if (meta) {
      meta.setAttribute("content", isNight ? "#12151a" : "#ffffff");
    }

    var button = document.getElementById("theme-toggle");
    if (button) {
      button.setAttribute(
        "aria-label",
        isNight ? "Switch to day theme" : "Switch to night theme"
      );
      button.setAttribute("aria-pressed", isNight ? "true" : "false");
    }

    try {
      window.localStorage.setItem(STORAGE_KEY, theme);
    } catch (err) {
      // Ignore storage write errors.
    }
  }

  /**
   * Toggle between day and night themes.
   *
   * @returns {void}
   */
  function toggleTheme() {
    var current = document.documentElement.getAttribute("data-theme");
    applyTheme(current === THEME_NIGHT ? THEME_DAY : THEME_NIGHT);
  }

  applyTheme(preferredTheme());

  document.addEventListener("DOMContentLoaded", function () {
    var button = document.getElementById("theme-toggle");
    if (!button) {
      return;
    }

    applyTheme(preferredTheme());
    button.addEventListener("click", toggleTheme);
  });
})();
