# frozen_string_literal: true

require "json"

module Jekyll
  module GitHubMetadata
    class Value
      extend Forwardable
      def_delegators :render, :+, :to_s, :to_json, :eql?, :hash

      attr_reader :key, :value

      def initialize(*args)
        case args.size
        when 1
          @key = "{anonymous}"
          @value = args.first
        when 2
          @key = args.first.to_s
          @value = args.last
        else
          raise ArgumentError, "#{args.size} args given but expected 1 or 2"
        end
      end

      def render
        return @rendered if defined? @rendered

        @rendered = @value = Sanitizer.sanitize(call_or_value)
      rescue RuntimeError, NameError => e
        Jekyll::GitHubMetadata.log :error, "Error processing value '#{key}':"
        raise e
      end

      def to_liquid
        case render
        when nil, true, false, Hash, String, Numeric, Array
          value
        else
          to_json
        end
      end

      private

      # Calls the value Proc with the appropriate number of arguments
      # or returns the raw value if it's a literal
      def call_or_value
        return value unless value.respond_to?(:call)

        case value.arity
        when 0
          value.call
        when 1
          value.call(GitHubMetadata.client)
        when 2
          value.call(GitHubMetadata.client, GitHubMetadata.repository)
        else
          raise ArgumentError, "Whoa, arity of 0, 1, or 2 please in your procs."
        end
      end
    end
  end
end
