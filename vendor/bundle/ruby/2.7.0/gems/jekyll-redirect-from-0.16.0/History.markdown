## 0.16.0 / 2020-01-26

### Minor Enhancements

  * Allows generation of `redirects.json` to be disabled (#207)
  * Allow redirects from and for subclasses of page and document (#204)

### Bug Fixes

  * Use `Hash#key?` instead of `Hash#keys.any?` (#201)

### Development Fixes

  * Target Ruby 2.4
  * Stop testing with backwards-compatible site config (#211)

### Documentation

  * Simplifies YAML for `redirect_to` (#185)

## 0.15.0 / 2019-03-23

### Development Fixes

  * chore(deps): rubocop-jekyll 0.3 (#187)

### Bug Fixes

  * Allow testing and using with Jekyll 4.x (#196)

## 0.14.0 / 2018-06-29

### Minor Enhancements

  * Run javascript at first to avoid splash (#158)

### Development Fixes

  * Use Rubocop 0.57
  * Target Ruby 2.3
  * Test against Ruby 2.5 (#173)

## 0.13.0 / 2017-12-03

  * Test against same version of Ruby that GitHub Pages uses (#132)

### Development Fixes

  * Rubocop (#141)
  * Fix tests for jekyll 3.5.x (#160)
  * Rubocop: autocorrect (#165)

### Minor Enhancements

  * HTML encode ellipsis (#142)
  * Added no-index to template (#152)
  * Define path with __dir__ (#161)

### Major Enhancements

  * Create redirects.json file (#147)

### Documentation

  * Update README.md (#167)

## 0.12.1 / 2017-01-12

### Development Fixes

  * Stop testing Ruby 1.9 (#133)

### Minor Enhancements

  * Use send to monkey patch to support Ruby < 2.2.0 (#136)
  * set `page.output` to empty string instead of nil (#137)

## 0.12.0 / 2017-01-02

### Major Enhancements

  * Support for custom redirect templates
  * Use Jekyll's `absolute_url` filter to generate canonical URLs (now respecting `baseurl`)
  * Rely more heavily on Jekyll's native Page, permalink, and extension handling logic

### Minor Enhancementse

  * redirect_to Pages should not have a layout. (#115)
  * Require Jekyll >= 3.3

### Development Enhancements

  * Push redirect logic to the redirect page model (#131)
  * Add Rubocop and enforce Jekyll coding standards
  * Tests no longer build and write the entire site between each example
  * Removed all the `is_*`? and `has_*`? helpers from the generator

## 0.11.0 / 2016-07-06

  * Redirect page should not have any layout (#106)
  * Include absolute path in canonical url (#109)
  * Add <html> tag and language (#100)
  * Ensure redirect_to links produce an HTML file. (#111)

## 0.10.0 / 2016-03-16

  * Ensure output extension is assigned (#96)

## 0.9.1 / 2015-12-11

  * Enforce double-quote strings to pass htmlhint (#83)
  * Stringify all values coming from `site.github` (#89)

## 0.9.0 / 2015-10-28

  * Support Jekyll 3 stable (#76)
  * Test against Jekyll 3, 2, and GitHub Pages (#72)

## 0.8.0 / 2015-05-20

  * Exclude redirect pages from sitemap (#69)

## 0.7.0 / 2015-03-16

  * Remove spaces in redirect page (#62)
  * Only parse through documents/pages/posts (#56)
  * Simplified `has_alt_urls?` and `has_redirect_to_url?` conditions (#52)
  * Add support for Jekyll 3. (#59)

## 0.6.2 / 2014-09-12

  * Fixed error where `redirect_to` `Document`s were not being output properly (#46)

## 0.6.1 / 2014-09-08

  * Fixed error when the `site.github` config key is not a `Hash` (#43)

## 0.6.0 / 2014-08-22

  * Support redirecting to/from collection documents (#40)

## 0.5.0 / 2014-08-10

### Minor Enhancements

  * Support `redirect_to` property (#32)
  * Automatically prefix redirects with the `baseurl` or GitHub URL. (#26)

### Bug Fixes

  * Remove unnecessary `Array#flatten` (#34)

### Development Fixes

  * Use `be_truthy` instead of `be_true`. (#33)

## 0.4.0 / 2014-05-06

### Major Enhancements

  * Upgrade to Jekyll 2.0 (#27)

### Minor Enhancements

  * Shorten resulting HTML to make redirects quicker (#20)

### Development Fixes

  * Use SVG Travis badge in README (#21)

## 0.3.1 / 2014-01-22

### Bug Fixes

  * Add `safe true` to the `Jekyll::Generator` so it can be run in safe mode (#12)

## 0.3.0 / 2014-01-15

### Major Enhancements

  * `redirect_from` items are now proper permalinks rooted in site source (#8)

### Development Fixes

  * Add forgotten `s` to `gems` in README.md (#7)

## 0.2.0 / 2014-01-04

### Minor Enhancements

  * Allow user to set one or many `redirect_from` URLs
  * Rename from `jekyll-alt-urls` to `jekyll-redirect-from` (props to @benbalter)
  * Namespace now its own module: `JekyllRedirectFrom` (#3)

### Development Fixes

  * Add history file
  * Add specs (#3)
  * Add TravisCI badge (#4)

## 0.1.0 / 2013-12-15

  * Birthday!
