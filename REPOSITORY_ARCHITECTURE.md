# 🏗️ Repository Architecture Report

> **Project:** [`simoouahbi/eco-academicpages.github.io`](https://github.com/simoouahbi/eco-academicpages.github.io)
>
> **Foundation:** [`academicpages/academicpages.github.io`](https://github.com/academicpages/academicpages.github.io)

This report explains the repository architecture only. Developer identity is documented in [`simoouahbi.md`](./simoouahbi.md), and the implementation history is documented in [`REPORT-CHANGES.md`](./REPORT-CHANGES.md).

---

## 🧱 01 — Project Type

This is a Jekyll-generated static personal and academic website based on Academic Pages and the Minimal Mistakes theme.

It is not a React, Vue, Angular, or Next.js application.

- 🧾 **Data:** YAML and front matter
- 📝 **Content:** Markdown and HTML
- 🧩 **Templates:** Liquid
- 🎨 **Styles:** Sass/SCSS
- ⚙️ **Behavior:** Browser JavaScript
- 🏗️ **Build:** Jekyll
- 🐳 **Local environment:** Docker
- 🌐 **Deployment:** GitHub Pages

The browser receives generated HTML, CSS, JavaScript, images, fonts, PDFs, and JSON/XML data files.

---

## 🔄 02 — How a Page Is Generated

```text
_config.yml + _data/*.yml + Markdown/HTML front matter
                         |
                         v
              Jekyll + Liquid + Plugins
                         |
          ┌──────────────┼──────────────┐
          v              v              v
      _layouts/      _includes/      assets/
          │              │              │
          └──────────────┼──────────────┘
                         v
                  Generated HTML/CSS/JS
                         |
                         v
                       _site/
                         |
         ┌───────────────┴───────────────┐
         v                               v
   Local preview                  GitHub Pages
 http://localhost:4000        GitHub Actions
```

---

## 🗂️ 03 — Data and Content Locations

| Category | Location | Purpose |
| --- | --- | --- |
| 🌐 Site configuration | `_config.yml` | Title, URL, author, repository, plugins, theme, collections |
| 👥 Author profiles | `_data/authors.yml` | Named author records |
| 🧭 Header navigation | `_data/navigation.yml` | Header labels and URLs |
| 🌍 Interface labels | `_data/ui-text.yml` | Localized UI strings |
| 💬 Static comments | `_data/comments/` | YAML comment records |
| 🏠 Homepage | `_pages/about.md` | Main `/` page |
| 📄 Standalone pages | `_pages/` | CV, archives, guide, sitemap, terms, and utility pages |
| 📚 Publications | `_publications/` | Publication Markdown records |
| 🎤 Talks | `_talks/` | Talk and tutorial records |
| 🎓 Teaching | `_teaching/` | Course records |
| 🧰 Portfolio | `_portfolio/` | Portfolio projects |
| ✍️ Blog posts | `_posts/` | Dated blog articles |
| 📑 Downloads | `files/` | PDFs and BibTeX |
| 🖼️ Images | `images/` | Avatar, favicon, social, and example images |
| 🧪 Content generators | `markdown_generator/` | CSV/TSV and Python/notebook generators |
| 🗺️ Talk map | `talkmap.py`, `talkmap.ipynb`, `talkmap/` | Talk-location processing and Leaflet display |

---

## 🧩 04 — Layout and Component Map

### Layout hierarchy

```text
_layouts/default.html
├── _includes/head.html
├── _includes/masthead.html
├── #main
│   ├── _includes/sidebar.html
│   │   └── _includes/author-profile.html
│   └── Article or archive content
├── _includes/footer.html
└── _includes/scripts.html
```

| Layout | Responsibility |
| --- | --- |
| `_layouts/default.html` | Outer document shell |
| `_layouts/compress.html` | Minifies generated HTML |
| `_layouts/single.html` | Individual content pages and articles |
| `_layouts/archive.html` | Collection indexes |
| `_layouts/archive-taxonomy.html` | Category/tag archives |
| `_layouts/splash.html` | Landing/splash pages |
| `_layouts/talk.html` | Talk detail pages |

### Important reusable components

| Include | Responsibility |
| --- | --- |
| `_includes/masthead.html` | Header, title, navigation, theme, avatar |
| `_includes/sidebar.html` | Sidebar wrapper |
| `_includes/author-profile.html` | Author name, bio, avatar, location, social links |
| `_includes/footer.html` | Follow links and copyright |
| `_includes/head.html` | Metadata, CSS, favicon |
| `_includes/seo.html` | SEO and structured data |
| `_includes/scripts.html` | JavaScript loading |
| `_includes/archive-single.html` | Publication card |
| `_includes/archive-single-talk.html` | Talk card |
| `_includes/archive-pages.html` | Archive page helpers |

---

## 🎨 05 — Frontend and Responsive Behavior

### Header

- Fixed at the top
- Full viewport width
- 40px high
- 240 × 38px site-title element
- 43 × 38px theme control
- 46 × 38px menu control
- 38 × 38px mobile avatar area

Header markup: `_includes/masthead.html`

Header styles: `_sass/layout/_masthead.scss`, `_sass/layout/_navigation.scss`

### Footer

- Fixed at the bottom
- Full viewport width
- 40px high
- One-line content
- Compact below 900px
- Follow links hidden below 800px

Footer markup: `_includes/footer.html`

Footer styles: `_sass/layout/_footer.scss`

### Main content

`#main` occupies the viewport area between the 40px header and 40px footer and scrolls internally.

Page styles: `_sass/layout/_page.scss`

### Sidebar

| Width | Behavior |
| --- | --- |
| `≥ 1024px` | Fixed sidebar |
| `925px–1023px` | Sticky sidebar |
| `769px–924px` | Flowing above content |
| `≤ 768px` | Hidden |

Sidebar styles: `_sass/layout/_sidebar.scss`

At 768px and below, the profile avatar moves into the masthead and the sidebar is hidden.

---

## 🔧 06 — Styles and JavaScript

### Styles

| Location | Purpose |
| --- | --- |
| `assets/css/main.scss` | Main Sass entry |
| `assets/css/fontawesome.scss` | Font Awesome entry |
| `_sass/_themes.scss` | Theme selection |
| `_sass/layout/` | Page shell layout |
| `_sass/include/` | Mixins and utilities |
| `_sass/theme/` | Theme palettes |
| `_sass/vendor/` | Bundled Breakpoint, Font Awesome, and Susy |

Jekyll compiles source Sass into `assets/css/main.css`.

### JavaScript

| Location | Purpose |
| --- | --- |
| `assets/js/_main.js` | Main browser behavior |
| `assets/js/theme.js` | Theme switching |
| `assets/js/plugins/jquery.greedy-navigation.js` | Responsive menu behavior |
| `assets/js/main.min.js` | Generated bundle |

`assets/js/main.min.js` is generated and ignored or excluded from source changes. Readable source is maintained in `assets/js/`.

---

## 🐳 07 — Docker and Jekyll Environment

| File | Purpose |
| --- | --- |
| `Dockerfile` | Ruby/Jekyll container environment |
| `docker-compose.yaml` | Container service and port 4000 |
| `_config_docker.yml` | Docker URL configuration |
| `.devcontainer/devcontainer.json` | VS Code dev container |
| `Gemfile` | Ruby dependencies |
| `package.json` | JavaScript scripts |

### Start locally

```powershell
docker compose up -d --build
docker compose exec -d jekyll-site bundle exec jekyll serve -H 0.0.0.0 -w --config _config.yml,_config_docker.yml
```

Open:

- `http://localhost:4000/`
- `http://127.0.0.1:4000/`

Stop:

```powershell
docker compose down
```

---

## 🚀 08 — Build and Deployment

GitHub Actions deploys the site through `.github/workflows/jekyll.yml` when changes are pushed to `master`.

Deployment flow:

```text
Source Markdown/YAML/Liquid/SCSS/JS
                |
                v
      Jekyll build in Actions
                |
                v
        Generated static HTML
                |
                v
       GitHub Pages hosting
```

Generated `_site/` and `.jekyll-cache/` directories are build output, not primary source.

---

## 📂 09 — Repository Folder Guide

### Root

- `.gitignore`
- `AGENTS.md`
- `README.md`
- `LICENSE`
- `Gemfile`
- `Gemfile.lock`
- `_config.yml`
- `_config_docker.yml`
- `Dockerfile`
- `docker-compose.yaml`
- `package.json`
- `talkmap.py`
- `talkmap.ipynb`
- `talkmap_out.ipynb`

### Main source folders

- `.devcontainer/`
- `.github/`
- `_data/`
- `_drafts/`
- `_includes/`
- `_layouts/`
- `_pages/`
- `_posts/`
- `_publications/`
- `_talks/`
- `_teaching/`
- `_portfolio/`
- `_sass/`
- `assets/`
- `images/`
- `files/`
- `markdown_generator/`
- `scripts/`
- `talkmap/`

---

## 📄 10 — Complete Project File Inventory

```text
C:\.
|   .gitignore
|   AGENTS.md
|   docker-compose.yaml
|   Dockerfile
|   Gemfile
|   Gemfile.lock
|   LICENSE
|   package.json
|   README.md
|   REPOSITORY_ARCHITECTURE.md
|   REPORT-CHANGES.md
|   simoouahbi.md
|   talkmap.ipynb
|   talkmap.py
|   talkmap_out.ipynb
|   _config.yml
|   _config_docker.yml
|
+---.devcontainer
|       devcontainer.json
|
+---.github
|   |   CONTRIBUTING.md
|   |   PULL_REQUEST_TEMPLATE.md
|   |
|   +---ISSUE_TEMPLATE
|   |       bug_report.md
|   |       config.yml
|   |
|   \---workflows
|           bad-pr.yml
|           close-llm-run.yml
|           jekyll.yml
|           lock-closed-cron.yml
|           scrape_talks.yml
|
+---assets
|   +---css
|   |       academicons.css
|   |       academicons.min.css
|   |       fontawesome.scss
|   |       main.scss
|   +---fonts
|   |       academicons.eot
|   |       academicons.svg
|   |       academicons.ttf
|   |       academicons.woff
|   +---js
|   |   |   _main.js
|   |   |   theme.js
|   |   \---plugins
|   |           jquery.greedy-navigation.js
|   \---webfonts
|           fa-brands-400.ttf
|           fa-brands-400.woff2
|           fa-regular-400.ttf
|           fa-regular-400.woff2
|           fa-solid-900.ttf
|           fa-solid-900.woff2
|
+---images
+---files
+---markdown_generator
+---scripts
+---talkmap
|   +---leaflet_dist
+---_data
|   \---comments
+---_drafts
+---_includes
|   +---analytics-providers
|   +---comments-providers
|   +---components
|   +---footer
|   \---head
+---_layouts
+---_pages
+---_posts
+---_publications
+---_talks
+---_teaching
```
