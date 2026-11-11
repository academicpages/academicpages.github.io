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
   * Wire filter controls for archive pages.
   * @returns {void}
   */
  function init() {
    if (!document.querySelector("[data-filter-item]")) {
      return;
    }

    document.addEventListener("click", function (event) {
      var target = event.target;
      if (!(target instanceof Element)) {
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
