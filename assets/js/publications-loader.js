// Publications loader script
let allPublications = [];

document.addEventListener('DOMContentLoaded', function() {
  // Set up tab click handlers
  document.getElementById('all-tab').addEventListener('click', function() {
    setActiveTab('all-tab');
    renderPublications(allPublications);
  });
  
  document.getElementById('first-author-tab').addEventListener('click', function() {
    setActiveTab('first-author-tab');
    const firstAuthorPubs = filterFirstAuthorPublications(allPublications);
    renderPublications(firstAuthorPubs);
  });

  loadPublications();
});

function setActiveTab(activeId) {
  document.querySelectorAll('.tab-button').forEach(button => {
    button.classList.remove('active');
  });
  document.getElementById(activeId).classList.add('active');
}

function filterFirstAuthorPublications(publications) {
  return publications.filter(pub => {
    const firstAuthor = pub.authors.split(',')[0].toLowerCase().trim();
    return firstAuthor.includes('yuan');
  });
}

function loadPublications() {
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

  tryLoadPublications(possiblePaths, 0);
}

function tryLoadPublications(paths, index) {
  if (index >= paths.length) {
    var container = document.getElementById('publications-container');
    if (container) {
      container.innerHTML = '<p style="color: red;">Error: Could not load publications data.</p>';
    }
    return;
  }

  var path = paths[index];
  fetch(path)
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      if (data && data.publications) {
        allPublications = data.publications;
        
        // Display summary statistics if available
        if (data.summary_stats) {
          displaySummaryStats(data.summary_stats);
        }
        
        renderPublications(allPublications);
      }
    })
    .catch(() => {
      tryLoadPublications(paths, index + 1);
    });
}

function displaySummaryStats(stats) {
  const statsSection = document.getElementById('publication-summary-text');
  if (!statsSection || !stats) return;
  
  const totalPapers = document.getElementById('total-papers');
  const totalCitations = document.getElementById('total-citations');
  const hIndex = document.getElementById('h-index');
  const i10Index = document.getElementById('i10-index');
  
  if (totalPapers) totalPapers.textContent = stats.total_papers || 0;
  if (totalCitations) totalCitations.textContent = stats.total_citations || 0;
  if (hIndex) hIndex.textContent = stats.h_index || 0;
  if (i10Index) i10Index.textContent = stats.i10_index || 0;
  
  statsSection.style.display = 'block';
}

function renderPublications(publications) {
  var container = document.getElementById('publications-container');
  if (!container) return;

  container.innerHTML = '';

  // Add last updated info if available
  if (publications.length > 0) {
    var lastUpdated = document.createElement('div');
    lastUpdated.className = 'last-updated';
    lastUpdated.textContent = 'Last updated: ' + new Date().toLocaleDateString();
    container.appendChild(lastUpdated);
  }

  var list = document.createElement('div');
  list.className = 'publications-list';

  publications.forEach(function(pub) {
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

    var info = document.createElement('div');
    info.className = 'publication-info';

    var authors = document.createElement('div');
    authors.className = 'publication-authors';
    authors.textContent = pub.authors;
    info.appendChild(authors);

    if (pub.citation_count && pub.citation_count > 0) {
      var citations = document.createElement('span');
      citations.className = 'citation-count';
      citations.textContent = pub.citation_count + ' citations';
      info.appendChild(citations);
    }

    item.appendChild(info);

    var journal = document.createElement('div');
    journal.className = 'publication-journal';
    journal.textContent = pub.journal_info;
    item.appendChild(journal);

    list.appendChild(item);
  });

  if (publications.length === 0) {
    var noResults = document.createElement('p');
    noResults.style.color = '#666';
    noResults.style.fontStyle = 'italic';
    noResults.textContent = 'No publications found.';
    list.appendChild(noResults);
  }

  container.appendChild(list);
}