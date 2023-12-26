# frozen_string_literal: true

require "jekyll"
require "jekyll-titles-from-headings/generator"

module JekyllTitlesFromHeadings
  autoload :Context, "jekyll-titles-from-headings/context"
  autoload :Filters, "jekyll-titles-from-headings/filters"
end
