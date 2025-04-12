// src/utils/MarkdownService.js
export async function getMarkdownFiles(directory) {
  try {
    // Get directory listing
    const files = await scanDirectory(directory);
    const markdownFiles = [];

    // Process each file to extract frontmatter
    for (const filename of files) {
      try {
        const response = await fetch(`/content/${directory}/${filename}`);
        if (!response.ok) {
          throw new Error(`Failed to fetch ${filename}: ${response.status}`);
        }

        const markdown = await response.text();
        const metadata = extractFrontmatter(markdown);

        // Generate ID from filename (remove extension)
        const id = filename.replace(/\.md$/, '');

        markdownFiles.push({
          id,
          ...metadata,
          filename
        });
      } catch (error) {
        console.error(`Error processing file ${filename}:`, error);
      }
    }

    // Sort by date (newest first)
    return markdownFiles.sort((a, b) => new Date(b.date) - new Date(a.date));
  } catch (error) {
    console.error(`Error loading markdown files from ${directory}:`, error);
    throw error;
  }
}

async function scanDirectory(directory) {
  try {
    // In development, use the API endpoint
    const response = await fetch(`/api/list-files/${directory}`);
    if (!response.ok) {
      throw new Error(`Failed to list files in ${directory}`);
    }

    const data = await response.json();
    return data.files || [];
  } catch (error) {
    console.error(`Error scanning directory ${directory}:`, error);

    // Fallback to hardcoded files if the API fails
    if (directory === 'publications') {
      return [
        '2023-12-05-patent-CN117153334.md',
        '2023-12-05-GxP-Cloud-Adoption-Guidelines-Whitepaper.md'
      ];
    } else if (directory === 'talks') {
      return [
        '2023-10-20-talk.md',
        '2023-10-12-talk.md'
      ];
    }

    return [];
  }
}

function extractFrontmatter(markdown) {
  const frontmatterRegex = /^---\n([\s\S]*?)\n---/;
  const match = markdown.match(frontmatterRegex);

  if (!match) return {};

  const frontmatter = match[1];
  const metadata = {};

  // Extract each field from the frontmatter
  const lines = frontmatter.split('\n');
  for (const line of lines) {
    const colonIndex = line.indexOf(':');
    if (colonIndex === -1) continue;

    const key = line.slice(0, colonIndex).trim();
    let value = line.slice(colonIndex + 1).trim();

    // Remove quotes if present
    if ((value.startsWith("'") && value.endsWith("'")) ||
        (value.startsWith('"') && value.endsWith('"'))) {
      value = value.slice(1, -1);
    }

    metadata[key] = value;
  }

  // Extract excerpt from the content if not in frontmatter
  if (!metadata.excerpt) {
    const contentWithoutFrontmatter = markdown.replace(frontmatterRegex, '').trim();
    const firstParagraph = contentWithoutFrontmatter.split('\n\n')[0];
    metadata.excerpt = firstParagraph.slice(0, 150) + (firstParagraph.length > 150 ? '...' : '');
  }

  return metadata;
}