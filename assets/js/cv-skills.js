/**
 * Foldable CV skill groups and a lightweight native word cloud.
 */
(function () {
  "use strict";

  /**
   * Storage key for folded skill groups on this page.
   * @returns {string}
   */
  function foldStorageKey() {
    return "cv-skills-fold:" + window.location.pathname;
  }

  /**
   * Read fold state from localStorage.
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
   * Persist fold state.
   * @param {Object<string, boolean>} state Fold map.
   * @returns {void}
   */
  function writeFoldState(state) {
    try {
      localStorage.setItem(foldStorageKey(), JSON.stringify(state));
    } catch (err) {
      // Ignore storage failures.
    }
  }

  /**
   * Expand or collapse one skill group.
   * @param {string} slug Group slug.
   * @param {boolean} expanded Open state.
   * @returns {void}
   */
  function setGroupExpanded(slug, expanded) {
    var group = document.querySelector('[data-skills-group="' + slug + '"]');
    var button = document.querySelector('[data-skills-fold="' + slug + '"]');
    if (!group || !button) {
      return;
    }
    group.classList.toggle("is-collapsed", !expanded);
    button.setAttribute("aria-expanded", expanded ? "true" : "false");
  }

  /**
   * Wire fold toggles for skill categories.
   * @returns {void}
   */
  function initFolds() {
    var state = readFoldState();
    document.querySelectorAll("[data-skills-fold]").forEach(function (button) {
      var slug = button.getAttribute("data-skills-fold") || "";
      var expanded = state[slug] !== false;
      setGroupExpanded(slug, expanded);
    });

    document.addEventListener("click", function (event) {
      var target = event.target;
      if (!(target instanceof Element)) {
        return;
      }
      var button = target.closest("[data-skills-fold]");
      if (!button) {
        return;
      }
      event.preventDefault();
      var slug = button.getAttribute("data-skills-fold") || "";
      var expanded = button.getAttribute("aria-expanded") !== "true";
      setGroupExpanded(slug, expanded);
      var nextState = readFoldState();
      nextState[slug] = expanded;
      writeFoldState(nextState);
    });
  }

  /**
   * Rect intersection helper.
   * @param {{x:number,y:number,w:number,h:number}} a First box.
   * @param {{x:number,y:number,w:number,h:number}} b Second box.
   * @returns {boolean}
   */
  function overlaps(a, b) {
    return !(
      a.x + a.w < b.x ||
      b.x + b.w < a.x ||
      a.y + a.h < b.y ||
      b.y + b.h < a.y
    );
  }

  /**
   * Lay out word-cloud chips with a spiral search.
   * @returns {void}
   */
  function layoutCloud() {
    var canvas = document.querySelector("[data-skills-cloud]");
    if (!canvas) {
      return;
    }

    var words = Array.prototype.slice.call(
      canvas.querySelectorAll(".skills-cloud__word")
    );
    if (!words.length) {
      return;
    }

    var width = canvas.clientWidth;
    var height = canvas.clientHeight;
    var cx = width / 2;
    var cy = height / 2;
    var placed = [];

    words.sort(function (a, b) {
      return (
        Number(b.getAttribute("data-weight") || 3) -
        Number(a.getAttribute("data-weight") || 3)
      );
    });

    words.forEach(function (word, index) {
      var weight = Number(word.getAttribute("data-weight") || 3);
      var fontSize = 0.85 + weight * 0.28;
      var rotate = ((index % 5) - 2) * 8;
      word.style.fontSize = fontSize + "rem";
      word.style.transform = "translate(-50%, -50%) rotate(" + rotate + "deg)";

      var rect = word.getBoundingClientRect();
      var box = { w: rect.width + 10, h: rect.height + 8 };
      var found = null;
      var angle = 0;
      var radius = 0;

      for (var step = 0; step < 500; step += 1) {
        angle += 0.35;
        radius = 4 + step * 0.9;
        var x = cx + Math.cos(angle) * radius;
        var y = cy + Math.sin(angle) * radius * 0.72;
        var candidate = {
          x: x - box.w / 2,
          y: y - box.h / 2,
          w: box.w,
          h: box.h,
        };

        if (
          candidate.x < 4 ||
          candidate.y < 4 ||
          candidate.x + candidate.w > width - 4 ||
          candidate.y + candidate.h > height - 4
        ) {
          continue;
        }

        var hit = placed.some(function (other) {
          return overlaps(candidate, other);
        });
        if (!hit) {
          found = candidate;
          break;
        }
      }

      if (!found) {
        found = {
          x: 8 + (index * 37) % Math.max(40, width - box.w - 16),
          y: 8 + (index * 29) % Math.max(40, height - box.h - 16),
          w: box.w,
          h: box.h,
        };
      }

      placed.push(found);
      word.style.left = found.x + found.w / 2 + "px";
      word.style.top = found.y + found.h / 2 + "px";
    });
  }

  /**
   * Initialize skills interactions.
   * @returns {void}
   */
  function init() {
    if (!document.querySelector(".skills")) {
      return;
    }
    initFolds();
    layoutCloud();
    window.addEventListener("resize", layoutCloud);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
