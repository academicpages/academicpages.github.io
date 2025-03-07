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
  <div id="debug-status">No JavaScript executed yet</div>
  
  <div>
    <button onclick="testJsonAccess()" style="margin-top: 10px; padding: 5px 10px; background: #007bff; color: white; border: none; border-radius: 3px; cursor: pointer;">Test JSON Access</button>
    <div id="json-test-result" style="margin-top: 10px;"></div>
  </div>
  
  <div>
    <button onclick="testBasicScript()" style="margin-top: 10px; padding: 5px 10px; background: #28a745; color: white; border: none; border-radius: 3px; cursor: pointer;">Test Basic Script</button>
  </div>
</div>

<noscript>
  <div style="background-color: #dc3545; color: white; padding: 10px; margin-top: 20px; border-radius: 5px;">
    <p><strong>JavaScript is disabled or not supported in your browser.</strong></p>
    <p>This page requires JavaScript to display publications. Please enable JavaScript or use a different browser.</p>
  </div>
</noscript>

<script>
// Immediately update the debug status to confirm script is running
document.getElementById('debug-status').textContent = 'Script tag is executing!';

// Test function that will be called by the button
function testBasicScript() {
  // Simple DOM manipulation to confirm JavaScript is working
  const status = document.getElementById('debug-status');
  status.textContent = 'Basic script test successful at ' + new Date().toLocaleString();
  status.style.color = 'green';
  status.style.fontWeight = 'bold';
  
  // Add some diagnostic information
  const debugInfo = document.getElementById('debug-info');
  debugInfo.innerHTML += '<div style="margin-top: 10px; border-top: 1px solid #ccc; padding-top: 10px;">' +
    '<strong>Browser Information:</strong><br>' +
    'User Agent: ' + navigator.userAgent + '<br>' +
    'Platform: ' + navigator.platform + '<br>' +
    '</div>';
}

// Function to manually test JSON access with button click
function testJsonAccess() {
  const resultDiv = document.getElementById('json-test-result');
  resultDiv.innerHTML = 'Attempting to access publications.json...';
  
  // Using XMLHttpRequest for maximum compatibility
  const xhr = new XMLHttpRequest();
  xhr.open('GET', '/assets/js/publications.json');
  
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4) { // Request completed
      if (xhr.status === 200) {
        resultDiv.innerHTML = '<span style="color: green;">SUCCESS!</span> JSON file is accessible. First 50 characters:<br>' +
          '<pre>' + xhr.responseText.substring(0, 50) + '...</pre>';
        
        // Try to parse it
        try {
          const data = JSON.parse(xhr.responseText);
          resultDiv.innerHTML += '<div style="color: green;">JSON parsed successfully!</div>';
          
          // Show number of publications
          if (data && data.publications) {
            resultDiv.innerHTML += '<div>Found ' + data.publications.length + ' publications</div>';
            
            // Show first publication title
            if (data.publications.length > 0) {
              resultDiv.innerHTML += '<div>First publication: ' + data.publications[0].title + '</div>';
              
              // Now try to render the publication
              loadFirstPublication(data.publications[0]);
            }
          }
        } catch (e) {
          resultDiv.innerHTML += '<div style="color: red;">Error parsing JSON: ' + e.message + '</div>';
        }
      } else {
        resultDiv.innerHTML = '<span style="color: red;">ERROR:</span> Failed to access JSON file. Status: ' + xhr.status;
      }
    }
  };
  
  xhr.onerror = function() {
    resultDiv.innerHTML = '<span style="color: red;">ERROR:</span> Network error occurred';
  };
  
  xhr.send();
}

// Function to load and display just the first publication
function loadFirstPublication(pub) {
  try {
    const container = document.getElementById('publications-container');
    
    // Clear existing content
    container.innerHTML = '';
    
    // Create elements manually for maximum compatibility
    const item = document.createElement('div');
    item.className = 'publication-item';
    
    const title = document.createElement('div');
    title.className = 'publication-title';
    
    const titleLink = document.createElement('a');
    titleLink.href = pub.ads_link;
    titleLink.target = '_blank';
    titleLink.textContent = pub.title;
    
    title.appendChild(titleLink);
    item.appendChild(title);
    
    const authors = document.createElement('div');
    authors.className = 'publication-authors';
    authors.textContent = pub.authors;
    item.appendChild(authors);
    
    const journal = document.createElement('div');
    journal.className = 'publication-journal';
    journal.textContent = pub.journal_info;
    item.appendChild(journal);
    
    const links = document.createElement('div');
    links.className = 'publication-links';
    
    const adsLink = document.createElement('a');
    adsLink.href = pub.ads_link;
    adsLink.target = '_blank';
    adsLink.className = 'pub-link';
    adsLink.textContent = 'ADS';
    links.appendChild(adsLink);
    
    if (pub.arxiv_link) {
      links.appendChild(document.createTextNode(' | '));
      
      const arxivLink = document.createElement('a');
      arxivLink.href = pub.arxiv_link;
      arxivLink.target = '_blank';
      arxivLink.className = 'pub-link';
      arxivLink.textContent = 'arXiv';
      links.appendChild(arxivLink);
    }
    
    item.appendChild(links);
    container.appendChild(item);
    
    // Add notice that this is just one publication
    const notice = document.createElement('p');
    notice.style.marginTop = '20px';
    notice.style.fontStyle = 'italic';
    notice.textContent = 'Success! This is just the first publication as a test.';
    container.appendChild(notice);
    
    // Update debug info
    document.getElementById('json-test-result').innerHTML += '<div style="color: green;">✓ Successfully rendered first publication!</div>';
  } catch (e) {
    document.getElementById('json-test-result').innerHTML += '<div style="color: red;">Error rendering publication: ' + e.message + '</div>';
  }
}

// Note: We're NOT automatically loading the publications on page load
// We'll rely on the buttons for testing instead
</script>

<style>
.publications-list {
  padding: 0;
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
  margin-top: 0.5em;
}

.pub-link {
  color: #3498db;
  text-decoration: none;
}

.pub-link:hover {
  text-decoration: underline;
}
</style>
