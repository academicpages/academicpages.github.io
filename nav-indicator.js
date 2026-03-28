document.addEventListener("DOMContentLoaded", function () {
  var sideNav = document.getElementById("side-nav");
  if (!sideNav) return;

  var trackWrapper = sideNav.querySelector(".nav-track-wrapper");
  var track = sideNav.querySelector(".nav-track");
  var dotMover = sideNav.querySelector(".nav-dot-mover");
  var navLinks = sideNav.querySelectorAll(".nav-link[data-section]");

  // Filter to only scrollable sections (exclude external links like CV)
  var scrollLinks = [];
  var sectionIds = [];
  navLinks.forEach(function (link) {
    var section = link.getAttribute("data-section");
    if (section && document.getElementById(section)) {
      scrollLinks.push(link);
      sectionIds.push(section);
    }
  });

  if (scrollLinks.length === 0) return;

  var sectionOffsets = [];
  var dotPositions = [];
  var ticking = false;

  function computePositions() {
    // Get absolute offsets of each content section
    sectionOffsets = sectionIds.map(function (id) {
      var el = document.getElementById(id);
      return el.getBoundingClientRect().top + window.scrollY;
    });

    // Get Y positions of each dot relative to the track wrapper
    var wrapperRect = trackWrapper.getBoundingClientRect();
    var wrapperTop = wrapperRect.top + window.scrollY;

    dotPositions = scrollLinks.map(function (link) {
      var dot = link.querySelector(".nav-dot");
      if (!dot) return 0;
      var dotRect = dot.getBoundingClientRect();
      var dotCenter = dotRect.top + dotRect.height / 2 + window.scrollY;
      return dotCenter - wrapperTop;
    });

    // Position the track line between first and last dots
    if (dotPositions.length >= 2) {
      var firstDot = dotPositions[0];
      var lastDot = dotPositions[dotPositions.length - 1];
      track.style.top = firstDot + "px";
      track.style.height = (lastDot - firstDot) + "px";
    }
  }

  function updateIndicator() {
    var scrollY = window.scrollY;
    var viewportHeight = window.innerHeight;
    var triggerPoint = scrollY + viewportHeight * 0.3;

    // Find active section index
    var activeIndex = 0;
    for (var i = sectionOffsets.length - 1; i >= 0; i--) {
      if (triggerPoint >= sectionOffsets[i]) {
        activeIndex = i;
        break;
      }
    }

    // Calculate progress between current and next section
    var progress = 0;
    if (activeIndex < sectionOffsets.length - 1) {
      var sectionStart = sectionOffsets[activeIndex];
      var sectionEnd = sectionOffsets[activeIndex + 1];
      var range = sectionEnd - sectionStart;
      if (range > 0) {
        progress = Math.max(0, Math.min(1, (triggerPoint - sectionStart) / range));
      }
    }

    // Snap to first dot when at or near the top of the page
    if (scrollY <= sectionOffsets[0]) {
      progress = 0;
      activeIndex = 0;
    }

    // Interpolate dot mover position
    var currentDotY = dotPositions[activeIndex] || 0;
    var nextDotY = dotPositions[activeIndex + 1] || currentDotY;
    var interpolatedY = currentDotY + progress * (nextDotY - currentDotY);

    // Account for the mover's own size (center it)
    var moverSize = dotMover.offsetHeight;
    dotMover.style.transform = "translateY(" + (interpolatedY - moverSize / 2) + "px)";

    // Toggle active class on nav links
    scrollLinks.forEach(function (link, i) {
      if (i === activeIndex) {
        link.classList.add("active");
      } else {
        link.classList.remove("active");
      }
    });

    ticking = false;
  }

  function onScroll() {
    if (!ticking) {
      ticking = true;
      requestAnimationFrame(updateIndicator);
    }
  }

  // Smooth scroll on nav link click
  scrollLinks.forEach(function (link) {
    link.addEventListener("click", function (e) {
      e.preventDefault();
      var targetId = link.getAttribute("data-section");
      var target = document.getElementById(targetId);
      if (target) {
        target.scrollIntoView({ behavior: "smooth", block: "start" });
      }
    });
  });

  // Debounced resize handler
  var resizeTimeout;
  window.addEventListener("resize", function () {
    clearTimeout(resizeTimeout);
    resizeTimeout = setTimeout(function () {
      computePositions();
      updateIndicator();
    }, 100);
  });

  window.addEventListener("scroll", onScroll, { passive: true });

  // Initial setup - wait a frame for layout to settle
  requestAnimationFrame(function () {
    computePositions();
    // Skip transition on initial positioning
    dotMover.style.transition = "none";
    updateIndicator();
    // Re-enable transitions after paint
    requestAnimationFrame(function () {
      dotMover.style.transition = "";
    });
  });
});
