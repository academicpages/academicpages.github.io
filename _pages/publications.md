---
layout: archive
title: "Publications"
permalink: /pubs/
author_profile: true
---

Full publication list can be found here: [ADS](https://ui.adsabs.harvard.edu/search/q=orcid%3A0000-0002-5992-7586&sort=date%20desc%2C%20bibcode%20desc&p_=0) and here: [arXiv](https://arxiv.org/search/?query=sihan+yuan&searchtype=all&source=header)

<div id="publications-container">
  <p>Loading publications...</p>
</div>

<div id="debug-info" style="background-color: #f8d7da; border: 1px solid #f5c6cb; padding: 10px; margin-top: 20px; border-radius: 5px;">
  <h4>Debug Information:</h4>
  <div id="debug-status">Initializing debug...</div>
</div>

<noscript>
  <div class="publication-notice">
    <p>JavaScript is required to view the dynamic publications list.</p>
    <p>Please visit the direct links above to see the complete list of publications.</p>
  </div>
</noscript>

<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script>
// Debug function to update both console and visible debug area
function debug(message) {
  console.log('DEBUG: ' + message);
  $('#debug-status').append('<div>' + message + '</div>');
}

// Check if jQuery is loaded correctly
if (typeof jQuery != 'undefined') {
  debug('jQuery is loaded (version: ' + jQuery.fn.jquery + ')');
} else {
  debug('jQuery is NOT loaded!');
}

$(document).ready(function() {
  debug('Document ready event fired');
  
  // Verify URL of the JSON file
  var jsonUrl = "/assets/js/publications.json";
  debug('Going to fetch JSON data from: ' + jsonUrl);
  
  // Simple approach: load the JSON file directly
  $.ajax({
    url: jsonUrl,
    dataType: "json",
    cache: false,
    beforeSend: function() {
      debug('AJAX request started');
    },
    success: function(data) {
      debug('AJAX request successful');
      try {
        if (!data) {
          debug('ERROR: data is null or undefined');
          return;
        }
        
        debug('Data object received: ' + JSON.stringify(data).substring(0, 100) + '...');
        
        const lastUpdated = data.last_updated || "";
        debug('Last updated: ' + lastUpdated);
        
        const publications = data.publications || [];
        debug('Number of publications found: ' + publications.length);
        
        if (publications.length > 0) {
          debug('Building HTML for publications');
          let html = "<div class='publications-list'>";
          
          // Add last updated info
          html += `<p class="last-updated">Last updated: ${lastUpdated}</p>`;
          
          // Add publications
          for (let i = 0; i < publications.length; i++) {
            const pub = publications[i];
            
            // Format citation count if available
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
          
          debug('Updating DOM with publications HTML');
          $("#publications-container").html(html);
          debug('DOM updated successfully');
        } else {
          debug('No publications found in the data');
          $("#publications-container").html(`
            <div class="publication-notice">
              <p>No publications found.</p>
              <p>Please check back later or visit the direct links above.</p>
            </div>
          `);
        }
      } catch (e) {
        debug('ERROR in success handler: ' + e.message);
        debug('Error stack: ' + e.stack);
      }
    },
    error: function(jqXHR, textStatus, errorThrown) {
      debug('AJAX request failed');
      debug('Status: ' + textStatus);
      debug('Error: ' + errorThrown);
      debug('Response Text: ' + jqXHR.responseText?.substring(0, 100) + '...');
      debug('Status Code: ' + jqXHR.status);
      
      // Simple error handling
      $("#publications-container").html(`
        <div class="publication-notice">
          <p>Unable to load publications data.</p>
          <p>Error: ${textStatus} - ${errorThrown}</p>
          <p>Please visit the direct links above to see the complete list of publications.</p>
        </div>
      `);
    }
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
</style>
