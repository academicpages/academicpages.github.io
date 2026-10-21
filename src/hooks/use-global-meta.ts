import { useEffect } from "react";

import site from "@/data/generated/site.json";

export function useGlobalMeta() {
  useEffect(() => {
    document.title = site.name;

    const descriptionMeta = document.querySelector('meta[name="description"]');
    if (descriptionMeta) {
      descriptionMeta.setAttribute("content", site.description || "");
    }

    const authorMeta = document.querySelector('meta[name="author"]');
    if (authorMeta) {
      authorMeta.setAttribute("content", site.author || "");
    }
  }, []);
}
