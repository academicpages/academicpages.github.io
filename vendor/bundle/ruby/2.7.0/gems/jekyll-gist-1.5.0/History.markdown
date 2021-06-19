## HEAD

### Documentation

  * replace &#39;plugins&#39; key in config with &#39;gems&#39; (#46)
  * Docs: Remove username in gist (#54)

### Development Fixes

  * Remove testing for Jekyll 2.x
  * Requires Ruby > 2.1
  * Add release script
  * Inherit Jekyll&#39;s rubocop config for consistency (#48)
  * define path with __dir__ (#47)


## 1.4.1 / 2017-06-21

  * Don't ask .empty? until it's a String. (#38)
  * rename Liquid 4 `has_key?` to `key?` to add compatibility for liquid 4 (#41)
  * Test against Ruby 2.1 to 2.4 (#45)

## 1.4.0 / 2015-12-01

  * Allow `noscript` fallback to be disabled (#29)
  * Use Octokit to fetch Gist content when passed `JEKYLL_GITHUB_TOKEN` in env(#28)

## 1.3.5 / 2015-10-23

  * Fix encoding error for `noscript` code (#23)
  * Test against Jekyll 3, 2, and the github-pages gem (#19)

## 1.3.4 / 2015-08-28

  * Catch `TimeoutError` to further support 1.9.3 (#16)

## 1.3.3 / 2015-08-20

  * Fix gemspec to allow Ruby 1.9.3 (relates to #14)

## 1.3.2 / 2016-08-19

  * Re-add support for Ruby 1.9.3. Fixes #11 for 1.9.3 (#14)
  * Replaced `OpenURI` with `Net::HTTP` and introduced timeout of 3 seconds (#11)

## 1.3.1 / 2015-08-16

  * Replaced `OpenURI` with `Net::HTTP` and introduced timeout of 3 seconds (#11)

## 1.3.0 / 2015-08-05

  * Added an `noscript` fallback for browsers without JavaScript enabled. (#7)

## 1.2.1 / 2015-03-22

  * Use `has_key?` (#6)

## 1.2.0 / 2015-03-21

### Minor Enhancements

  * Allow variables as parameters (#4)

### Development Fixes

  * Fix RSpec deprecation warning (#5)

## 1.1.0 / 2014-06-18

### Minor Enhancements

  * Update regex to allow for new sha-ish ids in Gist. (#1)

## 1.0.0 / 2014-06-01

  * Birthday!
