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

<div id="debug-info" style="background-color: #f8d7da; border: 1px solid #f5c6cb; padding: 10px; margin-top: 20px; border-radius: 5px;">
  <h4>Debug Information:</h4>
  <div id="debug-status">Initializing debug...</div>
  
  <div style="margin-top: 15px;">
    <button id="check-json-button" style="padding: 5px 10px; background: #007bff; color: white; border: none; border-radius: 3px; cursor: pointer;">Check JSON File Directly</button>
    <div id="json-check-result" style="margin-top: 10px;"></div>
  </div>
</div>

<noscript>
  <div class="publication-notice">
    <p>JavaScript is required to view the dynamic publications list.</p>
    <p>Please visit the direct links above to see the complete list of publications.</p>
  </div>
</noscript>

<script>
// Debug function to update both console and visible debug area
function debug(message) {
  console.log('DEBUG: ' + message);
  document.getElementById('debug-status').innerHTML += '<div>' + message + '</div>';
}

// Initialize debugging
debug('Page loaded at: ' + new Date().toLocaleString());
debug('Testing if basic JavaScript works');

// Check if required DOM elements exist
if (document.getElementById('publications-container')) {
  debug('Publications container found');
} else {
  debug('ERROR: Publications container not found');
}

// Check if browser supports fetch
if (window.fetch) {
  debug('Fetch API is supported');
} else {
  debug('WARNING: Fetch API not supported, will fall back to XMLHttpRequest');
}

// Function to load publications with fetch
function loadPublications() {
  debug('Starting to load publications data');
  
  const jsonUrl = '/assets/js/publications.json';
  debug('JSON URL: ' + jsonUrl);
  
  // First try with fetch API
  fetch(jsonUrl)
    .then(response => {
      debug('Response received with status: ' + response.status);
      if (!response.ok) {
        throw new Error('Network response was not ok: ' + response.status);
      }
      return response.json();
    })
    .then(data => {
      debug('Data successfully parsed as JSON');
      processPublications(data);
    })
    .catch(error => {
      debug('ERROR with fetch: ' + error.message);
      debug('Falling back to XMLHttpRequest');
      
      // Fall back to XMLHttpRequest
      const xhr = new XMLHttpRequest();
      xhr.open('GET', jsonUrl);
      
      xhr.onload = function() {
        if (xhr.status === 200) {
          debug('XMLHttpRequest successful');
          try {
            const data = JSON.parse(xhr.responseText);
            processPublications(data);
          } catch (parseError) {
            debug('ERROR: Failed to parse JSON: ' + parseError.message);
            showError('JSON Parse Error: ' + parseError.message);
          }
        } else {
          debug('XMLHttpRequest failed with status: ' + xhr.status);
          showError('Failed to load data: ' + xhr.status);
        }
      };
      
      xhr.onerror = function() {
        debug('XMLHttpRequest error occurred');
        showError('Network error occurred');
      };
      
      xhr.send();
    });
}

// Process publications data
function processPublications(data) {
  try {
    if (!data) {
      debug('ERROR: data is null or undefined');
      showError('Data is empty');
      return;
    }
    
    debug('Data object properties: ' + Object.keys(data).join(', '));
    
    const lastUpdated = data.last_updated || "";
    debug('Last updated: ' + lastUpdated);
    
    const publications = data.publications || [];
    debug('Number of publications found: ' + publications.length);
    
    if (publications.length > 0) {
      debug('Building HTML for publications');
      let html = "<div class='publications-list'>";
      
      // Add last updated info
      html += `<p class="last-updated">Last updated: ${lastUpdated}</p>`;
      
      // Add publications (first 5 for testing)
      const displayCount = Math.min(publications.length, 5);
      debug(`Rendering first ${displayCount} publications for testing`);
      
      for (let i = 0; i < displayCount; i++) {
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
      
      if (publications.length > displayCount) {
        html += `<p>... and ${publications.length - displayCount} more publications</p>`;
      }
      
      html += "</div>";
      
      debug('Updating DOM with publications HTML');
      document.getElementById('publications-container').innerHTML = html;
      debug('DOM updated successfully');
    } else {
      debug('No publications found in the data');
      showError('No publications found in the data');
    }
  } catch (e) {
    debug('ERROR in processPublications: ' + e.message);
    debug('Error stack: ' + e.stack);
    showError('Error processing data: ' + e.message);
  }
}

// Show error message
function showError(message) {
  document.getElementById('publications-container').innerHTML = `
    <div class="publication-notice">
      <p>Unable to load publications data.</p>
      <p>Error: ${message}</p>
      <p>Please visit the direct links above to see the complete list of publications.</p>
    </div>
  `;
}

// Direct check of JSON file
document.getElementById('check-json-button').addEventListener('click', function() {
  const resultDiv = document.getElementById('json-check-result');
  resultDiv.innerHTML = 'Checking JSON file directly...';
  
  const xhr = new XMLHttpRequest();
  xhr.open('GET', '/assets/js/publications.json');
  xhr.onload = function() {
    if (xhr.status === 200) {
      resultDiv.innerHTML = 'SUCCESS: JSON file exists and is accessible. First 100 characters:<br>' + 
        '<pre>' + xhr.responseText.substring(0, 100) + '...</pre>';
    } else {
      resultDiv.innerHTML = 'ERROR: JSON file request failed with status: ' + xhr.status;
    }
  };
  xhr.onerror = function() {
    resultDiv.innerHTML = 'ERROR: Network error when trying to access the JSON file';
  };
  xhr.send();
});

// Start loading publications
document.addEventListener('DOMContentLoaded', loadPublications);
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
