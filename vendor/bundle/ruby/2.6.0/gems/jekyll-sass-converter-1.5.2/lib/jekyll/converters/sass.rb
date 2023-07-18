# frozen_string_literal: true

require "sass"
require "jekyll/utils"
require "jekyll/converters/scss"

module Jekyll
  module Converters
    class Sass < Scss
      safe true
      priority :low

      def matches(ext)
        ext =~ %r!^\.sass$!i
      end

      def syntax
        :sass
      end
    end
  end
end
