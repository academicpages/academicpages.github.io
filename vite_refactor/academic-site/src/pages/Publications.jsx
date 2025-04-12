// src/pages/Publications.jsx
import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { getMarkdownFiles } from '../utils/MarkdownService';

export default function Publications() {
  const [publications, setPublications] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function loadPublications() {
      try {
        const files = await getMarkdownFiles('publications');
        setPublications(files);
      } catch (err) {
        console.error('Error loading publications:', err);
        setError('Failed to load publications. Using demo data instead.');
        // Fallback data
        setPublications([
          {
            id: '2023-12-05-patent-CN117153334',
            title: 'A deep learning prediction method and device for liver tumor ablation treatment',
            date: '2023-12-05',
            venue: 'Patent CN117153334',
            citation: 'ZHANG LAN; XU XIN; REN ZHENGGANG; CHEN HAIDONG (2023). "A deep learning prediction method and device for liver tumor ablation treatment" <i>Patent CN117153334</i>.'
          }
        ]);
      } finally {
        setIsLoading(false);
      }
    }

    loadPublications();
  }, []);

  // Format date to a more readable format (December 5, 2023)
  const formatDate = (dateString) => {
    if (!dateString) return '';
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'long',
      day: 'numeric'
    });
  };

  if (isLoading) return (
    <div className="loading-container">
      <div className="loading-spinner"></div>
      <p>Loading publications...</p>
    </div>
  );

  return (
    <div className="publications-container">
      <div className="page-header">
        <h1 className="page-title">Publications</h1>
      </div>

      {error && <p className="error-message">{error}</p>}

      <div className="publications-list">
        {publications.length > 0 ? (
          publications.map(pub => (
            <div key={pub.id} className="publication">
              <h3 className="publication-title">
                <Link to={`/publication/${pub.id}`}>{pub.title}</Link>
              </h3>
              <p className="publication-date">Published on: {formatDate(pub.date)}</p>
              {pub.venue && <p className="publication-venue">Venue: {pub.venue}</p>}
              {pub.excerpt && <p className="publication-excerpt">{pub.excerpt}</p>}
              {pub.citation && (
                <p className="publication-citation" dangerouslySetInnerHTML={{ __html: pub.citation }}></p>
              )}
              <div className="publication-links">
                <Link to={`/publication/${pub.id}`} className="btn btn-sm">Read More</Link>
                {pub.paperurl && <a href={pub.paperurl} target="_blank" rel="noopener noreferrer" className="btn btn-sm">Download</a>}
              </div>
            </div>
          ))
        ) : (
          <p>No publications available at this time.</p>
        )}
      </div>
    </div>
  );
}