## HEAD

## 0.15.1 / 2020-10-04

### Bug Fixes

  * MetaTag: when encoding for XML special characters, handle non-string objects (#326)

## 0.15.0 / 2020-07-10

### Minor Enhancements

  * Add support for drafts (#316)

## 0.14.0 / 2020-06-24

### Minor Enhancements

  * add support for categories (#153) (#233)
  * add support for tags (#264)
  * Make posts limit configurable (#314)
  * XML escape the title field of feed_meta (#306)

### Bug Fixes

  * Fix feed link when post title contains HTML (#305)

### Development Fixes

  * Use Dir to list source files (#309)
  * Require Ruby &gt;=2.4.0 (#307)

## 0.13.0 / 2019-11-13

### Minor Enhancements

  * Excerpt only flag (#287)
  * Add media:content tag (#290)

### Development Fixes

  * test: use categories in post (#249)

## 0.12.1 / 2019-03-23

### Bug Fixes

  * Re-introduce Ruby 2.3 support and test Jekyll 3.7+ (#272)

## 0.12.0 / 2019-03-21

  * Allow Jekyll v4 (still alpha)

### Development Fixes

  * style: fix offenses in specs (#248)
  * dev: update CI and style settings (#258)
  * Enable testing for Windows platform (#265)

## 0.11.0 / 2018-09-09

### Development Fixes

  * Require Ruby 2.3 (#222)
  * Refactor to remove redundant calls and variables (#240)

### Minor Enhancements

  * Categories and collections (#228)
  * Remove check for older version of Jekyll (#234)

## 0.10.0 / 2018-06-04

### Bug Fixes

  * Escape image URL (#209)

### Development Fixes

  * Rubocop 0.55 (#223)
  * Bump Rubocop (#230)

### Minor Enhancements

  * Support Typhoeus 1.0 (#232)

## 0.9.3 / 2018-02-04

  * Define path with __dir (#187)
  * Bump Ruby for Travis (#188)

### Documentation

  * Fix: Add note about using plugins instead of gems key (#197)
  * Add documentation for disabling smartify filter (#205)
  * Use `https` in more places. (#165)

### Development Fixes

  * Rubocop: Target Ruby 2.2 (#195)
  * Test feeds that have a `site.lang` (#164)
  * Test against Ruby 2.5 (#201)

### Minor Enhancements

  * fix <entry> template for posts with post.lang defined (#168)

## 0.9.3 / 2017-03-28

## 0.9.1 / 2017-02-17

### Minor Enhancements

  * Update feed.xml (#162)

## 0.9.0 / 2017-02-16

### Minor Enhancements

  * Use absolute_url to generate the feed_meta url (#150)
  * Make feed stylesheet optional (#149)
  * Use new `normalize_whitespace` filter (#143)
  * Feed entries must contain <author> (#152)
  * Remove trailing slash from feed ID (#159)

### Development Fixes

  * Simplify minify regular expression (#141)
  * Namespace as JekyllFeed (#151)
  * rubocop -a (#160)

### Bug Fixes

  * Filter out drafts before limit (#154)

## 0.8.0 / 2016-10-06

  * Use filters to clean up Liquid template (#134)

### Minor Enhancements

  * Don't set @site.config["time"] on feed generation (#138)

### pedantry

  * Appease Rubocop (#139)

## 0.7.2 / 2016-10-06

  * Support `image.path` when `post.image` is an object (#137)

## 0.7.1 / 2016-09-26

  * Assign `url_base` before first usage (#133)

## 0.7.0 / 2016-09-06

  * Use type="html" to skirt around double escaping problem (#127)

## 0.6.0 / 2016-07-08

  * Cleanup `post_author` logic (#113)
  * Add XML stylesheet example with XSLT (#119)
  * DRY up and add more doc (#120)
  * Use smartify filter (#117)

## 0.5.1 / 2016-04-18

  * Fix mangling of whitespace when `site.lang` is set (#110)

## 0.5.0 / 2016-04-13

  * Consolidate regexps for stripping whitespace (#82)
  * Only test against Jekyll 3 (#99)
  * Think about how i18n might work (#75)
  * Find author by reference (#106)
  * Drop support for Jekyll 2 (#105)
  * Add support for post image (#104)

### Minor Enhancements

  * Use Module#method_defined? (#83)
  * Use site.title for meta tag if available (#100)

### Development Fixes

  * Do not require [**jekyll-last-modified-at**](https://github.com/gjtorikian/jekyll-last-modified-at) in tests (#87)
  * Add Rubocop (#81)
  * Correct typo in tests (#102)
  * Simplify testing feed_meta tag (#101)
  * Quiet known warnings in tests (#103)

## 0.4.0 / 2015-12-30

  * Feed uses `site.title`, or `site.name` if `title` doesn't exist (#72)
  * Replace newlines with spaces in `title` and `summary` elements (#67)
  * Properly render post content with Jekyll (#73)
