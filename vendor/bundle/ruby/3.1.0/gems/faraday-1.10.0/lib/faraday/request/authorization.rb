# frozen_string_literal: true

require 'base64'

module Faraday
  class Request
    # Request middleware for the Authorization HTTP header
    class Authorization < Faraday::Middleware
      unless defined?(::Faraday::Request::Authorization::KEY)
        KEY = 'Authorization'
      end

      # @param type [String, Symbol]
      # @param token [String, Symbol, Hash]
      # @return [String] a header value
      def self.header(type, token)
        case token
        when String, Symbol, Proc
          token = token.call if token.is_a?(Proc)
          "#{type} #{token}"
        when Hash
          build_hash(type.to_s, token)
        else
          raise ArgumentError,
                "Can't build an Authorization #{type}" \
                  "header from #{token.inspect}"
        end
      end

      # @param type [String]
      # @param hash [Hash]
      # @return [String] type followed by comma-separated key=value pairs
      # @api private
      def self.build_hash(type, hash)
        comma = ', '
        values = []
        hash.each do |key, value|
          value = value.call if value.is_a?(Proc)
          values << "#{key}=#{value.to_s.inspect}"
        end
        "#{type} #{values * comma}"
      end

      # @param app [#call]
      # @param type [String, Symbol] Type of Authorization
      # @param param [String, Symbol, Hash, Proc] parameter to build the Authorization header.
      #   This value can be a proc, in which case it will be invoked on each request.
      def initialize(app, type, param)
        @type = type
        @param = param
        super(app)
      end

      # @param env [Faraday::Env]
      def on_request(env)
        return if env.request_headers[KEY]

        env.request_headers[KEY] = self.class.header(@type, @param)
      end
    end
  end
end
