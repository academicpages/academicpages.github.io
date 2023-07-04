# HTML::Pipeline [![Build Status](https://travis-ci.org/jch/html-pipeline.svg?branch=master)](https://travis-ci.org/jch/html-pipeline)

HTML processing filters and utilities. This module includes a small
framework for defining DOM based content filters and applying them to user
provided content.

[This project was started at GitHub](https://github.com/blog/1311-html-pipeline-chainable-content-filters). While GitHub still uses a similar design and pattern for rendering content, this gem should be considered standalone and independent from GitHub.

- [Installation](#installation)
- [Usage](#usage)
  - [Examples](#examples)
- [Filters](#filters)
- [Dependencies](#dependencies)
- [Documentation](#documentation)
- [Extending](#extending)
  - [3rd Party Extensions](#3rd-party-extensions)
- [Instrumenting](#instrumenting)
- [Contributing](#contributing)
  - [Contributors](#contributors)
  - [Releasing A New Version](#releasing-a-new-version)

## Installation

Add this line to your application's Gemfile:

```ruby
gem 'html-pipeline'
```

And then execute:

```sh
$ bundle
```

Or install it by yourself as:

```sh
$ gem install html-pipeline
```

## Usage

This library provides a handful of chainable HTML filters to transform user
content into markup. A filter takes an HTML string or
`Nokogiri::HTML::DocumentFragment`, optionally manipulates it, and then
outputs the result.

For example, to transform Markdown source into Markdown HTML:

```ruby
require 'html/pipeline'

filter = HTML::Pipeline::MarkdownFilter.new("Hi **world**!")
filter.call
```

Filters can be combined into a pipeline which causes each filter to hand its
output to the next filter's input. So if you wanted to have content be
filtered through Markdown and be syntax highlighted, you can create the
following pipeline:

```ruby
pipeline = HTML::Pipeline.new [
  HTML::Pipeline::MarkdownFilter,
  HTML::Pipeline::SyntaxHighlightFilter
]
result = pipeline.call <<-CODE
This is *great*:

    some_code(:first)

CODE
result[:output].to_s
```

Prints:

```html
<p>This is <em>great</em>:</p>

<pre><code>some_code(:first)
</code></pre>
```

To generate CSS for HTML formatted code, use the [Rouge CSS Theme](https://github.com/rouge-ruby/rouge#css-options) `#css` method. `rouge` is a dependency of the `SyntaxHighlightFilter`.

Some filters take an optional **context** and/or **result** hash. These are
used to pass around arguments and metadata between filters in a pipeline. For
example, if you don't want to use GitHub formatted Markdown, you can pass an
option in the context hash:

```ruby
filter = HTML::Pipeline::MarkdownFilter.new("Hi **world**!", :gfm => false)
filter.call
```

### Examples

We define different pipelines for different parts of our app. Here are a few
paraphrased snippets to get you started:

```ruby
# The context hash is how you pass options between different filters.
# See individual filter source for explanation of options.
context = {
  :asset_root => "http://your-domain.com/where/your/images/live/icons",
  :base_url   => "http://your-domain.com"
}

# Pipeline providing sanitization and image hijacking but no mention
# related features.
SimplePipeline = Pipeline.new [
  SanitizationFilter,
  TableOfContentsFilter, # add 'name' anchors to all headers and generate toc list
  CamoFilter,
  ImageMaxWidthFilter,
  SyntaxHighlightFilter,
  EmojiFilter,
  AutolinkFilter
], context

# Pipeline used for user provided content on the web
MarkdownPipeline = Pipeline.new [
  MarkdownFilter,
  SanitizationFilter,
  CamoFilter,
  ImageMaxWidthFilter,
  HttpsFilter,
  MentionFilter,
  EmojiFilter,
  SyntaxHighlightFilter
], context.merge(:gfm => true) # enable github formatted markdown


# Define a pipeline based on another pipeline's filters
NonGFMMarkdownPipeline = Pipeline.new(MarkdownPipeline.filters,
  context.merge(:gfm => false))

# Pipelines aren't limited to the web. You can use them for email
# processing also.
HtmlEmailPipeline = Pipeline.new [
  PlainTextInputFilter,
  ImageMaxWidthFilter
], {}

# Just emoji.
EmojiPipeline = Pipeline.new [
  PlainTextInputFilter,
  EmojiFilter
], context
```

## Filters

* `MentionFilter` - replace `@user` mentions with links
* `TeamMentionFilter` - replace `@org/team` mentions with links
* `AbsoluteSourceFilter` - replace relative image urls with fully qualified versions
* `AutolinkFilter` - auto_linking urls in HTML
* `CamoFilter` - replace http image urls with [camo-fied](https://github.com/atmos/camo) https versions
* `EmailReplyFilter` - util filter for working with emails
* `EmojiFilter` - everyone loves [emoji](http://www.emoji-cheat-sheet.com/)!
* `HttpsFilter` - HTML Filter for replacing http github urls with https versions.
* `ImageMaxWidthFilter` - link to full size image for large images
* `MarkdownFilter` - convert markdown to html
* `PlainTextInputFilter` - html escape text and wrap the result in a div
* `SanitizationFilter` - allow sanitize user markup
* `SyntaxHighlightFilter` - code syntax highlighter
* `TextileFilter` - convert textile to html
* `TableOfContentsFilter` - anchor headings with name attributes and generate Table of Contents html unordered list linking headings

## Dependencies

Filter gem dependencies are not bundled; you must bundle the filter's gem
dependencies. The below list details filters with dependencies. For example,
`SyntaxHighlightFilter` uses [rouge](https://github.com/jneen/rouge)
to detect and highlight languages. For example, to use the `SyntaxHighlightFilter`,
add the following to your Gemfile:

```ruby
gem 'rouge'
```

* `AutolinkFilter` - `rinku`
* `EmailReplyFilter` - `escape_utils`, `email_reply_parser`
* `EmojiFilter` - `gemoji`
* `MarkdownFilter` - `commonmarker`
* `PlainTextInputFilter` - `escape_utils`
* `SanitizationFilter` - `sanitize`
* `SyntaxHighlightFilter` - `rouge`
* `TableOfContentsFilter` - `escape_utils`
* `TextileFilter` - `RedCloth`

_Note:_ See [Gemfile](/Gemfile) `:test` block for version requirements.

## Documentation

Full reference documentation can be [found here](http://rubydoc.info/gems/html-pipeline/frames).

## Extending
To write a custom filter, you need a class with a `call` method that inherits
from `HTML::Pipeline::Filter`.

For example this filter adds a base url to images that are root relative:

```ruby
require 'uri'

class RootRelativeFilter < HTML::Pipeline::Filter

  def call
    doc.search("img").each do |img|
      next if img['src'].nil?
      src = img['src'].strip
      if src.start_with? '/'
        img["src"] = URI.join(context[:base_url], src).to_s
      end
    end
    doc
  end

end
```

Now this filter can be used in a pipeline:

```ruby
Pipeline.new [ RootRelativeFilter ], { :base_url => 'http://somehost.com' }
```

### 3rd Party Extensions

If you have an idea for a filter, propose it as
[an issue](https://github.com/jch/html-pipeline/issues) first. This allows us discuss
whether the filter is a common enough use case to belong in this gem, or should be
built as an external gem.

Here are some extensions people have built:

* [html-pipeline-asciidoc_filter](https://github.com/asciidoctor/html-pipeline-asciidoc_filter)
* [jekyll-html-pipeline](https://github.com/gjtorikian/jekyll-html-pipeline)
* [nanoc-html-pipeline](https://github.com/burnto/nanoc-html-pipeline)
* [html-pipeline-bitly](https://github.com/dewski/html-pipeline-bitly)
* [html-pipeline-cite](https://github.com/lifted-studios/html-pipeline-cite)
* [tilt-html-pipeline](https://github.com/bradgessler/tilt-html-pipeline)
* [html-pipeline-wiki-link'](https://github.com/lifted-studios/html-pipeline-wiki-link) - WikiMedia-style wiki links
* [task_list](https://github.com/github/task_list) - GitHub flavor Markdown Task List
* [html-pipeline-nico_link](https://github.com/rutan/html-pipeline-nico_link) - An HTML::Pipeline filter for [niconico](http://www.nicovideo.jp) description links
* [html-pipeline-gitlab](https://gitlab.com/gitlab-org/html-pipeline-gitlab) - This gem implements various filters for html-pipeline used by GitLab
* [html-pipeline-youtube](https://github.com/st0012/html-pipeline-youtube) - An HTML::Pipeline filter for YouTube links
* [html-pipeline-flickr](https://github.com/st0012/html-pipeline-flickr) - An HTML::Pipeline filter for Flickr links
* [html-pipeline-vimeo](https://github.com/dlackty/html-pipeline-vimeo) - An HTML::Pipeline filter for Vimeo links
* [html-pipeline-hashtag](https://github.com/mr-dxdy/html-pipeline-hashtag) - An HTML::Pipeline filter for hashtags
* [html-pipeline-linkify_github](https://github.com/jollygoodcode/html-pipeline-linkify_github) - An HTML::Pipeline filter to autolink GitHub urls
* [html-pipeline-redcarpet_filter](https://github.com/bmikol/html-pipeline-redcarpet_filter) - Render Markdown source text into Markdown HTML using Redcarpet
* [html-pipeline-typogruby_filter](https://github.com/bmikol/html-pipeline-typogruby_filter) - Add Typogruby text filters to your HTML::Pipeline
* [korgi](https://github.com/jodeci/korgi) - HTML::Pipeline filters for links to Rails resources


## Instrumenting

Filters and Pipelines can be set up to be instrumented when called. The pipeline
must be setup with an
[ActiveSupport::Notifications](http://api.rubyonrails.org/classes/ActiveSupport/Notifications.html)
compatible service object and a name. New pipeline objects will default to the
`HTML::Pipeline.default_instrumentation_service` object.

``` ruby
# the AS::Notifications-compatible service object
service = ActiveSupport::Notifications

# instrument a specific pipeline
pipeline = HTML::Pipeline.new [MarkdownFilter], context
pipeline.setup_instrumentation "MarkdownPipeline", service

# or set default instrumentation service for all new pipelines
HTML::Pipeline.default_instrumentation_service = service
pipeline = HTML::Pipeline.new [MarkdownFilter], context
pipeline.setup_instrumentation "MarkdownPipeline"
```

Filters are instrumented when they are run through the pipeline. A
`call_filter.html_pipeline` event is published once the filter finishes. The
`payload` should include the `filter` name. Each filter will trigger its own
instrumentation call.

``` ruby
service.subscribe "call_filter.html_pipeline" do |event, start, ending, transaction_id, payload|
  payload[:pipeline] #=> "MarkdownPipeline", set with `setup_instrumentation`
  payload[:filter] #=> "MarkdownFilter"
  payload[:context] #=> context Hash
  payload[:result] #=> instance of result class
  payload[:result][:output] #=> output HTML String or Nokogiri::DocumentFragment
end
```

The full pipeline is also instrumented:

``` ruby
service.subscribe "call_pipeline.html_pipeline" do |event, start, ending, transaction_id, payload|
  payload[:pipeline] #=> "MarkdownPipeline", set with `setup_instrumentation`
  payload[:filters] #=> ["MarkdownFilter"]
  payload[:doc] #=> HTML String or Nokogiri::DocumentFragment
  payload[:context] #=> context Hash
  payload[:result] #=> instance of result class
  payload[:result][:output] #=> output HTML String or Nokogiri::DocumentFragment
end
```

## FAQ

### 1. Why doesn't my pipeline work when there's no root element in the document?

To make a pipeline work on a plain text document, put the `PlainTextInputFilter`
at the beginning of your pipeline. This will wrap the content in a `div` so the
filters have a root element to work with. If you're passing in an HTML fragment,
but it doesn't have a root element, you can wrap the content in a `div`
yourself. For example:

```ruby
EmojiPipeline = Pipeline.new [
  PlainTextInputFilter,  # <- Wraps input in a div and escapes html tags
  EmojiFilter
], context

plain_text = "Gutentag! :wave:"
EmojiPipeline.call(plain_text)

html_fragment = "This is outside of an html element, but <strong>this isn't. :+1:</strong>"
EmojiPipeline.call("<div>#{html_fragment}</div>") # <- Wrap your own html fragments to avoid escaping
```

### 2. How do I customize an allowlist for `SanitizationFilter`s?

`SanitizationFilter::ALLOWLIST` is the default allowlist used if no `:allowlist`
argument is given in the context. The default is a good starting template for
you to add additional elements. You can either modify the constant's value, or
re-define your own constant and pass that in via the context.

## Contributing

Please review the [Contributing Guide](https://github.com/jch/html-pipeline/blob/master/CONTRIBUTING.md).

1. [Fork it](https://help.github.com/articles/fork-a-repo)
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Added some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new [Pull Request](https://help.github.com/articles/using-pull-requests)

To see what has changed in recent versions, see the [CHANGELOG](https://github.com/jch/html-pipeline/blob/master/CHANGELOG.md).

### Contributors

Thanks to all of [these contributors](https://github.com/jch/html-pipeline/graphs/contributors).

Project is a member of the [OSS Manifesto](http://ossmanifesto.org/).

The current maintainer is @gjtorikian

### Releasing A New Version

This section is for gem maintainers to cut a new version of the gem.

* create a new branch named `release-x.y.z` where `x.y.z` follows [semver](http://semver.org)
* update lib/html/pipeline/version.rb to next version number X.X.X
* update CHANGELOG.md. Prepare a draft with `script/changelog`
* push branch and create a new pull request
* after tests are green, merge to master
* on the master branch, run `script/release`
