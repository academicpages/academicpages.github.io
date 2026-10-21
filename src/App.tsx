import { HashRouter as Router, Routes, Route } from "react-router";

import Layout from "@/layout";
import { loadLazy } from "@/lib/loadComponent";
import { ThemeProvider } from "@/components/theme-provider";
import { ScrollToTop } from "@/hooks/scroll-to-top";
import { useGlobalMeta } from "./hooks/use-global-meta";

const HomePage = loadLazy(() => import("@/pages/home"));
const ProjectsPage = loadLazy(() => import("@/pages/projects"));
const PublicationsPage = loadLazy(() => import("@/pages/publications"));
const ArticlesPage = loadLazy(() => import("@/pages/articles"));
const ArticlePage = loadLazy(() => import("@/pages/articles/page"));
const NotFoundPage = loadLazy(() => import("@/pages/notfound"));

export default function App() {
  useGlobalMeta();

  return (
    <ThemeProvider defaultTheme="dark" storageKey="vite-ui-theme">
      <Router>
        <ScrollToTop />
        <Routes>
          <Route path="/" element={<Layout />}>
            <Route index element={<HomePage />} />
            <Route path="projects" element={<ProjectsPage />} />
            <Route path="publications" element={<PublicationsPage />} />
            <Route path="articles" element={<ArticlesPage />} />
            <Route path="/articles/:slug" element={<ArticlePage />} />
            <Route path="*" element={<NotFoundPage />} />
          </Route>
        </Routes>
      </Router>
    </ThemeProvider>
  );
}
