# Jekyll::Gist

Liquid tag for displaying GitHub Gists in Jekyll sites: `{% gist %}`.

[![Build Status](https://travis-ci.org/jekyll/jekyll-gist.svg?branch=master)](https://travis-ci.org/jekyll/jekyll-gist)

## Installation

Add this line to your application's Gemfile:

    $ gem 'jekyll-gist'

And then execute:

    $ bundle

Or install it yourself as:

    $ gem install jekyll-gist

Then add the following to your site's `_config.yml`:

```
plugins:
  - jekyll-gist
```

💡 If you are using a Jekyll version less than 3.5.0, use the `gems` key instead of `plugins`.

## Usage

Use the tag as follows in your Jekyll pages, posts and collections:

```liquid
{% gist c08ee0f2726fd0e3909d %}
```

This will create the associated script tag:

```html
<script src="https://gist.github.com/parkr/c08ee0f2726fd0e3909d.js"> </script>
```

You may optionally specify a `filename` after the `gist_id`:

```liquid
{% gist c08ee0f2726fd0e3909d test.md %}
```

This will produce the correct URL to show just the specified file in your post rather than the entire Gist.

**Pro-tip**: If you provide a personal access token with Gist scope, as the environmental variable `JEKYLL_GITHUB_TOKEN`, Jekyll Gist will use the Gist API to speed up site generation.

## Disabling `noscript` support

By default, Jekyll Gist will make an HTTP call per Gist to retrieve the raw content of the Gist. This information is used to propagate `noscript` tags for search engines and browsers without Javascript support. If you'd like to disable this feature, for example, to speed up builds locally, add the following to your site's `_config.yml`:

```yml
gist:
  noscript: false
```

## Contributing

1. Fork it ( https://github.com/jekyll/jekyll-gist/fork )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request
