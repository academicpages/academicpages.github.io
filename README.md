# Ayush V. Patel — Portfolio Website

Source for my personal website: **<https://ayush253.github.io>**

Built with [Jekyll](https://jekyllrb.com/) using a customized
[Academic Pages](https://github.com/academicpages/academicpages.github.io) theme,
and hosted for free on GitHub Pages.

## Site structure

| Section | Source |
|---|---|
| Home / About | [`_pages/about.md`](_pages/about.md) |
| Publications | [`_publications/`](_publications/) + [`_pages/publications.html`](_pages/publications.html) |
| CV | [`_pages/cv.md`](_pages/cv.md) |
| Sidebar (bio, photo, links) | `author:` block in [`_config.yml`](_config.yml) |
| Header menu | [`_data/navigation.yml`](_data/navigation.yml) |

## Making changes

1. Edit the Markdown/YAML files above.
2. Add downloadable files (e.g. paper PDFs) to the [`files/`](files/) directory —
   they become available at `https://ayush253.github.io/files/<filename>`.
3. Replace `images/profile.png` with a square profile photo (currently a placeholder).
4. Commit and push — GitHub Pages rebuilds the site automatically.

Search for `TODO(Ayush)` comments across the repo to find the spots still
waiting for personal details (email, institution, social links, CV entries).

## Local preview (optional)

```bash
bundle install
bundle exec jekyll serve -l -H localhost
```

or with Docker:

```bash
docker compose up
```
