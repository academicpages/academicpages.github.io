# JekyllRedirectFrom

Give your Jekyll posts and pages multiple URLs.

When importing your posts and pages from, say, Tumblr, it's annoying and
impractical to create new pages in the proper subdirectories so they, e.g.
`/post/123456789/my-slug-that-is-often-incompl`, redirect to the new post URL.

Instead of dealing with maintaining those pages for redirection, let
`jekyll-redirect-from` handle it for you.

[![Build Status](https://travis-ci.org/jekyll/jekyll-redirect-from.svg?branch=master)](https://travis-ci.org/jekyll/jekyll-redirect-from)

## How it Works

Redirects are performed by serving an HTML file with an HTTP-REFRESH meta
tag which points to your destination. No `.htaccess` file, nginx conf, xml
file, or anything else will be generated. It simply creates HTML files.

## Installation

Add this line to your application's Gemfile:

    gem 'jekyll-redirect-from'

And then execute:

    $ bundle

Or install it yourself as:

    $ gem install jekyll-redirect-from

Once it's installed into your evironment, add it to your `_config.yml`:

```yaml
plugins:
  - jekyll-redirect-from
```

💡 If you are using a Jekyll version less than 3.5.0, use the `gems` key instead of `plugins`.

If you're using Jekyll in `safe` mode to mimic GitHub Pages, make sure to
add jekyll-redirect-from to your whitelist:

```yaml
whitelist:
  - jekyll-redirect-from
```

Then run `jekyll <cmd> --safe` like normal.

## Usage

The object of this gem is to allow an author to specify multiple URLs for a
page, such that the alternative URLs redirect to the new Jekyll URL.

To use it, simply add the array to the YAML front-matter of your page or post:

```yaml
title: My amazing post
redirect_from:
  - /post/123456789/
  - /post/123456789/my-amazing-post/
```

Redirects including a trailing slash will generate a corresponding subdirectory containing an `index.html`, while redirects without a trailing slash will generate a corresponding `filename` without an extension, and without a subdirectory.

For example...

```text
redirect_from:
  - /post/123456789/my-amazing-post
```

...will generate the following page in the destination:

```text
/post/123456789/my-amazing-post
```

While...

```text
redirect_from:
  - /post/123456789/my-amazing-post/
```

...will generate the following page in the destination:

```text
/post/123456789/my-amazing-post/index.html
```

These pages will contain an HTTP-REFRESH meta tag which redirect to your URL.

You can also specify just **one url** like this:

```text
title: My other awesome post
redirect_from: /post/123456798/
```

### Prefix

If `site.url` is set, its value, together with `site.baseurl`, is used as a prefix for the redirect url automatically. This is useful for scenarios where a site isn't available from the domain root, so the redirects point to the correct path. If `site.url` is not set, only `site.baseurl` is used, if set.

**_Note_**: If you are hosting your Jekyll site on [GitHub Pages](https://pages.github.com/), and `site.url` is not set, the prefix is set to the pages domain name i.e. http://example.github.io/project or a custom CNAME.

### Redirect To

Sometimes, you may want to redirect a site page to a totally different website. This plugin also supports that with the `redirect_to` key:

```yaml
title: My amazing post
redirect_to: http://www.github.com
```

**Note**: Using `redirect_to` or `redirect_from` with collections will only work with files which are output to HTML, such as `.md`, `.textile`, `.html` etc.

## Customizing the redirect template

If you want to customize the redirect template, you can. Simply create a layout in your site's `_layouts` directory called `redirect.html`.

Your layout will get the following variables:

* `page.redirect.from` - the relative path to the redirect page
* `page.redirect.to` - the absolute URL (where available) to the target page

## Configuration

You can configure this plugin in `_config.yml` by adding to the `redirect_from` key.

### Disabling `redirects.json`

By default, a file called `redirects.json`, which can be used for automated testing or to implement server-side redirects, will be included in the output. To exclude it from the output, set the `json` key to `false`:

```yml
redirect_from:
  json: false
```

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request
