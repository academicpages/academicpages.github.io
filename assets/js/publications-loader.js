// Publications loader script

// Immediately update the debug status to confirm script is running
document.addEventListener('DOMContentLoaded', function() {
  // Set initial status to show script is running
  var statusElement = document.getElementById('debug-status');
  if (statusElement) {
    statusElement.textContent = 'Script loaded and running! Time: ' + new Date().toLocaleString();
  }
  
  // Setup button event listeners
  var testBasicButton = document.getElementById('test-basic-button');
  if (testBasicButton) {
    testBasicButton.addEventListener('click', testBasicScript);
    console.log('Added event listener to basic test button');
  }
  
  var testJsonButton = document.getElementById('test-json-button');
  if (testJsonButton) {
    testJsonButton.addEventListener('click', testJsonAccess);
    console.log('Added event listener to JSON test button');
  }
  
  // Extra check for GitHub Pages
  var isGitHubPages = window.location.hostname.indexOf('github.io') !== -1;
  if (isGitHubPages && statusElement) {
    statusElement.textContent += ' (Running on GitHub Pages)';
  }
});

// Test function for basic scripting
function testBasicScript() {
  console.log('Basic Script Test clicked');
  
  // Simple DOM manipulation to confirm JavaScript is working
  var status = document.getElementById('debug-status');
  if (status) {
    status.textContent = 'Basic script test successful at ' + new Date().toLocaleString();
    status.style.color = 'green';
    status.style.fontWeight = 'bold';
  }
  
  // Add browser information
  var debugInfo = document.getElementById('debug-info');
  if (debugInfo) {
    var browserInfoDiv = document.createElement('div');
    browserInfoDiv.style.marginTop = '10px';
    browserInfoDiv.style.borderTop = '1px solid #ccc';
    browserInfoDiv.style.paddingTop = '10px';
    browserInfoDiv.innerHTML = '<strong>Browser Information:</strong><br>' +
      'User Agent: ' + navigator.userAgent + '<br>' +
      'Platform: ' + navigator.platform + '<br>';
    debugInfo.appendChild(browserInfoDiv);
  }
}

// Function to test JSON access
function testJsonAccess() {
  console.log('JSON Access Test clicked');
  
  var resultDiv = document.getElementById('json-test-result');
  if (!resultDiv) return;
  
  resultDiv.innerHTML = 'Attempting to access publications.json...';
  
  // Get repository name from URL for GitHub Pages
  var baseUrl = '';
  var isGitHubPages = window.location.hostname.indexOf('github.io') !== -1;
  if (isGitHubPages) {
    // Extract repo name from github.io URL
    var pathSegments = window.location.pathname.split('/');
    // GitHub Pages path might have a repo name segment
    if (pathSegments.length > 1 && pathSegments[1]) {
      baseUrl = '/' + pathSegments[1];
    }
    resultDiv.innerHTML += '<div>Running on GitHub Pages. Base URL: ' + (baseUrl || '/') + '</div>';
  }
  
  // Try multiple possible paths for the JSON file
  var possiblePaths = [
    '/assets/js/publications.json',
    baseUrl + '/assets/js/publications.json',
    './assets/js/publications.json',
    '../assets/js/publications.json'
  ];
  
  resultDiv.innerHTML += '<div>Trying multiple paths:</div>';
  
  // Using XMLHttpRequest for maximum compatibility
  tryNextPath(possiblePaths, 0, resultDiv);
}

function tryNextPath(paths, index, resultDiv) {
  if (index >= paths.length) {
    resultDiv.innerHTML += '<div style="color: red;">All paths failed. Could not access publications.json</div>';
    return;
  }
  
  var path = paths[index];
  resultDiv.innerHTML += '<div>Trying path: ' + path + '</div>';
  
  var xhr = new XMLHttpRequest();
  xhr.open('GET', path);
  
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4) {
      if (xhr.status === 200) {
        resultDiv.innerHTML += '<div style="color: green;">SUCCESS with path: ' + path + '</div>';
        resultDiv.innerHTML += '<div>First 50 characters:<br><pre>' + 
          xhr.responseText.substring(0, 50) + '...</pre></div>';
        
        // Try to parse it
        try {
          var data = JSON.parse(xhr.responseText);
          resultDiv.innerHTML += '<div style="color: green;">JSON parsed successfully!</div>';
          
          // Show number of publications
          if (data && data.publications) {
            resultDiv.innerHTML += '<div>Found ' + data.publications.length + ' publications</div>';
            
            // Now try to render the publication
            loadFirstPublication(data.publications[0]);
          }
        } catch (e) {
          resultDiv.innerHTML += '<div style="color: red;">Error parsing JSON: ' + e.message + '</div>';
        }
      } else {
        resultDiv.innerHTML += '<div>Failed with path: ' + path + ' (Status: ' + xhr.status + ')</div>';
        // Try next path
        tryNextPath(paths, index + 1, resultDiv);
      }
    }
  };
  
  xhr.onerror = function() {
    resultDiv.innerHTML += '<div>Error with path: ' + path + '</div>';
    // Try next path
    tryNextPath(paths, index + 1, resultDiv);
  };
  
  xhr.send();
}

// Function to render the first publication
function loadFirstPublication(pub) {
  try {
    var container = document.getElementById('publications-container');
    if (!container) return;
    
    // Clear existing content
    container.innerHTML = '';
    
    // Create elements for the publication
    var item = document.createElement('div');
    item.className = 'publication-item';
    
    var title = document.createElement('div');
    title.className = 'publication-title';
    
    var titleLink = document.createElement('a');
    titleLink.href = pub.ads_link;
    titleLink.target = '_blank';
    titleLink.textContent = pub.title;
    
    title.appendChild(titleLink);
    item.appendChild(title);
    
    var authors = document.createElement('div');
    authors.className = 'publication-authors';
    authors.textContent = pub.authors;
    item.appendChild(authors);
    
    var journal = document.createElement('div');
    journal.className = 'publication-journal';
    journal.textContent = pub.journal_info;
    item.appendChild(journal);
    
    var links = document.createElement('div');
    links.className = 'publication-links';
    
    var adsLink = document.createElement('a');
    adsLink.href = pub.ads_link;
    adsLink.target = '_blank';
    adsLink.className = 'pub-link';
    adsLink.textContent = 'ADS';
    links.appendChild(adsLink);
    
    if (pub.arxiv_link) {
      links.appendChild(document.createTextNode(' | '));
      
      var arxivLink = document.createElement('a');
      arxivLink.href = pub.arxiv_link;
      arxivLink.target = '_blank';
      arxivLink.className = 'pub-link';
      arxivLink.textContent = 'arXiv';
      links.appendChild(arxivLink);
    }
    
    item.appendChild(links);
    container.appendChild(item);
    
    // Add success message
    var notice = document.createElement('p');
    notice.style.marginTop = '20px';
    notice.style.fontStyle = 'italic';
    notice.textContent = 'Success! This is just the first publication as a test.';
    container.appendChild(notice);
    
    // Update debug info
    var resultDiv = document.getElementById('json-test-result');
    if (resultDiv) {
      resultDiv.innerHTML += '<div style="color: green;">✓ Successfully rendered first publication!</div>';
    }
    
    // Add "load all" button
    var loadAllButton = document.createElement('button');
    loadAllButton.textContent = 'Load All Publications';
    loadAllButton.style.marginTop = '20px';
    loadAllButton.style.padding = '5px 10px';
    loadAllButton.style.background = '#28a745';
    loadAllButton.style.color = 'white';
    loadAllButton.style.border = 'none';
    loadAllButton.style.borderRadius = '3px';
    loadAllButton.style.cursor = 'pointer';
    
    loadAllButton.addEventListener('click', loadAllPublications);
    
    container.appendChild(loadAllButton);
  } catch (e) {
    var resultDiv = document.getElementById('json-test-result');
    if (resultDiv) {
      resultDiv.innerHTML += '<div style="color: red;">Error rendering publication: ' + e.message + '</div>';
    }
  }
}

// Function to load all publications after successful test
function loadAllPublications() {
  var resultDiv = document.getElementById('json-test-result');
  if (resultDiv) {
    resultDiv.innerHTML += '<div>Loading all publications...</div>';
  }
  
  // Use the same path discovery logic as before
  var baseUrl = '';
  var isGitHubPages = window.location.hostname.indexOf('github.io') !== -1;
  if (isGitHubPages) {
    var pathSegments = window.location.pathname.split('/');
    if (pathSegments.length > 1 && pathSegments[1]) {
      baseUrl = '/' + pathSegments[1];
    }
  }
  
  var possiblePaths = [
    '/assets/js/publications.json',
    baseUrl + '/assets/js/publications.json',
    './assets/js/publications.json',
    '../assets/js/publications.json'
  ];
  
  // Try each path until success
  tryLoadAllWithPath(possiblePaths, 0);
}

function tryLoadAllWithPath(paths, index) {
  var resultDiv = document.getElementById('json-test-result');
  
  if (index >= paths.length) {
    if (resultDiv) {
      resultDiv.innerHTML += '<div style="color: red;">Failed to load all publications.</div>';
    }
    return;
  }
  
  var path = paths[index];
  var xhr = new XMLHttpRequest();
  xhr.open('GET', path);
  
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4) {
      if (xhr.status === 200) {
        try {
          var data = JSON.parse(xhr.responseText);
          renderAllPublications(data);
        } catch (e) {
          tryLoadAllWithPath(paths, index + 1);
        }
      } else {
        tryLoadAllWithPath(paths, index + 1);
      }
    }
  };
  
  xhr.onerror = function() {
    tryLoadAllWithPath(paths, index + 1);
  };
  
  xhr.send();
}

function renderAllPublications(data) {
  var container = document.getElementById('publications-container');
  if (!container) return;
  
  container.innerHTML = '';
  
  if (!data || !data.publications || data.publications.length === 0) {
    container.innerHTML = '<p>No publications found.</p>';
    return;
  }
  
  var wrapper = document.createElement('div');
  wrapper.className = 'publications-list';
  
  // Add last updated info
  var lastUpdated = document.createElement('p');
  lastUpdated.className = 'last-updated';
  lastUpdated.textContent = 'Last updated: ' + (data.last_updated || 'Unknown');
  wrapper.appendChild(lastUpdated);
  
  // Add all publications
  data.publications.forEach(function(pub) {
    var item = document.createElement('div');
    item.className = 'publication-item';
    
    var title = document.createElement('div');
    title.className = 'publication-title';
    
    var titleLink = document.createElement('a');
    titleLink.href = pub.ads_link;
    titleLink.target = '_blank';
    titleLink.textContent = pub.title;
    
    title.appendChild(titleLink);
    item.appendChild(title);
    
    var authors = document.createElement('div');
    authors.className = 'publication-authors';
    authors.textContent = pub.authors;
    item.appendChild(authors);
    
    var journal = document.createElement('div');
    journal.className = 'publication-journal';
    journal.textContent = pub.journal_info;
    item.appendChild(journal);
    
    // Citation badge if available
    if (pub.citation_count && pub.citation_count > 0) {
      var metrics = document.createElement('div');
      metrics.className = 'publication-metrics';
      
      var badge = document.createElement('span');
      badge.className = 'citation-badge';
      badge.title = 'Citation count';
      badge.textContent = '📄 ' + pub.citation_count;
      
      metrics.appendChild(badge);
      item.appendChild(metrics);
    }
    
    var links = document.createElement('div');
    links.className = 'publication-links';
    
    if (pub.ads_link) {
      var adsLink = document.createElement('a');
      adsLink.href = pub.ads_link;
      adsLink.target = '_blank';
      adsLink.className = 'pub-link';
      adsLink.textContent = 'ADS';
      links.appendChild(adsLink);
    }
    
    if (pub.arxiv_link) {
      if (pub.ads_link) {
        links.appendChild(document.createTextNode(' | '));
      }
      
      var arxivLink = document.createElement('a');
      arxivLink.href = pub.arxiv_link;
      arxivLink.target = '_blank';
      arxivLink.className = 'pub-link';
      arxivLink.textContent = 'arXiv';
      links.appendChild(arxivLink);
    }
    
    item.appendChild(links);
    wrapper.appendChild(item);
  });
  
  container.appendChild(wrapper);
  
  // Update debug info
  var resultDiv = document.getElementById('json-test-result');
  if (resultDiv) {
    resultDiv.innerHTML += '<div style="color: green;">✓ Successfully loaded all ' + 
      data.publications.length + ' publications!</div>';
  }
} 