/**
 * Filter and sort publications by hierarchical area tags.
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
   * Apply the active tag filter and optional sort to publication cards.
   * @param {HTMLElement} root Publications list root.
   * @param {string} activeTag Active tag slug, or "" for all.
   * @returns {void}
   */
  function applyFilter(root, activeTag) {
    var items = Array.prototype.slice.call(
      root.querySelectorAll(".publication-item")
    );
    var empty = document.querySelector(".pub-tag-empty");
    var visibleCount = 0;

    items.forEach(function (item) {
      var tags = parseTags(item.getAttribute("data-tags"));
      var matches = !activeTag || tags.indexOf(activeTag) !== -1;
      item.classList.toggle("is-hidden", !matches);
      if (matches) {
        visibleCount += 1;
      }
    });

    if (activeTag) {
      items.sort(function (a, b) {
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
        // Narrower tags (later in chain) first when sorting within a filter.
        return bIdx - aIdx;
      });
      items.forEach(function (item) {
        root.appendChild(item);
      });
    }

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
   * Wire filter controls for the publications page.
   * @returns {void}
   */
  function init() {
    var root = document.querySelector("[data-publications-list]");
    if (!root) {
      return;
    }

    var params = new URLSearchParams(window.location.search);
    var initial = params.get("tag") || "";

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
      var current = new URLSearchParams(window.location.search).get("tag") || "";
      if (next === current) {
        next = "";
      }
      applyFilter(root, next);
    });

    applyFilter(root, initial);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
