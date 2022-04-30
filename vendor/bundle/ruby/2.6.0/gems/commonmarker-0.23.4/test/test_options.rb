# frozen_string_literal: true

require 'test_helper'

class TestExtensions < Minitest::Test
  def test_full_info_string
    md = <<~MD
      ```ruby
      module Foo
      ```
    MD

    CommonMarker.render_html(md, :FULL_INFO_STRING).tap do |out|
      assert_includes out, '<pre><code class="language-ruby">'
    end

    md = <<~MD
      ```ruby my info string
      module Foo
      ```
    MD

    CommonMarker.render_html(md, :FULL_INFO_STRING).tap do |out|
      assert_includes out, '<pre><code class="language-ruby" data-meta="my info string">'
    end

    md = <<~MD
      ```ruby my \x00 string
      module Foo
      ```
    MD

    CommonMarker.render_html(md, :FULL_INFO_STRING).tap do |out|
      assert_includes out, %(<pre><code class="language-ruby" data-meta="my � string">)
    end
  end
end
