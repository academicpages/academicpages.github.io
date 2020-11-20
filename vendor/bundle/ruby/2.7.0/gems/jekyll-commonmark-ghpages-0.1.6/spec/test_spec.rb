require "spec_helper"

describe JekyllCommonMarkCustomRenderer do
  let(:renderer) { JekyllCommonMarkCustomRenderer.new }
  subject { renderer.render(doc) }

  context "headers" do
    let(:doc) { CommonMarker.render_doc("# Hello\n\n## Hi, world!") }
    it { is_expected.to match %r{<h1 id="hello">Hello</h1>} }
    it { is_expected.to match %r{<h2 id="hi-world">Hi, world!</h2>} }
  end

  context "code blocks" do
    let(:doc) { CommonMarker.render_doc("```ruby\nputs \"Hi!\"\n```\n") }
    it { is_expected.to match %r{<div class="language-ruby highlighter-rouge">} }
    it { is_expected.to match %r{<code><span class=".*?">puts</span> <span class=".*?">"Hi!"</span>} }
  end
end

describe Jekyll::Converters::Markdown::CommonMarkGhPages do
  let(:converter) { Jekyll::Converters::Markdown::CommonMarkGhPages.new(config) }
  let(:config) {
    {"commonmark" => {
      "options" => ["SMART", "FOOTNOTES"],
      "extensions" => ["tagfilter"],
    }}
  }
  subject { converter.convert("### \"Hi\" <xmp>[^nb]\n\n[^nb]: Yes.\n") }

  it { is_expected.to match %r{<h3 id="[^"]*">“Hi” &lt;xmp><sup[^>]*><a href="#fn1"[^>]*>1</a></sup></h3>\n<section class="footnotes">\n<ol>\n<li id="fn1">\n<p>Yes. <a href="#fnref1".*</a></p>} }
end

describe Jekyll::Renderer do
  it "should not re-process markdown in a liquid tag" do
    site = Jekyll::Site.new(Jekyll.configuration("markdown" => "CommonMarkGhPages"))
    collection = Jekyll::Collection.new(site, "pages")
    document = Jekyll::Document.new("hello.md", site: site, collection: collection)
    document.content = "**Hi**\n" \
                       "\n" \
                       "```markdown\n" \
                       "**Yo**\n" \
                       "```\n" \
                       "\n" \
                       "{% highlight markdown %}\n" \
                       "**Hey**\n" \
                       "\n" \
                       "**Hello**\n" \
                       "{% endhighlight %}\n"
    out = Jekyll::Renderer.new(site, document).run
    expect(out).to match %r(<p><strong>Hi</strong></p>)
    expect(out).to match %r(<span class="gs">\*\*Yo\*\*</span>)
    expect(out).to match %r(<span class="gs">\*\*Hey\*\*</span>\n\n)
    expect(out).to match %r(<span class="gs">\*\*Hello\*\*</span>)
  end
end
