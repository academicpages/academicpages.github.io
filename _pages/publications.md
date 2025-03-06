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

<noscript>
  <div class="publication-notice">
    <p>JavaScript is required to view the publications list.</p>
    <p>Please visit the direct links above to see the complete list of publications.</p>
  </div>
</noscript>

<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script>
// Debug mode - set to true to enable console logging
const DEBUG = true;

function debugLog(message, data) {
  if (DEBUG && console) {
    if (data) {
      console.log(message, data);
    } else {
      console.log(message);
    }
  }
}

$(document).ready(function() {
  debugLog("Starting to load publications...");
  
  // Static URL as a fallback in case of template issues
  const jsonUrl = "{{ site.baseurl }}/assets/js/publications.json";
  const fallbackUrl = "/assets/js/publications.json";
  
  debugLog("Using JSON URL:", jsonUrl);
  
  // Load publications from the local JSON file
  $.getJSON(jsonUrl)
    .done(function(data) {
      debugLog("Successfully loaded publications data:", data);
      
      const lastUpdated = data.last_updated || "";
      const publications = data.publications || [];
      
      if (publications.length > 0) {
        let html = "<div class='publications-list'>";
        
        // Add last updated info
        html += `<p class="last-updated">Last updated: ${lastUpdated}</p>`;
        
        // Add publications
        for (let i = 0; i < publications.length; i++) {
          const pub = publications[i];
          debugLog(`Processing publication ${i+1}:`, pub);
          
          // Format citation count
          const citationBadge = pub.citation_count > 0 
            ? `<span class="citation-badge" title="Citation count">📄 ${pub.citation_count}</span>` 
            : '';
          
          html += `
            <div class="publication-item">
              <div class="publication-title">
                <a href="${pub.ads_link}" target="_blank">${pub.title}</a>
              </div>
              <div class="publication-authors">${pub.authors}</div>
              <div class="publication-journal">${pub.journal_info}</div>
              <div class="publication-metrics">
                ${citationBadge}
              </div>
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
        debugLog("Publications rendered successfully");
      } else {
        debugLog("No publications found in data");
        $("#publications-container").html(`
          <div class="publication-notice">
            <p>No publications found in the local cache.</p>
            <p>Please check back later or visit the direct links above.</p>
            <p class="last-updated">Last attempted update: ${lastUpdated}</p>
          </div>
        `);
      }
    })
    .fail(function(jqXHR, textStatus, errorThrown) {
      // Log the error
      debugLog("Error loading JSON from primary URL:", textStatus);
      debugLog("Error details:", jqXHR);
      
      // Try the fallback URL
      debugLog("Trying fallback URL:", fallbackUrl);
      $.getJSON(fallbackUrl)
        .done(function(data) {
          debugLog("Successfully loaded publications from fallback URL:", data);
          // Repeat the same processing as above
          // This is simplified for brevity
          if (data.publications && data.publications.length > 0) {
            let html = "<div class='publications-list'>";
            html += `<p class="last-updated">Last updated: ${data.last_updated || ""}</p>`;
            
            for (let pub of data.publications) {
              // Format citation count
              const citationBadge = pub.citation_count > 0 
                ? `<span class="citation-badge" title="Citation count">📄 ${pub.citation_count}</span>` 
                : '';
                
              html += `
                <div class="publication-item">
                  <div class="publication-title">
                    <a href="${pub.ads_link}" target="_blank">${pub.title}</a>
                  </div>
                  <div class="publication-authors">${pub.authors}</div>
                  <div class="publication-journal">${pub.journal_info}</div>
                  <div class="publication-metrics">
                    ${citationBadge}
                  </div>
                </div>
              `;
            }
            
            html += "</div>";
            $("#publications-container").html(html);
          } else {
            showError("No publications found in fallback data");
          }
        })
        .fail(function(jqXHR2, textStatus2, errorThrown2) {
          debugLog("Fallback also failed:", textStatus2);
          showError(textStatus, errorThrown || errorThrown2 || "Unknown error");
        });
    });
    
  function showError(textStatus, errorThrown) {
    $("#publications-container").html(`
      <div class="publication-notice">
        <p>Unable to load publications data.</p>
        <p>Error: ${textStatus}${errorThrown ? ` - ${errorThrown}` : ''}</p>
        <p>Please visit the direct links above to see the complete list of publications.</p>
        <p><button id="debug-btn" class="btn">Show Debug Info</button></p>
      </div>
    `);
    
    // Add debug button functionality
    $("#debug-btn").click(function() {
      const debugInfo = `
        <div class="debug-info">
          <h3>Debug Information:</h3>
          <p>Browser: ${navigator.userAgent}</p>
          <p>URL tried: ${jsonUrl}</p>
          <p>Fallback URL: ${fallbackUrl}</p>
          <p>Error: ${textStatus}${errorThrown ? ` - ${errorThrown}` : ''}</p>
          <p>Date/Time: ${new Date().toString()}</p>
        </div>
      `;
      
      $(this).after(debugInfo);
      $(this).remove();
    });
  }
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

.publication-metrics {
  margin-bottom: 0.3em;
}

.citation-badge {
  display: inline-block;
  background-color: #f1f8ff;
  color: #0366d6;
  border: 1px solid #c8e1ff;
  border-radius: 3px;
  padding: 0.1em 0.5em;
  font-size: 0.85em;
  margin-right: 0.5em;
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

.debug-info {
  text-align: left;
  margin-top: 1em;
  padding: 1em;
  background-color: #f5f5f5;
  border: 1px solid #ddd;
  border-radius: 5px;
  font-family: monospace;
  font-size: 0.9em;
}
</style>
