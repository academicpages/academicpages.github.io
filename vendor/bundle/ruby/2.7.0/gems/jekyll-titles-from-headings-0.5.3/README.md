# Jekyll Titles from Headings

*A Jekyll plugin to pull the page title from the first Markdown heading when none is specified.*

[![Build Status](https://travis-ci.org/benbalter/jekyll-titles-from-headings.svg?branch=master)](https://travis-ci.org/benbalter/jekyll-titles-from-headings)

## What it does

If you have a Jekyll page that doesn't have a title specified in the YAML Front Matter, but the first non-whitespace line in the page is a Markdown H1 / H2 / H3, this plugin instructs Jekyll to use that first heading as the page's title.

## Why

Because lots of plugins and templates rely on `page.title`.

If you're using a plugin like [Jekyll Optional Front Matter](https://github.com/benbalter/jekyll-optional-front-matter), you'd have to add Front Matter, just to get the title, which you're already specifying in the document.

Additionally, this allows you to store the title semantically, in the document itself so that it's readable, both as Markdown and when rendered, as machine-readable for plugins like [Jekyll SEO Tag](https://github.com/benbalter/jekyll-seo-tag).

## Usage

1. Add the following to your site's Gemfile:

  ```ruby
  gem 'jekyll-titles-from-headings'
  ```

2. Add the following to your site's config file:

  ```yml
  plugins:
    - jekyll-titles-from-headings
  ```
  Note: If you are using a Jekyll version less than 3.5.0, use the `gems` key instead of `plugins`.

## Configuration

Configuration options are optional and placed in `_config.yml` under the `titles_from_headings` key. They default to:

```yml
titles_from_headings:
  enabled:     true
  strip_title: false
  collections: false
```

### Stripping titles

If your theme renders titles based on `page.title`, you can remove the title from the content by setting `strip_title` to prevent rendering it twice.

To limit this behavior to a certain layouts or paths, you can use [front matter defaults](https://jekyllrb.com/docs/configuration/#front-matter-defaults), e.g.

```yml
defaults:
  - scope:
      path: some-path
      layout: some_layout
    values:
      strip_title: true
```

### Processing Collections

If you want to enable this plugin for collection items, set the `collections` option to `true`.

Since collection items (including posts) already have a title inferred from their filename, this option changes the behavior of this plugin to override the inferred title. The inferred title is only used as a fallback in case the document doesn't start with a heading.

### Disabling

Even if the plugin is enabled (e.g., via the `:jekyll_plugins` group in your Gemfile) you can disable it by setting the `enabled` key to `false`.
