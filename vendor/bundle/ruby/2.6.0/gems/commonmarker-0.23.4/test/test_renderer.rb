# frozen_string_literal: true

require 'test_helper'

class TestRenderer < Minitest::Test
  def setup
    @doc = CommonMarker.render_doc('Hi *there*')
  end

  def test_html_renderer
    renderer = HtmlRenderer.new
    result = renderer.render(@doc)
    assert_equal "<p>Hi <em>there</em></p>\n", result
  end

  def test_multiple_tables
    content = <<~DOC
      | Input       | Expected         | Actual    |
      | ----------- | ---------------- | --------- |
      | One         | Two              | Three     |

      | Header   | Row  | Example |
      | :------: | ---: | :------ |
      | Foo      | Bar  | Baz     |
    DOC
    doc = CommonMarker.render_doc(content, :DEFAULT, %i[autolink table tagfilter])
    results = CommonMarker::HtmlRenderer.new.render(doc)
    assert_equal 2, results.scan(/<tbody>/).size
  end

  def test_escape_html_encoding
    my_renderer = Class.new(HtmlRenderer) do
      attr_reader :input_encoding, :output_encoding

      def text(node)
        @input_encoding = node.string_content.encoding
        escape_html(node.string_content).tap do |escaped|
          @output_encoding = escaped.encoding
        end
      end
    end

    renderer = my_renderer.new
    assert_equal Encoding::UTF_8, renderer.render(@doc).encoding
    assert_equal renderer.input_encoding, renderer.output_encoding
  end
end
