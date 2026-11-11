/**
 * Subtle Game of Life backdrop for the homepage.
 */
(function () {
  "use strict";

  /**
   * Read whether night theme is active.
   * @returns {boolean}
   */
  function isNight() {
    return document.documentElement.getAttribute("data-theme") === "night";
  }

  /**
   * Create an empty grid.
   * @param {number} rows Row count.
   * @param {number} cols Column count.
   * @returns {Uint8Array[]}
   */
  function makeGrid(rows, cols) {
    var grid = [];
    var r;
    for (r = 0; r < rows; r += 1) {
      grid.push(new Uint8Array(cols));
    }
    return grid;
  }

  /**
   * Seed a sparse random pattern.
   * @param {Uint8Array[]} grid Grid to fill.
   * @returns {void}
   */
  function seed(grid) {
    var r;
    var c;
    for (r = 0; r < grid.length; r += 1) {
      for (c = 0; c < grid[r].length; c += 1) {
        grid[r][c] = Math.random() < 0.22 ? 1 : 0;
      }
    }
  }

  /**
   * Count live neighbors with wraparound.
   * @param {Uint8Array[]} grid Source grid.
   * @param {number} r Row.
   * @param {number} c Column.
   * @returns {number}
   */
  function neighbors(grid, r, c) {
    var rows = grid.length;
    var cols = grid[0].length;
    var total = 0;
    var dr;
    var dc;
    for (dr = -1; dr <= 1; dr += 1) {
      for (dc = -1; dc <= 1; dc += 1) {
        if (dr === 0 && dc === 0) {
          continue;
        }
        total += grid[(r + dr + rows) % rows][(c + dc + cols) % cols];
      }
    }
    return total;
  }

  /**
   * Advance one generation.
   * @param {Uint8Array[]} current Current grid.
   * @param {Uint8Array[]} next Destination grid.
   * @returns {void}
   */
  function step(current, next) {
    var r;
    var c;
    var n;
    var alive;
    for (r = 0; r < current.length; r += 1) {
      for (c = 0; c < current[r].length; c += 1) {
        n = neighbors(current, r, c);
        alive = current[r][c] === 1;
        next[r][c] = (alive && (n === 2 || n === 3)) || (!alive && n === 3) ? 1 : 0;
      }
    }
  }

  /**
   * Initialize the homepage Game of Life.
   * @returns {void}
   */
  function init() {
    var canvas = document.querySelector("[data-home-gol]");
    if (!canvas || !(canvas instanceof HTMLCanvasElement)) {
      return;
    }

    var ctx = canvas.getContext("2d");
    if (!ctx) {
      return;
    }

    var cell = 10;
    var cols = 0;
    var rows = 0;
    var current = [];
    var next = [];
    var timer = 0;
    var generations = 0;

    /**
     * Resize canvas and reseed if geometry changed.
     * @returns {void}
     */
    function resize() {
      var rect = canvas.getBoundingClientRect();
      var dpr = window.devicePixelRatio || 1;
      canvas.width = Math.max(1, Math.floor(rect.width * dpr));
      canvas.height = Math.max(1, Math.floor(rect.height * dpr));
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      cols = Math.max(8, Math.floor(rect.width / cell));
      rows = Math.max(6, Math.floor(rect.height / cell));
      current = makeGrid(rows, cols);
      next = makeGrid(rows, cols);
      seed(current);
      generations = 0;
    }

    /**
     * Paint the current grid.
     * @returns {void}
     */
    function draw() {
      var rect = canvas.getBoundingClientRect();
      var night = isNight();
      var alive = night ? "rgba(142, 192, 245, 0.28)" : "rgba(31, 95, 139, 0.22)";
      var r;
      var c;
      ctx.clearRect(0, 0, rect.width, rect.height);
      ctx.fillStyle = alive;
      for (r = 0; r < rows; r += 1) {
        for (c = 0; c < cols; c += 1) {
          if (current[r][c]) {
            ctx.beginPath();
            ctx.roundRect
              ? ctx.roundRect(c * cell + 1, r * cell + 1, cell - 2, cell - 2, 2)
              : ctx.rect(c * cell + 1, r * cell + 1, cell - 2, cell - 2);
            ctx.fill();
          }
        }
      }
    }

    /**
     * Tick the simulation.
     * @returns {void}
     */
    function tick() {
      step(current, next);
      var swap = current;
      current = next;
      next = swap;
      generations += 1;
      if (generations % 90 === 0) {
        seed(current);
      }
      draw();
    }

    resize();
    draw();
    timer = window.setInterval(tick, 160);
    window.addEventListener("resize", function () {
      resize();
      draw();
    });

    var observer = new MutationObserver(function () {
      draw();
    });
    observer.observe(document.documentElement, {
      attributes: true,
      attributeFilter: ["data-theme"],
    });

    document.addEventListener("visibilitychange", function () {
      if (document.hidden) {
        window.clearInterval(timer);
        timer = 0;
      } else if (!timer) {
        timer = window.setInterval(tick, 160);
      }
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
