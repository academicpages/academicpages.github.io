# frozen_string_literal: true

module Jekyll
  class SeoTag
    class Filters
      include Jekyll::Filters
      include Liquid::StandardFilters

      def initialize(context)
        @context = context
      end
    end
  end
end
