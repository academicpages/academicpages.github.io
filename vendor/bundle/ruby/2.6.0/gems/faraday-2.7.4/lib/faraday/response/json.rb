# frozen_string_literal: true

require 'json'

module Faraday
  class Response
    # Parse response bodies as JSON.
    class Json < Middleware
      def initialize(app = nil, parser_options: nil, content_type: /\bjson$/, preserve_raw: false)
        super(app)
        @parser_options = parser_options
        @content_types = Array(content_type)
        @preserve_raw = preserve_raw
      end

      def on_complete(env)
        process_response(env) if parse_response?(env)
      end

      private

      def process_response(env)
        env[:raw_body] = env[:body] if @preserve_raw
        env[:body] = parse(env[:body])
      rescue StandardError, SyntaxError => e
        raise Faraday::ParsingError.new(e, env[:response])
      end

      def parse(body)
        ::JSON.parse(body, @parser_options || {}) unless body.strip.empty?
      end

      def parse_response?(env)
        process_response_type?(env) &&
          env[:body].respond_to?(:to_str)
      end

      def process_response_type?(env)
        type = response_type(env)
        @content_types.empty? || @content_types.any? do |pattern|
          pattern.is_a?(Regexp) ? type.match?(pattern) : type == pattern
        end
      end

      def response_type(env)
        type = env[:response_headers][CONTENT_TYPE].to_s
        type = type.split(';', 2).first if type.index(';')
        type
      end
    end
  end
end

Faraday::Response.register_middleware(json: Faraday::Response::Json)
