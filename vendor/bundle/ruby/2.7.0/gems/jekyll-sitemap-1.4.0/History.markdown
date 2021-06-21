## 1.4.0 / 2019-11-21

### Minor Enhancements

  * Avoid overwriting an existing robots.txt (#246)

### Bug Fixes

  * Simulate `last_modified_at` injection by plugin (#256)

## 1.3.1 / 2019-03-25

### Bug Fixes

  * Update plugin metadata and dev environment (#244)

### Development Fixes

  * Lock requirement for `jekyll-last-modified-at` to `>= 1.0`

## 1.3.0 / 2019-03-21

  * Allow Jekyll v4 (still alpha)

### Documentation

  * Add PDF file exclusion documentation (#213)
  * Correct capitalization of GitHub (#207)

### Development Fixes

  * Use Ruby 2.3 and Rubocop 0.55 (#214)
  * chore(deps): rubocop-jekyll-0.3 (#227)

## 1.2.0 / 2018-01-25

### Minor Enhancements

  * Remove excluded static files from the sitemap (#166)
  * filter/replace static index.html paths to permalink (#170)

### Development Fixes

  * Condition the static file tests on Jekyll 3.4.2 and above (#167)
  * Update versions for Travis (#174)
  * Fix Travis Deploy (#173)
  * Test against Jekyll 3.4.x *and* latest 3.x (#177)
  * Define path with __dir__ (#186)
  * Style: Rubocop auto-correct (#195)
  * Test against Ruby 2.5 (#201)

### Documentation

  * Add note about use with Github Pages gem (#179)
  * Fix a couple of typos (#184)
  * Use plugins instead of gems in README config (#185)
  * Docs: set site.url in config (#172)

## 1.1.1 / 2017-04-11

  * Cut a new version to alleviate sha256 checksum issue on RubyGems.org (#165)

## 1.1.0 / 2017-04-10

### Minor Enhancements

  * escape& (#162)
  * feat: remove 404 pages from the sitemap. closes #113 (#164)

## 1.0.0 / 2017-01-06

  * No new changes

## 0.13.0 / 2017-01-05

### Minor Enhancements

  * Add sitemap.xsl if exists (#143)
  * Add robots.txt when none exists (#146)
  * Refactor and add sitemap to `site.pages` (#137)
  * DRY in sitemap.xml (#136)

### Documentation

  * Fix #134: Rename "Issues" to "Known Issues" (#135)
  * Fix #104: Add explanation in README for <lastmod> tag (#139)
  * Update copyright attribution (#149)

### Development Fixes

  * Travis should do a deep clone (#147)

## 0.12.0 / 2016-10-06

### Minor Enhancements

  * Don't set @site.config["time"] on sitemap generation (#131)
  * Use filters to clean up Liquid template (#128)

### Development Fixes

  * Appease Rubocop (#132)
  * Drop Addressable dependency (#133)

## 0.11.0 / 2016-07-08

  * Add Rubocop (#100)
  * Allow Travis to cache dependencies (#108)
  * Properly Escape URLs (#107)
  * Include PDF files in sitemap (#109)

## 0.10.0 / 2016-01-05

  * URI encode sitemap URLs (#85)
  * Do not include 'posts' collection twice (#92)
  * Fix GitHub Pages tests to test just the Jekyll version (#87)
  * Allow HTML files to end with `.xhtml` or `.htm` (#93)
  * Simplify whitespace regex for stripping whitespace (#96)

## 0.9.0 / 2015-09-21

  * Test against Jekyll 2, 3, and the GitHub Pages version. (#83)

## 0.8.1 / 2015-03-11

  * Do not assume all pages have changed (#35)
  * Remove duplicated range from regex (#73)

## 0.8.0 / 2015-02-03

  * Call each page `page` in pages loop in `sitemap.xml` for clarity (#64)
  * Remove `changefreq` (#34)
  * Remove `priority` (#33)
  * Don't strip 'index.html' when there is more to filename ## Minor Enhancements (#68)

## 0.7.0 / 2014-12-07

  * Make `site.baseurl` support more robust (#59)
  * Add `site.baseurl` to base site URL construction ## Development Fixes (#50)
  * Remove unnecessary spaces and escaping in README ## Bug Fixes (#58)

## 0.6.3 / 2014-11-11

  * Be backwards-compatible when `Site#in_source_dir` and `Site#in_dest_dir` don't exist (#57)

## 0.6.2 / 2014-11-08

### Bug Fixes

  * Don't attempt to read the sitemap upon page creation. (#52)
  * Use new secure methods to build source & dest paths. (#53)

## 0.6.1 / 2014-10-17

### Minor Enhancements

  * Strip excess whitespace (#40)

### Bug Fixes

  * Add UTC offset to `<lastmod>` to handle non-UTC timezones (#49)

### Development Fixes

  * Adding information about exclusion flag (#45)

## 0.6.0 / 2014-09-05

### Minor Enhancements

  * Include custom collections in the sitemap. (#30)
  * Use `post.last_modified_at` for post `<lastmod>` if available (#37)

## 0.5.1 / 2014-07-31

### Bug Fixes

  * Explicitly set sitemap layout to `nil` to avoid warning (#32)

## 0.5.0 / 2014-06-02

### Minor Enhancements

  * Allow users to exclude a page/post from the sitemap (#11)

## 0.4.1 / 2014-05-10

### Bug Fixes

  * Force sitemap layout to be `nil` (#16)
  * Correct seconds in timestamp for static files # Development Fixes (#24)
  * Upgrade to Rspec 3.0 and use `be_truthy` (#24)

## 0.4.0 / 2014-05-06

### Major Enhancements

  * Support Jekyll 2.0 (#12)

## 0.3.0 / 2014-05-05

### Minor Enhancements

  * Generate sitemap using html_pages (#10)

### Bug Fixes

  * Remove stray sitemap.xsl from template (#8)

### Development Fixes

  * Added travis (#6)
  * Better timezone support (#7)

## 0.2.0 / 2014-03-24

  * Loosen Jekyll requirement (#4)

## 0.1.0 / 2014-03-15

  * Birthday!
