## Unreleased

### Bug Fixes

- Fix unlisted YouTube video embeds in documentation/test sites. [#3649](https://github.com/mmistakes/minimal-mistakes/issues/3649)
- Fix error in Algolia search script when returning a hit that without `html` and `hightlight.html`. [#3101](https://github.com/mmistakes/minimal-mistakes/issues/3101) [#3102](https://github.com/mmistakes/minimal-mistakes/pull/3102)
- Fix links to Font Awesome gallery. [#3599](https://github.com/mmistakes/minimal-mistakes/pull/3599)
- Fix GreedyNav.js attribution link. [#3553](https://github.com/mmistakes/minimal-mistakes/pull/3553)
- Fix typo about loading JavaScript in layout documentation. [#3350](https://github.com/mmistakes/minimal-mistakes/pull/3350)
- Fix inline code style not applied to stylized text. [#3253](https://github.com/mmistakes/minimal-mistakes/pull/3253)
- Fix documentation typos. [#3232](https://github.com/mmistakes/minimal-mistakes/pull/3232) [#3318](https://github.com/mmistakes/minimal-mistakes/pull/3318)
- Fix Keybase icon in author sidebar. [#3221](https://github.com/mmistakes/minimal-mistakes/pull/3221)
- Fix sort order of Staticman comments when data files aren't named alphabetically. [#3184](https://github.com/mmistakes/minimal-mistakes/pull/3184)
- Fix `layout: compress` issue with HTML comment in video include. [#3117](https://github.com/mmistakes/minimal-mistakes/pull/3117)
- Add Magnific Popup class to anchors that only contain an `img` element. [#3111](https://github.com/mmistakes/minimal-mistakes/issues/3111) [#3114](https://github.com/mmistakes/minimal-mistakes/pull/3114)
- Enable Magnific Popups on anchors only when they wrap an `<img>` element. [#3114](https://github.com/mmistakes/minimal-mistakes/pull/3114)
- Fix heading level of related posts section from `h4` to `h2` to improve accessibility and SEO. [#3064](https://github.com/mmistakes/minimal-mistakes/pull/3064)
- Fix grammar error in German localized UI text string. [#3063](https://github.com/mmistakes/minimal-mistakes/pull/3063)
- Remove site.url from first breadcrumb link. [#3051](https://github.com/mmistakes/minimal-mistakes/pull/3051)

### Enhancements

- Update breadcrumbs conditional to enable/disable them via Front Matter on pages using `layout: single`. [#3096](https://github.com/mmistakes/minimal-mistakes/pull/3096) [#3669](https://github.com/mmistakes/minimal-mistakes/pull/3669)
- Remove Internet Explorer 9 upgrade notice. [#3666](https://github.com/mmistakes/minimal-mistakes/pull/3666)
- Add Kiswahili localized UI text strings. [#3489](https://github.com/mmistakes/minimal-mistakes/pull/3489)
- Exclude `main.scss` from Lunr search index.
- Allow `site.pages` to be indexed and searched via Lunr. [#3352](https://github.com/mmistakes/minimal-mistakes/pull/3352)
- Update jQuery to v3.6.0. [#3254](https://github.com/mmistakes/minimal-mistakes/pull/3254)
- Use notice `<a>` colors for blockquotes that have `notice--` classes applied. [#3140](https://github.com/mmistakes/minimal-mistakes/pull/3140) [#3068](https://github.com/mmistakes/minimal-mistakes/issues/3068)
- Add sameAs itemprop to author link. [#3087](https://github.com/mmistakes/minimal-mistakes/pull/3087)
- Automatically close invalid PRs using GitHub Actions. [#3313](https://github.com/mmistakes/minimal-mistakes/pull/3313)
- Update and add missing Brazilian Portuguese translations. [#3204](https://github.com/mmistakes/minimal-mistakes/pull/3204)
- Add link to documentation clarifying how to add plugins. [#3181](https://github.com/mmistakes/minimal-mistakes/pull/3181)
- Add optional label attribute for utterances comments. [#3128](https://github.com/mmistakes/minimal-mistakes/pull/3128)
- Bump path-parse from 1.0.6 to 1.0.7. [#3116](https://github.com/mmistakes/minimal-mistakes/pull/3116)
- Add missing Danish translations. [#3095](https://github.com/mmistakes/minimal-mistakes/pull/3095)
- Add ARIA role to search forms. [#3086](https://github.com/mmistakes/minimal-mistakes/pull/3086)
- Add overflow scroll bar to sticky table of contents that are taller than the viewport's height. [#2874](https://github.com/mmistakes/minimal-mistakes/pull/2874)
- Add Microformats markup. [#3052](https://github.com/mmistakes/minimal-mistakes/pull/3052)
- Add instructions on how to unminify `main.js` for easier browser debugging. [#3055](https://github.com/mmistakes/minimal-mistakes/pull/3055)

## [4.24.0](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.24.0)

### Bug Fixes

- Fix README text for Gumshoejs license. [#3024](https://github.com/mmistakes/minimal-mistakes/pull/3024)
- Remove `tabindex="-1"` from `input` elements in `search.html` layout to allow them to be accessible by keyboard. [#2982](https://github.com/mmistakes/minimal-mistakes/issues/2982)
- Fix broken sidebar image in sample post. [#3013](https://github.com/mmistakes/minimal-mistakes/issues/3013)
- Fix broken links in Upgrading documentation. [#3004](https://github.com/mmistakes/minimal-mistakes/issues/3004)

### Enhancements

- Remove IE9 flexbox fallback. [#3042](https://github.com/mmistakes/minimal-mistakes/pull/3042)
- Remove `h2` from skip links navigation as it is not important for site structure. [#3012](https://github.com/mmistakes/minimal-mistakes/pull/3012)
- Loads Font Awesome asynchronously. [#2967](https://github.com/mmistakes/minimal-mistakes/pull/2967)
- Replace custom search icon SVG with Font Awesome icon. [#2774](https://github.com/mmistakes/minimal-mistakes/pull/2774)
- Adds support for giscus comments. [#3022](https://github.com/mmistakes/minimal-mistakes/pull/3022)

## [4.23.0](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.23.0)

### Enhancements

- Add Arabic (عربي) localized UI text strings. [#2936](https://github.com/mmistakes/minimal-mistakes/pull/2936)
- Update onchange and uglify-js dependencies.
- Document head and footer `custom.html` includes. [#2815](https://github.com/mmistakes/minimal-mistakes/pull/2815)
- Color notices based on skin colors instead of fixed values. [#2887](https://github.com/mmistakes/minimal-mistakes/pull/2887)
- Add configurable datetime format. [#2844](https://github.com/mmistakes/minimal-mistakes/pull/2844)
- Add Baidu site verification [#2830](https://github.com/mmistakes/minimal-mistakes/pull/2830)
- Add `alt` attribute to site logo. [#2529](https://github.com/mmistakes/minimal-mistakes/issues/2529) [#2824](https://github.com/mmistakes/minimal-mistakes/issues/2824)

### Bug Fixes

- Fix menu toggle to properly show close icon when open.
- Fix Jekyll environment note in configuration documentation. [#2912](https://github.com/mmistakes/minimal-mistakes/issues/2912)
- Fix typo in Helpers documentation. [#2940](https://github.com/mmistakes/minimal-mistakes/pull/2940)
- Remove all references to official public Staticman API instance. [#2818](https://github.com/mmistakes/minimal-mistakes/issues/2818) [#2831](https://github.com/mmistakes/minimal-mistakes/pull/2831)
- Remove Google Search CSS. [#2852](https://github.com/mmistakes/minimal-mistakes/issues/2852) [#2855](https://github.com/mmistakes/minimal-mistakes/pull/2855)

## [4.22.0](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.22.0)

### Bug Fixes

- Remove Google Search script from `404.md`. [#2597](https://github.com/mmistakes/minimal-mistakes/issues/2597) [#2737](https://github.com/mmistakes/minimal-mistakes/pull/2737) [#2789](https://github.com/mmistakes/minimal-mistakes/pull/2789)
- Fix Font Awesome icon color in `contrast`, `dark`, `mint`, `neon`, `plum`, and `sunrise` skins. [#2724](https://github.com/mmistakes/minimal-mistakes/issues/2724)

### Enhancements

- Allow custom sorting for collections. [#2723](https://github.com/mmistakes/minimal-mistakes/pull/2723)
- Use `sort_natural` instead of custom Liquid logic to sort tags and categories. [#2756](https://github.com/mmistakes/minimal-mistakes/pull/2756)
- Add configuration option to toggle off RSS feed link in `<head>` and site footer. [#2787](https://github.com/mmistakes/minimal-mistakes/pull/2787)
- Upgrade Lunrjs to 2.3.9 and switch to `relative_url`. [#2805](https://github.com/mmistakes/minimal-mistakes/pull/2805)
- Adds `.webp` to list of supported image extensions for the image popup lightbox. [#2788](https://github.com/mmistakes/minimal-mistakes/pull/2788)
- Add Hebrew localized UI text strings. [#2760](https://github.com/mmistakes/minimal-mistakes/pull/2760)
- Update documentation to include `toc_sticky` parameter's description. [#2741](https://github.com/mmistakes/minimal-mistakes/pull/2741)
- Update Indonesian localized UI text strings. [#2731](https://github.com/mmistakes/minimal-mistakes/pull/2731)
- Update remote theme documentation. [#2734](https://github.com/mmistakes/minimal-mistakes/pull/2734)
- Update allejo/jekyll-toc to v1.1.0, skip headings without an ID. [#2752](https://github.com/mmistakes/minimal-mistakes/pull/2752)
- Allow custom gradient for page header overlay. [#2806](https://github.com/mmistakes/minimal-mistakes/pull/2806)

## [4.21.0](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.21.0)

### Bug Fixes

- Fix greedy navigation by improving reliability of remaining space for visible links. [#2664](https://github.com/mmistakes/minimal-mistakes/issues/2664)
- Collapse white-space in `figure` helper to fix issues when used in Markdown ordered and unordered lists. [#2697](https://github.com/mmistakes/minimal-mistakes/pull/2697)
- Fix dead link to CI services in documentation. [#2635](https://github.com/mmistakes/minimal-mistakes/issues/2635) [#2692](https://github.com/mmistakes/minimal-mistakes/pull/2692)
- Fix a small typo in documentation. [#2718](https://github.com/mmistakes/minimal-mistakes/pull/2718)

### Enhancements

- Update jQuery to 3.5.1. [#2713](https://github.com/mmistakes/minimal-mistakes/pull/2713)
- Add Indonesian localized UI text strings. [#2725](https://github.com/mmistakes/minimal-mistakes/pull/2725)
- Update Vietnamese localized UI text strings. [#2722](https://github.com/mmistakes/minimal-mistakes/pull/2722)
- Add Norwegian (Norsk) localized UI text strings. [#2702](https://github.com/mmistakes/minimal-mistakes/pull/2702)
- Update allejo/jekyll-toc to v1.0.14 [#2700](https://github.com/mmistakes/minimal-mistakes/pull/2700)

## [4.20.2](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.20.2)

### Bug Fixes

- Fix broken link in documentation. [#2677](https://github.com/mmistakes/minimal-mistakes/issues/2677)
- Fix typo in documentation. [#2678](https://github.com/mmistakes/minimal-mistakes/issues/2678)
- Remove duplicate CSS definitions. [#2666](https://github.com/mmistakes/minimal-mistakes/pull/2666)
- Fix `entries_layout: grid` in various layouts. [#2639](https://github.com/mmistakes/minimal-mistakes/issues/2639)
- Change `fa` to `fas` for Font Awesome 5. [#2649](https://github.com/mmistakes/minimal-mistakes/pull/2649)

### Enhancements

- Refactor page meta include. [#2641](https://github.com/mmistakes/minimal-mistakes/pull/2641)
- Add `article:author` Open Graph markup. [#2670](https://github.com/mmistakes/minimal-mistakes/pull/2670)

## [4.20.1](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.20.1)

### Bug Fixes

- Fix `entries_layout: grid` in `home.html` layout. [#2616](https://github.com/mmistakes/minimal-mistakes/pull/2616)

## [4.20.0](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.20.0)

### Bug Fixes

- Add `relative_url` filter to author home link [#2575](https://github.com/mmistakes/minimal-mistakes/pull/2575)
- Fix `analytics.provider` config comment to list all analytics providers. [#2607](https://github.com/mmistakes/minimal-mistakes/pull/2607)
- Fix typo in installation documentation. [#2570](https://github.com/mmistakes/minimal-mistakes/pull/2570)
- Fix broken Lunr search with Jekyll v4.1.0. [#2617](https://github.com/mmistakes/minimal-mistakes/pull/2617)

### Enhancements

- Add an optional date alongside the reading time. To enable set `show_date: true` similar to how reading time is. [#2526](https://github.com/mmistakes/minimal-mistakes/pull/2526)
- Remove hidden posts from posts.html layout. [#2625](https://github.com/mmistakes/minimal-mistakes/pull/2625)
- Add entry layout configuration for `list` (default) or `grid` views on `layout: home`. [#2616](https://github.com/mmistakes/minimal-mistakes/pull/2616)
- Add missing Chinese translations. [#2576](https://github.com/mmistakes/minimal-mistakes/pull/2576)
- Improve Chinese translations. [#2626](https://github.com/mmistakes/minimal-mistakes/pull/2626)
- Add `line-height` to `h4` element in notice helper. [#2602](https://github.com/mmistakes/minimal-mistakes/pull/2602)
- Improve Algolia search. [#2572](https://github.com/mmistakes/minimal-mistakes/pull/2572)
- Update link to wtfpl license in README. [#2571](https://github.com/mmistakes/minimal-mistakes/pull/2571)
- Ignore teaser headline in table of contents when including posts list in another page. [#2558](https://github.com/mmistakes/minimal-mistakes/pull/2558)
- Replace Font Awesome Kits with CSS from jsDelivr CDN. [#2583](https://github.com/mmistakes/minimal-mistakes/pull/2583)
- Add `danmaku` option to Bilibili video provider and add corresponding documentation/ [#2599](https://github.com/mmistakes/minimal-mistakes/pull/2599)
- Update documentation about loading l10n data file from the theme-gem. [#2621](https://github.com/mmistakes/minimal-mistakes/issues/2621) [#2624](https://github.com/mmistakes/minimal-mistakes/pull/2624)

## [4.19.3](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.19.3)

### Enhancements

- Update GreedyNav.js to reduce masthead link overflow/shifting on mobile devices. [#2551](https://github.com/mmistakes/minimal-mistakes/issues/2551)
- Replace `<section id="custom-comments"></section>` in `comments.html` include and add `custom_scripts.html` include for loading custom comment provider JavaScript in the footer. [#2549](https://github.com/mmistakes/minimal-mistakes/issues/2549)
- Move page date Liquid to include. [#2544](https://github.com/mmistakes/minimal-mistakes/pull/2544)
- Strip trailing whitespace in seo_description. [#2542](https://github.com/mmistakes/minimal-mistakes/pull/2542)
- Improve sticky sidebar's appearance with short content. [#2514](https://github.com/mmistakes/minimal-mistakes/pull/2514)

## [4.19.2](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.19.2)

### Enhancements

- Add support for bilibili videos in [responsive video helper](https://mmistakes.github.io/minimal-mistakes/docs/helpers/#responsive-video-embed). [#2512](https://github.com/mmistakes/minimal-mistakes/pull/2512)
- Add Myanmar (Burmese) localized UI text strings. [#2500](https://github.com/mmistakes/minimal-mistakes/pull/2500)
- Improve author links underline on hover. [#2472](https://github.com/mmistakes/minimal-mistakes/pull/2472)
- Add documentation for applying Front Matter defaults to jekyll-archives pages. [#2466](https://github.com/mmistakes/minimal-mistakes/pull/2466)
- Add missing Vietnamese translations. [#2459](https://github.com/mmistakes/minimal-mistakes/pull/2459) [#2486](https://github.com/mmistakes/minimal-mistakes/pull/2486)
- Fix Finnish localized UI text strings. [#2455](https://github.com/mmistakes/minimal-mistakes/pull/2455)
- Clarify documentation that Lunr only searches documents in collections. [#2450](https://github.com/mmistakes/minimal-mistakes/pull/2450)
- Add guide on applying Front Matter defaults to jekyll-archives pages [#2466](https://github.com/mmistakes/minimal-mistakes/pull/2466)

### Bug Fixes

- Fix typo in configuration documentation. [#2497](https://github.com/mmistakes/minimal-mistakes/pull/2497)
- Fix "Follow menu falls under post links" on small screens. [#2479](https://github.com/mmistakes/minimal-mistakes/issues/2479)
- Hide index page from page-archive. [#2482](https://github.com/mmistakes/minimal-mistakes/pull/2482)

## [4.19.1](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.19.1)

### Enhancements

- Add [Dracula](https://draculatheme.com/) Base16 syntax highlighting theme Sass variables to [stylesheets documentation](https://mmistakes.github.io/minimal-mistakes/docs/stylesheets/#syntax-highlighting). [#2438](https://github.com/mmistakes/minimal-mistakes/pull/2438)
- Update links to `HTTPS` and remove Google+ from configuration documentation. [#2432](https://github.com/mmistakes/minimal-mistakes/pull/2432)
- Use `first_page_path` from jekyll-paginate-v2 if available. [#2431](https://github.com/mmistakes/minimal-mistakes/pull/2431)
- Update onchange and uglify-js dependencies.
- Update smooth-scroll.js to `v16.1.2`. [#2430](https://github.com/mmistakes/minimal-mistakes/issues/2430)

### Bug Fixes

- Fix author profile links `z-index` order on small screens. [#2440](https://github.com/mmistakes/minimal-mistakes/issues/2440)

## [4.19.0](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.19.0)

### Enhancements

- Add "click" overlay to close masthead and follow button menus when open. [#1168](https://github.com/mmistakes/minimal-mistakes/issues/1168)
- Remove deprecated Staticman v1 configurations from `_config.yml`. [#2386](https://github.com/mmistakes/minimal-mistakes/issues/2386)
- Use `relative_url` and `absolute_url` filters where possible. [#2387](https://github.com/mmistakes/minimal-mistakes/pull/2387)
- Improve headline hierarchy and add Sass specific variables `$h-size-x`. [#2423](https://github.com/mmistakes/minimal-mistakes/issues/2423)
- Improve accessibility of `default` skin by increasing color contrast of text and links.
- Hide posts with `hidden: true` YAML front matter from appearing in listings. [#2345](https://github.com/mmistakes/minimal-mistakes/pull/2345)
- Add Irish (Gaeilge) localized UI text strings. [#2422](https://github.com/mmistakes/minimal-mistakes/pull/2422)
- Remove `box-shadow` on radio and checkbox inputs. [#2398](https://github.com/mmistakes/minimal-mistakes/pull/2398)
- Bump Jekyll gem dependency to `v3.7`.

### Bug Fixes

- Fix documentation around using `bundle info` command. [#2425](https://github.com/mmistakes/minimal-mistakes/pull/2425)
- Fix rake vulnerability in `.gemspec` file.
- Fix Staticman v2 comment submission. [#2402](https://github.com/mmistakes/minimal-mistakes/pull/2402)
- Fix repeated site base path for masthead logo. [#2385](https://github.com/mmistakes/minimal-mistakes/pull/2385)

## [4.18.1](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.18.1)

### Bug Fixes

- Fix compatibility issue with jekyll-paginate-v2. [#2381](https://github.com/mmistakes/minimal-mistakes/pull/2381)

## [4.18.0](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.18.0)

### Enhancements

- Allow `home` layout to display posts without pagination. [#2378](https://github.com/mmistakes/minimal-mistakes/pull/2378)
- Add links to high resolution skin screenshots in README. [#2363](https://github.com/mmistakes/minimal-mistakes/issues/2363)
- Update README and LICENSE. [#2367](https://github.com/mmistakes/minimal-mistakes/pull/2367)
- Update `.gitignore` file. [#2366](https://github.com/mmistakes/minimal-mistakes/pull/2366)
- Allow override of page excerpt in hero header via `tagline` YAML front matter. [#2307](https://github.com/mmistakes/minimal-mistakes/pull/2307)
- Exclude `package-lock.json` from Jekyll build. [#2364](https://github.com/mmistakes/minimal-mistakes/pull/2364)
- Use `%-d` instead of `%d` so displayed dates aren't padded with zero. [#2359](https://github.com/mmistakes/minimal-mistakes/pull/2359)
- Update table of contents helper (`toc.html`) to [v1.0.8](https://github.com/allejo/jekyll-toc/releases). [#2355](https://github.com/mmistakes/minimal-mistakes/pull/2355)
- Add missing Dutch localized UI text strings. [#2321](https://github.com/mmistakes/minimal-mistakes/pull/2321)
- Support page header (hero) in `archive-taxonomy` layout. [#2320](https://github.com/mmistakes/minimal-mistakes/pull/2320)
- Add social icon color for Keybase. [#2302](https://github.com/mmistakes/minimal-mistakes/pull/2302)

### Bug Fixes

- Fix JavaScript comments in Disqus include to be compatible with `compress` layout. [#2373](https://github.com/mmistakes/minimal-mistakes/pull/2373)
- Fix wrong newline concatenation in SEO description [#2368](https://github.com/mmistakes/minimal-mistakes/pull/2368) [#2354](https://github.com/mmistakes/minimal-mistakes/issues/2354)
- Fix Staticman v2/v3 conditional for showing comments. [#2351](https://github.com/mmistakes/minimal-mistakes/pull/2351)
- Fix masthead logo path. [#2332](https://github.com/mmistakes/minimal-mistakes/pull/2332)
- Fix schema.org dates to ISO-8601. [#2339](https://github.com/mmistakes/minimal-mistakes/pull/2339)
- Fix background color of code blocks in notices. [#2328](https://github.com/mmistakes/minimal-mistakes/pull/2328)
- Fix alignment of feature rows when placed next to a sticky sidebar. [#2327](https://github.com/mmistakes/minimal-mistakes/issues/2327)
- Fix `seo_description` in `_includes/seo.html`. [#2326](https://github.com/mmistakes/minimal-mistakes/pull/2326)
- Fix typo in `_config.yml`. [#2319](https://github.com/mmistakes/minimal-mistakes/pull/2319)

## [4.17.2](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.17.2)

### Enhancements

- Add collection step to documentation about creating a portfolio page. [#2294](https://github.com/mmistakes/minimal-mistakes/pull/2294)
- Replace sticky footer JavaScript with flexbox styles. [#2289](https://github.com/mmistakes/minimal-mistakes/pull/2289)

### Bug Fixes

- Fix sticky footer when using MozBar extension. [#2281](https://github.com/mmistakes/minimal-mistakes/issues/2281)

## [4.17.1](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.17.1)

### Enhancements

- Update Chinese (Simplified) localized UI text strings. [#2286](https://github.com/mmistakes/minimal-mistakes/pull/2286)
- Update list of 3rd party JavaScript used and licenses. [#2276](https://github.com/mmistakes/minimal-mistakes/pull/2276)

### Bug Fixes

- Fix indention of nested GFM task lists. [#2283](https://github.com/mmistakes/minimal-mistakes/issues/2283)

## [4.17.0](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.17.0)

### Enhancements

- Show a permalink anchor when hovering over headings in main content area. [#2251](https://github.com/mmistakes/minimal-mistakes/pull/2251)
- Allow per-page override of `words_per_minute`. [#2250](https://github.com/mmistakes/minimal-mistakes/pull/2250)
- Update [onchange](https://www.npmjs.com/package/onchange) development dependency in `package.json`. [#2241](https://github.com/mmistakes/minimal-mistakes/issues/2241)
- Add Catalan localized UI text strings. [#2237](https://github.com/mmistakes/minimal-mistakes/pull/2237)

### Bug Fixes

- Remove extraneous space from Internet Explorer conditional statement. [#2273](https://github.com/mmistakes/minimal-mistakes/pull/2273)
- Fix typo in `_config.yml`. [#2243](https://github.com/mmistakes/minimal-mistakes/pull/2243)
- Replace `http` URLs with `https` where applicable in `_config.yml`. [#2244](https://github.com/mmistakes/minimal-mistakes/pull/2244)

## [4.16.6](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.16.6)

### Enhancements

- Relax Jekyll dependency to allow for version 4.0.
- Add missing Spanish localized UI text strings. [#2229](https://github.com/mmistakes/minimal-mistakes/pull/2229)
- Allow Markdown in author bio. [#2215](https://github.com/mmistakes/minimal-mistakes/pull/2215)

### Bug Fixes

- Fix `site.url` in Organization/Person JSON-LD schema. [#1906](https://github.com/mmistakes/minimal-mistakes/issues/1906)
- Remove full stop in some `comment_form_info` UI text strings. [#2220](https://github.com/mmistakes/minimal-mistakes/pull/2220)
- Fix default `site.author` in seo.html [#2230](https://github.com/mmistakes/minimal-mistakes/pull/2230)
- Fix overlapping links (linked to and post's permalink) in post link type. [#2222](https://github.com/mmistakes/minimal-mistakes/issues/2222)

## [4.16.5](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.16.5)

### Enhancements

- Add optional site subtitle to masthead. [#2173](https://github.com/mmistakes/minimal-mistakes/issues/2173)
- Add missing Punjabi and Hindi localized UI text strings. [#2212](https://github.com/mmistakes/minimal-mistakes/pull/2212)
- Add missing Korean localized UI text strings. [#2209](https://github.com/mmistakes/minimal-mistakes/pull/2209)
- Use [Font Awesome Kits](https://blog.fontawesome.com/introducing-font-awesome-kits-7134d1d59959) to use the latest version of icons. [#2184](https://github.com/mmistakes/minimal-mistakes/issues/2184)
- Remove unnecessary console.log in `lunr-en.js` and `lunr-gr.js` JavaScript. [#2193](https://github.com/mmistakes/minimal-mistakes/issues/2193)
- Remove unnecessary `type="text/javascript"` from Google Analytics JavaScript. [#2190](https://github.com/mmistakes/minimal-mistakes/pull/2190)
- Update links and fix typos in documentation. [#2186](https://github.com/mmistakes/minimal-mistakes/pull/2186)
- Add skip links. [#2182](https://github.com/mmistakes/minimal-mistakes/issues/2182)

### Bug Fixes

- Fix aria issues with Lunr search form. [#2211](https://github.com/mmistakes/minimal-mistakes/pull/2211)
- Fix missing fallback title for table of contents.

## [4.16.4](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.16.4)

### Enhancements

- Update Brazilian Portuguese localized UI text strings. [#2162](https://github.com/mmistakes/minimal-mistakes/pull/2162)
- Update Font Awesome to v5.8.2. [#2150](https://github.com/mmistakes/minimal-mistakes/pull/2150)
- Add missing Spanish localized UI text strings. [#2149](https://github.com/mmistakes/minimal-mistakes/pull/2149)

### Bug Fixes

- Fix arithmetic in `_form.scss` partial. [#2169](https://github.com/mmistakes/minimal-mistakes/pull/2169)
- Fix pound symbol not displaying properly for post categories and tags. [#2156](https://github.com/mmistakes/minimal-mistakes/issues/2156)
- Fix permalink stacking order and click-able area in archives.

## [4.16.3](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.16.3)

### Enhancements

- Update jQuery to v3.4.1. [#2137](https://github.com/mmistakes/minimal-mistakes/issues/2137)
- Update Gumshoe to v5.1.1. [#2140](https://github.com/mmistakes/minimal-mistakes/issues/2140)

### Bug Fixes

- Fix JavaScript error when resizing pages with table of contents. [#2140](https://github.com/mmistakes/minimal-mistakes/issues/2140)

## [4.16.2](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.16.2)

### Bug Fixes

- Revert jQuery back to version v3.3.1, v.3.4.0 causes issues with other plugins that haven't been updated. [#2137](https://github.com/mmistakes/minimal-mistakes/issues/2137)

## [4.16.1](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.16.1)

### Enhancements

- Update [`compress` layout](https://mmistakes.github.io/minimal-mistakes/docs/layouts/#compress-layout) to v3.1.0. [#2128](https://github.com/mmistakes/minimal-mistakes/pull/2128)
- Update jQuery to v3.4.0. [#2129](https://github.com/mmistakes/minimal-mistakes/pull/2129)

### Bug Fixes

- Fix Gumshoe related JavaScript error on pages without a table of contents. [#2124](https://github.com/mmistakes/minimal-mistakes/pull/2124)

## [4.16.0](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.16.0)

### Enhancements

- Improve search `input` semantics for Lunr and Google search providers. [#2123](https://github.com/mmistakes/minimal-mistakes/pull/2123)
- Allow adding JavaScript files after those bundled in the theme. [#2110](https://github.com/mmistakes/minimal-mistakes/issues/2110) [#2116](https://github.com/mmistakes/minimal-mistakes/pull/2116)
- Add `$max-width` Sass variable for adjusting page content's maximum width. [#2093](https://github.com/mmistakes/minimal-mistakes/pull/2093)
- Add Thai localized UI text strings. [#2111](https://github.com/mmistakes/minimal-mistakes/pull/2111)
- Update Font Awesome to [v5.8.1](https://github.com/FortAwesome/Font-Awesome/releases/tag/5.8.1). [#2102](https://github.com/mmistakes/minimal-mistakes/pull/2102)
- Add missing Vietnamese localized UI text strings. [#2097](https://github.com/mmistakes/minimal-mistakes/pull/2097)
- Replace jQuery Smooth Scroll with Smooth Scroll + Gumshoe. [#2082](https://github.com/mmistakes/minimal-mistakes/pull/2082)
- Add styling for [GFM task lists](https://help.github.com/en/articles/about-task-lists#creating-task-lists). [#2092](https://github.com/mmistakes/minimal-mistakes/issues/2092)
- Update Google Universal Analytics to load async. [#2079](https://github.com/mmistakes/minimal-mistakes/pull/2079)
- Remove Google+ social sharing button, comment provider, and author link configs from theme.
- Add missing Chinese text strings. [#2072](https://github.com/mmistakes/minimal-mistakes/pull/2072)

### Bug Fixes

- Fix table of contents active link styling.
- Add missing Hindi localized UI text strings. [#2105](https://github.com/mmistakes/minimal-mistakes/pull/2105) [#2106](https://github.com/mmistakes/minimal-mistakes/pull/2106)
- Fix Brazilian Portuguese text strings. [#2098](https://github.com/mmistakes/minimal-mistakes/pull/2098)
- Fix typo in French `results_found` text string. [#2096](https://github.com/mmistakes/minimal-mistakes/pull/2096)
- Fix figures inside of list elements. [#2094](https://github.com/mmistakes/minimal-mistakes/pull/2094)
- Remove Font Awesome `data-search-pseudo-elements` attribute as it degrades smooth scroll performance. [#2075](https://github.com/mmistakes/minimal-mistakes/issues/2075#issuecomment-472437014)
- Fix footnote links incompatibility with smooth scroll plugin. [#2075](https://github.com/mmistakes/minimal-mistakes/issues/2075)
- Loosen Bundler dependency in ruby gem.

## [4.15.2](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.15.2)

### Enhancements

- Close search overlay with <kbd>Esc</kbd>. [#2055](https://github.com/mmistakes/minimal-mistakes/pull/2055)
- Update Swedish localized UI text strings. [#2056](https://github.com/mmistakes/minimal-mistakes/pull/2056)
- Update Font Awesome to 5.7.1 and add `data-search-pseudo-elements` attribute. [#2053](https://github.com/mmistakes/minimal-mistakes/pull/2053)
- Add Malayalam localized UI text strings. [#2037](https://github.com/mmistakes/minimal-mistakes/pull/2037)

### Bug Fixes

- Fix table of contents errors with non-English characters in the headings. [#2042](https://github.com/mmistakes/minimal-mistakes/pull/2042)
- Fix `site.logo` false positives. [#2026](https://github.com/mmistakes/minimal-mistakes/pull/2026#issuecomment-455770730)
- Add empty `alt` attribute to `site.logo` image. [#2035](https://github.com/mmistakes/minimal-mistakes/pull/2035)

## [4.15.1](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.15.1)

### Bug Fixes

- Fix empty `<img>` when `site_logo` is not assigned. [#2026](https://github.com/mmistakes/minimal-mistakes/pull/2026#issuecomment-454809876)

## [4.15.0](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.15.0)

### Enhancements

- Add logo and title customization to the masthead. [#2026](https://github.com/mmistakes/minimal-mistakes/pull/2026)
- Add support to customize `issue-term` for utterances comment provider. [#2022](https://github.com/mmistakes/minimal-mistakes/pull/2022)
- Allow custom canonical url on a page-by-page basis. [#2021](https://github.com/mmistakes/minimal-mistakes/pull/2021)
- Update table of contents navigation based on scroll position to indicate which link is currently active in the viewport. [#2020](https://github.com/mmistakes/minimal-mistakes/pull/2020)
- Clicking table of contents links changes URL has fragment. [#2019](https://github.com/mmistakes/minimal-mistakes/pull/2019) [#2023](https://github.com/mmistakes/minimal-mistakes/pull/2023)

## [4.14.2](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.14.2)

### Enhancements

- Improve accessibility by adding label text to search button toggle. [#2014](https://github.com/mmistakes/minimal-mistakes/pull/2014)
- Update Lunr to 2.3.5. [#2010](https://github.com/mmistakes/minimal-mistakes/pull/2010)
- Shorten Internet Explorer conditional statement in `_includes/head.html`. [#2006](https://github.com/mmistakes/minimal-mistakes/pull/2006)
- Add Persian localized UI text strings. [#2004](https://github.com/mmistakes/minimal-mistakes/pull/2004)
- Remove unused JavaScript variables from Staticman comment script. [#1996](https://github.com/mmistakes/minimal-mistakes/pull/1996)
- Update Font Awesome to 5.6.0. [#1995](https://github.com/mmistakes/minimal-mistakes/pull/1995)
- Change remaining schema.org markup to `https`. [#1978](https://github.com/mmistakes/minimal-mistakes/pull/1978)
- Update NPM dependencies.

### Bug Fixes

- Fix wide tables that overflow parent container. [#2008](https://github.com/mmistakes/minimal-mistakes/issues/2008)
- Fix Spanish `comments_label` and `comments_title` UI text strings. [#1997](https://github.com/mmistakes/minimal-mistakes/pull/1997)
- Allow sidebar navigation with custom sidebar content. [#1986](https://github.com/mmistakes/minimal-mistakes/issues/1986)
- Fix Google Custom Search JavaScript error when not using Instant Search. [#1983](https://github.com/mmistakes/minimal-mistakes/pull/1983)

## [4.14.1](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.14.1)

### Bug Fixes

- Fix closed navicon on hover.

## [4.14.0](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.14.0)

### Enhancements

- Change schema.org markup to `https`. [#1969](https://github.com/mmistakes/minimal-mistakes/pull/1969)
- Add Google Drive as video provider. [#1967](https://github.com/mmistakes/minimal-mistakes/pull/1967)
- Match `:focus` color to skin.
- Add support for [utterances](https://utteranc.es/) comments. [#1909](https://github.com/mmistakes/minimal-mistakes/issues/1909)
- Use privacy aware embed options for YouTube and Vimeo in [responsive video helper](https://mmistakes.github.io/minimal-mistakes/docs/helpers/#responsive-video-embed). [#1964](https://github.com/mmistakes/minimal-mistakes/pull/1964)
- Add `rel="nofollow noopener noreferrer"` to author profile links. [#1924](https://github.com/mmistakes/minimal-mistakes/pull/1924)
- Improve color contrast of primary buttons and links.
- Add Punjabi localized UI text strings. [#1962](https://github.com/mmistakes/minimal-mistakes/pull/1962)
- Add Hindi localized UI text strings. [#1888](https://github.com/mmistakes/minimal-mistakes/pull/1888)
- Update Lunr to `2.3.3`. [#1885](https://github.com/mmistakes/minimal-mistakes/pull/1885)
- Cache "static" includes to improve build performance. **Note:** The theme uses the [jekyll-include-cache](https://github.com/benbalter/jekyll-include-cache) plugin which will need to be installed in your `Gemfile` and added to the `plugins` array of `_config.yml`. Otherwise you'll throw `Unknown tag 'include_cached'` errors at build. [#1874](https://github.com/mmistakes/minimal-mistakes/pull/1874)
- Make entire feature and archive items "clickable". [#1864](https://github.com/mmistakes/minimal-mistakes/pull/1864)
- Allow custom Staticman endpoints. [#1842](https://github.com/mmistakes/minimal-mistakes/issues/1842)
- Remove `type="text/css"` from Algolia script includes. [#1836](https://github.com/mmistakes/minimal-mistakes/pull/1836)
- Remove unneeded `HandheldFriendly` and `MobileOptimized` meta tags. [#1837](https://github.com/mmistakes/minimal-mistakes/pull/1837)
- Update Font Awesome to version `5.5.0` and add `integrity` hash. [#1922](https://github.com/mmistakes/minimal-mistakes/pull/1922)
- Always load Google 404 Linkhelp script over HTTPS. [#1829](https://github.com/mmistakes/minimal-mistakes/pull/1829)
- Remove deprecated `base_path` include helper.

### Bug Fixes

- Prevent current post from showing in the related posts section. [#1976](https://github.com/mmistakes/minimal-mistakes/pull/1976)
- Fix dark skins syntax highlighting colors. [#1973](https://github.com/mmistakes/minimal-mistakes/issues/1973)
- Remove unnecessary closing bracket in analytics documentation. [#1915](https://github.com/mmistakes/minimal-mistakes/pull/1915)
- Fix breadcrumb navigation alignment. [#1917](https://github.com/mmistakes/minimal-mistakes/issues/1917)
- Fix Algolia search link positioning. [#1904](https://github.com/mmistakes/minimal-mistakes/pull/1904)
- Fix Lunr search index merging words. [#1883](https://github.com/mmistakes/minimal-mistakes/issues/1883)
- Properly apply `relative_url` filter to internal links in header overlay `actions` array.
- Revert cached includes (`include_cached`) for comment and analytics providers. [#1905](https://github.com/mmistakes/minimal-mistakes/issues/1905)

## [4.13.0](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.13.0)

### Enhancements

- Add Romanian localized UI text strings. [#1814](https://github.com/mmistakes/minimal-mistakes/pull/1814)
- Improve author link flexibility. [#1581](https://github.com/mmistakes/minimal-mistakes/issues/1581)
- Improve footer link flexibility.
- Deprecate `cta_label` and `cta_url` in header overlay in favor of new `actions` array that allows for multiple "call to action" button links. [#1461](https://github.com/mmistakes/minimal-mistakes/issues/1461)
- Add support to [gallery helper](https://mmistakes.github.io/minimal-mistakes/docs/helpers/#gallery) for defining column layout (`half`, `third`, or single `''`). [#1821](https://github.com/mmistakes/minimal-mistakes/issues/1821)

### Bug Fixes

- Fix sidebar navigation list toggle. [#1819](https://github.com/mmistakes/minimal-mistakes/issues/1819)
- Fix hover animation for links with `:visited` state. [#1820](https://github.com/mmistakes/minimal-mistakes/issues/1820)

## [4.12.2](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.12.2)

### Enhancements

- Add missing Italian localized UI text strings. [#1793](https://github.com/mmistakes/minimal-mistakes/pull/1793)
- Update [jekyll-toc](https://github.com/allejo/jekyll-toc) to `v1.0.5`.
- Support heading levels 1-6 in table of contents with proper indentation styling. [#1782](https://github.com/mmistakes/minimal-mistakes/issues/1782)
- Use relative links for masthead navigation menu items when possible. [#1784](https://github.com/mmistakes/minimal-mistakes/pull/1784)
- Add `.emoji` class to author sidebar to normalize image sizes. [#1780](https://github.com/mmistakes/minimal-mistakes/pull/1780)
- Update Staticman commit message to include comment author's name.
- Improve side navigation spacing in relation to masthead.
- Style archive links with appropriate link color.
- Adjust feature row spacing and font-sizes.
- Use sentence case and increase font-sizes for improved readability in table of contents.
- Add `{{ content }}` to `home` layout. [#1775](https://github.com/mmistakes/minimal-mistakes/pull/1775)

## [4.12.1](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.12.1)

### Enhancements

- Add missing French localized UI text strings. [#1769](https://github.com/mmistakes/minimal-mistakes/pull/1769) [#1741](https://github.com/mmistakes/minimal-mistakes/pull/1741)
- Update Font Awesome to version [`5.2.0`](https://github.com/FortAwesome/Font-Awesome/blob/master/CHANGELOG.md). [#1754](https://github.com/mmistakes/minimal-mistakes/pull/1754)
- Add documentation note to update root `Gemfile` when forking theme.

### Bug Fixes

- Remove slash at the beginning of `path` in staticman.yml example. [#1772](https://github.com/mmistakes/minimal-mistakes/pull/1772)
- Fix `read_time` logic in header image overlay. [#1756](https://github.com/mmistakes/minimal-mistakes/pull/1756)

## [4.12.0](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.12.0)

### Enhancements

- Add Hungarian localized UI text strings. [#1682](https://github.com/mmistakes/minimal-mistakes/pull/1682)
- DRY `tags_max` calculation in tags.html layout. [#1696](https://github.com/mmistakes/minimal-mistakes/pull/1696)
- DRY `categories_max` calculation in categories.html layout.
- Add support for ["sticking" table of contents](https://mmistakes.github.io/minimal-mistakes/layout-table-of-contents-sticky/) to top of page via `toc_sticky: true` YAML Front Matter.
- Add support for captioning images in feature row helper via `image_caption` YAML Front Matter. [#1440](https://github.com/mmistakes/minimal-mistakes/issues/1440)
- Add [Google Custom Search Engine](https://cse.google.com/cse) support. [#1652](https://github.com/mmistakes/minimal-mistakes/issues/1652)
- Update Font Awesome to version [`5.1.13`](https://github.com/FortAwesome/Font-Awesome/blob/master/CHANGELOG.md)
- Add "Pets" sample archive page to documentation site. [#1664](https://github.com/mmistakes/minimal-mistakes/pull/1664)
- Add GitLab social icon brand color. [#1653](https://github.com/mmistakes/minimal-mistakes/issues/1653)
- Prevent line breaks between FontAwesome icon and text in footer social links. [#1659](https://github.com/mmistakes/minimal-mistakes/issues/1659)

### Bug Fixes

- Set default `title_separator`. [#1701](https://github.com/mmistakes/minimal-mistakes/pull/1701)
- Fix `naver_site_verification` typo in /_includes/seo.html. [#1687](https://github.com/mmistakes/minimal-mistakes/pull/1687)
- Fix table of contents missing borders. [#1675](https://github.com/mmistakes/minimal-mistakes/issues/1675)
- Fix link to "Recipes" sample archive on documentation site. [#1664](https://github.com/mmistakes/minimal-mistakes/pull/1664)
- Update example Reddit social share interpolation syntax in documentation. [#1656](https://github.com/mmistakes/minimal-mistakes/issues/1656)
- Fix "Back to Top" links on pages that use [header overlays](https://mmistakes.github.io/minimal-mistakes/docs/layouts/#header-overlay).

## [4.11.2](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.11.2)

### Enhancements

* Update Font Awesome to version [`5.0.12`](https://github.com/FortAwesome/Font-Awesome/blob/master/CHANGELOG.md).
* Add Slovak localized UI text strings. [#1613](https://github.com/mmistakes/minimal-mistakes/pull/1613)
* Add option to anonymize IP addresses of hits sent to Google Analytics. [#1636](https://github.com/mmistakes/minimal-mistakes/pull/1636)

### Bug Fixes

* Use correct text string for "Back to Top" link. [#1595](https://github.com/mmistakes/minimal-mistakes/issues/1595)
* Add conditionals for showing `reCaptcha.siteKey` and `reCaptcha.secret` in Staticman comments form.

## [4.11.1](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.11.1)

### Enhancements

* Add default `theme` and `remote_theme` values to `_config.yml`.
* Add new layouts (`posts`, `categories`, `tags`, `collection`, `category`, and `tag`) for easier archive page creation.

### Bug Fixes

* Replace `absolute_url` filter with `relative_url` where it makes sense (asset/navigation related paths). [#1588](https://github.com/mmistakes/minimal-mistakes/issues/1588)
* Fix search excerpts that run together because of implied spaces.

## [4.10.1](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.10.1)

### Enhancements

* Update jQuery to version `3.3.1`. [#1491](https://github.com/mmistakes/minimal-mistakes/issues/1491)
* Add link to jekyll-algolia's `files_to_exclude` documentation.
* Update Font Awesome to version [`5.0.8`](https://github.com/FortAwesome/Font-Awesome/blob/master/CHANGELOG.md). [#1561](https://github.com/mmistakes/minimal-mistakes/pull/1561)
* Activate Algolia search for documentation site. [#1570](https://github.com/mmistakes/minimal-mistakes/issues/1570)
* Add missing German translations. [#1577](https://github.com/mmistakes/minimal-mistakes/pull/1577)
* Add support for Google Analytics with global site tag (gtag.js) [#1563](https://github.com/mmistakes/minimal-mistakes/pull/1563)

### Bug Fixes

* Focus Algolia search input after clicking on search toggle.

## [4.10.0](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.10.0)

### Enhancements

* Add support for [Algolia](https://www.algolia.com/) search provider ([see demo](https://mmistakes.github.io/minimal-mistakes-algolia-search/)). [#1416](https://github.com/mmistakes/minimal-mistakes/issues/1416)

## [4.9.1](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.9.1)

### Enhancements

* Simplify year archive Liquid.
* Add documentation on how to downgrade theme.
* Improve greedy navigation's layout when JavaScript is disabled.
* Improve SEO include by grouping similar tags, reducing white-space, and adding `article:modified_time`. [#1456](https://github.com/mmistakes/minimal-mistakes/pull/1456)
* Minify `assets/js/lunr/lunr.js`.
* Improve calculation of Greedy navigation's `availableSpace`.
* Add Danish and Russian translations for new search strings. [#1472](https://github.com/mmistakes/minimal-mistakes/pull/1472) [#1477](https://github.com/mmistakes/minimal-mistakes/pull/1477)
* Indicate that archive titles are links with an underline.
* Remove `base_path` include from `/test` pages.
* Reduce font-size of page meta in list/grid items.
* Improve feature row styling when used with `archive` layout. [#1484](https://github.com/mmistakes/minimal-mistakes/issues/1484)
* Improve German translations. [#1511](https://github.com/mmistakes/minimal-mistakes/pull/1511)
* Update Font Awesome to `5.0.6`. [#1513](https://github.com/mmistakes/minimal-mistakes/pull/1513)
* Add `wide` variant to single layout. [#1516](https://github.com/mmistakes/minimal-mistakes/pull/1516)

### Bug Fixes

* Allow `author` to accept an object or string. [#289](https://github.com/mmistakes/minimal-mistakes/issues/289)
* Fix syntax highlighting line number styling inconsistency. [#1467](https://github.com/mmistakes/minimal-mistakes/issues/1467)
* Fix author sidebar icon colors for dark skins. [#1482](https://github.com/mmistakes/minimal-mistakes/issues/1482)
* Remove misleading underline hover state on feature row items.
* Properly escape quotes in `site.social.name` and `site.name`. [#1485](https://github.com/mmistakes/minimal-mistakes/pull/1485)
* Fix typo in upgrading documentation. [#1487](https://github.com/mmistakes/minimal-mistakes/pull/1487)
* Fix `border-bottom` for Gist line numbers.
* Replace `|` with HTML entity when used as title separator. [#760](https://github.com/mmistakes/minimal-mistakes/issues/760)

## [4.9.0](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.9.0)

### Enhancements

* Add `show_overlay_excerpt` for disabling overlay image excerpt text. [#1436](https://github.com/mmistakes/minimal-mistakes/pull/1436)
* Update remote theme installation instructions in Quick Start Guide. [#1439](https://github.com/mmistakes/minimal-mistakes/pull/1439)
* Reduce visual weight of code blocks.
* Add Lunr.js Greek stemmer. [#1445](https://github.com/mmistakes/minimal-mistakes/pull/1445)
* Update Font Awesome 5 [SVG with JavaScript version](https://fontawesome.com/how-to-use/svg-with-js). [#1446](https://github.com/mmistakes/minimal-mistakes/pull/1446)
  * Note: if Font Awesome icons were used in the content of posts/pages or custom table of contents, find and replace any icons that have different names between version 4 and 5. Make sure to read the [complete list](https://fontawesome.com/how-to-use/upgrading-from-4#icon-name-changes-full) on Font Awesome's site.
* Reduce size of Lunr.js search JSON data and introduce `site.search_full_content` flag for limiting size of JSON file. [#1449](https://github.com/mmistakes/minimal-mistakes/pull/1449)
* Improve syntax highlighting styles. [#1450](https://github.com/mmistakes/minimal-mistakes/pull/1450)

### Bug Fixes

* Fix code block extra white-space when using [Jekyll's highlight tag](https://jekyllrb.com/docs/templates/#code-snippet-highlighting) with `linenos`. [#1437](https://github.com/mmistakes/minimal-mistakes/issues/1437)
* Round top-right corner of code block icon.
* Remove Lunr.js trimmer and bring back colons. [#1445](https://github.com/mmistakes/minimal-mistakes/pull/1445)
* Fix sticky `.sidebar` that overlaps main content when resizing viewport. [#1447](https://github.com/mmistakes/minimal-mistakes/issues/1447)

## [4.8.1](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.8.1)

### Enhancements

* Add linkback functionality to author avatar and name in sidebar via `author.home`. [#1386](https://github.com/mmistakes/minimal-mistakes/pull/1386)
* Add Japanese localized UI text strings. [#1411](https://github.com/mmistakes/minimal-mistakes/pull/1411)
* Update Lunr.js to 2.1.5 [#1419](https://github.com/mmistakes/minimal-mistakes/pull/1419)

### Bug Fixes

* Fixed broken link to Staticman's page [#1422](https://github.com/mmistakes/minimal-mistakes/pull/1422)
* Fix Lunr search to work with number tags. [#1409](https://github.com/mmistakes/minimal-mistakes/issues/1409) [#1419](https://github.com/mmistakes/minimal-mistakes/pull/1419)

## [4.8.0](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.8.0)

### Enhancements

* Open social share links in a new window. [#1357](https://github.com/mmistakes/minimal-mistakes/pull/1357)
* Remove Alexa.com verification due to retiring of "[Claim Your Site](https://support.alexa.com/hc/en-us/articles/219135887)" feature. [#1350](https://github.com/mmistakes/minimal-mistakes/issues/1350)
* Disable analytics in `development` environment. [#1362](https://github.com/mmistakes/minimal-mistakes/pull/1362)
* Disable comments in `development` environment. [#1363](https://github.com/mmistakes/minimal-mistakes/pull/1363)
* Exclude specific pages/posts from search index by adding `search: false` to the YAML Front Matter. [#1369](https://github.com/mmistakes/minimal-mistakes/pull/1369)
* Add optional `description` key to masthead links for clarifying their purpose with the `title` attribute. [#1380](https://github.com/mmistakes/minimal-mistakes/pull/1380)
* Incorporate site search into masthead. [#1383](https://github.com/mmistakes/minimal-mistakes/pull/1383)
* Update gem dependencies. [#1388](https://github.com/mmistakes/minimal-mistakes/pull/1388)

### Bug Fixes

* Fix `post.content` typo in `assets/js/lunr-en.js`. [#1354](https://github.com/mmistakes/minimal-mistakes/pull/1354)
* Fix "lunr-en.js:1 Uncaught SyntaxError: Unexpected token <" in `assets/js/lunr-en.js`. [#1356](https://github.com/mmistakes/minimal-mistakes/pull/1356)
* Rename Naver verification `naver_site_verification` to be consistent with other site variables.
* Fix button class in "Post with Table Of Contents" demo content. [#1368](https://github.com/mmistakes/minimal-mistakes/pull/1368)
* Fix capitalization of WordPress in documentation. [#1381](https://github.com/mmistakes/minimal-mistakes/pull/1381)
* Fix zh-HK UI text to point to Traditional Chinese. [#1374](https://github.com/mmistakes/minimal-mistakes/issues/1374) [#1389](https://github.com/mmistakes/minimal-mistakes/pull/1389)

## [4.7.1](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.7.1)

### Enhancements

* Add search layout powered by [Lunr](https://lunrjs.com/). [#1353](https://github.com/mmistakes/minimal-mistakes/pull/1353)
* Use [jekyll-remote-theme](https://github.com/benbalter/jekyll-remote-theme) for demo site. [#1339](https://github.com/mmistakes/minimal-mistakes/issues/1339)
* Add note about WordPress to Staticman comment migration tool in documentation. [#1346](https://github.com/mmistakes/minimal-mistakes/issues/1346)

### Bug Fixes

* Change `http` to `https` for Jekyll and Browserhappy links. [#1342](https://github.com/mmistakes/minimal-mistakes/pull/1342) [#1343](https://github.com/mmistakes/minimal-mistakes/pull/1343)
* Change `http` author profile links to `https` when supported. [#1349](https://github.com/mmistakes/minimal-mistakes/pull/1349)
* Fix broken SCSS partial links in layouts documentation. [#1351](https://github.com/mmistakes/minimal-mistakes/issues/1351)

## [4.7.0](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.7.0)

### Enhancements

* Add `alt` description to avatar image. [#1226](https://github.com/mmistakes/minimal-mistakes/pull/1226)
* Clarify documentation about which `assets` folders and files to remove when migrating to the gem version of the theme. [#1268](https://github.com/mmistakes/minimal-mistakes/issues/1268)
* Add note about Staticman GitHub compatibility. [#1273](https://github.com/mmistakes/minimal-mistakes/issues/1273)
* Add missing Brazilian Portuguese translations to `ui-text.yml`. [#1278](https://github.com/mmistakes/minimal-mistakes/pull/1278)
* Update font stack documentation. [#1292](https://github.com/mmistakes/minimal-mistakes/pull/1292)
* Improve accessibility of navigation menu button. [#1099](https://github.com/mmistakes/minimal-mistakes/issues/1099)
* Add Naver Webmaster Tools verification. [#1286](https://github.com/mmistakes/minimal-mistakes/pull/1286)
* Add support for Staticman v2 endpoint and reCAPTCHA.
* Add Polish localized UI text strings. [#1304](https://github.com/mmistakes/minimal-mistakes/pull/1304)
* Add toggleable table of contents via YAML Front Matter. Note: `toc` helper include will be deprecated in next major version. [#1222](https://github.com/mmistakes/minimal-mistakes/issues/1222)
* Refactor seo.html include to DRY-up page image handling.
* Add support for setting what image is used by OpenGraph and Twitter via `page.header.og_image`. [#1316](https://github.com/mmistakes/minimal-mistakes/issues/1316)
* Fix the spelling of some product names in the author profile. [#1328](https://github.com/mmistakes/minimal-mistakes/pull/1328)
* Add `aqua`, `neon`, and `plum` skins. [#1336](https://github.com/mmistakes/minimal-mistakes/pull/1336)
* Update **jekyll-toc** with heading classes fix. [#1337](https://github.com/mmistakes/minimal-mistakes/pull/1337)
* Remove `+` from Google+ author link to allow non-vanity URLs. [#1319](https://github.com/mmistakes/minimal-mistakes/pull/1319)

### Bug Fixes

* Fix system font rendering in Chrome on macOS/OS X. [#1290](https://github.com/mmistakes/minimal-mistakes/pull/1290)
* Fix extra padding in syntax highlighted code blocks due to Rouge 2 adding `<div class="highlight"></div>` to markup.

## [4.6.0](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.6.0)

### Enhancements

* Test strict Front Matter in `/test` site. [#1236](https://github.com/mmistakes/minimal-mistakes/pull/1236)
* Rename `gems` key to `plugins`. [#1239](https://github.com/mmistakes/minimal-mistakes/pull/1239)
* Add [YIQ Color Contrast](https://github.com/easy-designs/yiq-color-contrast) mixin for determining lightness of a color.
* DRY up button CSS using Sass lists and YIQ Color Contrast mixin.
* Add `btn--primary` button class. **Note:** elements that were previously using only a `.btn` class will now also need `.btn--primary` (eg. `<a class="btn btn--primary" href="#">my link</a>`).
* Add `air`, `contrast`, `dark`, `dirt`, `mint`, and `sunrise` skin color options. [#1208](https://github.com/mmistakes/minimal-mistakes/issues/1208)
* Allow scripts in `<head>` and before `</body>` to be added/overridden with `head_scripts` and `footer_scripts` arrays in `_config.yml`. [#1241](https://github.com/mmistakes/minimal-mistakes/pull/1241)
* Update JavaScript dependencies: jQuery `v3.2.1`, jQuery Smooth Scroll `v2.2.0`, and Magnific Popup `v1.1.0`. [#328690652](https://github.com/mmistakes/minimal-mistakes/pull/1241#issuecomment-328690652)

## [4.5.2](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.5.2)

### Enhancements

* Add `.page__comments-form` to "non-printing" selectors in print styles. [#1195](https://github.com/mmistakes/minimal-mistakes/pull/1195)
* Add LinkedIn and Steam author sidebar examples to `_config.yml`. [#1203](https://github.com/mmistakes/minimal-mistakes/pull/1203) [#1204](https://github.com/mmistakes/minimal-mistakes/pull/1204)
* Remove the http-equiv="cleartype" meta tag. [#1087](https://github.com/mmistakes/minimal-mistakes/pull/1087)
* Clarify documentation for `jekyll-archives` plugin and how to install. [#1206](https://github.com/mmistakes/minimal-mistakes/pull/1206)
* Clarify documentation around taxonomy page and index generation. [#1207](https://github.com/mmistakes/minimal-mistakes/pull/1207)
* Fix "Posts by tag" grammar in documentation. [#1209](https://github.com/mmistakes/minimal-mistakes/pull/1209)
* Improve Chinese `date_label` and `minute_read` translations in `ui-text.yml`. [#1205](https://github.com/mmistakes/minimal-mistakes/pull/1205) [#1211](https://github.com/mmistakes/minimal-mistakes/pull/1211)
* Add note to Quick-Start Guide about GitHub Pages hosting alternatives that allow 3rd party gem themes and Jekyll plugins.
* Add note to configuration documentation about Cloudflare minification as an alternative to `layout: compress`. [#1217](https://github.com/mmistakes/minimal-mistakes/pull/1217)
* Show 4 latest posts in "You May Also Enjoy" module when `related: true` and no related posts are found due to `lsi` ([latent semantic indexing](https://en.wikipedia.org/wiki/Latent_semantic_analysis#Latent_semantic_indexing)) being disabled on GitHub Pages. [#554](https://github.com/mmistakes/minimal-mistakes/issues/554)
* Truncate archive item titles' that overflow with an ellipsis. [#1213](https://github.com/mmistakes/minimal-mistakes/issues/1213)

### Bug Fixes

* Fix license URL in README file. [#1189](https://github.com/mmistakes/minimal-mistakes/pull/1189)
* Reduce amount of blank pages when printing in Chrome. [#1196](https://github.com/mmistakes/minimal-mistakes/issues/1196)
* Remove `#disqus_thread` duplicate from `comments-providers/disqus.html` as it is already in `comments.html` include. [#1199](https://github.com/mmistakes/minimal-mistakes/issues/1199)
* Fix Liquid syntax errors in `tag-list.html` and `category-list.html` includes by removing parenthesis in `assign`s. [#1223](https://github.com/mmistakes/minimal-mistakes/issues/1223)
* Fix Liquid syntax error: "Expected id but found open_square in `"{{ page.[include.id] }}"`" in `gallery` and `feature_row` includes.
* Fix Liquid syntax error: "Expected end_of_string but found pipe in `"name in __names | sort"`" in `group-by-array` include.

## [4.5.1](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.5.1)

### Enhancements

* Add Greek and Danish localized UI text strings. [#1159](https://github.com/mmistakes/minimal-mistakes/pull/1159) [#1188](https://github.com/mmistakes/minimal-mistakes/pull/1188)
* Remove blank YAML Front Matter from JavaScript banner. [#1158](https://github.com/mmistakes/minimal-mistakes/issues/1158)
* Improve `page` and `archive` layouts to visually center main content and harmonize sidebar widths and placement. [#1166](https://github.com/mmistakes/minimal-mistakes/pull/1166)
* Increase font-size of code blocks.
* Reduce indent of nested "table of contents" links.
* Extend [archive grid view](https://mmistakes.github.io/minimal-mistakes/docs/layouts/) to the right to better fill the page.
* URL encode title and page URL in social share links. [#1177](https://github.com/mmistakes/minimal-mistakes/pull/1177)
* Replace old Disqus script with new Universal Embed Code. [#1179](https://github.com/mmistakes/minimal-mistakes/pull/1179)

### Bug Fixes

* Fix positioning of sidebar table of contents when using `layout: splash`. [#1169](https://github.com/mmistakes/minimal-mistakes/issues/1169)
* Fix "follow" links `z-index` order to avoid overlapping issues. [#1167](https://github.com/mmistakes/minimal-mistakes/issues/1167)

### Maintenance

* Fix typo `words_per_minute` typo in documentation. [#1164](https://github.com/mmistakes/minimal-mistakes/pull/1164)
* Remove outside and right borders in `table`s.
* Adjust width of `.sidebar` to match `.sidebar__right`.
* Add sample documents to ["portfolio" collection](https://mmistakes.github.io/minimal-mistakes/portfolio/) for testing grid view.
* Fix typo in stylesheets documentation. [#1170](https://github.com/mmistakes/minimal-mistakes/pull/1170)
* Add note about setting Discourse `server` as a scheme-less URL (eg. `meta.discourse.com` and not `http://meta.discourse.com`) in `_config.yml`. [#1182](https://github.com/mmistakes/minimal-mistakes/issues/1182)

## [4.5.0](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.5.0)

### Enhancements

* Add scrollbar to sidebars with overflowing content that extends outside the viewport's height. [#706](https://github.com/mmistakes/minimal-mistakes/issues/706)
* Add missing Spanish UI text strings. [#1118](https://github.com/mmistakes/minimal-mistakes/pull/1118)
* Update Susy to version 3 and rewrite grid CSS to be more readable.
* Refactor intro animations into a separate Sass variable `$intro-transition` to allow for customizing. [#1147](https://github.com/mmistakes/minimal-mistakes/pull/1147)
* Add [**jekyll-data**](https://github.com/ashmaroli/jekyll-data) as a dependency to read data files from theme-gem. [#1131](https://github.com/mmistakes/minimal-mistakes/pull/1131)
* Add support for customizing header image alternative text through YAML Front Matter. [#1138](https://github.com/mmistakes/minimal-mistakes/pull/1138)

### Bug Fixes

* Fix Sass `DEPRECATION WARNING: Passing a string to call()` by [upgrading Susy to version 3](https://github.com/mmistakes/minimal-mistakes/commit/387f8149d6270b876f224a57a07062ffb0647938). [#1114](https://github.com/mmistakes/minimal-mistakes/issues/1114)
* Fix disappearing author profile links due to tapping the "Follow" button and changing a browser's viewport width to > `$lg`. [#1136](https://github.com/mmistakes/minimal-mistakes/issues/1136)

### Maintenance

* Replace reference to "Basically Basic theme" with **Minimal Mistakes**. [#1149](https://github.com/mmistakes/minimal-mistakes/pull/1149)
* Add documentation for disabling CSS3 animations. [#1150](https://github.com/mmistakes/minimal-mistakes/pull/1150)
* Update quickstart, installation, and overriding defaults documentation. [#1151](https://github.com/mmistakes/minimal-mistakes/pull/1151)

## [4.4.2](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.4.2)

### Enhancements

* Add Swedish, Dutch, and Indonesian localized UI text strings. [#996](https://github.com/mmistakes/minimal-mistakes/pull/996) [#1081](https://github.com/mmistakes/minimal-mistakes/pull/1081) [#1101](https://github.com/mmistakes/minimal-mistakes/pull/1101)
* Add Bitbucket social icon color. [#1009](https://github.com/mmistakes/minimal-mistakes/pull/1009)
* Add GitLab to author sidebar. [#1050](https://github.com/mmistakes/minimal-mistakes/pull/1050)
* Add Sass variable for navicon link hover color. [#1089](https://github.com/mmistakes/minimal-mistakes/pull/1089) [#1088](https://github.com/mmistakes/minimal-mistakes/pull/1088)

### Bug Fixes

* Toggle close button on `mouseleave`. [#975](https://github.com/mmistakes/minimal-mistakes/issues/975)
* Remove extraneous `</a>` and `</li>` tags from `paginator.html` include. [#1038](https://github.com/mmistakes/minimal-mistakes/pull/1038)
* Fix Google+ comments provider includes. [#1092](https://github.com/mmistakes/minimal-mistakes/issues/1092)
* Replace category variable used in `_includes/breadcrumbs.html` to `site.category_archive` to avoid conflicts with `site.categories`. [#1063](https://github.com/mmistakes/minimal-mistakes/pull/1063) [#329](https://github.com/mmistakes/minimal-mistakes/issues/329)

### Maintenance

* Add mention of Greek localized UI text strings to theme documentation. [#972](https://github.com/mmistakes/minimal-mistakes/pull/972)
* Update Greek localized UI text strings. [#1054](https://github.com/mmistakes/minimal-mistakes/pull/1054)
* Add documentation for adding teaser images in grid view using `header.teaser`.

## [4.4.1](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.4.1)

### Enhancements

* Add Greek localized UI text strings. [#958](https://github.com/mmistakes/minimal-mistakes/pull/958)

### Bug Fixes

* Fix `video` helper to load Vimeo videos over https. [#945](https://github.com/mmistakes/minimal-mistakes/pull/945)
* Fix close menu button that was removed when updating Greedy navigation script. [#969](https://github.com/mmistakes/minimal-mistakes/issues/969)

## [4.4.0](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.4.0)

### Enhancements

* Move SCSS partials to `/_sass/minimal-mistakes` for easier CSS customization.
* Replace `modified` with `last_modified_at` to leverage various Jekyll plugins that utilize this variable. [#930](https://github.com/mmistakes/minimal-mistakes/pull/930)
* Add Lithuanian localized UI text. [#924](https://github.com/mmistakes/minimal-mistakes/pull/924)
* Improve print stylesheet by increasing text contrast, removing elements that don't need to be printed, expanding URLs, and reducing amount of blank pages. [#909](https://github.com/mmistakes/minimal-mistakes/issues/909)

### Maintenance

* Remove extra word in comment. [#911](https://github.com/mmistakes/minimal-mistakes/pull/911)
* Fix typo in Utility Class docs. [#915](https://github.com/mmistakes/minimal-mistakes/pull/915)

## [4.3.1](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.3.1)

### Bug Fixes

* Fix `.masthead` and `.page__footer` overlapping full screen video elements. [#933](https://github.com/mmistakes/minimal-mistakes/issues/933)
* Correctly show Related Posts heading when UI Text data file is omitted and `related: true` in YAML Front Matter. [#901](https://github.com/mmistakes/minimal-mistakes/pull/901)

## [4.3.0](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.3.0)

### Enhancements

* Add workaround to allow theme gem's `/assets/js/main.min.js` file to be overridden by a local version. Simply add the following YAML Front Matter to the file:

  ```
  ---
  layout:
  ---
  ```

  Any local customizations you make to `/assets/js/main.min.js` should now replace the theme gem's version.

## [4.2.2](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.2.2)

### Enhancements

* Update [Greedy Navigation](https://github.com/lukejacksonn/GreedyNav) to flexbox version to make it more flexible when dealing with long site titles (`site.title`). [#836](https://github.com/mmistakes/minimal-mistakes/issues/836)
* Adjust `box-shadow` in navigation and author sidebar. [#576](https://github.com/mmistakes/minimal-mistakes/pull/576)
* Add Russian, Korean, and zh-TW localized UI text. [#815](https://github.com/mmistakes/minimal-mistakes/issues/815) [#834](https://github.com/mmistakes/minimal-mistakes/pull/834) [#838](https://github.com/mmistakes/minimal-mistakes/pull/838)

### Bug Fixes

* Fix Discourse embedded comments bug. [#823](https://github.com/mmistakes/minimal-mistakes/issues/823)
* Fix `seo_author` default value in `seo.html` and add `author` meta. [#858](https://github.com/mmistakes/minimal-mistakes/pull/858)

### Maintenance

* Add theme meta info to `_layouts/default.html` and `main.css`.
* Update README.
* Improve the pagination and taxonomy archive documentation. [#826](https://github.com/mmistakes/minimal-mistakes/pull/826)
* Add comments to `/docs/_config.yml` to clarify use of YAML references. [#847](https://github.com/mmistakes/minimal-mistakes/pull/847)

## [4.2.1](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.2.1)

### Enhancements

* Improve `paginator.html` to support paginated pages that live inside of a subfolder. See [documentation](https://mmistakes.github.io/minimal-mistakes/docs/layouts/#home-page) for more details. [#764](https://github.com/mmistakes/minimal-mistakes/pull/764/)

### Maintenance

* Add `https` protocol to Google Universal Analytics embed. [#772](https://github.com/mmistakes/minimal-mistakes/pull/772)

## [4.2.0](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.2.0)

### Enhancements

* Add `video` helper (for YouTube/Vimeo) and video headers to `single`, `archive`, and `splash` layouts. [#788](https://github.com/mmistakes/minimal-mistakes/pull/788)
* Add missing simplified Chinese localized UI text strings. [#747](https://github.com/mmistakes/minimal-mistakes/pull/747)
* Add Nepali (Nepalese) localized UI text strings. [#785](https://github.com/mmistakes/minimal-mistakes/pull/785)
* Remove borders from table elements found in Google Custom Search Engine widget. [#759](https://github.com/mmistakes/minimal-mistakes/issues/759)

### Bug Fixes

* Remove `position: sticky` JavaScript polyfill and fallback to default positioning for browsers that don't support it. [#752](https://github.com/mmistakes/minimal-mistakes/issues/752)

### Maintenance

* Fix invalid Google Universal Analytics example in documentation. [#783](https://github.com/mmistakes/minimal-mistakes/pull/783)
* Bump `jekyll-sitemap` gem dependency to (1.0).

## [4.1.1](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.1.1)

### Enhancements

* Remove hardcoded `words_per_minute` "less than" and "minute read" values and make dynamic. [#703](https://github.com/mmistakes/minimal-mistakes/issues/703)
* Update Font Awesome to `v4.7.0`. [#723](https://github.com/mmistakes/minimal-mistakes/issues/723), [#722](https://github.com/mmistakes/minimal-mistakes/issues/722)
* Add support for YouTube channel URLs in author profile. [#716](https://github.com/mmistakes/minimal-mistakes/issues/716)

### Bug Fixes

* Add Jekyll as `spec.add_runtime_dependency` in `.gemspec`.

## [4.1.0](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.1.0)

### Enhancements

* Add Jekyll include for adding [custom author profile links](https://github.com/mmistakes/minimal-mistakes/blob/master/_includes/author-profile-custom-links.html) to sidebar

### Bug Fixes

* Fix link to Discourse.org homepage in `noscript` section [#699](https://github.com/mmistakes/minimal-mistakes/pull/699)
* Fix padding issue with pagination buttons [#694](https://github.com/mmistakes/minimal-mistakes/issues/694)

## [4.0.10](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.0.10)

### Bug Fixes

* Add Staticman default `path`. [#683](https://github.com/mmistakes/minimal-mistakes/issues/683)

### Maintenance

* Slight correction/improvements to French UI text. [#685](https://github.com/mmistakes/minimal-mistakes/pull/685)

## [4.0.9](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.0.9)

### Bug Fixes

* Fix overlapping sidebar navigation lists due to `max-height: 100vh`. [#668](https://github.com/mmistakes/minimal-mistakes/issues/668)

## [4.0.8](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.0.8)

### Bug Fixes

* Set default value for `words_per_minute`. [#657](https://github.com/mmistakes/minimal-mistakes/issues/657)
* Adjust sidebar navigation list CSS so it collapses at the correct width.

### Maintenance

* Add Google AdSense banner to `/docs/_layouts/default.html` for demo site.

## [4.0.7](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.0.7)

### Enhancements

* Add `!default` values to **\_sass/\_variables.scss**.
* Collapse sidebar navigation lists on smaller screens. [#607](https://github.com/mmistakes/minimal-mistakes/issues/607)

### Bug Fixes

* Rename `#comments` to something more unique to avoid clashes with Kramdown generated headline IDs. [#582](https://github.com/mmistakes/minimal-mistakes/issues/582)

### Maintenance

* Reorganize SCSS partials in **assets/css/main.scss**

## [4.0.6](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.0.6)

### Enhancements

* Add [`figure` helper](https://mmistakes.github.io/minimal-mistakes/docs/helpers/#figure) to make generating a `<figure>` element with a single image and caption easier. [#572](https://github.com/mmistakes/minimal-mistakes/pull/572)
* Add structured data markup for `itemprop="person"` in author profile sidebar. [#647](https://github.com/mmistakes/minimal-mistakes/pull/647)

### Bug Fixes

* Fix improper YAML formatting of some locales. [#651](https://github.com/mmistakes/minimal-mistakes/pull/651)

### Maintenance

* Clarify "migrating to gem-theme" instructions in **Quick Start Guide**.
* Add `rake preview` task for testing `/test` during theme development.

## [4.0.5](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.0.5)

### Enhancements

* Update gems: `jekyll-sitemap` (0.12), `jekyll-feed` (0.8).
* Improve next/previous pager links visibility by changing gray color to blue (`$link-color`).

### Bug Fixes

* Fix `.sidebar` flicker/jump when hovered. [#583](https://github.com/mmistakes/minimal-mistakes/issues/583)

### Maintenance

* Move contents of `gh-pages` branch to `master` inside of the `/docs` folder.

## [4.0.4](https://github.com/mmistakes/minimal-mistakes/releases/tag/4.0.4)

### Enhancements

* "Gemify" theme ~> `gem "minimal-mistakes-jekyll"`
* Replace `base_path` include with `absolute_url` filter where possible.
* Allow images to be placed in other folders. Remove `/images/` only restriction and encourage placement in `/assets/images/` instead. **Full paths are now required. If upgrading from MM 3.4 add `/images/` before filenames in Front Matter and `_config.yml` variables.**
* Add [home `layout`](https://github.com/mmistakes/minimal-mistakes/blob/master/_layouts/home.html)
* Added missing Turkish translations for UI text. [#621](https://github.com/mmistakes/minimal-mistakes/pull/621)
* Make author avatar optional in sidebar.
* Update **/\_includes/seo.html** for meta description. [#558](https://github.com/mmistakes/minimal-mistakes/pull/558)

### Bug Fixes

* Fix navigation bar animation "flicker" in Safari [#568](https://github.com/mmistakes/minimal-mistakes/issues/568)
* Fix `author.avatar` paths for externally hosted images.

### Maintenance

* Add documentation around `gem "minimal-mistakes-jekyll"` installation and use.
* Add note about using full image paths for eg. `assets/images/filename.jpg` (header images, overlays, galleries, feature rows, etc.) instead of assuming they will always be in `/images/`.
* Add "[Overriding Theme Defaults](https://mmistakes.github.io/minimal-mistakes/docs/overriding-theme-defaults/)" page to documentation.

## [3.4.8](https://github.com/mmistakes/minimal-mistakes/releases/tag/3.4.8)

### Enhancements

* Improve type readability for larger viewports by bumping up base `font-size`. [#533](https://github.com/mmistakes/minimal-mistakes/issues/533)
* Update Portuguese localized UI text. [#541](https://github.com/mmistakes/minimal-mistakes/pull/541)
* Add `page.title` and via parameter to Twitter share link. [#538](https://github.com/mmistakes/minimal-mistakes/pull/538)

### Bug Fixes

* Fix Last.fm author profile URL. [#540](https://github.com/mmistakes/minimal-mistakes/pull/540)

### Maintenance

* Move Brazilian Portuguese localized text under `pt-BR` key.

## [3.4.7](https://github.com/mmistakes/minimal-mistakes/releases/tag/3.4.7)

### Enhancements

* Add `layout` based and user-defined class names to `<body>` element for added CSS hooks. [#526](https://github.com/mmistakes/minimal-mistakes/pull/526)
* Add simplified Chinese localized UI text. [#532](https://github.com/mmistakes/minimal-mistakes/pull/532)

### Bug Fixes

* Remove duplicate include of `base_path` in category-list.html [#522](https://github.com/mmistakes/minimal-mistakes/pull/522)

## [3.4.6](https://github.com/mmistakes/minimal-mistakes/releases/tag/3.4.6)

### Enhancements

* Add Italian "comments" related localized UI text. [#514](https://github.com/mmistakes/minimal-mistakes/pull/514)

### Bug Fixes

* Disable `compress` HTML layout by default. To enable add `layout: compress` to `_layouts/default.html`.

## [3.4.5](https://github.com/mmistakes/minimal-mistakes/releases/tag/3.4.5)

### Enhancements

* Improve line numbered code block styling when using `{% highlight linenos %}` tag. [#513](https://github.com/mmistakes/minimal-mistakes/issues/513)
* Add English fallback to "Follow" button label. [#496](https://github.com/mmistakes/minimal-mistakes/pull/496)

### Bug Fixes

* Fix Firefox alignment issues with code blocks generated with the `{% highlight %}` tag. [#512](https://github.com/mmistakes/minimal-mistakes/issues/512)

### Maintenance

- Clarified comment for `author.stackoverflow` value used in author sidebar links. [#487](https://github.com/mmistakes/minimal-mistakes/pull/487)
- Add list of localized text strings. [#488](https://github.com/mmistakes/minimal-mistakes/pull/488)
- Add `{% highlight %}` code block examples to demo site.
- Add documentation for using custom sidebar navigation menus. [#476](https://github.com/mmistakes/minimal-mistakes/issues/476)

## [3.4.4](https://github.com/mmistakes/minimal-mistakes/releases/tag/3.4.4)

### Enhancements

- Add French "comments" related localized UI text. [#472](https://github.com/mmistakes/minimal-mistakes/pull/472)

### Bug Fixes

- Exclude `vendor` in Jekyll config file.
- Fix Liquid syntax error for offending parenthesis. [#479](https://github.com/mmistakes/minimal-mistakes/issues/479)

### Maintenance

- Update gems: `colorator` (1.1.0), `forwardable-extended` (2.6.0), `github-pages` (93), `jekyll` (= 3.2.1), `minima` (= 1.0.1).

## [3.4.3](https://github.com/mmistakes/minimal-mistakes/releases/tag/3.4.3)

### Enhancements

- Make ["honeypot" `input`](https://github.com/mmistakes/minimal-mistakes/commit/06a8249a69a37dddda7e2a5bfbe32056c1a9a607) in Staticman comment form less obvious to spam bots
- Add padding to `.highlight` code blocks to better [align `overflow` scrollbar](https://github.com/mmistakes/minimal-mistakes/commit/e4abec0a6f7f8cff72505ca0754615df294fd5b3) to the bottom.
- Add additional image options for Twitter card social sharing meta tags. [#466](https://github.com/mmistakes/minimal-mistakes/pull/466)
- Add structured data markup for Staticman comments. [#458](https://github.com/mmistakes/minimal-mistakes/issues/458)

### Bug Fixes

- Format `og:locale` tag with `_` instead of `-`. [#462](https://github.com/mmistakes/minimal-mistakes/issues/462)

### Maintenance

- Add note to docs about using `url: http://localhost:4000` when working locally.

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

- Fix `Liquid Exception: undefined method 'gsub' for nil:NilClass in _layouts/single.html` error when `page.title` is null. `<h1>` element is now conditional if `title:` is not set for a `page` or collection item. [#312](https://github.com/mmistakes/minimal-mistakes/issues/312)

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
