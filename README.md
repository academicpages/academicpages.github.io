# Adam Umra — academic website

A compact, responsive academic profile inspired by [Rikiya Takehi’s website](https://rikiyat.github.io/), built on the existing Jekyll/AcademicPages repository. The homepage contains News, Publications, and Experience; it does not include a CV tab, achievements, or selected talks.

## Updating the site

- Biography and experience: `_pages/about.md`.
- Curated papers and overrides: `_data/publications.yml`. Automatic results are saved in `_data/publications_generated.json`; do not edit the generated file.
- Research updates: `_data/news.yml`.
- Profile links and metadata: `_config.yml`.
- Navigation: `_data/navigation.yml`.
- Layout and styling: `_layouts/academic.html` and `assets/css/academic.css`.

The existing portrait is displayed with its embedded credit, © RUB, Marquard. Unused template pages, sample collections, posts, and sample downloads remain in the repository but are excluded from the generated site. `/publications/` redirects to the homepage’s publication section.

## Content sources

Content checked on 4 November 2026 against the [university profile](https://www.dks.ruhr-uni-bochum.de/de/profiles/adam-umra/), [LinkedIn profile](https://de.linkedin.com/in/adam-umra-704b941b2), author biography in [Robust Communication Design in RIS-Assisted THz Channels](https://doi.org/10.1109/OJCOMS.2025.3541315), and publisher/arXiv records linked with each paper. The [Google Scholar profile](https://scholar.google.com/citations?user=7jGnTxYAAAAJ&hl=de) was supplied by Adam. Scholar rate-limited automated reading; IEEE Xplore and LinkedIn also restricted direct access, so indexed university and publication records were used to cross-check details. Publication metadata refreshes from Crossref and arXiv; it does not scrape or synchronize with Google Scholar.

No employment start date was inferred. News dates describe public preprint releases or updated acceptance notices, not unverified presentation dates.

## Automatic publications

The Pages workflow refreshes publications every Monday at 06:17 UTC (07:17 in Berlin in winter, 08:17 in summer), on pushes to `master`, and when run manually from **Actions → Update publications and deploy to Pages → Run workflow**. GitHub may delay scheduled jobs. This starts only after these changes are pushed to the repository’s default branch with Actions enabled and Pages configured to use GitHub Actions.

The updater queries Crossref for published papers and arXiv for preprints. It requires an exact full-name match (`Adam Umra`), or the matching ORCID in Crossref; a conflicting ORCID is rejected. Initial-only author records without an ORCID, records not indexed by these sources, and some title changes may need a manual entry. No paid service or API key is required.

Records are matched by DOI, arXiv ID, IEEE document ID, or normalized title. Existing publications are retained during source outages. Your curated text takes precedence, with additional paper links retained; a curated `Preprint` can automatically gain a verified publication venue and year. Acceptance notices are not inferred from free-text arXiv comments. To suppress a record, add it to `_data/publications.yml` with `hidden: true` and its identifying title/links.

After a successful build, the workflow commits changed generated data with `github-actions[bot]` and deploys the refreshed website in the same run. The build job requests `contents: write`; repository rules must allow the bot to commit to the default branch. No force pushes are used. API failures appear as workflow warnings and preserve saved records, so a temporary outage does not empty the page. GitHub may disable scheduled workflows in a public repository after 60 days of inactivity; they can be re-enabled in Actions.

Local refresh and checks:

```sh
python -m pip install PyYAML==6.0.3
python scripts/update-publications.py
python -m unittest discover -s scripts -p 'test_publications.py'
```

## Build

```sh
bundle install
bundle exec jekyll build
bundle exec jekyll serve
```

The existing GitHub Pages workflow remains in place. The inherited Sass theme currently emits deprecation warnings during builds.

---

# Academic Pages
**Academic Pages is a GitHub Pages template for personal and professional portfolio-oriented websites.**

![Academic Pages template example](images/themes/homepage-light.png "Academic Pages template example")

# Getting Started

1. Register a GitHub account if you don't have one and confirm your e-mail (required!)
1. Click the "Use this template" button in the top right.
1. On the "New repository" page, enter your public repository name as "[your GitHub username].github.io", which will also be your website's URL.
1. Edit site-wide configuration in `_config.yml` and double check that the `url` is the one that you just selected in the previous step and that `repository` reflects the correct path for your repository.
1. Add your site content, upload any files (like PDFs, .zip files, etc.) to the `files/` directory. They will appear at https://[your GitHub username].github.io/files/example.pdf.
1. Check status by going to the repository settings, under: Settings -> Pages -> Source: GitHub Actions
1. (Optional) Use the Jupyter notebooks or python scripts in the `markdown_generator` folder to generate markdown files for publications and talks from a TSV file.

See more info at https://academicpages.github.io/

### Additional Tutorials

Additional tutorials for working with the Academic Pages template can be found at the following sites:
- https://jayrobwilliams.com/posts/2020/06/academic-website/

## Running locally

When you are initially working on your website, it is very useful to be able to preview the changes locally before pushing them to GitHub. To work locally you will need to:

1. Clone the repository and made updates as detailed above.

### Using a different IDE
1. Make sure you have ruby-dev, bundler, and nodejs installed
    
    On most Linux distributions and [Windows Subsystem Linux](https://learn.microsoft.com/en-us/windows/wsl/about) the command is:
    ```bash
    sudo apt install ruby-dev ruby-bundler nodejs
    ```
    If you see error `Unable to locate package ruby-bundler`, `Unable to locate package nodejs `, run the following:
    ```bash
    sudo apt update && sudo apt upgrade -y
    ```
    then try running `sudo apt install ruby-dev ruby-bundler nodejs` again.

    On MacOS the commands are:
    ```bash
    brew install ruby
    brew install node
    gem install bundler
    ```
1. Run `bundle install` to install ruby dependencies. If you get errors, delete Gemfile.lock and try again.

    If you see file permission error like `Fetching bundler-2.6.3.gem ERROR:  While executing gem (Gem::FilePermissionError) You don't have write permissions for the /var/lib/gems/3.2.0 directory.` or `Bundler::PermissionError: There was an error while trying to write to /usr/local/bin.`
    Install Gems Locally (Recommended):
    ```bash
    bundle config set --local path 'vendor/bundle'
    ```
    then try run `bundle install` again. If succeeded, you should see a folder called `vendor` and `.bundle`.

1. Run `jekyll serve -l -H localhost` to generate the HTML and serve it from `localhost:4000` the local server will automatically rebuild and refresh the pages on change to Markdown (*.md) and HTML files, while changes to the core template and configuration (i.e., `_config.yml`) will require stopping and restarting Jekyll.
    You may also try `bundle exec jekyll serve -l -H localhost` to ensure jekyll to use specific dependencies on your own local machine.

If you are running on Linux it may be necessary to install some additional dependencies prior to being able to run locally: `sudo apt install build-essential gcc make`

## Using Docker

Working from a different OS, or just want to avoid installing dependencies? You can use the provided `Dockerfile` to build a container that will run the site for you if you have [Docker](https://www.docker.com/) installed.

You can build and execute the container by running the following command in the repository:

```bash
chmod -R 777 .
docker compose up
```

You should now be able to access the website from `localhost:4000`.

### Using the DevContainer in VS Code

If you are using [Visual Studio Code](https://code.visualstudio.com/) you can use the [Dev Container](https://code.visualstudio.com/docs/devcontainers/containers) that comes with this Repository. Normally VS Code detects that a development container configuration is available and asks you if you want to use the container. If this doesn't happen you can manually start the container by **F1->DevContainer: Reopen in Container**. This restarts your VS Code in the container and automatically hosts your academic page locally on http://localhost:4000. All changes will be updated live to that page after a few seconds.

# Maintenance

Bug reports and feature requests to the template should be [submitted via GitHub](https://github.com/academicpages/academicpages.github.io/issues/new/choose). For questions concerning how to style the template, please feel free to start a [new discussion on GitHub](https://github.com/academicpages/academicpages.github.io/discussions).

This repository was forked (then detached) by [Stuart Geiger](https://github.com/staeiou) from the [Minimal Mistakes Jekyll Theme](https://mmistakes.github.io/minimal-mistakes/), which is © 2016 Michael Rose and released under the MIT License (see LICENSE.md). It is currently being maintained by [Robert Zupko](https://github.com/rjzupkoii), and additional maintainers would be welcome.

## Bugfixes and enhancements

If you have bugfixes and enhancements that you would like to submit as a pull request, you will need to [fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) this repository as opposed to using it as a template. This will also allow you to [synchronize your copy](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork) of the template to your fork as well.

Unfortunately, one logistical issue with a template theme like Academic Pages that makes it a little tricky to get bug fixes and updates to the core theme. If you use this template and customize it, you will probably get merge conflicts if you attempt to synchronize, although [rebasing](https://git-scm.com/docs/git-rebase) the changes from this template will work along with manually [cherry picking](https://git-scm.com/docs/git-cherry-pick) the relevant commits. If you are not comfortable with the Git command line, you can save your various `.yml` configuration files and Markdown files, delete the repository, and fork it again. 

---
<div align="center">
    
![pages-build-deployment](https://github.com/academicpages/academicpages.github.io/actions/workflows/pages/pages-build-deployment/badge.svg)
[![GitHub contributors](https://img.shields.io/github/contributors/academicpages/academicpages.github.io.svg)](https://github.com/academicpages/academicpages.github.io/graphs/contributors)
[![GitHub release](https://img.shields.io/github/v/release/academicpages/academicpages.github.io)](https://github.com/academicpages/academicpages.github.io/releases/latest)
[![GitHub license](https://img.shields.io/github/license/academicpages/academicpages.github.io?color=blue)](https://github.com/academicpages/academicpages.github.io/blob/master/LICENSE)

[![GitHub stars](https://img.shields.io/github/stars/academicpages/academicpages.github.io)](https://github.com/academicpages/academicpages.github.io)
[![GitHub forks](https://img.shields.io/github/forks/academicpages/academicpages.github.io)](https://github.com/academicpages/academicpages.github.io/fork)
</div>
