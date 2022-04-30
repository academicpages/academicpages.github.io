# frozen_string_literal: true

require 'test_helper'

class TestEncoding < Minitest::Test
  # see http://git.io/vq4FR
  def test_encoding
    contents = fixtures_file('curly.md')
    doc = CommonMarker.render_doc(contents, :SMART)
    render = doc.to_html
    assert_equal('<p>This curly quote “makes commonmarker throw an exception”.</p>', render.rstrip)

    render = doc.to_xml
    assert_includes(render, '<text xml:space="preserve">This curly quote “makes commonmarker throw an exception”.</text>')
  end

  def test_string_content_is_utf8
    doc = CommonMarker.render_doc('Hi *there*')
    text = doc.first_child.last_child.first_child
    assert_equal('there', text.string_content)
    assert_equal('UTF-8', text.string_content.encoding.name)
  end
end
