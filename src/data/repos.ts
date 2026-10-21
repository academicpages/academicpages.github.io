import reposImport from "@/data/generated/repos.json";
import type { RepoProps } from "@/types/repo";

type RepoMap = Record<string, RepoProps>;
export const repos = reposImport as RepoMap;

export const featuredRepos: RepoMap = Object.fromEntries(
  Object.entries(repos).filter(([, repo]) => repo.featured === true),
);

export const featuredReposArray: RepoProps[] = Object.values(featuredRepos);
