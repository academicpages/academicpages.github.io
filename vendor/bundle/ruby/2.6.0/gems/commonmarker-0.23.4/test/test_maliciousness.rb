# frozen_string_literal: true

require 'test_helper'

module CommonMarker
  class TestMaliciousness < Minitest::Test
    def setup
      @doc = CommonMarker.render_doc('Hi *there*')
    end

    def test_init_with_bad_type
      assert_raises TypeError do
        Node.new(123)
      end

      assert_raises NodeError do
        Node.new(:totes_fake)
      end

      assert_raises TypeError do
        Node.new([])
      end

      assert_raises TypeError do
        Node.new([23])
      end

      assert_raises TypeError do
        Node.new(nil)
      end
    end

    def test_rendering_with_bad_type
      assert_raises TypeError do
        CommonMarker.render_html("foo \n baz", 123)
      end

      assert_raises TypeError do
        CommonMarker.render_html("foo \n baz", :totes_fake)
      end

      assert_raises TypeError do
        CommonMarker.render_html("foo \n baz", [])
      end

      assert_raises TypeError do
        CommonMarker.render_html("foo \n baz", [23])
      end

      assert_raises TypeError do
        CommonMarker.render_html("foo \n baz", nil)
      end

      assert_raises TypeError do
        CommonMarker.render_html("foo \n baz", [:SMART, 'totes_fake'])
      end

      assert_raises TypeError do
        CommonMarker.render_html(123)
      end

      assert_raises TypeError do
        CommonMarker.render_html([123])
      end

      assert_raises TypeError do
        CommonMarker.render_html(nil)
      end

      assert_raises TypeError do
        CommonMarker.render_doc("foo \n baz", 123)
      end

      err = assert_raises TypeError do
        CommonMarker.render_doc("foo \n baz", :safe)
      end
      assert_equal('option \':safe\' does not exist for CommonMarker::Config::OPTS[:parse]', err.message)

      assert_raises TypeError do
        CommonMarker.render_doc("foo \n baz", :totes_fake)
      end

      assert_raises TypeError do
        CommonMarker.render_doc("foo \n baz", [])
      end

      assert_raises TypeError do
        CommonMarker.render_doc("foo \n baz", [23])
      end

      assert_raises TypeError do
        CommonMarker.render_doc("foo \n baz", nil)
      end

      assert_raises TypeError do
        CommonMarker.render_doc("foo \n baz", [:SMART, 'totes_fake'])
      end

      assert_raises TypeError do
        CommonMarker.render_doc(123)
      end

      assert_raises TypeError do
        CommonMarker.render_doc([123])
      end

      assert_raises TypeError do
        CommonMarker.render_doc(nil)
      end
    end

    def test_bad_set_string_content
      assert_raises TypeError do
        @doc.string_content = 123
      end
    end

    def test_bad_walking
      assert_nil @doc.parent
      assert_nil @doc.previous
    end

    def test_bad_insertion
      code = Node.new(:code)
      assert_raises NodeError do
        @doc.insert_before(code)
      end

      paragraph = Node.new(:paragraph)
      assert_raises NodeError do
        @doc.insert_after(paragraph)
      end

      document = Node.new(:document)
      assert_raises NodeError do
        @doc.prepend_child(document)
      end

      assert_raises NodeError do
        @doc.append_child(document)
      end
    end

    def test_bad_url_get
      assert_raises NodeError do
        @doc.url
      end
    end

    def test_bad_url_set
      assert_raises NodeError do
        @doc.url = '123'
      end

      link = CommonMarker.render_doc('[GitHub](https://www.github.com)').first_child.first_child
      assert_raises TypeError do
        link.url = 123
      end
    end

    def test_bad_title_get
      assert_raises NodeError do
        @doc.title
      end
    end

    def test_bad_title_set
      assert_raises NodeError do
        @doc.title = '123'
      end

      image = CommonMarker.render_doc('![alt text](https://github.com/favicon.ico "Favicon")')
      image = image.first_child.first_child
      assert_raises TypeError do
        image.title = 123
      end
    end

    def test_bad_header_level_get
      assert_raises NodeError do
        @doc.header_level
      end
    end

    def test_bad_header_level_set
      assert_raises NodeError do
        @doc.header_level = 1
      end

      header = CommonMarker.render_doc('### Header Three').first_child
      assert_raises TypeError do
        header.header_level = '123'
      end
    end

    def test_bad_list_type_get
      assert_raises NodeError do
        @doc.list_type
      end
    end

    def test_bad_list_type_set
      assert_raises NodeError do
        @doc.list_type = :bullet_list
      end

      ul_list = CommonMarker.render_doc("* Bullet\n*Bullet").first_child
      assert_raises NodeError do
        ul_list.list_type = :fake
      end
      assert_raises TypeError do
        ul_list.list_type = 1234
      end
    end

    def test_bad_list_start_get
      assert_raises NodeError do
        @doc.list_start
      end
    end

    def test_bad_list_start_set
      assert_raises NodeError do
        @doc.list_start = 12
      end

      ol_list = CommonMarker.render_doc("1. One\n2. Two").first_child
      assert_raises TypeError do
        ol_list.list_start = :fake
      end
    end

    def test_bad_list_tight_get
      assert_raises NodeError do
        @doc.list_tight
      end
    end

    def test_bad_list_tight_set
      assert_raises NodeError do
        @doc.list_tight = false
      end
    end

    def test_bad_fence_info_get
      assert_raises NodeError do
        @doc.fence_info
      end
    end

    def test_bad_fence_info_set
      assert_raises NodeError do
        @doc.fence_info = 'ruby'
      end

      fence = CommonMarker.render_doc("``` ruby\nputs 'wow'\n```").first_child
      assert_raises TypeError do
        fence.fence_info = 123
      end
    end
  end
end
