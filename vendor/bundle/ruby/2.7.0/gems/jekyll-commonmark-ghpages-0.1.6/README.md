# jekyll-commonmark-ghpages

*GitHub Flavored Markdown converter for Jekyll, based on [`jekyll-commonmark`](https://github.com/jekyll/jekyll-commonmark)*

[![Gem Version](https://img.shields.io/gem/v/jekyll-commonmark-ghpages.svg)](https://rubygems.org/gems/jekyll-commonmark-ghpages)
[![Build Status](https://img.shields.io/travis/github/jekyll-commonmark-ghpages/master.svg)](https://travis-ci.org/github/jekyll-commonmark-ghpages)
[![Windows Build status](https://img.shields.io/appveyor/ci/github/jekyll-commonmark-ghpages/master.svg?label=Windows%20build)](https://ci.appveyor.com/project/github/jekyll-commonmark-ghpages)

Jekyll Markdown converter that uses [libcmark-gfm](https://github.com/github/cmark), GitHub's fork of [cmark](https://github.com/commonmark/cmark), the reference parser for CommonMark, with some additions to ensure compatibility with existing Kramdown-based sites.

## Installation

Add the following to your `Gemfile`:

```ruby
group :jekyll_plugins do
  gem 'jekyll-commonmark-ghpages'
end
```

and modify your `_config.yml` to use **CommonMarkGhPages** as your Markdown converter:

```yaml
markdown: CommonMarkGhPages
```

This processor is currently in testing for use in GitHub Pages.

To specify extensions and options for use in converting Markdown to HTML, supply options to the Markdown converter:

```yaml
commonmark:
  options: ["SMART", "FOOTNOTES"]
  extensions: ["strikethrough", "autolink", "table", "tagfilter"]
```
