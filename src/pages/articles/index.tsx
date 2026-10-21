import { FaNewspaper } from "react-icons/fa6";
import { useSearchParams, useNavigate, Link } from "react-router";

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
import { usePageTitle } from "@/hooks/use-pagetitle";
import ArticlesData from "@/data/generated/articles.json";

const validSorts = ["updated", "created"] as const;
type SortByType = (typeof validSorts)[number];

const allTags = Array.from(
  new Set(Object.values(ArticlesData).flatMap((article) => article.tags ?? [])),
).sort();

export default function ArticlesPage() {
  usePageTitle("Articles");

  const [searchParams] = useSearchParams();
  const navigate = useNavigate();

  const tag = searchParams.get("tag");
  const sort = searchParams.get("sort");

  const tagFilter: string = tag && allTags.includes(tag) ? tag : "all";
  const sortBy: SortByType = validSorts.find((s) => s === sort) ?? "updated";

  const updateTagFilter = (newTag: string) => {
    const params = new URLSearchParams(searchParams);
    if (newTag === "all") params.delete("tag");
    else params.set("tag", newTag);
    navigate({ search: params.toString() }, { replace: true });
  };

  const updateSortBy = (newSortBy: SortByType) => {
    const params = new URLSearchParams(searchParams);
    params.set("sort", newSortBy);
    navigate({ search: params.toString() }, { replace: true });
  };

  const filteredArticles = (
    Object.keys(ArticlesData) as (keyof typeof ArticlesData)[]
  )
    .filter((article_name) => {
      const article = ArticlesData[article_name];
      if (article.draft === true) return false;
      const tags = (article.tags ?? []) as string[];
      const matchesTag = tagFilter === "all" || tags.includes(tagFilter);
      return matchesTag;
    })
    .sort((a, b) => {
      const aData = ArticlesData[a];
      const bData = ArticlesData[b];

      if (sortBy === "created") {
        return (
          new Date(bData.created_at).getTime() -
          new Date(aData.created_at).getTime()
        );
      } else {
        return (
          new Date(bData.updated_at).getTime() -
          new Date(aData.updated_at).getTime()
        );
      }
    });

  return (
    <div className="flex flex-1 flex-col items-center gap-10">
      <div className="w-full max-w-6xl space-y-10">
        <div className="flex flex-row justify-center items-center gap-4 text-4xl font-semibold">
          <FaNewspaper />
          Articles
        </div>

        <div className="flex justify-between flex-wrap gap-2 items-center mx-2 sm:mx-6 my-1 relative -top-2">
          <TagFilter tagFilter={tagFilter} setTagFilter={updateTagFilter} />
          <SortSelector sortBy={sortBy} setSortBy={updateSortBy} />
        </div>

        <Separator />

        <div className="grid grid-cols-1 w-full gap-4 px-2 sm:px-6">
          {filteredArticles.map((articleName) => (
            <ArticleCard
              key={articleName}
              articleName={articleName}
              setTagFilter={updateTagFilter}
            />
          ))}
        </div>
      </div>
    </div>
  );
}

function TagFilter({
  tagFilter,
  setTagFilter,
}: {
  tagFilter: string;
  setTagFilter: (val: string) => void;
}) {
  return (
    <div className="flex items-center gap-2">
      <label>Filter by tag:</label>
      <Select value={tagFilter} onValueChange={setTagFilter}>
        <SelectTrigger className="w-[180px] cursor-pointer">
          <SelectValue placeholder="Tag" />
        </SelectTrigger>
        <SelectContent>
          <SelectItem value="all">🏷️ All Tags</SelectItem>
          {allTags.map((tag) => (
            <SelectItem key={tag} value={tag}>
              {tag}
            </SelectItem>
          ))}
        </SelectContent>
      </Select>

      {tagFilter !== "all" && (
        <Button
          variant="ghost"
          size="sm"
          onClick={() => setTagFilter("all")}
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
        </SelectContent>
      </Select>
    </div>
  );
}

function ArticleCard({
  articleName,
  setTagFilter,
}: {
  articleName: keyof typeof ArticlesData;
  setTagFilter: (val: string) => void;
}) {
  const article = ArticlesData[articleName];

  return (
    <Card className="rounded-md overflow-hidden py-4 px-4 sm:px-8">
      <div className="flex flex-col gap-2">
        <Button
          asChild
          variant="link"
          className="p-0 h-7 text-base font-semibold text-left justify-start"
        >
          <Link
            to={`/articles/${articleName}`}
            aria-label={`Read full article: ${article.title}`}
          >
            {article.title}
          </Link>
        </Button>

        <p className="text-sm text-muted-foreground line-clamp-3">
          {article.summary || "No summary available."}
        </p>

        {article.tags && article.tags.length > 0 && (
          <div className="flex flex-wrap gap-1.5 mt-1">
            {article.tags.map((tag: string) => (
              <Button
                key={tag}
                variant="secondary"
                size="sm"
                onClick={() => setTagFilter(tag)}
                className="rounded-sm cursor-pointer font-normal px-2 h-7.5 text-sm"
              >
                {tag}
              </Button>
            ))}
          </div>
        )}

        <div className="flex justify-between items-center text-sm text-muted-foreground mt-auto pt-2">
          <span>
            Published {formatDate(article.created_at)}
            {!isSameDate(article.created_at, article.updated_at) && (
              <> • Updated {formatDate(article.updated_at)}</>
            )}
          </span>
          <Button
            asChild
            variant="link"
            className="p-0 text-primary underline text-sm h-7.5"
          >
            <Link
              to={`/articles/${articleName}`}
              aria-label={`Read full article: ${article.title}`}
            >
              Read More →
            </Link>
          </Button>
        </div>
      </div>
    </Card>
  );
}

function formatDate(dateStr: string) {
  return new Date(dateStr).toLocaleDateString(undefined, {
    year: "numeric",
    month: "short",
    day: "numeric",
  });
}

function isSameDate(date1: string, date2: string): boolean {
  const d1 = new Date(date1);
  const d2 = new Date(date2);
  return (
    d1.getFullYear() === d2.getFullYear() &&
    d1.getMonth() === d2.getMonth() &&
    d1.getDate() === d2.getDate()
  );
}
