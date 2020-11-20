## 2.6.1 / 2019-05-17

### Development Fixes

  * Test against Jekyll 4.x (#336)

## 2.6.0 / 2019-03-16

### Minor Enhancements

  * Twitter Image and Title (#330)

### Bug Fixes

  * Do not cache the drop payload for SeoTag (#306)
  * Update url of schema website (#296)

### Development Fixes

  * Relax version constraint on Bundler (#325)
  * chore(ci): Add Ruby 2.6, drop Ruby 2.3 (#326)
  * chore (ci): remove deprecated `sudo: false` in .travis.yml (#333)
  * Lint Ruby code with rubocop-jekyll gem (#302)
  * chore(deps): bump rubocop-jekyll to v0.4 (#320)
  * chore(deps): bump rubocop-jekyll to v0.3 (#316)
  * Correct RuboCop offenses in spec files (#319)

### Documentation

  * Rectify error in Usage documentation (#328)

## 2.5.0 / 2018-05-18

  * Docs: Prevent GitHub Pages from processing Liquid raw tag (#276)

### Documentation

  * Use gems config key for Jekyll &lt; 3.5.0 (#255)
  * docs/usage - replace &#34;below&#34; with correct link (#280)

### Development Fixes

  * Test against Ruby 2.5 (#260)
  * add tests for twitter.card types (#289)
  * Target Ruby 2.3 and Rubocop 0.56.0 (#292)

### Minor Enhancements

  * Add webmaster_verifications for baidu (#263)
  * Include page number in title (#250)
  * Configure default Twitter summary card type (V2) (#225)

## 2.4.0 / 2017-12-04

### Minor

  * Add meta generator (#236)
  * Consistently use self-closing tags (#246)
  * Strip null values from JSON-LD hash (#249)

### Documentation

  * Avoid deprecation warning when building docs (#243)

### Development Fixes

  * Test against latest Rubies (#242)
  * Use Nokigiri on CI (#181)

## 2.3.0

### Minor Enhancements

  * Use canonical_url specified in page if present #211
  * Fix for image.path causing an invalid url error #228
  * Ensure `site.data.authors` is properly formatted before attempting to retrieve author meta #227
  * Convert author, image, and JSON-LD to dedicated drops #229
  * Cache parsed template #231
  * Define path with `__dir__` #232

### Documentation

  * gems: is deprecated in current Jekyll version of github-pages #230

## 2.2.3

  * Guard against the author's Twitter handle being Nil when stripping @'s #203
  * Guard against empty title or description strings #206

## 2.2.2

### Minor Enhancements

  * Guard against arrays in subhashes #197
  * Guard against invalid or missing URLs #199

### Development fixes

  * Remove dynamic GitHub Pages logic from Gemfile #194

## 2.2.1

  * Convert template logic to a Liquid Drop (significant performance improvement) (#184)
  * Fix for JSON-LD validation warning for images missing required properties (#183)

## 2.2.0

### Major Enhancements

  * Add author meta (#103)
  * Add og:locale support #166
  * Add support for Bing and Yandex webmaster tools. Closes #147 (#148)
  * Add SEO author and date modified to validate JSON-LD output (#151)

### Minor Enhancements

  * Use `|` for title separator (#162)
  * Use `og:image` for twitter image (#174)

### Development Fixes

  * Style fixes (#170, #157, #149)
  * Test against latest version of Jekyll (#171)
  * Bump dev dependencies (#172)
  * Remove Rake dependency (#180)

## 2.1.0

### Major Enhancement

  * Use new URL filters (#123)

### Minor Enhancements

  * Wraps logo image json data in a publisher property (#133)
  * Fix duplicated `escape_once` (#93)
  * Simplify minify regex (#125)
  * Don't mangle text with newlines #126

### Documentation

  * Add front matter default example for image (#132)
  * Fix tiny typo (#106)
  * add example usage of social profiles (#139)

### Development

  * Inherit Jekyll's rubocop config for consistency (#109)
  * Correct spelling in .travis.yml (#112)
