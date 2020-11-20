## About Jekyll SEO Tag

A Jekyll plugin to add metadata tags for search engines and social networks to better index and display your site's content.

[![Gem Version](https://badge.fury.io/rb/jekyll-seo-tag.svg)](https://badge.fury.io/rb/jekyll-seo-tag) [![Build Status](https://travis-ci.org/jekyll/jekyll-seo-tag.svg)](https://travis-ci.org/jekyll/jekyll-seo-tag)

## What it does

Jekyll SEO Tag adds the following meta tags to your site:

* Page title, with site title or description appended
* Page description
* Canonical URL
* Next and previous URLs on paginated pages
* [JSON-LD Site and post metadata](https://developers.google.com/structured-data/) for richer indexing
* [Open Graph](http://ogp.me/) title, description, site title, and URL (for Facebook, LinkedIn, etc.)
* [Twitter Summary Card](https://dev.twitter.com/cards/overview) metadata

While you could theoretically add the necessary metadata tags yourself, Jekyll SEO Tag provides a battle-tested template of crowdsourced best-practices.

## What it doesn't do

Jekyll SEO tag is designed to output machine-readable metadata for search engines and social networks to index and display. If you're looking for something to analyze your Jekyll site's structure and content (e.g., more traditional SEO optimization), take a look at [The Jekyll SEO Gem](https://github.com/pmarsceill/jekyll-seo-gem).

Jekyll SEO tag isn't designed to accommodate every possible use case. It should work for most site out of the box and without a laundry list of configuration options that serve only to confuse most users.

## Documentation

For more information, see:

* [Installation](installation.md)
* [Usage](usage.md)
* [Advanced usage](advanced-usage.md)
