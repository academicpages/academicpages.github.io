# frozen_string_literal: true

require 'test_helper'

class SmartPunctTest < Minitest::Test
  smart_punct = open_spec_file('smart_punct.txt')

  smart_punct.each do |testcase|
    doc = CommonMarker.render_doc(testcase[:markdown], :SMART)
    html = CommonMarker.render_html(testcase[:markdown], :SMART)

    define_method("test_smart_punct_example_#{testcase[:example]}") do
      doc_rendered = doc.to_html.strip
      html_rendered = html.strip

      assert_equal testcase[:html], doc_rendered, testcase[:markdown]
      assert_equal testcase[:html], html_rendered, testcase[:markdown]
    end
  end

  def test_smart_hardbreak_no_spaces_render_doc
    markdown = "\"foo\"\nbaz"
    result = "<p>“foo”<br />\nbaz</p>\n"
    doc = CommonMarker.render_doc(markdown, :SMART)
    assert_equal result, doc.to_html([:HARDBREAKS])
  end
end
