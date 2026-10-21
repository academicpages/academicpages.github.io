import { useSearchParams, useNavigate } from "react-router";
import { FaWrench, FaGithub, FaGlobe, FaRegStar } from "react-icons/fa6";

import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { Card } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Separator } from "@/components/ui/separator";
import { ScrollArea } from "@/components/ui/scroll-area";
import { usePageTitle } from "@/hooks/use-pagetitle";
import { repos } from "@/data/repos";

const validSorts = ["stars", "updated", "created"] as const;
type SortByType = (typeof validSorts)[number];

const allTopics = Array.from(
  new Set(Object.values(repos).flatMap((repo) => repo.topics ?? [])),
).sort();

export default function ProjectsPage() {
  usePageTitle("Projects");

  const [searchParams] = useSearchParams();
  const navigate = useNavigate();

  const topic = searchParams.get("topic");
  const sort = searchParams.get("sort");

  const topicFilter: string =
    topic && allTopics.includes(topic) ? topic : "all";
  const sortBy: SortByType = validSorts.find((s) => s === sort) ?? "updated";

  const updateTopicFilter = (newTopic: string) => {
    const params = new URLSearchParams(searchParams);
    if (newTopic === "all") params.delete("topic");
    else params.set("topic", newTopic);
    navigate({ search: params.toString() }, { replace: true });
  };

  const updateSortBy = (newSortBy: SortByType) => {
    const params = new URLSearchParams(searchParams);
    params.set("sort", newSortBy);
    navigate({ search: params.toString() }, { replace: true });
  };

  const filteredProjects = (Object.keys(repos) as (keyof typeof repos)[])
    .filter((project_name) => {
      const project = repos[project_name];
      const topics = (project.topics ?? []) as string[];
      const matchesTopic =
        topicFilter === "all" || topics.includes(topicFilter);
      return matchesTopic;
    })
    .sort((a, b) => {
      const aData = repos[a];
      const bData = repos[b];

      if (sortBy === "stars") {
        return (bData.stargazers_count ?? 0) - (aData.stargazers_count ?? 0);
      } else if (sortBy === "created") {
        return (
          new Date(bData.created_at).getTime() -
          new Date(aData.created_at).getTime()
        );
      } else {
        return (
          new Date(bData.pushed_at).getTime() -
          new Date(aData.pushed_at).getTime()
        );
      }
    });

  return (
    <div className="flex flex-1 flex-col items-center gap-10">
      <div className="w-full max-w-6xl space-y-10">
        <div className="flex flex-row justify-center items-center gap-4 text-4xl font-semibold">
          <FaWrench />
          Projects
        </div>

        <div className="flex justify-between flex-wrap gap-2 items-center mx-2 sm:mx-6 my-1 relative -top-2">
          <TopicFilter
            topicFilter={topicFilter}
            setTopicFilter={updateTopicFilter}
          />
          <SortSelector sortBy={sortBy} setSortBy={updateSortBy} />
        </div>

        <Separator />

        <div className="grid grid-cols-1 w-full gap-4 px-2 sm:px-6">
          {filteredProjects.map((projectName) => (
            <ProjectCard
              key={projectName}
              project_name={projectName}
              setTopicFilter={updateTopicFilter}
            />
          ))}
        </div>
      </div>
    </div>
  );
}

function TopicFilter({
  topicFilter,
  setTopicFilter,
}: {
  topicFilter: string;
  setTopicFilter: (val: string) => void;
}) {
  return (
    <div className="flex items-center gap-2">
      <label>Filter by topic:</label>
      <Select value={topicFilter} onValueChange={setTopicFilter}>
        <SelectTrigger className="w-[180px] cursor-pointer">
          <SelectValue placeholder="Topic" />
        </SelectTrigger>
        <SelectContent>
          <SelectItem value="all">📂 All Topics</SelectItem>
          {allTopics.map((topic) => (
            <SelectItem key={topic} value={topic}>
              {topic}
            </SelectItem>
          ))}
        </SelectContent>
      </Select>

      {topicFilter !== "all" && (
        <Button
          variant="ghost"
          size="sm"
          onClick={() => setTopicFilter("all")}
          className="px-2 text-sm cursor-pointer text-muted-foreground"
        >
          Clear filter ✕
        </Button>
      )}
    </div>
  );
}

function SortSelector({
  sortBy,
  setSortBy,
}: {
  sortBy: SortByType;
  setSortBy: (val: SortByType) => void;
}) {
  return (
    <div className="flex items-center gap-2">
      <label>Sort by:</label>
      <Select value={sortBy} onValueChange={setSortBy}>
        <SelectTrigger className="w-[160px] cursor-pointer">
          <SelectValue placeholder="Sort by" />
        </SelectTrigger>
        <SelectContent>
          <SelectItem value="updated">🕒 Last Updated</SelectItem>
          <SelectItem value="created">📅 Created Time</SelectItem>
          <SelectItem value="stars">⭐ Star Count</SelectItem>
        </SelectContent>
      </Select>
    </div>
  );
}

function ProjectCard({
  project_name,
  setTopicFilter,
}: {
  project_name: keyof typeof repos;
  setTopicFilter: (val: string) => void;
}) {
  const repo = repos[project_name];
  const {
    html_url,
    previewImage,
    displayName,
    name,
    description,
    topics = [],
    language,
    stargazers_count,
    homepage,
  } = repo;

  return (
    <Card className="rounded-md overflow-hidden gap-0 py-0 w-full">
      <div className="flex flex-col lg:flex-row">
        <a
          href={html_url}
          target="_blank"
          rel="noopener noreferrer"
          className="block"
        >
          <div className="aspect-3/2 w-full max-h-72 lg:max-w-75 lg:h-50 overflow-hidden">
            {previewImage ? (
              <img
                src={previewImage}
                alt={name || "Project image"}
                className="w-full h-full object-cover"
                loading="lazy"
              />
            ) : (
              <div className="flex flex-col items-center justify-center p-4 w-full h-full bg-muted">
                <span className="text-lg font-semibold opacity-80 text-center">
                  {name || "Unnamed Project"}
                </span>
                <span className="text-sm text-muted-foreground text-center">
                  Image not available
                </span>
              </div>
            )}
          </div>
        </a>

        <div className="w-full border-t block lg:hidden" />
        <div className="h-full border-l hidden lg:block" />

        <div className="flex flex-col p-4 lg:py-2.5 lg:px-5 flex-1 lg:h-50">
          <ScrollArea className="flex-1 min-h-0">
            <div className="flex flex-col gap-y-2">
              <div className="text-base font-semibold">
                {html_url ? (
                  <a
                    href={html_url}
                    target="_blank"
                    rel="noopener noreferrer"
                    aria-label="GitHub repository"
                    className="hover:underline underline-offset-4"
                  >
                    {displayName || name}
                  </a>
                ) : (
                  displayName || name
                )}
              </div>

              <p className="text-sm text-muted-foreground">
                {description || "Details unavailable"}
              </p>

              {topics?.length ? (
                <div className="flex flex-wrap gap-1.5">
                  {topics.map((topic: string) => (
                    <Button
                      key={topic}
                      variant="secondary"
                      size="sm"
                      onClick={() => setTopicFilter(topic)}
                      className="rounded-sm cursor-pointer font-normal px-2 h-7.5 text-sm"
                    >
                      {topic}
                    </Button>
                  ))}
                </div>
              ) : null}
            </div>
          </ScrollArea>

          <div className="flex flex-row items-center justify-between text-muted-foreground pt-2">
            <div className="flex items-center gap-2 text-sm">
              <p>Language: {language || "Unknown"}</p>
              {stargazers_count !== null && (
                <a
                  href={`${html_url}/stargazers`}
                  target="_blank"
                  rel="noopener noreferrer"
                  aria-label="Stargazers"
                  className="flex items-center gap-1 text-yellow-600 hover:text-yellow-500"
                >
                  <FaRegStar className="w-4 h-4" />
                  <span>{stargazers_count}</span>
                </a>
              )}
            </div>

            <div className="flex items-center gap-2">
              {homepage && (
                <a
                  href={homepage}
                  target="_blank"
                  rel="noopener noreferrer"
                  aria-label="Project homepage"
                  className="hover:text-foreground"
                >
                  <FaGlobe className="w-6 h-6" />
                </a>
              )}
              {html_url && (
                <a
                  href={html_url}
                  target="_blank"
                  rel="noopener noreferrer"
                  aria-label="GitHub repository"
                  className="hover:text-foreground"
                >
                  <FaGithub className="w-6 h-6" />
                </a>
              )}
            </div>
          </div>
        </div>
      </div>
    </Card>
  );
}
