# frozen_string_literal: true

# Jekyll 4.x comptable caching class for pre-4.x compatability
module JekyllIncludeCache
  class Cache
    extend Forwardable

    def_delegators :@cache, :[]=, :key?, :delete, :clear

    def initialize(_name = nil)
      @cache = {}
    end

    def getset(key)
      if key?(key)
        @cache[key]
      else
        value = yield
        @cache[key] = value
        value
      end
    end

    def [](key)
      if key?(key)
        @cache[key]
      else
        raise
      end
    end
  end
end
