/* Optional archive thumbnail carousel */
(function () {
  "use strict";

  function showSlide(slider, index) {
    const slides = Array.from(
      slider.querySelectorAll(".portfolio-thumb-slide"),
    );

    if (slides.length < 2) return;

    const nextIndex = (index + slides.length) % slides.length;

    slides.forEach(function (slide, i) {
      const active = i === nextIndex;
      slide.classList.toggle("is-active", active);
      slide.hidden = !active;
    });

    slider.dataset.currentSlide = String(nextIndex);

    const counter = slider.querySelector(".portfolio-thumb-counter");
    if (counter) {
      counter.textContent = nextIndex + 1 + " / " + slides.length;
    }
  }

  document.addEventListener("click", function (event) {
    const button = event.target.closest(
      ".portfolio-thumb-prev, .portfolio-thumb-next",
    );

    if (!button) return;

    const slider = button.closest(".portfolio-thumb-slider");
    if (!slider) return;

    event.preventDefault();
    event.stopPropagation();

    const current = Number(slider.dataset.currentSlide || 0);
    const direction = button.classList.contains("portfolio-thumb-next")
      ? 1
      : -1;

    showSlide(slider, current + direction);
  });

  document.addEventListener("keydown", function (event) {
    const slider = event.target.closest(".portfolio-thumb-slider");
    if (!slider) return;

    if (event.key !== "ArrowLeft" && event.key !== "ArrowRight") return;

    event.preventDefault();

    const current = Number(slider.dataset.currentSlide || 0);
    showSlide(slider, current + (event.key === "ArrowRight" ? 1 : -1));
  });
})();
