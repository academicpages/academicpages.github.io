import { useEffect } from "react";

import site from "@/data/generated/site.json";

export function usePageTitle(title: string) {
  useEffect(() => {
    document.title = `${title} - ${site.name}`;
  }, [title]);
}
