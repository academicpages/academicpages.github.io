# frozen_string_literal: true

require 'test_helper'

class TestDocNode < Minitest::Test
  def setup
    @doc = CommonMarker.render_doc('Hi *there*. This has __many nodes__!')
    @first_child = @doc.first_child
    @last_child = @doc.last_child
    @link = CommonMarker.render_doc('[GitHub](https://www.github.com)').first_child.first_child
    @image = CommonMarker.render_doc('![alt text](https://github.com/favicon.ico "Favicon")')
    @image = @image.first_child.first_child
    @header = CommonMarker.render_doc('### Header Three').first_child
    @ul_list = CommonMarker.render_doc("* Bullet\n*Bullet").first_child
    @ol_list = CommonMarker.render_doc("1. One\n2. Two").first_child
    @fence = CommonMarker.render_doc("``` ruby\nputs 'wow'\n```").first_child
  end

  def test_get_type
    assert_equal(:document, @doc.type)
  end

  def test_get_type_string
    assert_equal('document', @doc.type_string)
  end

  def test_get_first_child
    assert_equal(:paragraph, @first_child.type)
  end

  def test_get_next
    assert_equal(:emph, @first_child.first_child.next.type)
  end

  def test_insert_before
    paragraph = Node.new(:paragraph)
    assert(@first_child.insert_before(paragraph))
    assert_match "<p></p>\n<p>Hi <em>there</em>.", @doc.to_html
  end

  def test_insert_after
    paragraph = Node.new(:paragraph)
    assert(@first_child.insert_after(paragraph))
    assert_match "<strong>many nodes</strong>!</p>\n<p></p>\n", @doc.to_html
  end

  def test_prepend_child
    code = Node.new(:code)
    assert(@first_child.prepend_child(code))
    assert_match '<p><code></code>Hi <em>there</em>.', @doc.to_html
  end

  def test_append_child
    strong = Node.new(:strong)
    assert(@first_child.append_child(strong))
    assert_match "!<strong></strong></p>\n", @doc.to_html
  end

  def test_get_last_child
    assert_equal(:paragraph, @last_child.type)
  end

  def test_get_parent
    assert_equal(:paragraph, @first_child.first_child.next.parent.type)
  end

  def test_get_previous
    assert_equal(:text, @first_child.first_child.next.previous.type)
  end

  def test_get_url
    assert_equal('https://www.github.com', @link.url)
  end

  def test_set_url
    assert_equal('https://www.mozilla.org', @link.url = 'https://www.mozilla.org')
  end

  def test_get_title
    assert_equal('Favicon', @image.title)
  end

  def test_set_title
    assert_equal('Octocat', @image.title = 'Octocat')
  end

  def test_get_header_level
    assert_equal(3, @header.header_level)
  end

  def test_set_header_level
    assert_equal(6, @header.header_level = 6)
  end

  def test_get_list_type
    assert_equal(:bullet_list, @ul_list.list_type)
    assert_equal(:ordered_list, @ol_list.list_type)
  end

  def test_set_list_type
    assert_equal(:ordered_list, @ul_list.list_type = :ordered_list)
    assert_equal(:bullet_list, @ol_list.list_type = :bullet_list)
  end

  def test_get_list_start
    assert_equal(1, @ol_list.list_start)
  end

  def test_set_list_start
    assert_equal(8, @ol_list.list_start = 8)
  end

  def test_get_list_tight
    assert(@ul_list.list_tight)
    assert(@ol_list.list_tight)
  end

  def test_set_list_tight
    refute(@ul_list.list_tight = false)
    refute(@ol_list.list_tight = false)
  end

  def test_get_fence_info
    assert_equal('ruby', @fence.fence_info)
  end

  def test_set_fence_info
    assert_equal('javascript', @fence.fence_info = 'javascript')
  end
end
