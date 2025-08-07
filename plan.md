## Research Highlights: Implementation Plan

### Objective
Create a “Research highlights” section that turns a small set of your selected first‑author papers and GitHub repos into concise, visual highlights (1–2 key figures and a short summary), with a manual vetting step before publication. Keep changes minimal and compatible with the current Jekyll site.

### Deliverables
- New site section reachable via top navigation: `Research highlights` → `/research-highlights/`.
- New Jekyll collection: `/_highlights` (published items) with a listing page.
- Generator CLI that ingests inputs (paper PDFs, arXiv/DOI, repo URLs), extracts 1–2 figures, drafts a short summary, and outputs Markdown drafts plus assets.
- Draft workflow: generate to `/_drafts/` with assets in `images/highlights/<slug>/`; after manual approval, move to `/_highlights/`.

---

### Step 0 — Prerequisites and configuration
Tasks
- Ensure local environment works (Ruby/Jekyll already present in this repo).
- Python 3.9+ environment for generator (virtualenv or conda).
- Install figure extraction tool:
  - Preferred: `pdffigures2` (requires Java and sbt; robust figure + caption extraction).
  - Fallback: Python `PyMuPDF` rasterization + heuristics (less accurate).
- API access:
  - ADS API token (for astro metadata + citation counts).
  - GitHub token (read public repos to avoid rate limits).
- Secrets: store tokens in environment variables (e.g., `ADS_TOKEN`, `GITHUB_TOKEN`).

Acceptance
- `bundler` builds site; Python env created; `pdffigures2` runs on a sample PDF; tokens available via env.

---

### Step 1 — Site wiring (minimal Jekyll changes)
Tasks
- Add a new collection in `_config.yml`:
  - `collections: highlights: { output: true, permalink: /highlights/:name/ }`
  - Defaults: `layout: single`, `author_profile: true` for `highlights`.
- Create listing page `/_pages/research-highlights.html` that lists items from the `highlights` collection (reuse `archive` layout or a minimal custom block).
- Add nav item in `/_data/navigation.yml` pointing to `/research-highlights/`.

Acceptance
- Local build shows a new “Research highlights” tab in masthead.
- Navigating to `/research-highlights/` renders an empty listing without errors.

---

### Step 2 — Input specification
Tasks
- Create `markdown_generator/highlights.yml` (or `.tsv`) that you will curate. Proposed YAML schema:

```yaml
items:
  - id: desi-voids-2023
    type: paper            # paper | repo
    title: "Title here"
    arxiv: 2301.01234      # optional if doi provided
    doi: 10.1234/xyz.2023  # optional
    pdf: files/paper1.pdf  # optional override; else inferred from arXiv/doi
    preferred_figures:     # optional hints
      - page: 5
      - page: 7
    tags: [large-scale-structure, desi]
  - id: repo-forecast-lib
    type: repo
    github: https://github.com/<owner>/<repo>
    preferred_images:      # optional hints (paths in README)
      - docs/figure1.png
    tags: [forecasting, pipeline]
```

Acceptance
- File loads; schema validated by the generator (basic checks).

---

### Step 3 — Paper ingestion and drafting
Tasks
- For each `type: paper`:
  1. Resolve metadata via ADS (title, authors, venue, year, citation count, stable links). Fallback to arXiv/DOI APIs if needed.
  2. Obtain PDF (use provided `pdf` or download from arXiv).
  3. Extract figures:
     - Run `pdffigures2` to get candidate images and captions.
     - If unavailable, rasterize pages with `PyMuPDF` and select likely figure pages (keywords in captions, image area, aspect ratio).
     - Rank and select 1–2 figures; allow `preferred_figures` override.
     - Save as PNG to `images/highlights/<slug>/fig1.png`, `fig2.png` and store original captions.
  4. Summarize:
     - Generate a 150–300 word highlight:
       - TL;DR (1–2 sentences)
       - 3–5 bullet points on contributions/novelty/impact
       - Links: arXiv/DOI and (if exists) code
     - Use an LLM; run a short “fact-check” pass referencing extracted metadata and captions.
  5. Emit Markdown draft to `/_drafts/<slug>.md` with front matter fields:
     - `title`, `date`, `categories: [research-highlights]`, `links`, `citations`, `tags`.
     - Body inserts selected figures with captions and credit.

Acceptance
- For 1 sample paper, a draft `.md` is created and images saved under `images/highlights/<slug>/`.
- Draft renders locally with images and links; no broken assets.

---

### Step 4 — Repo ingestion and drafting
Tasks
- For each `type: repo`:
  1. Fetch repo metadata via GitHub API (name, description, stars, topics).
  2. Parse README for images; prefer `preferred_images` if provided; fallback to first meaningful image.
  3. Summarize (150–300 words) focusing on purpose, key features, and impact; include badges (stars) if desired.
  4. Emit Markdown draft with figures to `/_drafts/<slug>.md`; save images to `images/highlights/<slug>/` (downloaded from README if remote).

Acceptance
- For 1 sample repo, a draft `.md` is created with at least one image and summary.

---

### Step 5 — Manual review workflow
Tasks
- Document a short checklist in the generator output (top of each draft):
  - Facts correct? Claims aligned with paper/repo?
  - Selected figures representative and legible?
  - Figure credit/source included? Licensing OK? (Prefer arXiv figures.)
  - Tags and links correct?
- Approve: move the draft from `/_drafts/` → `/_highlights/` (keep same filename/slug).
- Decline: edit text or update `highlights.yml` (e.g., add `skip: true`) and re-run.

Acceptance
- Approved items appear in `/research-highlights/` listing and have individual pages under `/highlights/<slug>/`.

---

### Step 6 — Generator CLI details (implementation guide)
Tasks
- Create `markdown_generator/highlights.py` (or similar) with subcommands:
  - `ingest papers` | `ingest repos` | `generate all`
  - `--dry-run` (no writes), `--limit N`, `--overwrite`
  - `--only id1,id2` to target specific items
- Structure:
  - `inputs.py` (read YAML, validate schema)
  - `papers.py` (ADS/arXiv resolve, PDF fetch, figures)
  - `repos.py` (GitHub fetch, README parse, images)
  - `summarize.py` (LLM prompts + fact-check pass)
  - `emit.py` (front matter + Markdown + asset paths)
- Logging: concise per-item logs; write a JSON report summarizing successes/failures and any manual actions suggested.

Acceptance
- Running `python markdown_generator/highlights.py generate all --dry-run` prints a plan with items to be created.
- Without `--dry-run`, drafts and assets are written as specified.

---

### Step 7 — Polishing and optional safeguards
Optional tasks (only if needed)
- Broken link checker for the highlights collection.
- Simple license guard:
  - If figure source is journal PDF and no arXiv image exists, downscale and watermark “source” with a link, or skip figure.
- Simple tests: unit tests for ranking heuristic and path emit logic.

Acceptance
- Optional features pass basic checks and don’t block the core flow.

---

### Roles and responsibilities
- You: curate `highlights.yml` and approve drafts.
- Coding agent: implement generator, wire Jekyll collection and listing page, ensure figures and summaries are emitted correctly, and keep changes minimal.

### Risks and mitigations
- Figure extraction brittle → allow manual `preferred_figures`, produce a draft even if figures fail, and flag items in the report.
- LLM hallucinations → prompt grounded on extracted metadata + captions; include a mini fact-check pass; manual review before publish.
- Licensing ambiguity → prefer arXiv; always include credit; allow “no-figure” mode per item.

### Done criteria (MVP)
- New nav tab exists and lists published highlights.
- Given 3 items in `highlights.yml` (mix of paper/repo), `generate all` produces drafts with summaries and 1–2 figures each.
- After manual approval (moving to `/_highlights/`), pages render cleanly with images and links.


