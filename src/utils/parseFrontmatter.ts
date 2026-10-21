import yaml from "js-yaml";

export interface FrontMatter {
  title?: string;
  created_at?: string;
  updated_at?: string;
  summary?: string;
  cover_image?: string;
  author?: string;
  draft?: boolean;
}

export function parseFrontmatter(content: string): {
  attributes: FrontMatter;
  body: string;
} {
  const match = /^---\n([\s\S]*?)\n---\n?/.exec(content);

  if (!match) return { attributes: {}, body: content };

  const yamlBlock = match[1];
  const body = content.slice(match[0].length);

  let attributes: FrontMatter = {};
  try {
    attributes = yaml.load(yamlBlock) as FrontMatter;
  } catch (err) {
    console.error("Failed to parse YAML frontmatter:", err);
  }

  return { attributes, body };
}
