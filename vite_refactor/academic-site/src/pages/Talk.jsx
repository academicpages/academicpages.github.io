// src/pages/Talk.jsx
import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import ReactMarkdown from 'react-markdown';
import rehypeRaw from 'rehype-raw';
import rehypeSanitize from 'rehype-sanitize';
import remarkGfm from 'remark-gfm';

export default function Talk() {
  const { id } = useParams();
  const [talk, setTalk] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function fetchTalk() {
      try {
        const response = await fetch(`/content/talks/${id}.md`);
        if (!response.ok) {
          throw new Error(`Failed to load talk: ${response.status}`);
        }

        const text = await response.text();

        // Parse frontmatter
        const frontmatterRegex = /^---\n([\s\S]*?)\n---/;
        const match = text.match(frontmatterRegex);
        const metadata = {};

        if (match) {
          const frontmatter = match[1];

          // Extract key metadata
          const titleMatch = frontmatter.match(/title:\s*["']?(.*?)["']?(\n|$)/);
          const dateMatch = frontmatter.match(/date:\s*["']?(.*?)["']?(\n|$)/);
          const venueMatch = frontmatter.match(/venue:\s*["']?(.*?)["']?(\n|$)/);
          const locationMatch = frontmatter.match(/location:\s*["']?(.*?)["']?(\n|$)/);
          const typeMatch = frontmatter.match(/type:\s*["']?(.*?)["']?(\n|$)/);

          if (titleMatch) metadata.title = titleMatch[1].trim();
          if (dateMatch) metadata.date = dateMatch[1].trim();
          if (venueMatch) metadata.venue = venueMatch[1].trim();
          if (locationMatch) metadata.location = locationMatch[1].trim();
          if (typeMatch) metadata.type = typeMatch[1].trim();
        }

        // Remove frontmatter before setting content
        const contentWithoutFrontmatter = text.replace(frontmatterRegex, '');

        setTalk({
          ...metadata,
          content: contentWithoutFrontmatter
        });
      } catch (err) {
        console.error('Error loading talk:', err);
        setError(err.message);
      } finally {
        setIsLoading(false);
      }
    }

    fetchTalk();
  }, [id]);

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
      <p>Loading talk details...</p>
    </div>
  );

  if (error) return <div className="error-message">Error: {error}</div>;

  if (!talk) return <div>Talk not found</div>;

  return (
    <div className="talk-detail">
      <div className="page-header">
        <h1 className="page-title">{talk.title}</h1>
      </div>

      <div className="talk-meta">
        {talk.date && (
          <p className="talk-date">Date: {formatDate(talk.date)}</p>
        )}
        {talk.type && (
          <p className="talk-type">Type: {talk.type}</p>
        )}
        {talk.venue && (
          <p className="talk-venue">Venue: {talk.venue}</p>
        )}
        {talk.location && (
          <p className="talk-location">Location: {talk.location}</p>
        )}
      </div>

      <div className="talk-content markdown-content">
        <ReactMarkdown
          rehypePlugins={[rehypeRaw, rehypeSanitize]}
          remarkPlugins={[remarkGfm]}
        >
          {talk.content}
        </ReactMarkdown>
      </div>

      <div className="back-link">
        <Link to="/talks">← Back to all talks</Link>
      </div>
    </div>
  );
}