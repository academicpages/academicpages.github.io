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
    assert_equal @doc.type, :document
  end

  def test_get_type_string
    assert_equal @doc.type_string, 'document'
  end

  def test_get_first_child
    assert_equal @first_child.type, :paragraph
  end

  def test_get_next
    assert_equal @first_child.first_child.next.type, :emph
  end

  def test_insert_before
    paragraph = Node.new(:paragraph)
    assert_equal @first_child.insert_before(paragraph), true
    assert_match "<p></p>\n<p>Hi <em>there</em>.", @doc.to_html
  end

  def test_insert_after
    paragraph = Node.new(:paragraph)
    assert_equal @first_child.insert_after(paragraph), true
    assert_match "<strong>many nodes</strong>!</p>\n<p></p>\n", @doc.to_html
  end

  def test_prepend_child
    code = Node.new(:code)
    assert_equal @first_child.prepend_child(code), true
    assert_match '<p><code></code>Hi <em>there</em>.', @doc.to_html
  end

  def test_append_child
    strong = Node.new(:strong)
    assert_equal @first_child.append_child(strong), true
    assert_match "!<strong></strong></p>\n", @doc.to_html
  end

  def test_get_last_child
    assert_equal @last_child.type, :paragraph
  end

  def test_get_parent
    assert_equal @first_child.first_child.next.parent.type, :paragraph
  end

  def test_get_previous
    assert_equal @first_child.first_child.next.previous.type, :text
  end

  def test_get_url
    assert_equal @link.url, 'https://www.github.com'
  end

  def test_set_url
    assert_equal @link.url = 'https://www.mozilla.org', 'https://www.mozilla.org'
  end

  def test_get_title
    assert_equal @image.title, 'Favicon'
  end

  def test_set_title
    assert_equal @image.title = 'Octocat', 'Octocat'
  end

  def test_get_header_level
    assert_equal @header.header_level, 3
  end

  def test_set_header_level
    assert_equal @header.header_level = 6, 6
  end

  def test_get_list_type
    assert_equal @ul_list.list_type, :bullet_list
    assert_equal @ol_list.list_type, :ordered_list
  end

  def test_set_list_type
    assert_equal @ul_list.list_type = :ordered_list, :ordered_list
    assert_equal @ol_list.list_type = :bullet_list, :bullet_list
  end

  def test_get_list_start
    assert_equal @ol_list.list_start, 1
  end

  def test_set_list_start
    assert_equal @ol_list.list_start = 8, 8
  end

  def test_get_list_tight
    assert_equal @ul_list.list_tight, true
    assert_equal @ol_list.list_tight, true
  end

  def test_set_list_tight
    assert_equal @ul_list.list_tight = false, false
    assert_equal @ol_list.list_tight = false, false
  end

  def test_get_fence_info
    assert_equal @fence.fence_info, 'ruby'
  end

  def test_set_fence_info
    assert_equal @fence.fence_info = 'javascript', 'javascript'
  end
end
