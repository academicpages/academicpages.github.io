// Publications loader script

document.addEventListener('DOMContentLoaded', function() {
  loadPublications();
});

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
        renderPublications(data.publications);
      }
    })
    .catch(() => {
      tryLoadPublications(paths, index + 1);
    });
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

    var authors = document.createElement('div');
    authors.className = 'publication-authors';
    authors.textContent = pub.authors;
    item.appendChild(authors);

    var journal = document.createElement('div');
    journal.className = 'publication-journal';
    journal.textContent = pub.journal_info;
    item.appendChild(journal);

    list.appendChild(item);
  });

  container.appendChild(list);
} 