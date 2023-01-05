## [3.4.2](https://github.com/mmistakes/minimal-mistakes/releases/tag/3.4.2)

### Enhancements

- Improve UX of static comment forms. [#448](https://github.com/mmistakes/minimal-mistakes/issues/448)

## [3.4.1](https://github.com/mmistakes/minimal-mistakes/releases/tag/3.4.1)

### Enhancements

- Add `staticman.filename` configuration with UNIX timestamp for sorting data files. example ~> `comment-1470943149`.

### Bug Fixes

- Don't add `<a>` to author name if URL is blank.

## [3.4.0](https://github.com/mmistakes/minimal-mistakes/releases/tag/3.4.0)

### Enhancements

- Support static-based commenting via [Staticman](https://staticman.net/) for sites hosted with GitHub Pages. [#424](https://github.com/mmistakes/minimal-mistakes/issues/424)

## [3.3.7](https://github.com/mmistakes/minimal-mistakes/releases/tag/3.3.7)

### Bug Fixes

- Re-enabled Jekyll plugins in `_config.yml` in case they aren't autoloaded in `Gemfile`. [#417](https://github.com/mmistakes/minimal-mistakes/issues/417)

### Enhancements

- Fallback to `site.github.url` for use in `{{ base_path }}` when `site.url` is `nil`.
- Replace Sass and Autoprefixer `npm` build scripts with [Jekyll's built-in asset support](https://jekyllrb.com/docs/assets/). [#333](https://github.com/mmistakes/minimal-mistakes/issues/333)

### Maintenance

- Document `site.repository` and its role with [`github-metadata`](https://github.com/jekyll/github-metadata) gem.
- Add sample [archive page with content](https://mmistakes.github.io/minimal-mistakes/archive-layout-with-content/) for testing styles on demo site.

## [3.3.6](https://github.com/mmistakes/minimal-mistakes/releases/tag/3.3.6)

### Bug Fixes

- Fix blank `site.teaser` bug. [#412](https://github.com/mmistakes/minimal-mistakes/issues/412)

## [3.3.5](https://github.com/mmistakes/minimal-mistakes/releases/tag/3.3.5)

### Enhancements

- Add English default text `site.locale` strings. [#407](https://github.com/mmistakes/minimal-mistakes/issues/407)
- Add Portuguese localized UI text. [#411](https://github.com/mmistakes/minimal-mistakes/pull/411)
- Add Italian localized UI text. [#409](https://github.com/mmistakes/minimal-mistakes/pull/409)

### Maintenance

- Remove unused Google AdSense variables in `_config.yml`. [#404](https://github.com/mmistakes/minimal-mistakes/issues/404)
- Update `Gemfile` instructions for using `github-pages` vs. native `jekyll` gems.
- Disable `gems:` in `_config.yml` and enable plugins with Bundler instead.
- Add `repository` to `_config.yml` to suppress GitHub Pages error `Liquid Exception: No repo name found.`

## [3.3.4](https://github.com/mmistakes/minimal-mistakes/releases/tag/3.3.4)

### Enhancements

- Add support for configurable feed URL to use a service like FeedBurner instead of linking directly to `feed.xml` in `<head>` and the site footer. [#378](https://github.com/mmistakes/minimal-mistakes/issues/378), [#379](https://github.com/mmistakes/minimal-mistakes/pull/379), [#406](https://github.com/mmistakes/minimal-mistakes/pull/406)
- Add Turkish localized UI text. [#403](https://github.com/mmistakes/minimal-mistakes/pull/403)

### Maintenance

- Update gems: `activesupport` (4.2.7), `ffi` (1.9.14), `github-pages` (88), `jekyll-redirect-from` (0.11.0), `jekyll-watch` (1.5.0).

## [3.3.3](https://github.com/mmistakes/minimal-mistakes/releases/tag/3.3.3)

### Enhancements

- Make footer stick to the bottom of the page.

### Bug Fixes

- Fix `gallery` size bug [#402](https://github.com/mmistakes/minimal-mistakes/issues/402)

### Maintenance

- Set default `lang` to `en`.

## [3.3.2](https://github.com/mmistakes/minimal-mistakes/releases/tag/3.3.2)

### Bug Fixes

- Fix JavaScript that triggers "sticky" sidebar to avoid layout issues on screen sizes < `1024px`. [#396](https://github.com/mmistakes/minimal-mistakes/issues/396)

## [3.3.1](https://github.com/mmistakes/minimal-mistakes/releases/tag/3.3.1)

### Enhancements

- Enable image popup on < 500px wide screens. [#385](https://github.com/mmistakes/minimal-mistakes/issues/385)
- Indicate the relationship between component URLs in a paginated series by applying `rel="prev"` and `rel="next"` to pages that use `site.paginator`. [#253](https://github.com/mmistakes/minimal-mistakes/issues/253)
- Improve link posts in archive listings. [#276](https://github.com/mmistakes/minimal-mistakes/issues/276)

### Maintenance

- Update gems: `github-pages` (86), `ffi` 1.9.13, `jekyll-mentions` 1.1.3, and `rouge` 1.11.1
- Fix note about custom sidebar content appearing below author profile. [#388](https://github.com/mmistakes/minimal-mistakes/issues/388)

## [3.2.13](https://github.com/mmistakes/minimal-mistakes/releases/tag/3.2.13)

### Enhancements

- Add English default UI text for Canada, Great Britain, and Australia. [#377](https://github.com/mmistakes/minimal-mistakes/issues/377)
- Switch default locale from `en-US` to `en`.

## [3.2.12](https://github.com/mmistakes/minimal-mistakes/releases/tag/3.2.12)

### Enhancements

- Remove window width "magic number" from sticky sidebar check in `main.js` for improved flexibility. [#375](https://github.com/mmistakes/minimal-mistakes/pull/375)

### Bug Fixes

- Fix author override conditional where a missing `authors.yml` would show broken sidebar content. Defaults to `site.author`. [#376](https://github.com/mmistakes/minimal-mistakes/pull/376)

## [3.2.11](https://github.com/mmistakes/minimal-mistakes/releases/tag/3.2.11)

### Bug Fixes

- Fix disappearing author sidebar links [#372](https://github.com/mmistakes/minimal-mistakes/issues/372)

### Maintenance

- Update gems: `github-pages` (84), `jekyll-github-metadata` 2.0.2, and `kramdown` 1.11.1
- Update vendor JavaScript: jQuery 1.12.4, Stickyfill.js 1.1.4
- Update Font Awesome 4.6.3

## [3.2.10](https://github.com/mmistakes/minimal-mistakes/releases/tag/3.2.10)

### Maintenance

- Add `CONTRIBUTING.md`

## [3.2.9](https://github.com/mmistakes/minimal-mistakes/releases/tag/3.2.9)

### Enhancements

- Add support for [header overlay images](https://mmistakes.github.io/minimal-mistakes/docs/layouts/#header-overlay) for Open Graph images. [#358](https://github.com/mmistakes/minimal-mistakes/pull/358)

### Bug Fixes

- Fix `Person` typo Schema.org type [#358](https://github.com/mmistakes/minimal-mistakes/pull/358)

### Maintenance

- Update `github-pages` gem and dependencies.
- Remove `minutes_read` to avoid awkward reading time wording [#356](https://github.com/mmistakes/minimal-mistakes/issues/356)

## [3.2.8](https://github.com/mmistakes/minimal-mistakes/releases/tag/3.2.8)

### Bug Fixes

- Remove `cursor: pointer` that appears on white-space surrounding author side list items and links. [#354](https://github.com/mmistakes/minimal-mistakes/pull/354)

### Maintenance

- Add contributing information to `README.md`. [#357](https://github.com/mmistakes/minimal-mistakes/issues/357)

## [3.2.7](https://github.com/mmistakes/minimal-mistakes/releases/tag/3.2.7)

### Enhancements

- Add French localized UI text. [#346](https://github.com/mmistakes/minimal-mistakes/pull/346)

### Bug Fixes

- Fix branch logic for Yandex and Alexa in `seo.html`. [#348](https://github.com/mmistakes/minimal-mistakes/pull/348)

## [3.2.6](https://github.com/mmistakes/minimal-mistakes/releases/tag/3.2.6)

### Bug Fixes

- Fix error `Liquid Exception: divided by 0 in _includes/archive-single.html, included in _layouts/single.html` caused by null `words_per_minute` in `_config.yml`. [#345](https://github.com/mmistakes/minimal-mistakes/pull/345)

## [3.2.5](https://github.com/mmistakes/minimal-mistakes/releases/tag/3.2.5)

### Bug Fixes

- Fix link color in hero overlay to be white.
- Remove underlines from archive item titles.

## [3.2.4](https://github.com/mmistakes/minimal-mistakes/releases/tag/3.2.4)

### Enhancements

- Improve text alignment of masthead, hero overlay, page footer to be flush left and remove awkward white-space gaps. [#342](https://github.com/mmistakes/minimal-mistakes/issues/342)
- Add Spanish localized UI text. [#338](https://github.com/mmistakes/minimal-mistakes/pull/338)

### Bug Fixes

- Fix alignment of icons in author sidebar [#341](https://github.com/mmistakes/minimal-mistakes/issues/341)

### Maintenance

- Add background color to page footer to set it apart from main content. [#342](https://github.com/mmistakes/minimal-mistakes/issues/342)
- Add terms and privacy policy to theme's demo site. [#343](https://github.com/mmistakes/minimal-mistakes/issues/343)
- Update screenshots found in theme documentation.

## [3.2.3](https://github.com/mmistakes/minimal-mistakes/releases/tag/3.2.3)

### Enhancements

- Add [Discourse](https://www.discourse.org/) as a commenting provider. [#335](https://github.com/mmistakes/minimal-mistakes/pull/335)

## [3.2.2](https://github.com/mmistakes/minimal-mistakes/releases/tag/3.2.2)

### Enhancements

- Add support for image captions in Magnific Popup overlays via the [`gallery`](https://mmistakes.github.io/minimal-mistakes/docs/helpers/#gallery) helper. [#334](https://github.com/mmistakes/minimal-mistakes/issues/334)

## [3.2.1](https://github.com/mmistakes/minimal-mistakes/releases/tag/3.2.1)

### Bug Fixes

- Remove need for "double tapping" masthead menu links on iOS devices. [#315](https://github.com/mmistakes/minimal-mistakes/issues/315)

### Maintenance

- Add `ISSUE_TEMPLATE.md` for improve issue submission process.

## [3.2.0](https://github.com/mmistakes/minimal-mistakes/releases/tag/3.2.0)

### Bug Fixes

- Fix missing category/tag links in post footer due to possible conflict with `site.tags` and `site.categories`. [#329](https://github.com/mmistakes/minimal-mistakes/issues/329#issuecomment-222375568)

## [3.1.8](https://github.com/mmistakes/minimal-mistakes/releases/tag/3.1.8)

### Bug Fixes

- Fix `Liquid Exception: undefined method 'gsub' for nil:NilClass in _layouts/single.html` error when `page.title` is null. `<h1>` element is now conditional if `title: ` is not set for a `page` or collection item. [#312](https://github.com/mmistakes/minimal-mistakes/issues/312)

### Maintenance

- Remove duplicate `fa-twitter` and `fa-twitter-square` classes from `_utilities.scss`. [#302](https://github.com/mmistakes/minimal-mistakes/issues/302)

- Document installing additional Jekyll gem dependencies when using `gem "jekyll"` instead of `gem "github-pages"` to avoid any errors on run. [#305](https://github.com/mmistakes/minimal-mistakes/issues/305)

## [3.1.7](https://github.com/mmistakes/minimal-mistakes/releases/tag/3.1.7)

### Enhancements

- Add translation key for "Recent Posts" used in home page `index.html`. [#316](https://github.com/mmistakes/minimal-mistakes/pull/316)

### Maintenance

- Small fix to avoid underlying the whitespace between icons and related text when hovering. [#303](https://github.com/mmistakes/minimal-mistakes/pull/303)

## [3.1.6](https://github.com/mmistakes/minimal-mistakes/releases/tag/3.1.6)

### Maintenance

- Update gem dependencies. Run `bundle` to update `Gemfile.lock`.

## [3.1.5](https://github.com/mmistakes/minimal-mistakes/releases/tag/3.1.5)

### Maintenance

- Fix `www` and `https` links in author profile include [#293](https://github.com/mmistakes/minimal-mistakes/pull/293)

## [3.1.4](https://github.com/mmistakes/minimal-mistakes/releases/tag/3.1.4)

### Enhancements

- Add overlay_filter param to hero headers [#298](https://github.com/mmistakes/minimal-mistakes/pull/298)

## [3.1.3](https://github.com/mmistakes/minimal-mistakes/releases/tag/3.1.3)

### Enhancements

- Improve `site.locale` documentation [#284](https://github.com/mmistakes/minimal-mistakes/issues/284)
- Remove ProTip note about protocol-less `site.url` as it is an anti-pattern [#288](https://github.com/mmistakes/minimal-mistakes/issues/288)

### Bug Fixes

- Fix `og_image` URL in seo.html [#277](https://github.com/mmistakes/minimal-mistakes/issues/277)
- Fix `author_profile` toggle when assigned in a `_layout` [#285](https://github.com/mmistakes/minimal-mistakes/issues/285)
- Fix typo in `build:all` npm script [#283](https://github.com/mmistakes/minimal-mistakes/pull/283)
- Fix URL typo documentation [#287](https://github.com/mmistakes/minimal-mistakes/issues/287)
- SEO author bug. If `twitter.username` is set and `author.twitter` is `nil` bad things happen. [#289](https://github.com/mmistakes/minimal-mistakes/issues/289)

## [3.1.2](https://github.com/mmistakes/minimal-mistakes/releases/tag/3.1.2)

### Enhancements

- Explain how to use `nav_list` helper in [documentation](https://mmistakes.github.io/minimal-mistakes/docs/helpers/#navigation-list).
- Reduce left/right padding on smaller screens to increase width of main content column.

### Bug Fixes

- Fix alignment issues with related posts [#273](https://github.com/mmistakes/minimal-mistakes/issues/273) and "Follow" button in author profile [#274](https://github.com/mmistakes/minimal-mistakes/issues/274).

## [3.1.1](https://github.com/mmistakes/minimal-mistakes/releases/tag/3.1.1)

### Bug Fix

- Fixed reading time bug when `words_per_minute` wasn't set in `_config.yml` [#271](https://github.com/mmistakes/minimal-mistakes/issues/271)

## [3.1.0](https://github.com/mmistakes/minimal-mistakes/releases/tag/3.1.0)

### Enhancements

- Updated [Font Awesome](https://fortawesome.github.io/Font-Awesome/whats-new/) to version 4.6.1
- Added optional GitHub and Bitbucket links to footer if set on `site.author` in `_config.yml`.

### Bug Fixes
- Fixed Bitbucket URL typo in author sidebar.

## [3.0.3](https://github.com/mmistakes/minimal-mistakes/releases/tag/3.0.3)

### Enhancements

- Rebuilt the entire theme: layouts, includes, stylesheets, scripts, you name it.
- Refreshed the look and feel while staying true to the original design of the theme (author sidebar/main content).
- Replaced grid system with [Susy](http://susy.oddbird.net/).
- Replaced Grunt tasks with `npm` scripts.
- Removed Google Fonts and replaced with system fonts to improve performance (they can be [added back](https://mmistakes.github.io/minimal-mistakes/docs/stylesheets/) if desired)
- Greatly improved [theme documentation](https://mmistakes.github.io/minimal-mistakes/docs/quick-start-guide/).
- Increased the amount of sample posts, sample pages, and sample collections to throughly test the theme and edge-cases.
- Moved all sample content and assets out of `master` to keep it as clean as possible for forking.
- Added new layouts for `splash` pages, archives for [`jekyll-archives`](https://github.com/jekyll/jekyll-archives) if enabled, and [`compress.html`](https://github.com/penibelst/jekyll-compress-html) to improve performance.
- Added taxonomy links to posts (tags and categories).
- Added optional "reading time" meta data.
- Improved Liquid used for Twitter Cards and Open Graph data in `<head>`.
- Improved `gallery` include helper and added `feature_row` for use with splash page layout.
- Added Keybase.io, author web URI, and Bitbucket optional links to sidebar.
- Add `feed.xml` link to footer.
- Added a [UI text data file](https://mmistakes.github.io/minimal-mistakes/docs/ui-text/) to easily change all text found in the theme.
- Added LinkedIn to optional social share buttons.
- Added Facebook, Google+, and custom commenting options in addition to Disqus.
- Added optional breadcrumb links.

## [2.2.1](https://github.com/mmistakes/minimal-mistakes/releases/tag/2.2.1)

## [2.2.0](https://github.com/mmistakes/minimal-mistakes/releases/tag/2.2.0)

### Enhancements

- Add support for Jekyll 3.0
- Minor updates to syntax highlighting CSS and theme documentation

## [2.1.3](https://github.com/mmistakes/minimal-mistakes/releases/tag/2.1.3)

### Enhancements

- Cleaner print styles that remove the top navigation, social sharing buttons, and other elements not needed when printed.

## [2.1.2](https://github.com/mmistakes/minimal-mistakes/releases/tag/2.1.2)

### Enhancements

- Add optional CodePen icon/url to author side bar [#156](https://github.com/mmistakes/minimal-mistakes/pull/156)
- Documented Stackoverflow username explanation in `_config.yml` [#157](https://github.com/mmistakes/minimal-mistakes/pull/157)
- Simplified Liquid in `post-index.html` to better handle year listings [#166](https://github.com/mmistakes/minimal-mistakes/pull/166)

### Bug Fixes

- Cleanup Facebook related Open Graph meta tags [#149](https://github.com/mmistakes/minimal-mistakes/issues/149)
- Corrected minor typos [#158](https://github.com/mmistakes/minimal-mistakes/pull/158) [#175](https://github.com/mmistakes/minimal-mistakes/issues/175)

## [2.1.1](https://github.com/mmistakes/minimal-mistakes/releases/tag/2.1.1)

### Enhancements

- Add optional XING profile link to author sidebar
- Include open graph meta tags for feature image (if assigned) [#149](https://github.com/mmistakes/minimal-mistakes/issues/149)
- Create an include for feed footer

### Bug Fixes

- Remove http protocol from Google search form on sample 404 page
- Only show related posts if there are one or more available
- Fix alignment of email address link in author sidebar

## [2.1.0](https://github.com/mmistakes/minimal-mistakes/releases/tag/2.1.0)

### Enhancements

- Add optional social sharing buttons ([#42](https://github.com/mmistakes/minimal-mistakes/issues/42))

![social sharing buttons](https://cloud.githubusercontent.com/assets/1376749/5860522/d9f28a96-a22f-11e4-9b83-940a3a9a766a.png)

- Add Soundcloud, YouTube ([#95](https://github.com/mmistakes/minimal-mistakes/pull/95)), Flickr ([#119](https://github.com/mmistakes/minimal-mistakes/pull/119)), and Weibo ([#116](https://github.com/mmistakes/minimal-mistakes/pull/116)) icons for use in author sidebar.
- Fix typos in posts and documentation and remove references to Less
- Include note about Octopress gem being optional
- Post author override support extended to the Atom feed ([#71](https://github.com/mmistakes/minimal-mistakes/pull/71))
- Only include email address in feed if specified in `_config.yml` or author `_data`
- Wrap all page content in `#main` to harmonize article and post index styles ([#86](https://github.com/mmistakes/minimal-mistakes/issues/86))
- Include new sample feature images for posts and pages
- Table of contents improvements: fix collapse toggle, indent nested elements, show on small screens, and create an `_include` for reusing in posts and pages.
- Include note about running Jekyll with `bundle exec` when using Bundler
- Fix home page path in top navigation
- Remove Google Authorship ([#120](https://github.com/mmistakes/minimal-mistakes/issues/120))
- Remove duplicate author content that displayed in `div.article-author-bottom`
- Removed unused `_sass/print.scss` styles
- Improve comments in `.scss` files

## [2.0.0](https://github.com/mmistakes/minimal-mistakes/releases/tag/v2.0)

## [1.3.3](https://github.com/mmistakes/minimal-mistakes/releases/tag/1.3.3)

### Enhancements

- Added new icons and profile links for Stackoverflow, Dribbble, Pinterest, Foursquare, and Steam to the author bio sidebar.
- Cleaned up the Kramdown auto table of contents styling to be more readable
- Removed page width specific .less stylesheets and created mixins for easier updating
- Removed Modernizr since it wasn't being used
- Added pages to sitemap.xml
- Added category: to rake new_post task
- Minor typographic changes

### Bug Fixes

- Corrected various broken links in README and Theme Setup.

## [1.3.1](https://github.com/mmistakes/minimal-mistakes/releases/tag/1.3.1)

### Enhancements

- Cleaned up table of contents styling
- Reworked top navigation to be a better experience on small screens. Nav items now display vertically when the menu button is tapped, revealing links with larger touch targets.

![menu animation](https://camo.githubusercontent.com/3fbd8c1326485f4b1ab32c0005c0fca7660b5d31/68747470733a2f2f662e636c6f75642e6769746875622e636f6d2f6173736574732f313337363734392f323136343037352f31653366303663322d393465372d313165332d383961612d6436623636376562306564662e676966)

## [1.2.0](https://github.com/mmistakes/minimal-mistakes/releases/tag/1.2.0)

### Bug Fixes

- Table weren't filling the entire width of the content container. They now scale at 100%. Thanks [@dhruvbhatia](https://github.com/dhruvbhatia)

### Enhancements

- Decreased spacing between Markdown footnotes
- Removed dark background on footer
- Removed UPPERCASE styling on post titles in the index listing

## [1.1.4](https://github.com/mmistakes/minimal-mistakes/releases/tag/1.1.4)

### Bug Fixes

- Fix top navigation bug issue ([#10](https://github.com/mmistakes/minimal-mistakes/issues/10)) for real this time. Remember to clear your floats kids.

## [1.1.3](https://github.com/mmistakes/minimal-mistakes/releases/tag/1.1.3)

### Bug Fixes

- Fix top navigation links that weren't click able on small viewports (Issue [#10](https://github.com/mmistakes/minimal-mistakes/issues/10)).
- Remove line wrap from top navigation links that may span multiple lines.

## [1.1.2](https://github.com/mmistakes/minimal-mistakes/releases/tag/1.1.2)

### Enhancements

- Added Grunt build script for compiling Less/JavaScript and optimizing image assets.
- Added support for large image summary Twitter card.
- Stylesheet adjustments

## [1.1.1](https://github.com/mmistakes/minimal-mistakes/releases/tag/1.1.1)

### Bug Fixes

- Removed [Typeplate](http://typeplate.com/) styles. Was [causing issues with newer versions of Less](https://github.com/typeplate/typeplate.github.io/issues/108) and is no longer maintained.

### Enhancements

- Added [image attribution](http://mmistakes.github.io/minimal-mistakes/theme-setup/#feature-images) for post and page feature images.
- Added [404 page](http://mmistakes.github.io/minimal-mistakes/404.html).
- Cleaned up various Less variables to better align with naming conventions used in other MM Jekyll themes.
- Removed Chrome Frame references.
- Added global CSS3 transitions to text and block elements.
- Improved typography in a few places.

## [1.0.2](https://github.com/mmistakes/minimal-mistakes/releases/tag/v1.0.2)

### Enhancements

- Google Analytics, Google Authorship, webmaster verifies, and Twitter card meta are now optional.

## [1.0.1](https://github.com/mmistakes/minimal-mistakes/releases/tag/v1.0.1)