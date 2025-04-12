// src/pages/Talks.jsx
import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { getMarkdownFiles } from '../utils/MarkdownService.js';

export default function Talks() {
  const [talks, setTalks] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function loadTalks() {
      try {
        const files = await getMarkdownFiles('talks');
        setTalks(files);
      } catch (err) {
        console.error('Error loading talks:', err);
        setError('Failed to load talks. Using demo data instead.');
        // Fallback data
        setTalks([
          {
            id: '2023-10-20-talk',
            title: 'Machine learning and its potential in a data rich space such as MICE',
            date: '2023-10-20',
            venue: 'HUONE Singapore Meeting and Event Venue',
            location: 'Singapore',
            type: 'Talk'
          }
        ]);
      } finally {
        setIsLoading(false);
      }
    }

    loadTalks();
  }, []);

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
      <p>Loading talks...</p>
    </div>
  );

  return (
    <div className="talks-container">
      <div className="page-header">
        <h1 className="page-title">Talks</h1>
      </div>

      {error && <p className="error-message">{error}</p>}

      <div className="talks-list">
        {talks.length > 0 ? (
          talks.map(talk => (
            <div key={talk.id} className="talk publication">
              <h3 className="talk-title publication-title">
                <Link to={`/talk/${talk.id}`}>{talk.title}</Link>
              </h3>
              {talk.date && <p className="talk-date publication-date">Date: {formatDate(talk.date)}</p>}
              {talk.type && <p className="talk-type publication-venue">Type: {talk.type}</p>}
              {talk.venue && <p className="talk-venue publication-venue">Venue: {talk.venue}</p>}
              {talk.location && <p className="talk-location">Location: {talk.location}</p>}
              <div className="talk-links publication-links">
                <Link to={`/talk/${talk.id}`} className="btn btn-sm">View Details</Link>
              </div>
            </div>
          ))
        ) : (
          <p>No talks available at this time.</p>
        )}
      </div>
    </div>
  );
}