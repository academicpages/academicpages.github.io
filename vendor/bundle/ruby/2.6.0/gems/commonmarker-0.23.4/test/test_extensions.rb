# frozen_string_literal: true

require 'test_helper'

class TestExtensions < Minitest::Test
  def setup
    @markdown = fixtures_file('table.md')
  end

  def test_uses_specified_extensions
    CommonMarker.render_html(@markdown, :DEFAULT, %i[]).tap do |out|
      assert_includes out, '| a'
      assert_includes out, '| <strong>x</strong>'
      assert_includes out, '~~hi~~'
    end

    CommonMarker.render_html(@markdown, :DEFAULT, %i[table]).tap do |out|
      refute_includes out, '| a'
      %w[<table> <tr> <th> a </th> <td> c </td> <strong>x</strong>].each { |html| assert_includes out, html }
      assert_includes out, '~~hi~~'
    end

    CommonMarker.render_html(@markdown, :DEFAULT, %i[strikethrough]).tap do |out|
      assert_includes out, '| a'
      refute_includes out, '~~hi~~'
      assert_includes out, '<del>hi</del>'
    end

    doc = CommonMarker.render_doc('~a~ ~~b~~ ~~~c~~~', :STRIKETHROUGH_DOUBLE_TILDE, [:strikethrough])
    assert_equal("<p>~a~ <del>b</del> ~~~c~~~</p>\n", doc.to_html)

    html = CommonMarker.render_html('~a~ ~~b~~ ~~~c~~~', :STRIKETHROUGH_DOUBLE_TILDE, [:strikethrough])
    assert_equal("<p>~a~ <del>b</del> ~~~c~~~</p>\n", html)

    CommonMarker.render_html(@markdown, :DEFAULT, %i[table strikethrough]).tap do |out|
      refute_includes out, '| a'
      refute_includes out, '| <strong>x</strong>'
      refute_includes out, '~~hi~~'
    end
  end

  def test_extensions_with_renderers
    doc = CommonMarker.render_doc(@markdown, :DEFAULT, %i[table])

    doc.to_html.tap do |out|
      refute_includes out, '| a'
      %w[<table> <tr> <th> a </th> <td> c </td> <strong>x</strong>].each { |html| assert_includes out, html }
      assert_includes out, '~~hi~~'
    end

    HtmlRenderer.new.render(doc).tap do |out|
      refute_includes out, '| a'
      %w[<table> <tr> <th> a </th> <td> c </td> <strong>x</strong>].each { |html| assert_includes out, html }
      assert_includes out, '~~hi~~'
    end

    doc = CommonMarker.render_doc('~a~ ~~b~~ ~~~c~~~', :STRIKETHROUGH_DOUBLE_TILDE, [:strikethrough])
    assert_equal("<p>~a~ <del>b</del> ~~~c~~~</p>\n", HtmlRenderer.new.render(doc))
  end

  def test_bad_extension_specifications
    assert_raises(TypeError) { CommonMarker.render_html(@markdown, :DEFAULT, 'nope') }
    assert_raises(TypeError) { CommonMarker.render_html(@markdown, :DEFAULT, ['table']) }
    assert_raises(ArgumentError) { CommonMarker.render_html(@markdown, :DEFAULT, %i[table bad]) }
  end

  def test_comments_are_kept_as_expected
    assert_equal "<!--hello--> <blah> &lt;xmp>\n",
                 CommonMarker.render_html("<!--hello--> <blah> <xmp>\n", :UNSAFE, %i[tagfilter])
  end

  def test_table_prefer_style_attributes
    assert_equal(<<~HTML, CommonMarker.render_html(<<~MD, :TABLE_PREFER_STYLE_ATTRIBUTES, %i[table]))
      <table>
      <thead>
      <tr>
      <th style="text-align: left">aaa</th>
      <th>bbb</th>
      <th style="text-align: center">ccc</th>
      <th>ddd</th>
      <th style="text-align: right">eee</th>
      </tr>
      </thead>
      <tbody>
      <tr>
      <td style="text-align: left">fff</td>
      <td>ggg</td>
      <td style="text-align: center">hhh</td>
      <td>iii</td>
      <td style="text-align: right">jjj</td>
      </tr>
      </tbody>
      </table>
    HTML
      aaa | bbb | ccc | ddd | eee
      :-- | --- | :-: | --- | --:
      fff | ggg | hhh | iii | jjj
    MD
  end

  def test_plaintext
    assert_equal(<<~HTML, CommonMarker.render_doc(<<~MD, :DEFAULT, %i[table strikethrough]).to_plaintext)
      Hello ~there~.

      | a |
      | --- |
      | b |
    HTML
      Hello ~~there~~.

      | a |
      | - |
      | b |
    MD
  end
end
