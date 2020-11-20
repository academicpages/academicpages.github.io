# frozen_string_literal: true

require "jekyll"
require "fileutils"
require "jekyll-feed/generator"

module JekyllFeed
  autoload :MetaTag,          "jekyll-feed/meta-tag"
  autoload :PageWithoutAFile, "jekyll-feed/page-without-a-file.rb"
end

Liquid::Template.register_tag "feed_meta", JekyllFeed::MetaTag
