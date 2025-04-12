// src/pages/Publication.jsx
import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import ReactMarkdown from 'react-markdown';
import rehypeRaw from 'rehype-raw';
import rehypeSanitize from 'rehype-sanitize';
import remarkGfm from 'remark-gfm';

export default function Publication() {
  const { id } = useParams();
  const [publication, setPublication] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function fetchPublication() {
      try {
        const response = await fetch(`/content/publications/${id}.md`);
        if (!response.ok) {
          throw new Error(`Failed to load publication: ${response.status}`);
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
          const citationMatch = frontmatter.match(/citation:\s*["']?(.*?)["']?(\n|$)/);
          const paperurlMatch = frontmatter.match(/paperurl:\s*["']?(.*?)["']?(\n|$)/);

          if (titleMatch) metadata.title = titleMatch[1].trim();
          if (dateMatch) metadata.date = dateMatch[1].trim();
          if (venueMatch) metadata.venue = venueMatch[1].trim();
          if (citationMatch) metadata.citation = citationMatch[1].trim();
          if (paperurlMatch) metadata.paperurl = paperurlMatch[1].trim();
        }

        // Remove frontmatter before setting content
        const contentWithoutFrontmatter = text.replace(frontmatterRegex, '');

        setPublication({
          ...metadata,
          content: contentWithoutFrontmatter
        });
      } catch (err) {
        console.error('Error loading publication:', err);
        setError(err.message);
      } finally {
        setIsLoading(false);
      }
    }

    fetchPublication();
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
      <p>Loading publication...</p>
    </div>
  );

  if (error) return <div className="error-message">Error: {error}</div>;

  if (!publication) return <div>Publication not found</div>;

  return (
    <div className="publication-detail">
      <div className="page-header">
        <h1 className="page-title">{publication.title}</h1>
      </div>

      <div className="publication-meta">
        {publication.date && (
          <p className="publication-date">Published on: {formatDate(publication.date)}</p>
        )}
        {publication.venue && (
          <p className="publication-venue">Venue: {publication.venue}</p>
        )}
        {publication.citation && (
          <div className="publication-citation" dangerouslySetInnerHTML={{ __html: publication.citation }}></div>
        )}
        {publication.paperurl && (
          <div className="publication-links">
            <a href={publication.paperurl} target="_blank" rel="noopener noreferrer" className="btn btn-sm">
              Download Paper
            </a>
          </div>
        )}
      </div>

      <div className="publication-content markdown-content">
        <ReactMarkdown
          rehypePlugins={[rehypeRaw, rehypeSanitize]}
          remarkPlugins={[remarkGfm]}
        >
          {publication.content}
        </ReactMarkdown>
      </div>

      <div className="back-link">
        <Link to="/publications">← Back to all publications</Link>
      </div>
    </div>
  );
}