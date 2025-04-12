// src/components/MarkdownPage.jsx
import React, { useEffect, useState } from 'react';
import ReactMarkdown from 'react-markdown';
import rehypeRaw from 'rehype-raw';
import rehypeSanitize from 'rehype-sanitize';
import remarkGfm from 'remark-gfm';

export default function MarkdownPage({ filePath }) {
  const [content, setContent] = useState('');
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    setIsLoading(true);
    fetch(filePath)
      .then(response => {
        if (!response.ok) {
          throw new Error(`Failed to load ${filePath}: ${response.status}`);
        }
        return response.text();
      })
      .then(text => {
        setContent(text);
        setIsLoading(false);
      })
      .catch(error => {
        console.error('Error loading markdown:', error);
        setError(error.message);
        setIsLoading(false);
      });
  }, [filePath]);

  if (isLoading) return <div>Loading content...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div className="markdown-content">
      <ReactMarkdown
        rehypePlugins={[rehypeRaw, rehypeSanitize]}
        remarkPlugins={[remarkGfm]}
      >
        {content}
      </ReactMarkdown>
    </div>
  );
}