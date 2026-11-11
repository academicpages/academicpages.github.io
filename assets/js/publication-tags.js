/**
 * Filter tagged archive items in both card and list views.
 */
(function () {
  "use strict";

  /**
   * Parse a comma-separated tag slug string into an array.
   * @param {string|null|undefined} value Raw data-tags attribute.
   * @returns {string[]} Tag slugs.
   */
  function parseTags(value) {
    if (!value) {
      return [];
    }
    return value
      .split(",")
      .map(function (tag) {
        return tag.trim();
      })
      .filter(Boolean);
  }

  /**
   * Return the currently visible view panel, if any.
   * @returns {HTMLElement|Document}
   */
  function activeScope() {
    var panel = document.querySelector("[data-view-panel]:not([hidden])");
    return panel || document;
  }

  /**
   * Apply the active tag filter across all filterable items.
   * @param {string} activeTag Active tag slug, or "" for all.
   * @returns {void}
   */
  function applyFilter(activeTag) {
    var items = Array.prototype.slice.call(
      document.querySelectorAll("[data-filter-item]")
    );
    var empty = document.querySelector(".pub-tag-empty");

    items.forEach(function (item) {
      var tags = parseTags(item.getAttribute("data-tags"));
      var matches = !activeTag || tags.indexOf(activeTag) !== -1;
      item.classList.toggle("is-hidden", !matches);
    });

    if (activeTag) {
      var roots = document.querySelectorAll(
        "[data-vignette-list], [data-list-root]"
      );
      roots.forEach(function (root) {
        var rootItems = Array.prototype.slice.call(
          root.querySelectorAll("[data-filter-item]")
        );
        rootItems.sort(function (a, b) {
          var aTags = parseTags(a.getAttribute("data-tags"));
          var bTags = parseTags(b.getAttribute("data-tags"));
          var aIdx = aTags.indexOf(activeTag);
          var bIdx = bTags.indexOf(activeTag);
          if (aIdx === -1 && bIdx === -1) {
            return 0;
          }
          if (aIdx === -1) {
            return 1;
          }
          if (bIdx === -1) {
            return -1;
          }
          return bIdx - aIdx;
        });
        rootItems.forEach(function (item) {
          root.appendChild(item);
        });
      });
    }

    var visibleCount = activeScope().querySelectorAll(
      "[data-filter-item]:not(.is-hidden)"
    ).length;

    if (empty) {
      empty.classList.toggle("is-visible", visibleCount === 0);
    }

    document.querySelectorAll("[data-tag-filter]").forEach(function (button) {
      var isActive = button.getAttribute("data-tag-filter") === activeTag;
      if (button.getAttribute("data-tag-filter") === "" && !activeTag) {
        isActive = true;
      }
      button.classList.toggle("is-active", isActive);
      button.setAttribute("aria-pressed", isActive ? "true" : "false");
    });

    if (history.replaceState) {
      var url = new URL(window.location.href);
      if (activeTag) {
        url.searchParams.set("tag", activeTag);
      } else {
        url.searchParams.delete("tag");
      }
      history.replaceState({}, "", url);
    }
  }

  /**
   * Read the current tag from the URL.
   * @returns {string}
   */
  function currentTag() {
    return new URLSearchParams(window.location.search).get("tag") || "";
  }

  /**
   * Storage key for folded filter rows.
   * @returns {string}
   */
  function foldStorageKey() {
    return "pub-tag-fold:" + window.location.pathname;
  }

  /**
   * Read folded level ids from localStorage.
   * @returns {Object<string, boolean>}
   */
  function readFoldState() {
    try {
      var raw = localStorage.getItem(foldStorageKey());
      return raw ? JSON.parse(raw) : {};
    } catch (err) {
      return {};
    }
  }

  /**
   * Persist folded level ids.
   * @param {Object<string, boolean>} state Fold map.
   * @returns {void}
   */
  function writeFoldState(state) {
    try {
      localStorage.setItem(foldStorageKey(), JSON.stringify(state));
    } catch (err) {
      // Ignore quota / private-mode failures.
    }
  }

  /**
   * Apply expanded/collapsed state to one filter row.
   * @param {string} level Level id.
   * @param {boolean} expanded Whether the row is open.
   * @returns {void}
   */
  function setFoldExpanded(level, expanded) {
    var button = document.querySelector('[data-tag-fold="' + level + '"]');
    var panel = document.querySelector('[data-tag-fold-panel="' + level + '"]');
    var row = document.querySelector('[data-tag-level="' + level + '"]');
    if (!button || !panel || !row) {
      return;
    }
    button.setAttribute("aria-expanded", expanded ? "true" : "false");
    row.classList.toggle("is-collapsed", !expanded);
  }

  /**
   * Wire foldable hierarchy rows.
   * @returns {void}
   */
  function initFolds() {
    var state = readFoldState();
    document.querySelectorAll("[data-tag-fold]").forEach(function (button) {
      var level = button.getAttribute("data-tag-fold") || "";
      var expanded = state[level] !== false;
      setFoldExpanded(level, expanded);
    });

    document.addEventListener("click", function (event) {
      var target = event.target;
      if (!(target instanceof Element)) {
        return;
      }
      var foldButton = target.closest("[data-tag-fold]");
      if (!foldButton) {
        return;
      }
      event.preventDefault();
      var level = foldButton.getAttribute("data-tag-fold") || "";
      var expanded = foldButton.getAttribute("aria-expanded") !== "true";
      setFoldExpanded(level, expanded);
      var nextState = readFoldState();
      nextState[level] = expanded;
      writeFoldState(nextState);
    });
  }

  /**
   * Wire filter controls for archive pages.
   * @returns {void}
   */
  function init() {
    if (!document.querySelector("[data-filter-item]")) {
      return;
    }

    initFolds();

    document.addEventListener("click", function (event) {
      var target = event.target;
      if (!(target instanceof Element)) {
        return;
      }
      if (target.closest("[data-tag-fold]")) {
        return;
      }
      var button = target.closest("[data-tag-filter]");
      if (!button) {
        return;
      }
      event.preventDefault();
      var next = button.getAttribute("data-tag-filter") || "";
      if (next === currentTag()) {
        next = "";
      }
      applyFilter(next);
    });

    document.addEventListener("view-toggle:changed", function () {
      applyFilter(currentTag());
    });

    applyFilter(currentTag());
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
