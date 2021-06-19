# frozen_string_literal: true
require "thread"

module Nokogiri
  module CSS
    class Parser < Racc::Parser
      CACHE_SWITCH_NAME = :nokogiri_css_parser_cache_is_off

      @cache = {}
      @mutex = Mutex.new

      class << self
        # Return a thread-local boolean indicating whether the CSS-to-XPath cache is active. (Default is `true`.)
        def cache_on?
          !Thread.current[CACHE_SWITCH_NAME]
        end

        # Set a thread-local boolean to turn cacheing on and off. Truthy values turn the cache on, falsey values turn the cache off.
        def set_cache(value)
          Thread.current[CACHE_SWITCH_NAME] = !value
        end

        # Get the css selector in +string+ from the cache
        def [](string)
          return unless cache_on?
          @mutex.synchronize { @cache[string] }
        end

        # Set the css selector in +string+ in the cache to +value+
        def []=(string, value)
          return value unless cache_on?
          @mutex.synchronize { @cache[string] = value }
        end

        # Clear the cache
        def clear_cache(create_new_object = false)
          @mutex.synchronize do
            if create_new_object
              @cache = {}
            else
              @cache.clear
            end
          end
        end

        # Execute +block+ without cache
        def without_cache(&block)
          original_cache_setting = cache_on?
          set_cache false
          block.call
        ensure
          set_cache original_cache_setting
        end
      end

      # Create a new CSS parser with respect to +namespaces+
      def initialize(namespaces = {})
        @tokenizer = Tokenizer.new
        @namespaces = namespaces
        super()
      end

      def parse(string)
        @tokenizer.scan_setup string
        do_parse
      end

      def next_token
        @tokenizer.next_token
      end

      # Get the xpath for +string+ using +options+
      def xpath_for(string, options = {})
        key = "#{string}#{options[:ns]}#{options[:prefix]}"
        v = self.class[key]
        return v if v

        args = [
          options[:prefix] || "//",
          options[:visitor] || XPathVisitor.new,
        ]
        self.class[key] = parse(string).map { |ast|
          ast.to_xpath(*args)
        }
      end

      # On CSS parser error, raise an exception
      def on_error(error_token_id, error_value, value_stack)
        after = value_stack.compact.last
        raise SyntaxError.new("unexpected '#{error_value}' after '#{after}'")
      end
    end
  end
end
