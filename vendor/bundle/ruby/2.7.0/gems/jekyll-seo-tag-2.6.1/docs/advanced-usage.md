## Advanced usage

Jekyll SEO Tag is designed to implement SEO best practices by default and to be the right fit for most sites right out of the box. If for some reason, you need more control over the output, read on:

### Disabling `<title>` output

If for some reason, you don't want the plugin to output `<title>` tags on each page, simply invoke the plugin within your template like so:

<!-- {% raw %} -->
```
{% seo title=false %}
```
<!-- {% endraw %} -->

### Author information

Author information is used to propagate the `creator` field of Twitter summary cards. This should be an author-specific, not site-wide Twitter handle (the site-wide username be stored as `site.twitter.username`).

*TL;DR: In most cases, put `author: [your Twitter handle]` in the document's front matter, for sites with multiple authors. If you need something more complicated, read on.*

There are several ways to convey this author-specific information. Author information is found in the following order of priority:

1. An `author` object, in the documents's front matter, e.g.:

  ```yml
  author:
    twitter: benbalter
  ```

2. An `author` object, in the site's `_config.yml`, e.g.:

  ```yml
  author:
    twitter: benbalter
  ```

3. `site.data.authors[author]`, if an author is specified in the document's front matter, and a corresponding key exists in `site.data.authors`. E.g., you have the following in the document's front matter:

  ```yml
  author: benbalter
  ```

  And you have the following in `_data/authors.yml`:

  ```yml
  benbalter:
    picture: /img/benbalter.png
    twitter: jekyllrb

  potus:
    picture: /img/potus.png
    twitter: whitehouse
  ```

  In the above example, the author `benbalter`'s Twitter handle will be resolved to `@jekyllrb`. This allows you to centralize author information in a single `_data/authors` file for site with many authors that require more than just the author's username.

  *Pro-tip: If `authors` is present in the document's front matter as an array (and `author` is not), the plugin will use the first author listed, as Twitter supports only one author.*

4. An author in the document's front matter (the simplest way), e.g.:

  ```yml
  author: benbalter
  ```

5. An author in the site's `_config.yml`, e.g.:

  ```yml
  author: benbalter
  ```

### Customizing JSON-LD output

The following options can be set for any particular page. While the default options are meant to serve most users in the most common circumstances, there may be situations where more precise control is necessary.

* `seo`
  * `name` - If the name of the thing that the page represents is different from the page title. (i.e.: "Frank's Café" vs "Welcome to Frank's Café")
  * `type` - The type of things that the page represents. This must be a [Schema.org type](http://schema.org/docs/schemas.html), and will probably usually be something like [`BlogPosting`](http://schema.org/BlogPosting), [`NewsArticle`](http://schema.org/NewsArticle), [`Person`](http://schema.org/Person), [`Organization`](http://schema.org/Organization), etc.
  * `links` - An array of other URLs that represent the same thing that this page represents. For instance, Jane's bio page might include links to Jane's GitHub and Twitter profiles.
  * `date_modified` - Manually specify the `dateModified` field in the JSON-LD output to override Jekyll's own `dateModified`.
  This field will take **first priority** for the `dateModified` JSON-LD output. This is useful when the file timestamp does not match the true time that the content was modified. A user may also install [Last Modified At](https://github.com/gjtorikian/jekyll-last-modified-at) which will offer an alternative way of providing for the `dateModified` field.

### Customizing image output

For most users, setting `image: [path-to-image]` on a per-page basis should be enough. If you need more control over how images are represented, the `image` property can also be an object, with the following options:

* `path` - The relative path to the image. Same as `image: [path-to-image]`
* `height` - The height of the Open Graph (`og:image`) image
* `width` - The width of the Open Graph (`og:image`) image

You can use any of the above, optional properties, like so:

```yml
image:
  path: /img/twitter.png
  height: 100
  width: 100
```

### Setting a default image

You can define a default image using [Front Matter default](https://jekyllrb.com/docs/configuration/#front-matter-defaults), to provide a default Twitter Card or OGP image to all of your posts and pages.

Here is a very basic example, that you are encouraged to adapt to your needs:

```yml
defaults:
  - scope:
      path: ""
    values:
      image: /assets/images/default-card.png
```

### SmartyPants Titles

Titles will be processed using [Jekyll's `smartify` filter](https://jekyllrb.com/docs/templates/). This will use SmartyPants to translate plain ASCII punctuation into "smart" typographic punctuation. This will not render or strip any Markdown you may be using in a page title.

### Setting customized Canonical URL

You can set custom Canonical URL for a page by specifying canonical_url option in page front-matter.
E.g., you have the following in the page's front matter:
```yml
layout: post
title: Title of Your Post
canonical_url: 'https://github.com/jekyll/jekyll-seo-tag/'
```

Which will generate canonical_url with specified link in canonical_url.
```html
<link rel="canonical" href="https://github.com/jekyll/jekyll-seo-tag/" />
```

If no canonical_url option was specified, then uses page url for generating canonical_url.
E.g., you have not specified canonical_url in front-matter:
```yml
layout: post
title: Title of Your Post
```

Which will generate following canonical_url:
```html
<link rel="canonical" href="http://yoursite.com/title-of-your-post" />
```
