# mattguida.github.io

Source for [mattguida.github.io](https://mattguida.github.io), built with [Showlit](https://github.com/pm25/showlit) (React + Vite + TypeScript + Tailwind + shadcn/ui).

## Local development

```bash
npm install
npm run dev      # http://localhost:5173
npm run build    # production build to dist/
npm run lint
```

Content lives in `config/*.yaml` (profile, publications, projects, sidebar, homepage layout) and `public/articles/{slug}/{slug}.md` (long-form writeups).

## Deployment

A GitHub Actions workflow (`.github/workflows/ci.yaml`) builds the site on every push to `master` and publishes `dist/` to the `gh-pages` branch. GitHub Pages is configured to serve from that branch.

## Previous Jekyll site

This site was previously built with Jekyll (the [academicpages](https://academicpages.github.io/) theme). That version is preserved on the [`legacy-jekyll-site`](https://github.com/mattguida/mattguida.github.io/tree/legacy-jekyll-site) branch and tagged [`backup-pre-showlit`](https://github.com/mattguida/mattguida.github.io/releases/tag/backup-pre-showlit), in case of rollback.
