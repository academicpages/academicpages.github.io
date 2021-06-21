# frozen_string_literal: true

require "sassc"
require "jekyll/utils"
require "jekyll/converters/scss"

module Jekyll
  module Converters
    class Sass < Scss
      EXTENSION_PATTERN = %r!^\.sass$!i.freeze

      safe true
      priority :low

      def syntax
        :sass
      end
    end
  end
end
