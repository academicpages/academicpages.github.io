// src/components/MarkdownPage.jsx
import React, { useEffect, useState, useRef } from 'react';
import ReactMarkdown from 'react-markdown';
import rehypeRaw from 'rehype-raw';
import rehypeSanitize from 'rehype-sanitize';
import remarkGfm from 'remark-gfm';
import { useLocation } from 'react-router-dom';

export default function MarkdownPage({ filePath }) {
  const [content, setContent] = useState('');
  const [parsedSections, setParsedSections] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);
  const [pageTitle, setPageTitle] = useState('');
  const contentRef = useRef(null);
  const location = useLocation();

  const isAboutPage = filePath.includes('about.md');
  const isResearchPage = filePath.includes('research.md');
  const useStyledFormat = isAboutPage || isResearchPage;

  useEffect(() => {
    async function fetchContent() {
      try {
        const response = await fetch(filePath);
        if (!response.ok) {
          throw new Error(`Failed to load content: ${response.status}`);
        }

        let text = await response.text();

        // Extract frontmatter
        const frontmatterRegex = /^---\n([\s\S]*?)\n---/;
        const match = text.match(frontmatterRegex);

        // Extract title from frontmatter if available
        if (match) {
          const frontmatter = match[1];
          const titleMatch = frontmatter.match(/title:\s*["']?(.*?)["']?(\n|$)/);
          if (titleMatch) {
            setPageTitle(titleMatch[1].trim());
          }

          // Remove frontmatter before displaying content
          text = text.replace(frontmatterRegex, '');
        }

        setContent(text);

        // Parse content into sections if using styled format
        if (useStyledFormat) {
          parseIntoStyledSections(text);
        }
      } catch (err) {
        console.error('Error loading markdown:', err);
        setError(err.message);
      } finally {
        setIsLoading(false);
      }
    }

    fetchContent();
    window.scrollTo(0, 0);
  }, [filePath, useStyledFormat]);

  // Parse content into sections for styled rendering
  const parseIntoStyledSections = (text) => {
    const sections = [];

    // Extract intro section (everything before first heading)
    const firstHeadingMatch = text.match(/(?:^|\n)# [^\n]+/);
    let intro = '';
    let rest = text;

    if (firstHeadingMatch) {
      const splitIndex = firstHeadingMatch.index;
      intro = text.substring(0, splitIndex).trim();
      rest = text.substring(splitIndex);
    } else {
      intro = text;
      rest = '';
    }

    // Add intro section as bio-section
    if (intro) {
      sections.push({
        type: 'bio-section',
        content: intro
      });
    }

    // Split remaining content by headings
    const headingSections = rest.split(/(?:^|\n)# [^\n]+/);
    const headingTitles = rest.match(/(?:^|\n)# [^\n]+/g) || [];

    // Add each section with its heading, alternating between styles
    headingTitles.forEach((heading, index) => {
      const content = headingSections[index + 1];

      if (content && content.trim()) {
        const sectionType = index % 2 === 0 ? 'news-section' : 'achievements-section';

        sections.push({
          type: sectionType,
          title: heading.replace(/^(?:\n)?# /, ''),
          content: content.trim()
        });
      }
    });

    setParsedSections(sections);
  };

  if (isLoading) return (
      <div className="loading-container">
        <div className="loading-spinner"></div>
        <p>Loading content...</p>
      </div>
  );

  if (error) return <div className="error-message">Error: {error}</div>;

  // Render with Home.jsx-like styling for about/research pages
  if (useStyledFormat) {
    return (
        <div ref={contentRef} className="home-container">
          {pageTitle && (
              <div className="page-header">
                <h1 className="page-title">{pageTitle}</h1>
              </div>
          )}

          {parsedSections.map((section, index) => {
            if (section.type === 'bio-section') {
              return (
                  <section key={index} className="bio-section">
                    <ReactMarkdown
                        rehypePlugins={[rehypeRaw, rehypeSanitize]}
                        remarkPlugins={[remarkGfm]}
                    >
                      {section.content}
                    </ReactMarkdown>
                  </section>
              );
            } else {
              return (
                  <section key={index} className={section.type}>
                    <h2>{section.title}</h2>
                    <ReactMarkdown
                        rehypePlugins={[rehypeRaw, rehypeSanitize]}
                        remarkPlugins={[remarkGfm]}
                    >
                      {section.content}
                    </ReactMarkdown>
                  </section>
              );
            }
          })}
        </div>
    );
  }

  // For non-styled pages, render as normal markdown with title
  return (
      <div>
        {pageTitle && (
            <div className="page-header">
              <h1 className="page-title">{pageTitle}</h1>
            </div>
        )}
        <div ref={contentRef} className="markdown-content">
          <ReactMarkdown
              rehypePlugins={[rehypeRaw, rehypeSanitize]}
              remarkPlugins={[remarkGfm]}
          >
            {content}
          </ReactMarkdown>
        </div>
      </div>
  );
}