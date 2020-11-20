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
end
