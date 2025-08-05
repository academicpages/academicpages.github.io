# Repository Specification: Academic Personal Website

## Purpose
This repository contains a Jekyll-based academic personal website for Sihan (Sandy) Yuan, a KIPAC Fellow at Stanford University. The site is built on the academicpages template (a fork of Minimal Mistakes Jekyll theme) and is hosted on GitHub Pages at `sandyyuan.github.io`.

## Core Technologies
- **Jekyll** - Static site generator
- **GitHub Pages** - Hosting platform
- **Minimal Mistakes** - Base Jekyll theme
- **GitHub Actions** - Automated publication updates
- **NASA ADS API** - Publication data source

## Repository Structure

### Configuration Files
- `_config.yml` - Main Jekyll configuration with site metadata, author info, navigation settings
- `Gemfile` / `Gemfile.lock` - Ruby dependencies for Jekyll
- `package.json` - Node.js dependencies for JavaScript build processes

### Content Directories

#### `_pages/` - Static Pages
- `about.md` - Homepage/about section (permalink: `/`)
- `publications.md` - Publications page with dynamic loading
- `cv.md` - CV page with embedded PDF viewer
- `404.md` - Error page
- Other utility pages (archive, sitemap, etc.)

#### `_posts/` - Blog Posts
- Contains sample blog posts (currently unused)
- Format: `YYYY-MM-DD-title.md`

#### `_publications/` - Publication Entries
- Individual publication markdown files
- Auto-generated from publication data

#### `_data/` - Data Files
- `navigation.yml` - Main navigation menu structure
- `authors.yml` - Author information
- `ui-text.yml` - UI text translations

### Layout & Theme

#### `_layouts/` - Page Templates
- `single.html` - Single page/post layout with sidebar
- `archive.html` - Archive page layout
- `cv.html` - CV-specific layout
- `default.html` - Base layout with responsive fixes
- `splash.html` - Hero/splash page layout

#### `_includes/` - Reusable Components
- `head/` - Header elements and metadata
- `author-profile.html` - Author sidebar widget
- `archive-single.html` - Archive item display
- `scripts.html` - JavaScript includes
- Analytics, comments, social sharing components

#### `_sass/` - Styles (not shown but referenced)
- SCSS files for styling

### Assets

#### `assets/`
- `css/` - Compiled stylesheets
  - `publications.css` - Publications page styling
  - `override.css` - Custom style overrides
- `js/` - JavaScript files
  - `publications.json` - Generated publication data
  - `publications-loader.js` - Dynamic publication loading
  - `custom.js` - Custom JavaScript
  - `main.min.js` - Minified main JavaScript

#### `files/`
- `CV1.pdf` - CV document
- Other downloadable files

#### `images/`
- `profile.jpg` - Profile photo
- Favicons and other images

### Automation

#### `.github/` - GitHub Actions

##### `workflows/update-publications.yml`
- Runs weekly (Sunday midnight) or manually
- Fetches publications from NASA ADS API
- Creates PR with updated publications

##### `scripts/`
- `fetch_publications.py` - Main script to fetch from ADS API
  - Uses ORCID: 0000-0002-5992-7586
  - Outputs to `assets/js/publications.json`
  - Handles errors gracefully
- `test_ads_token.py` - Token validation script

### Key Features

#### 1. Automated Publication Updates
- **Workflow**: GitHub Action runs weekly
- **Process**: 
  1. Fetches publications using NASA ADS API
  2. Processes and formats publication data
  3. Saves to `publications.json`
  4. Creates PR if changes detected
- **Requirements**: `ADS_TOKEN` GitHub secret

#### 2. Dynamic Publications Display
- **Frontend**: JavaScript-based loading from JSON
- **Features**:
  - Tab filtering (All/First Author)
  - Citation counts
  - Links to ADS and arXiv
- **Fallback**: Links to external publication databases

#### 3. Responsive Layout Fixes
- Custom CSS in `head/custom.html` ensures proper sidebar positioning
- Layout adjustments for mobile/tablet/desktop views
- Sidebar width: 250px (desktop), 200px (tablet), 100% (mobile)

#### 4. CV Integration
- Embedded PDF viewer with download option
- Custom layout for optimal display

## Important Files for Maintenance

### Content Updates
- `_pages/about.md` - Main bio/homepage content
- `_data/navigation.yml` - Menu items
- `_config.yml` - Site metadata and social links

### Publication System
- `.github/scripts/fetch_publications.py` - Modify publication fetching logic
- `assets/js/publications-loader.js` - Change publication display
- `.github/workflows/update-publications.yml` - Adjust update schedule

### Styling
- `assets/css/override.css` - Add custom styles
- `assets/css/publications.css` - Publication-specific styles

## Environment Variables/Secrets
- `ADS_TOKEN` - NASA ADS API token (stored as GitHub secret)

## Build Process
1. Jekyll processes markdown files into HTML
2. GitHub Pages automatically builds on push to main branch
3. Publications update via GitHub Actions (weekly)

## Local Development
```bash
bundle install          # Install Ruby dependencies
bundle exec jekyll serve # Run local server
```

## Key Customizations from Base Template
1. Automated publication fetching system
2. Responsive layout fixes for better sidebar behavior
3. Custom publications page with dynamic loading
4. Integrated CV viewer
5. Removed/disabled teaching section
6. Profile and bio specific to Sihan Yuan

## Notes for Developers
- The site uses Jekyll 3.10.0 (GitHub Pages compatible)
- Custom responsive fixes are critical - don't remove inline styles in layouts
- Publication updates create PRs rather than direct commits for safety
- The ADS API token must be kept secure and updated if expired

## File Naming Conventions
- **Pages**: `_pages/[name].md` or `.html`
- **Posts**: `_posts/YYYY-MM-DD-[title].md`
- **Publications**: `_publications/YYYY-MM-DD-[title].md`
- **Talks**: `_talks/YYYY-MM-DD-[title].md`

## Dependencies
### Ruby Gems (via Bundler)
- github-pages
- jekyll-feed
- jekyll-sitemap
- hawkins

### Python (for publication updates)
- requests
- datetime
- json

### JavaScript
- jQuery 1.12.4
- Various jQuery plugins (fitvids, greedy-navigation, magnific-popup, smooth-scroll)
- Stickyfill

## Debugging Tips
1. **Publications not updating**: Check GitHub Actions logs and ADS_TOKEN validity
2. **Layout issues**: Check responsive CSS in `head/custom.html`
3. **Build failures**: Run `bundle update` to update dependencies
4. **Local dev issues**: Delete `_site/` folder and rebuild

## Repository URLs
- **Live Site**: https://sandyyuan.github.io
- **Repository**: https://github.com/sandyyuan/sandyyuan.github.io
- **Base Template**: https://github.com/academicpages/academicpages.github.io