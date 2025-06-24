# frozen_string_literal: true

require "jekyll"

module JekyllIncludeCache
  autoload :Tag,   "jekyll-include-cache/tag"
  autoload :Cache, "jekyll-include-cache/cache"

  class << self
    def cache
      @cache ||= if defined? Jekyll::Cache
                   Jekyll::Cache.new(self.class.name)
                 else
                   JekyllIncludeCache::Cache.new
                 end
    end

    def reset
      JekyllIncludeCache.cache.clear
    end
  end
end

Liquid::Template.register_tag("include_cached", JekyllIncludeCache::Tag)
Jekyll::Hooks.register :site, :pre_render do |_site|
  JekyllIncludeCache.reset
end
