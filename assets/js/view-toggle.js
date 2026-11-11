/**
 * Persist vignette/list view preference for archive pages.
 */
(function () {
  "use strict";

  /**
   * Apply a view mode to the current page panels.
   *
   * @param {HTMLElement} toggleRoot Toggle control root.
   * @param {string} view View id (`vignette` or `list`).
   * @returns {void}
   */
  function applyView(toggleRoot, view) {
    var key = toggleRoot.getAttribute("data-view-toggle") || "view";
    var next = view === "list" ? "list" : "vignette";

    document.querySelectorAll("[data-view-panel]").forEach(function (panel) {
      var match = panel.getAttribute("data-view-panel") === next;
      panel.hidden = !match;
    });

    toggleRoot.querySelectorAll("[data-view]").forEach(function (button) {
      var active = button.getAttribute("data-view") === next;
      button.classList.toggle("is-active", active);
      button.setAttribute("aria-pressed", active ? "true" : "false");
    });

    try {
      window.localStorage.setItem(key, next);
    } catch (err) {
      // Ignore storage write errors.
    }

    document.dispatchEvent(
      new CustomEvent("view-toggle:changed", { detail: { view: next } })
    );
  }

  /**
   * Initialize view toggles on the page.
   *
   * @returns {void}
   */
  function init() {
    var toggles = document.querySelectorAll("[data-view-toggle]");
    if (!toggles.length) {
      return;
    }

    toggles.forEach(function (toggleRoot) {
      var key = toggleRoot.getAttribute("data-view-toggle") || "view";
      var stored = "";
      try {
        stored = window.localStorage.getItem(key) || "";
      } catch (err) {
        stored = "";
      }
      applyView(toggleRoot, stored === "list" ? "list" : "vignette");

      toggleRoot.addEventListener("click", function (event) {
        var target = event.target;
        if (!(target instanceof Element)) {
          return;
        }
        var button = target.closest("[data-view]");
        if (!button || !toggleRoot.contains(button)) {
          return;
        }
        applyView(toggleRoot, button.getAttribute("data-view") || "vignette");
      });
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
