## Usage

The SEO tag will respect any of the following if included in your site's `_config.yml` (and simply not include them if they're not defined):

* `title` - Your site's title (e.g., Ben's awesome site, The GitHub Blog, etc.)
* `description` - A short description (e.g., A blog dedicated to reviewing cat gifs)
* `url` - The full URL to your site. Note: `site.github.url` will be used by default.
* `author` - global author information (see [Advanced usage](advanced-usage.md#author-information))

* `twitter` - The following properties are available:
  * `twitter:card` - The site's default card type
  * `twitter:username` - The site's Twitter handle. You'll want to describe it like so:

  ```yml
  twitter:
    username: benbalter
    card: summary
  ```

* `facebook` - The following properties are available:
  * `facebook:app_id` - a Facebook app ID for Facebook insights
  * `facebook:publisher` - a Facebook page URL or ID of the publishing entity
  * `facebook:admins` - a Facebook user ID for domain insights linked to a personal account

  You'll want to describe one or more like so:

  ```yml
  facebook:
    app_id: 1234
    publisher: 1234
    admins: 1234
  ```

* `logo` - URL to a site-wide logo (e.g., `/assets/your-company-logo.png`) - If you would like the "publisher" property to be present, you must add this field to your site's configuration, during the validation of the structured data by Google web master tools, if the `logo` field is not validated, you will find errors inherent to the publisher in the [structured datas test](https://search.google.com/structured-data/testing-tool/u/0/)
* `social` - For [specifying social profiles](https://developers.google.com/structured-data/customize/social-profiles). The following properties are available:
  * `name` - If the user or organization name differs from the site's name
  * `links` - An array of links to social media profiles.

  ```yml
  social:
    name: Ben Balter
    links:
      - https://twitter.com/BenBalter
      - https://www.facebook.com/ben.balter
      - https://www.linkedin.com/in/BenBalter
      - https://plus.google.com/+BenBalter
      - https://github.com/benbalter
      - https://keybase.io/benbalter
  ```

* `google_site_verification` for verifying ownership via Google webmaster tools
* Alternatively, verify ownership with several services at once using the following format:

```yml
webmaster_verifications:
  google: 1234
  bing: 1234
  alexa: 1234
  yandex: 1234
  baidu: 1234
```

* `lang` - The locale these tags are marked up in. Of the format `language_TERRITORY`. Default is `en_US`.

The SEO tag will respect the following YAML front matter if included in a post, page, or document:

* `title` - The title of the post, page, or document
* `description` - A short description of the page's content
* `image` - URL to an image associated with the post, page, or document (e.g., `/assets/page-pic.jpg`)
* `author` - Page-, post-, or document-specific author information (see [Advanced usage](advanced-usage.md#author-information))
* `lang` - Page-, post-, or document-specific language information

*Note:* Front matter defaults can be used for any of the above values as described in advanced usage with an image example.
