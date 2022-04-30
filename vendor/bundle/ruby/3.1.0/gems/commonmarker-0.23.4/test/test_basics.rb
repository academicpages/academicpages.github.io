# frozen_string_literal: true

require 'test_helper'

class TestBasics < Minitest::Test
  def setup
    @doc = CommonMarker.render_doc('Hi *there*')
  end

  def test_to_html
    assert_equal "<p>Hi <em>there</em></p>\n", @doc.to_html
  end

  def test_markdown_to_html
    html = CommonMarker.render_html('Hi *there*')
    assert_equal "<p>Hi <em>there</em></p>\n", html
  end

  # basic test that just checks if every option is accepted & no errors are thrown
  def test_accept_every_option
    text = "Hello **world** -- how are _you_ today? I'm ~~fine~~, ~yourself~?"
    parse_opt = %i[SOURCEPOS UNSAFE VALIDATE_UTF8 SMART LIBERAL_HTML_TAG FOOTNOTES STRIKETHROUGH_DOUBLE_TILDE]
    render_opt = parse_opt + %i[HARDBREAKS NOBREAKS GITHUB_PRE_LANG TABLE_PREFER_STYLE_ATTRIBUTES FULL_INFO_STRING]

    extensions = %i[table tasklist strikethrough autolink tagfilter]

    assert_equal "<p>Hello <strong>world</strong> – how are <em>you</em> today? I’m <del>fine</del>, ~yourself~?</p>\n", CommonMarker.render_doc(text, parse_opt, extensions).to_html

    # NOTE: how tho the doc returned has sourcepos info, by default the renderer
    # won't emit it. for that we need to pass in the render opt
    assert_equal "<p data-sourcepos=\"1:1-1:65\">Hello <strong>world</strong> – how are <em>you</em> today? I’m <del>fine</del>, ~yourself~?</p>\n", CommonMarker.render_doc(text, parse_opt, extensions).to_html(render_opt, extensions)

    assert_equal "<p data-sourcepos=\"1:1-1:65\">Hello <strong>world</strong> – how are <em>you</em> today? I’m <del>fine</del>, ~yourself~?</p>\n", CommonMarker.render_html(text, parse_opt, extensions)
  end
end
