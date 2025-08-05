// Global variables to store publication data
let allPublications = [];
let currentView = 'all'; // 'all' or 'first-author'

// Load and display publications with summary statistics
document.addEventListener('DOMContentLoaded', function() {
    loadPublications();
    setupTabListeners();
});

function loadPublications() {
    fetch('/assets/js/publications.json')
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            // Store all publications globally
            allPublications = data.publications || [];
            
            // Display summary statistics
            displaySummaryStats(data.summary_stats);
            
            // Display publications based on current view
            updatePublicationDisplay();
        })
        .catch(error => {
            console.error('Error loading publications:', error);
            displayError();
        });
}

function displaySummaryStats(stats) {
    if (!stats) return;
    
    const statsSection = document.getElementById('publication-stats');
    
    document.getElementById('total-papers').textContent = stats.total_papers || 0;
    document.getElementById('total-citations').textContent = stats.total_citations || 0;
    document.getElementById('h-index').textContent = stats.h_index || 0;
    document.getElementById('i10-index').textContent = stats.i10_index || 0;
    document.getElementById('first-author-count').textContent = stats.first_author_papers || 0;
    document.getElementById('avg-citations').textContent = stats.avg_citations_per_paper || 0;
    document.getElementById('last-updated').textContent = stats.last_updated || 'Unknown';
    
    statsSection.style.display = 'block';
}

function setupTabListeners() {
    const allTab = document.getElementById('all-tab');
    const firstAuthorTab = document.getElementById('first-author-tab');
    
    if (allTab) {
        allTab.addEventListener('click', function() {
            currentView = 'all';
            allTab.classList.add('active');
            firstAuthorTab.classList.remove('active');
            updatePublicationDisplay();
        });
    }
    
    if (firstAuthorTab) {
        firstAuthorTab.addEventListener('click', function() {
            currentView = 'first-author';
            firstAuthorTab.classList.add('active');
            allTab.classList.remove('active');
            updatePublicationDisplay();
        });
    }
}

function updatePublicationDisplay() {
    let publicationsToShow = allPublications;
    
    // Filter for first author if needed
    if (currentView === 'first-author') {
        publicationsToShow = allPublications.filter(pub => pub.is_first_author === true);
    }
    
    displayPublications(publicationsToShow);
}

function displayPublications(publications) {
    const container = document.getElementById('publications-container');
    
    if (!publications || publications.length === 0) {
        container.innerHTML = currentView === 'first-author' 
            ? '<p>No first-author publications found.</p>'
            : '<p>No publications found.</p>';
        return;
    }
    
    let html = '<div class="publications-list">';
    
    publications.forEach((pub, index) => {
        const firstAuthorBadge = pub.is_first_author ? '<span class="first-author-badge">First Author</span>' : '';
        
        html += `
            <div class="publication-item">
                <h3 class="publication-title">
                    ${pub.title || 'Untitled'}
                    ${firstAuthorBadge}
                </h3>
                <p class="publication-authors">${pub.authors || 'No authors listed'}</p>
                <p class="publication-venue">${pub.journal_info || 'No venue information'}</p>
                <div class="publication-metrics">
                    ${pub.citation_count ? `<span class="metric">Citations: ${pub.citation_count}</span>` : ''}
                    ${pub.read_count ? `<span class="metric">Reads: ${pub.read_count}</span>` : ''}
                </div>
                <div class="publication-links">
                    ${pub.ads_link ? `<a href="${pub.ads_link}" target="_blank" class="btn btn-small">ADS</a>` : ''}
                    ${pub.arxiv_link ? `<a href="${pub.arxiv_link}" target="_blank" class="btn btn-small">arXiv</a>` : ''}
                </div>
            </div>
        `;
    });
    
    html += '</div>';
    container.innerHTML = html;
}

function displayError() {
    const container = document.getElementById('publications-container');
    container.innerHTML = `
        <div class="error-message">
            <p><strong>Unable to load publications.</strong></p>
            <p>Please try refreshing the page or visit my <a href="https://ui.adsabs.harvard.edu/search/q=orcid%3A0000-0002-5992-7586&sort=date%20desc%2C%20bibcode%20desc&p_=0" target="_blank">ADS profile</a> directly.</p>
        </div>
    `;
}