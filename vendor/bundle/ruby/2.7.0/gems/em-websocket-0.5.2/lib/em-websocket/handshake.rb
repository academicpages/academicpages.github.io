require "http/parser"
require "uri"

module EventMachine
  module WebSocket

    # Resposible for creating the server handshake response
    class Handshake
      include EM::Deferrable

      attr_reader :parser, :protocol_version

      # Unfortunately drafts 75 & 76 require knowledge of whether the
      # connection is being terminated as ws/wss in order to generate the
      # correct handshake response
      def initialize(secure)
        @parser = Http::Parser.new
        @secure = secure

        @parser.on_headers_complete = proc { |headers|
          @headers = Hash[headers.map { |k,v| [k.downcase, v] }]
        }
      end

      def receive_data(data)
        @parser << data

        if defined? @headers
          process(@headers, @parser.upgrade_data)
        end
      rescue HTTP::Parser::Error => e
        fail(HandshakeError.new("Invalid HTTP header: #{e.message}"))
      end

      # Returns the WebSocket upgrade headers as a hash.
      #
      # Keys are strings, unmodified from the request.
      #
      def headers
        @parser.headers
      end

      # The same as headers, except that the hash keys are downcased
      #
      def headers_downcased
        @headers
      end

      # Returns the request path (excluding any query params)
      #
      def path
        @path
      end

      # Returns the query params as a string foo=bar&baz=...
      def query_string
        @query_string
      end

      def query
        Hash[query_string.split('&').map { |c| c.split('=', 2) }]
      end

      # Returns the WebSocket origin header if provided
      #
      def origin
        @headers["origin"] || @headers["sec-websocket-origin"] || nil
      end

      def secure?
        @secure
      end

      private

      def process(headers, remains)
        unless @parser.http_method == "GET"
          raise HandshakeError, "Must be GET request"
        end

        # Validate request path
        #
        # According to http://tools.ietf.org/search/rfc2616#section-5.1.2, an
        # invalid Request-URI should result in a 400 status code, but
        # HandshakeError's currently result in a WebSocket abort. It's not
        # clear which should take precedence, but an abort will do just fine.
        begin
          uri = URI.parse(@parser.request_url)
          @path = uri.path
          @query_string = uri.query || ""
        rescue URI::InvalidURIError
          raise HandshakeError, "Invalid request URI: #{@parser.request_url}"
        end

        # Validate Upgrade
        unless @parser.upgrade?
          raise HandshakeError, "Not an upgrade request"
        end
        upgrade = @headers['upgrade']
        unless upgrade.kind_of?(String) && upgrade.downcase == 'websocket'
          raise HandshakeError, "Invalid upgrade header: #{upgrade.inspect}"
        end

        # Determine version heuristically
        version = if @headers['sec-websocket-version']
          # Used from drafts 04 onwards
          @headers['sec-websocket-version'].to_i
        elsif @headers['sec-websocket-draft']
          # Used in drafts 01 - 03
          @headers['sec-websocket-draft'].to_i
        elsif @headers['sec-websocket-key1']
          76
        else
          75
        end

        # Additional handling of bytes after the header if required
        case version
        when 75
          if !remains.empty?
            raise HandshakeError, "Extra bytes after header"
          end
        when 76, 1..3
          if remains.length < 8
            # The whole third-key has not been received yet.
            return nil
          elsif remains.length > 8
            raise HandshakeError, "Extra bytes after third key"
          end
          @headers['third-key'] = remains
        end

        handshake_klass = case version
        when 75
          Handshake75
        when 76, 1..3
          Handshake76
        when 5, 6, 7, 8, 13
          Handshake04
        else
          # According to spec should abort the connection
          raise HandshakeError, "Protocol version #{version} not supported"
        end

        upgrade_response = handshake_klass.handshake(@headers, @parser.request_url, @secure)

        handler_klass = Handler.klass_factory(version)

        @protocol_version = version
        succeed(upgrade_response, handler_klass)
      rescue HandshakeError => e
        fail(e)
      end
    end
  end
end
