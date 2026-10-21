export const publicBase = import.meta.env.BASE_URL + "articles";

export function resolveRelativePaths(content: string, slug: string) {
  const basePath = publicBase + `/${slug}`;

  return (
    content
      // markdown links
      .replace(/(\]|\))\(\.\/([^)\s]+)\)/g, (_match, prefix, file) => `${prefix}(${basePath}/${file})`)
      // HTML attributes: src/href"
      .replace(/(src|href)=["']\.\/([^"']+)["']/g, (_match, attr, file) => `${attr}="${basePath}/${file}"`)
  );
}
