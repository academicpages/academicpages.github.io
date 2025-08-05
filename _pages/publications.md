---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% include head/custom.html %}

<link rel="stylesheet" href="{{ '/assets/css/publications.css' | relative_url }}">
<script src="{{ '/assets/js/publications-loader.js' | relative_url }}" type="text/javascript"></script>

<!-- Summary Statistics Section (will be shown when data is available) -->
<div id="publication-stats" class="publication-summary" style="display: none;">
    <h2>Research Impact</h2>
    <div class="stats-grid">
        <div class="stat-item">
            <span class="stat-number" id="total-papers">-</span>
            <span class="stat-label">publications</span>
        </div>
        <div class="stat-item">
            <span class="stat-number" id="total-citations">-</span>
            <span class="stat-label">citations</span>
        </div>
        <div class="stat-item">
            <span class="stat-number" id="h-index">-</span>
            <span class="stat-label">h-index</span>
        </div>
        <div class="stat-item">
            <span class="stat-number" id="i10-index">-</span>
            <span class="stat-label">i10-index</span>
        </div>
    </div>
    <div class="stats-secondary">
        <span><span id="first-author-count">-</span> first author</span>
        <span><span id="avg-citations">-</span> avg citations</span>
        <span class="last-updated">Updated <span id="last-updated">-</span></span>
    </div>
</div>

Full publication list can be found here: [ADS](https://ui.adsabs.harvard.edu/search/q=orcid%3A0000-0002-5992-7586&sort=date%20desc%2C%20bibcode%20desc&p_=0) and here: [arXiv](https://arxiv.org/search/?query=sihan+yuan&searchtype=all&source=header)

<div class="publication-tabs">
  <button id="all-tab" class="tab-button active">All Publications</button>
  <button id="first-author-tab" class="tab-button">First Author</button>
</div>

<div id="publications-container">
  <p>Loading publications...</p>
</div>

<noscript>
  <div style="background-color: #dc3545; color: white; padding: 10px; margin-top: 20px; border-radius: 5px;">
    <p><strong>JavaScript is disabled or not supported in your browser.</strong></p>
    <p>This page requires JavaScript to display publications. Please enable JavaScript or use a different browser.</p>
  </div>
</noscript>
