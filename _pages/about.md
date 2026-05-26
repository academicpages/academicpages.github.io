---
permalink: /
title: "**Runchen** Xu"
author_profile: true
---

<div class="home-hero">
  <p class="home-hero__eyebrow">Academic Homepage</p>
  <h1 class="home-hero__title">Runchen Xu</h1>
  <div class="home-hero__intro intro-blurb" markdown="1">
I am a Ph.D. student at [the School of Computer Science](https://www.auckland.ac.nz/en/science/about-the-faculty/school-of-computer-science.html), [The University of Auckland](https://www.auckland.ac.nz), under the supervision of [Jiamou Liu](https://profiles.auckland.ac.nz/jiamou-liu) and [Ni Ding](https://profiles.auckland.ac.nz/ni-ding). Previously, I completed my Master's degree in Computer Technology at [University of Electronic Science and Technology of China (UESTC)](https://en.uestc.edu.cn/) in 2025, supervised by [Prof. Zheng chang](https://scholar.google.com/citations?user=MmARrhAAAAAJ&hl=zh-CN&oi=ao). I also earned my Bachelor's degree from UESTC in 2022.
  </div>
</div>

<div class="home-grid">
  <div class="home-grid__feature">
    <section class="home-section">
      <h2>News 🔥</h2>
      <div class="news-panel">
        <ul id="news-list" class="news-list">
          <li data-date="2026-04">
            <b>April 2026:</b> ❤️ Congratulations! My Chrome extension
            "<a href="https://chromewebstore.google.com/detail/quickpage-capture/afaeaifhhnjeihopkbpffabdafbfgban?pli=1" target="_blank" rel="noopener noreferrer">QuickPage Capture</a>"
            – a high-efficiency, one-click web screenshot tool – is now officially available on the Chrome Web Store!
          </li>
        </ul>
      </div>
    </section>

    <section class="home-section">
      <h2>Research</h2>
      <p class="research-summary">
        My research primarily focuses on two areas: <span style="color: var(--global-link-color, #0d6d66);">analyzing and optimizing interactions in multi-agent AI systems</span>, and <span style="color: var(--global-link-color, #0d6d66);">designing effective mechanisms for the AI marketplace</span>. I am also interested in Mobile Computing, Wireless Communications and Networking
      </p>
      <ul class="research-tags">
        <li>Decentralized Artificial Intelligence</li>
        <li>Multi-Agent AI System</li>
        <li>Marketplace</li>
        <li>Game Theory</li>
      </ul>
    </section>
  </div>

  <aside class="home-actions">
    <section class="action-card">
      <h2>Teaching</h2>
      <ul class="teaching-list">
        <li>May 2026 - Jun. 2026: Graduate Teaching Assistant, <strong>COMPSCI 120: Mathematics for Computer Science</strong>, 2026 Semester One, The University of Auckland, New Zealand</li>
        <li>Nov. 2025 - Feb. 2026: Graduate Teaching Assistant, <strong>COMPSCI 120: Mathematics for Computer Science</strong>, 2026 Summer School, The University of Auckland, New Zealand</li>
      </ul>
    </section>

    <section class="action-card">
      <h2>CV</h2>
      <p>A copy of my curriculum vitae is available for download.</p>
      <a class="cta-link" href="../files/CV.pdf">View CV.pdf</a>
    </section>

    <section class="action-card">
      <h2>Contact</h2>
      <p>For research inquiries, collaborations, or discussions, please feel free to contact me at:</p>
      <p><strong>Email</strong>: <a class="contact-link" href="mailto:xrc274@aucklanduni.ac.nz">xrc274@aucklanduni.ac.nz</a></p>
    </section>
  </aside>
</div>

<script>
  (function () {
    var newsList = document.getElementById("news-list");
    if (!newsList) return;
    var items = Array.from(newsList.querySelectorAll("li[data-date]"));
    items.sort(function (a, b) {
      var dateA = a.getAttribute("data-date") || "";
      var dateB = b.getAttribute("data-date") || "";
      return dateB.localeCompare(dateA);
    });
    items.forEach(function (item) {
      newsList.appendChild(item);
    });
  })();
</script>

---

> *Patience is all you need*
