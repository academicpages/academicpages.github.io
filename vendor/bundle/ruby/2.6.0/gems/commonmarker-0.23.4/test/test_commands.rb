# frozen_string_literal: true

require 'test_helper'

class TestCommands < Minitest::Test
  def test_basic
    out = make_bin('strong.md')
    assert_equal('<p>I am <strong>strong</strong></p>', out)
  end

  def test_does_not_have_extensions
    out = make_bin('table.md')
    assert_includes out, '| a'
    refute_includes out, '<p><del>hi</del>'
    refute_includes out, '<table> <tr> <th> a </th> <td> c </td>'
  end

  def test_understands_extensions
    out = make_bin('table.md', '--extension=table')
    refute_includes out, '| a'
    refute_includes out, '<p><del>hi</del>'
    %w[<table> <tr> <th> a </th> <td> c </td>].each { |html| assert_includes out, html }
  end

  def test_understands_multiple_extensions
    out = make_bin('table.md', '--extension=table,strikethrough')
    refute_includes out, '| a'
    assert_includes out, '<p><del>hi</del>'
    %w[<table> <tr> <th> a </th> <td> c </td>].each { |html| assert_includes out, html }
  end

  def test_understands_html_format_with_renderer_and_extensions
    out = make_bin('table.md', '--to=html --extension=table,strikethrough --html-renderer')
    refute_includes out, '| a'
    assert_includes out, '<p><del>hi</del>'
    %w[<table> <tr> <th> a </th> <td> c </td>].each { |html| assert_includes out, html }
  end

  def test_understands_xml_format
    out = make_bin('strong.md', '--to=xml')
    assert_includes out, '<?xml version="1.0" encoding="UTF-8"?>'
    assert_includes out, '<text xml:space="preserve">strong</text>'
  end

  def test_understands_commonmark_format
    out = make_bin('strong.md', '--to=commonmark')
    assert_equal('I am **strong**', out)
  end

  def test_understands_plaintext_format
    out = make_bin('strong.md', '--to=plaintext')
    assert_equal('I am strong', out)
  end

  def test_aborts_invalid_format
    _out, err = capture_subprocess_io do
      make_bin('strong.md', '--to=unknown')
    end

    assert_match "format 'unknown' not found", err
  end

  def test_aborts_format_and_html_renderer_combinations
    (CommonMarker::Config::OPTS[:format] - [:html]).each do |format|
      _out, err = capture_subprocess_io do
        make_bin('strong.md', "--to=#{format} --html-renderer")
      end

      assert_match "format '#{format}' does not support using the HtmlRenderer renderer", err
    end
  end
end
