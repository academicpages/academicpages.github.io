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
    content = '''
| Input       | Expected         | Actual    |
| ----------- | ---------------- | --------- |
| One         | Two              | Three     |

| Header   | Row  | Example |
| :------: | ---: | :------ |
| Foo      | Bar  | Baz     |
'''
    doc = CommonMarker.render_doc(content, :DEFAULT, [:autolink, :table, :tagfilter])
    results = CommonMarker::HtmlRenderer.new.render(doc)
    assert_equal 2, results.scan(/<tbody>/).size
  end
end
