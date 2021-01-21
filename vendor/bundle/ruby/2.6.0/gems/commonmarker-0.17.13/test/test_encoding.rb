# coding: utf-8
require 'test_helper'

class TestEncoding < Minitest::Test
  # see http://git.io/vq4FR
  def test_encoding
    contents = File.read(File.join(FIXTURES_DIR, 'curly.md'), encoding: 'utf-8')
    doc = CommonMarker.render_doc(contents, :SMART)
    render = doc.to_html
    assert_equal render.rstrip, '<p>This curly quote “makes commonmarker throw an exception”.</p>'
  end

  def test_string_content_is_utf8
    doc = CommonMarker.render_doc('Hi *there*')
    text = doc.first_child.last_child.first_child
    assert_equal text.string_content, 'there'
    assert_equal text.string_content.encoding.name, 'UTF-8'
  end
end
