# CHANGELOG

## 2.12.3

  * Bug fix in `SyntaxHighlightFilter` [#325](https://github.com/jch/html-pipeline/pull/325)

## 2.12.2

  * Allow unsafe option for Custom Renderer of `MarkdownFilter` [#322](https://github.com/jch/html-pipeline/pull/322)
  * Test with minitest-focus

## 2.12.1

  * Allow Custom Renderer for `MarkdownFilter` [#318](https://github.com/jch/html-pipeline/pull/318)
  * Test against more Rails versions

## 2.12.0

  * Team mention filter [#314](https://github.com/jch/html-pipeline/pull/314)

## 2.11.1

  * Avoid YARD warning: Unknown tag @mention [#309](https://github.com/jch/html-pipeline/pull/309)
  * Freeze string literals in Ruby 2.3 and beyond [#313](https://github.com/jch/html-pipeline/pull/313)

## 2.11.0

  * Test against Ruby 2.4 [#310](https://github.com/jch/html-pipeline/pull/310)
  * CamoFilter: use String#unpack to hexencode URLs [#256](https://github.com/jch/html-pipeline/pull/256)

## 2.10.0

  * Add XMPP URI [#307](https://github.com/jch/html-pipeline/pull/307)
  * Stop testing against Ruby 2.2

## 2.9.2

  * Whitelist various inline semantic/formatting tags [#306](https://github.com/jch/html-pipeline/pull/306)

## 2.9.1

  * Render irc and ircs URLs [#191](https://github.com/jch/html-pipeline/pull/191)

## 2.9.0

  * Fix one more missing freeze [#300](https://github.com/jch/html-pipeline/pull/300)
  * Adds `UNSAFE` option to CommonMarker usage where needed [#304](https://github.com/jch/html-pipeline/pull/304)

## 2.8.4

  * Freeze all elements in HTML::Pipeline::SanitizationFilter [#299](https://github.com/jch/html-pipeline/pull/299)

## 2.8.3

  * Whitelist some accessibility properties [#298](https://github.com/jch/html-pipeline/pull/298)

## 2.8.2

  * Update ruby-sanitize (fixes CVE-2018-3740)

## 2.8.1

  * Fix XSS vulnerability on table of content generation [#296](https://github.com/jch/html-pipeline/pull/296)

## 2.8.0

  * Ensure `<pre>` nodes are not removed after syntax highlighting [#295](https://github.com/jch/html-pipeline/pull/295)

## 2.7.2

  * Apply mention filter & emoji filter on node text [#290](https://github.com/jch/html-pipeline/pull/290)
  * Disable processing @mentions in `<script>` tag [#292](https://github.com/jch/html-pipeline/pull/292)
  * Update dependencies [#291](https://github.com/jch/html-pipeline/pull/291)

## 2.7.1

  * Output underlying load error when wrapping [#284](https://github.com/jch/html-pipeline/pull/284)

## 2.7.0

  * Let users set the common marker extensions [#279](https://github.com/jch/html-pipeline/pull/279)

## 2.6.0

  * Switch from github-markdown to CommonMark [#274](https://github.com/jch/html-pipeline/pull/274)
  * Fixed a few warnings

## 2.5.0

  * Ruby 2.4 support. Backwards compatible, but bumped minor version so projects can choose to lock at older version [#268](https://github.com/jch/html-pipeline/pull/268)

## 2.4.2

  * Make EmojiFilter generated img tag HTML attributes configurable [#258](https://github.com/jch/html-pipeline/pull/258)

## 2.4.1

  * Regression in EmailReplyPipeline: unfiltered content is being omitted [#253](https://github.com/jch/html-pipeline/pull/253)

## 2.4.0

  * Optionally filter email addresses [#247](https://github.com/jch/html-pipeline/pull/247)

## 2.3.0

  * Add option to pass in an anchor icon, instead of using octicons [#244](https://github.com/jch/html-pipeline/pull/244)

## 2.2.4

  * Use entire namespace so MissingDependencyError constant is resolved [#243](https://github.com/jch/html-pipeline/pull/243)

## 2.2.3

  * raise MissingDependencyError instead of aborting on missing dependency [#241](https://github.com/jch/html-pipeline/pull/241)
  * Fix typo [#239](https://github.com/jch/html-pipeline/pull/239)
  * Test against Ruby 2.3.0 on Travis CI [#238](https://github.com/jch/html-pipeline/pull/238)
  * use travis containers [#237](https://github.com/jch/html-pipeline/pull/237)

## 2.2.2

  * Fix for calling mention_link_filter with only one argument [#230](https://github.com/jch/html-pipeline/pull/230)
  * Add html-pipeline-linkify_github to 3rd Party Extensions in README [#228](https://github.com/jch/html-pipeline/pull/228)

## 2.2.1

  * Soften Nokogiri dependency to versions ">= 1.4" [#208](https://github.com/jch/html-pipeline/pull/208)

## 2.2.0

  * Only allow cite attribute on blockquote and restrict schemes [#223](https://github.com/jch/html-pipeline/pull/223)

## 2.1.0

  * Whitelist schemes for longdesc [#221](https://github.com/jch/html-pipeline/pull/221)
  * Extract emoji image tag generation to own method [#195](https://github.com/jch/html-pipeline/pull/195)
  * Update README.md [#211](https://github.com/jch/html-pipeline/pull/211)
  * Add ImageFilter for image url to img tag conversion [#207](https://github.com/jch/html-pipeline/pull/207)

## 2.0

**New**

  * Implement new EmojiFilter context option: ignored_ancestor_tags to accept more ignored tags. [#170](https://github.com/jch/html-pipeline/pull/170) @JuanitoFatas
  * Add GitHub flavor Markdown Task List extension [#162](https://github.com/jch/html-pipeline/pull/162) @simeonwillbanks
  * @mention allow for custom regex to identify usernames. [#157](https://github.com/jch/html-pipeline/pull/157) @brittballard
  * EmojiFilter now requires gemoji ~> 2. [#159](https://github.com/jch/html-pipeline/pull/159) @jch

**Changes**

  * Restrict nokogiri to >= 1.4, <= 1.6.5 [#176](https://github.com/jch/html-pipeline/pull/176) @simeonwillbanks
  * MentionFilter#link_to_mentioned_user: Replace String introspection with Regexp match [#172](https://github.com/jch/html-pipeline/pull/172) @simeonwillbanks
  * Whitelist summary and details element. [#171](https://github.com/jch/html-pipeline/pull/171) @JuanitoFatas
  * Support ~login for MentionFilter. [#167](https://github.com/jch/html-pipeline/pull/167) @JuanitoFatas
  * Revert "Search for text nodes on DocumentFragments without root tags" [#158](https://github.com/jch/html-pipeline/pull/158) @jch
  * Drop support for ruby ree, 1.9.2, 1.9.3 [#156](https://github.com/jch/html-pipeline/pull/156) @jch
  * Skip EmojiFilter in `<tt>` tags [#147](https://github.com/jch/html-pipeline/pull/147) @moskvax
  * Use Linguist lexers [#153](https://github.com/jch/html-pipeline/pull/153) @pchaigno
  * Constrain Active Support >= 2, < 5 [#180](https://github.com/jch/html-pipeline/pull/180) @jch

## 1.11.0

  * Search for text nodes on DocumentFragments without root tags #146 Razer6
  * Don't filter @mentions in `<style>` tags #145 jch
  * Prefer `http_url` in HttpsFilter. `base_url` still works. #142 bkeepers
  * Remove duplicate check in EmojiFilter #141 Razer6

## 1.10.0

  * Anchor TOCFilter with id's instead of name's #140 bkeepers
  * Add `details` to sanitization whitelist #139 tansaku
  * Fix README spelling #137 Razer6
  * Remove ActiveSupport `try` dependency #132 simeonwillbanks

## 1.9.0

  * Generalize https filter with :base_url #124 #131 rymohr
  * Clean up gemspec dependencies #130 mislav
  * EmojiFilter compatibility with gemoji v2 #129 mislav
  * Now using Minitest #126 simeonwillbanks

## 1.8.0

  * Add custom path support for EmojiFilter #122 bradly
  * Reorganize README and add table of contents #118 simeonwillbanks

## 1.7.0

  * SanitizationFilter whitelists <s> and <strike> elements #120 charliesome
  * ruby 2.1.1 support #119 simeonwillbanks

## 1.6.0

  * Doc update for syntax highlighting #108 simeonwillbanks
  * Add missing dependency for EmailReplyFilter #110 foca
  * Fix deprecation warning for Digest::Digest #103 chrishunt

## 1.5.0

  * More flexible whitelist configuration for SanitizationFilter #98 aroben

## 1.4.0

  * Fix CamoFilter double entity encoding. #101 josh

## 1.3.0

1.2.0 didn't actually include the following changes. Yanked that release.

  * CamoFilter now camos https images. #96 josh

## 1.1.0

  * escape emoji filenames in urls #92 jayroh

## 1.0.0

To upgrade to this release, you will need to include separate gems for each of
the filters. See [this section of the README](/README.md#dependencies) for
details.

  * filter dependencies are no longer included #80 from simeonwillbanks/simple-dependency-management
  * Add link_attr option to Autolink filter #89 from excid3/master
  * Add ActiveSupport back in as dependency for xml-mini #85 from mojavelinux/xml-mini

## 0.3.1

  * Guard against nil node replacement in SyntaxHighlightFilter #84 jbarnette

## 0.3.0

  * Add support for manually specified default language in SyntaxHighlightFilter #81 jbarnette

## 0.2.1

  * Moves ActiveSupport as a development dependency #79

## 0.2.0

  * Fix README typo #74 tricknotes
  * TableOfContentsFilter generates list of sections #75 simeonwillbanks

## 0.1.0

I realized I wasn't properly following [semver](http://semver.org) for interface
changes and new features. Starting from this release, semver will be followed.

  * Whitelist table section elements in sanitization filter #55 mojavelinux
  * Update readme typo #57 envygeeks
  * TOC unicode characters and anchor names for Ruby > 1.9 #64 jakedouglas/non_english_anchors
  * Add :skip_tags option for AutolinkFilter #65 pengwynn
  * Fix CI dependency issues #67 jch
  * Fix ignored test and add Ruby 2.0 to CI. #71, #72 tricknotes

## 0.0.14

  * Remove unused can_access_repo? method jch

## 0.0.13

  * Update icon class name (only affects TOC pipeline) cameronmcefee #52

## 0.0.12

  * add additional payload information for instrumentation mtodd #46
  * generate and link to gem docs in README

## 0.0.11

  * add instrumentation support. readme cleanup mtodd #45

## 0.0.10

  * add bin/html-pipeline util indirect #44
  * add result[:mentioned_usernames] for MentionFilter fachen #42

## 0.0.9

  * bump escape_utils ~> 0.3, github-linguist ~> 2.6.2 brianmario #41
  * remove nokogiri monkey patch for ruby >= 1.9 defunkt #40

## 0.0.8

  * raise LoadError instead of printing to stderr if linguist is missing. gjtorikian #36

## 0.0.7

  * optionally require github-linguist chrislloyd #33

## 0.0.6

  * don't mutate markdown strings: jakedouglas #32

## 0.0.5

  * fix li xss vulnerability in sanitization filter: vmg #31
  * gemspec cleanup: nbibler #23, jbarnette #24
  * doc updates: jch #16, pborreli #17, wickedshimmy #18, benubois #19, blackerby #21
  * loosen gemoji dependency: josh #15

## 0.0.4

  * initial public release
