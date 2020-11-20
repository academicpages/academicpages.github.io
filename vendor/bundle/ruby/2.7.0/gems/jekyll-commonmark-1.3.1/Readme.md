# jekyll-commonmark

*CommonMark Markdown converter for Jekyll*

[![Gem Version](https://img.shields.io/gem/v/jekyll-commonmark.svg)](https://rubygems.org/gems/jekyll-commonmark)
[![Build Status](https://img.shields.io/travis/jekyll/jekyll-commonmark/master.svg)](https://travis-ci.org/jekyll/jekyll-commonmark)
[![Windows Build status](https://img.shields.io/appveyor/ci/pathawks/jekyll-commonmark/master.svg?label=Windows%20build)](https://ci.appveyor.com/project/pathawks/jekyll-commonmark)
[![Dependency Status](https://img.shields.io/gemnasium/pathawks/jekyll-commonmark.svg)](https://gemnasium.com/pathawks/jekyll-commonmark)

Jekyll Markdown converter that uses [libcmark](https://github.com/jgm/CommonMark), the reference parser for CommonMark. 
As a result, it is faster than Kramdown.

GitHub Pages supports CommonMark through https://github.com/github/jekyll-commonmark-ghpages

## Installation

Add the following to your `Gemfile`

```ruby
group :jekyll_plugins do
  gem 'jekyll-commonmark'
end
```

and modify your `_config.yml` to use **CommonMark** as your Markdown converter

```yaml
markdown: CommonMark
```

## Configuration

To specify [extensions](https://github.com/gjtorikian/commonmarker#extensions) and [options](https://github.com/gjtorikian/commonmarker#options) for use in converting Markdown to HTML, supply options to the Markdown converter:

```yaml
commonmark:
  options: ["SMART", "FOOTNOTES"]
  extensions: ["strikethrough", "autolink", "table"]
 ```
 
