# frozen_string_literal: true

require 'test_helper'

class TestXml < Minitest::Test
  def setup
    @markdown = <<~MD
      Hi *there*!

      1. I am a numeric list.
      2. I continue the list.
      * Suddenly, an unordered list!
      * What fun!

      Okay, _enough_.

      | a   | b   |
      | --- | --- |
      | c   | d   |
    MD
  end

  def render_doc(doc)
    CommonMarker.render_doc(doc, :DEFAULT, [:table])
  end

  def test_to_xml
    compare = render_doc(@markdown).to_xml(:SOURCEPOS)

    assert_equal <<~XML, compare
      <?xml version="1.0" encoding="UTF-8"?>
      <!DOCTYPE document SYSTEM "CommonMark.dtd">
      <document sourcepos="1:1-12:13" xmlns="http://commonmark.org/xml/1.0">
        <paragraph sourcepos="1:1-1:11">
          <text sourcepos="1:1-1:3" xml:space="preserve">Hi </text>
          <emph sourcepos="1:4-1:10">
            <text sourcepos="1:5-1:9" xml:space="preserve">there</text>
          </emph>
          <text sourcepos="1:11-1:11" xml:space="preserve">!</text>
        </paragraph>
        <list sourcepos="3:1-4:23" type="ordered" start="1" delim="period" tight="true">
          <item sourcepos="3:1-3:23">
            <paragraph sourcepos="3:4-3:23">
              <text sourcepos="3:4-3:23" xml:space="preserve">I am a numeric list.</text>
            </paragraph>
          </item>
          <item sourcepos="4:1-4:23">
            <paragraph sourcepos="4:4-4:23">
              <text sourcepos="4:4-4:23" xml:space="preserve">I continue the list.</text>
            </paragraph>
          </item>
        </list>
        <list sourcepos="5:1-7:0" type="bullet" tight="true">
          <item sourcepos="5:1-5:30">
            <paragraph sourcepos="5:3-5:30">
              <text sourcepos="5:3-5:30" xml:space="preserve">Suddenly, an unordered list!</text>
            </paragraph>
          </item>
          <item sourcepos="6:1-7:0">
            <paragraph sourcepos="6:3-6:11">
              <text sourcepos="6:3-6:11" xml:space="preserve">What fun!</text>
            </paragraph>
          </item>
        </list>
        <paragraph sourcepos="8:1-8:15">
          <text sourcepos="8:1-8:6" xml:space="preserve">Okay, </text>
          <emph sourcepos="8:7-8:14">
            <text sourcepos="8:8-8:13" xml:space="preserve">enough</text>
          </emph>
          <text sourcepos="8:15-8:15" xml:space="preserve">.</text>
        </paragraph>
        <table sourcepos="10:1-12:13">
          <table_header sourcepos="10:1-10:13">
            <table_cell sourcepos="10:2-10:6">
              <text sourcepos="10:3-10:3" xml:space="preserve">a</text>
            </table_cell>
            <table_cell sourcepos="10:8-10:12">
              <text sourcepos="10:9-10:9" xml:space="preserve">b</text>
            </table_cell>
          </table_header>
          <table_row sourcepos="12:1-12:13">
            <table_cell sourcepos="12:2-12:6">
              <text sourcepos="12:3-12:3" xml:space="preserve">c</text>
            </table_cell>
            <table_cell sourcepos="12:8-12:12">
              <text sourcepos="12:9-12:9" xml:space="preserve">d</text>
            </table_cell>
          </table_row>
        </table>
      </document>
    XML
  end

  def test_to_xml_with_quotes
    compare = render_doc('"quotes" should be escaped').to_xml(:DEFAULT)

    assert_equal <<~XML, compare
      <?xml version="1.0" encoding="UTF-8"?>
      <!DOCTYPE document SYSTEM "CommonMark.dtd">
      <document xmlns="http://commonmark.org/xml/1.0">
        <paragraph>
          <text xml:space="preserve">&quot;quotes&quot; should be escaped</text>
        </paragraph>
      </document>
    XML
  end
end
