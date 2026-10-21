export interface RepoProps {
  name: string;
  html_url: string;
  description: string | null;
  topics: string[] | null;
  language: string | null;
  stargazers_count: number | null;
  homepage: string | null;
  created_at: string;
  pushed_at: string;
  displayName: string | null;
  previewImage: string | null;
  featured: boolean;
}
