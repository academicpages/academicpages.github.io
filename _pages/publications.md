---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

Full publication list can be found here: [ADS](https://ui.adsabs.harvard.edu/search/q=orcid%3A0000-0002-5992-7586&sort=date%20desc%2C%20bibcode%20desc&p_=0) and here: [arXiv](https://arxiv.org/search/?query=sihan+yuan&searchtype=all&source=header)

<div id="publications-container">
  <p>Loading publications...</p>
</div>

<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script>
$(document).ready(function() {
  // Load publications from the local JSON file
  $.getJSON("/assets/js/publications.json", function(data) {
    const lastUpdated = data.last_updated || "";
    const publications = data.publications || [];
    
    if (publications.length > 0) {
      let html = "<div class='publications-list'>";
      
      // Add last updated info
      html += `<p class="last-updated">Last updated: ${lastUpdated}</p>`;
      
      // Add publications
      for (let i = 0; i < publications.length; i++) {
        const pub = publications[i];
        
        html += `
          <div class="publication-item">
            <div class="publication-title">
              <a href="${pub.ads_link}" target="_blank">${pub.title}</a>
            </div>
            <div class="publication-authors">${pub.authors}</div>
            <div class="publication-journal">${pub.journal_info}</div>
            <div class="publication-links">
        `;
        
        // Add links
        if (pub.ads_link) {
          html += `<a href="${pub.ads_link}" target="_blank" class="pub-link">ADS</a>`;
        }
        
        if (pub.arxiv_link) {
          html += ` | <a href="${pub.arxiv_link}" target="_blank" class="pub-link">arXiv</a>`;
        }
        
        html += `
            </div>
          </div>
        `;
      }
      
      html += "</div>";
      
      // Display publications
      $("#publications-container").html(html);
    } else {
      $("#publications-container").html(`
        <div class="publication-notice">
          <p>No publications found in the local cache.</p>
          <p>Please check back later or visit the direct links above.</p>
          <p class="last-updated">Last attempted update: ${lastUpdated}</p>
        </div>
      `);
    }
  }).fail(function() {
    // Handle error loading the JSON file
    $("#publications-container").html(`
      <div class="publication-notice">
        <p>Unable to load publications data.</p>
        <p>Please visit the direct links above to see the complete list of publications.</p>
      </div>
    `);
  });
});
</script>

<style>
.publications-list {
  padding: 0;
}

.last-updated {
  font-size: 0.8em;
  color: #777;
  margin-bottom: 1.5em;
  text-align: right;
}

.publication-item {
  margin-bottom: 1.5em;
  padding-bottom: 1em;
  border-bottom: 1px solid #eee;
}

.publication-title {
  font-weight: bold;
  margin-bottom: 0.3em;
}

.publication-title a {
  color: #2c3e50;
  text-decoration: none;
}

.publication-title a:hover {
  color: #3498db;
  text-decoration: underline;
}

.publication-authors {
  font-style: italic;
  margin-bottom: 0.3em;
}

.publication-journal {
  color: #666;
  margin-bottom: 0.3em;
}

.publication-links {
  font-size: 0.9em;
}

.pub-link {
  color: #3498db;
  text-decoration: none;
}

.pub-link:hover {
  text-decoration: underline;
}

.publication-notice {
  background-color: #f8f9fa;
  border: 1px solid #eee;
  padding: 1em;
  border-radius: 5px;
  text-align: center;
}
</style>
