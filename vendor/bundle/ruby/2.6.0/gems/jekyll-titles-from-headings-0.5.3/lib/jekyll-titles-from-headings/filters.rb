# frozen_string_literal: true

module JekyllTitlesFromHeadings
  class Filters
    include Jekyll::Filters
    include Liquid::StandardFilters

    def initialize(site)
      @site    = site
      @context = JekyllTitlesFromHeadings::Context.new(site)
    end
  end
end
