module EventMachine
  module WebSocket
    class Connection < EventMachine::Connection
      include Debugger

      attr_writer :max_frame_size

      # define WebSocket callbacks
      def onopen(&blk);     @onopen = blk;    end
      def onclose(&blk);    @onclose = blk;   end
      def onerror(&blk);    @onerror = blk;   end
      def onmessage(&blk);  @onmessage = blk; end
      def onbinary(&blk);   @onbinary = blk; end
      def onping(&blk);     @onping = blk;    end
      def onpong(&blk);     @onpong = blk;    end

      def trigger_on_message(msg)
        @onmessage.call(msg) if defined? @onmessage
      end
      def trigger_on_binary(msg)
        @onbinary.call(msg) if defined? @onbinary
      end
      def trigger_on_open(handshake)
        @onopen.call(handshake) if defined? @onopen
      end
      def trigger_on_close(event = {})
        @onclose.call(event) if defined? @onclose
      end
      def trigger_on_ping(data)
        @onping.call(data) if defined? @onping
      end
      def trigger_on_pong(data)
        @onpong.call(data) if defined? @onpong
      end
      def trigger_on_error(reason)
        return false unless defined? @onerror
        @onerror.call(reason)
        true
      end

      def initialize(options)
        @options = options
        @debug = options[:debug] || false
        @secure = options[:secure] || false
        @secure_proxy = options[:secure_proxy] || false
        @tls_options = options[:tls_options] || {}
        @close_timeout = options[:close_timeout]
        @outbound_limit = options[:outbound_limit] || 0

        @handler = nil

        debug [:initialize]
      end

      # Use this method to close the websocket connection cleanly
      # This sends a close frame and waits for acknowlegement before closing
      # the connection
      def close(code = nil, body = nil)
        if code && !acceptable_close_code?(code)
          raise "Application code may only use codes from 1000, 3000-4999"
        end

        close_websocket_private(code, body)
      end

      # Deprecated, to be removed in version 0.6
      alias :close_websocket :close

      def post_init
        start_tls(@tls_options) if @secure
      end

      def receive_data(data)
        debug [:receive_data, data]

        if @handler
          @handler.receive_data(data)
        else
          dispatch(data)
        end
      rescue => e
        debug [:error, e]

        # There is no code defined for application errors, so use 3000
        # (which is reserved for frameworks)
        close_websocket_private(3000, "Application error")

        # These are application errors - raise unless onerror defined
        trigger_on_error(e) || raise(e)
      end

      def send_data(data)
        if @outbound_limit > 0 &&
            get_outbound_data_size + data.bytesize > @outbound_limit
          abort(:outbound_limit_reached)
          return 0
        end

        super(data)
      end

      def unbind
        debug [:unbind, :connection]

        @handler.unbind if @handler
      rescue => e
        debug [:error, e]
        # These are application errors - raise unless onerror defined
        trigger_on_error(e) || raise(e)
      end

      def dispatch(data)
        if data.match(%r|^GET /healthcheck|)
          send_healthcheck_response
        elsif data.match(/\A<policy-file-request\s*\/>/)
          send_flash_cross_domain_file
        else
          @handshake ||= begin
            handshake = Handshake.new(@secure || @secure_proxy)

            handshake.callback { |upgrade_response, handler_klass|
              debug [:accepting_ws_version, handshake.protocol_version]
              debug [:upgrade_response, upgrade_response]
              self.send_data(upgrade_response)
              @handler = handler_klass.new(self, @debug)
              @handshake = nil
              trigger_on_open(handshake)
            }

            handshake.errback { |e|
              debug [:error, e]
              trigger_on_error(e)
              # Handshake errors require the connection to be aborted
              abort(:handshake_error)
            }

            handshake
          end

          @handshake.receive_data(data)
        end
      end

      def send_healthcheck_response
        debug [:healthcheck, 'OK']

        healthcheck_res = ["HTTP/1.1 200 OK"]
        healthcheck_res << "Content-Type: text/plain"
        healthcheck_res << "Content-Length: 2"

        healthcheck_res = healthcheck_res.join("\r\n") + "\r\n\r\nOK"

        send_data healthcheck_res

        # handle the healthcheck request transparently
        # no need to notify the user about this connection
        @onclose = nil
        close_connection_after_writing
      end

      def send_flash_cross_domain_file
        file =  '<?xml version="1.0"?><cross-domain-policy><allow-access-from domain="*" to-ports="*"/></cross-domain-policy>'
        debug [:cross_domain, file]
        send_data file

        # handle the cross-domain request transparently
        # no need to notify the user about this connection
        @onclose = nil
        close_connection_after_writing
      end

      # Cache encodings since it's moderately expensive to look them up each time
      ENCODING_SUPPORTED = "string".respond_to?(:force_encoding)
      UTF8 = Encoding.find("UTF-8") if ENCODING_SUPPORTED
      BINARY = Encoding.find("BINARY") if ENCODING_SUPPORTED

      # Send a WebSocket text frame.
      #
      # A WebSocketError may be raised if the connection is in an opening or a
      # closing state, or if the passed in data is not valid UTF-8
      #
      def send_text(data)
        # If we're using Ruby 1.9, be pedantic about encodings
        if ENCODING_SUPPORTED
          # Also accept ascii only data in other encodings for convenience
          unless (data.encoding == UTF8 && data.valid_encoding?) || data.ascii_only?
            raise WebSocketError, "Data sent to WebSocket must be valid UTF-8 but was #{data.encoding} (valid: #{data.valid_encoding?})"
          end
          # This labels the encoding as binary so that it can be combined with
          # the BINARY framing
          data.force_encoding(BINARY)
        else
          # TODO: Check that data is valid UTF-8
        end

        if @handler
          @handler.send_text_frame(data)
        else
          raise WebSocketError, "Cannot send data before onopen callback"
        end

        # Revert data back to the original encoding (which we assume is UTF-8)
        # Doing this to avoid duping the string - there may be a better way
        data.force_encoding(UTF8) if ENCODING_SUPPORTED
        return nil
      end

      alias :send :send_text

      # Send a WebSocket binary frame.
      #
      def send_binary(data)
        if @handler
          @handler.send_frame(:binary, data)
        else
          raise WebSocketError, "Cannot send binary before onopen callback"
        end
      end

      # Send a ping to the client. The client must respond with a pong.
      #
      # In the case that the client is running a WebSocket draft < 01, false
      # is returned since ping & pong are not supported
      #
      def ping(body = '')
        if @handler
          @handler.pingable? ? @handler.send_frame(:ping, body) && true : false
        else
          raise WebSocketError, "Cannot ping before onopen callback"
        end
      end

      # Send an unsolicited pong message, as allowed by the protocol. The
      # client is not expected to respond to this message.
      #
      # em-websocket automatically takes care of sending pong replies to
      # incoming ping messages, as the protocol demands.
      #
      def pong(body = '')
        if @handler
          @handler.pingable? ? @handler.send_frame(:pong, body) && true : false
        else
          raise WebSocketError, "Cannot ping before onopen callback"
        end
      end

      # Test whether the connection is pingable (i.e. the WebSocket draft in
      # use is >= 01)
      def pingable?
        if @handler
          @handler.pingable?
        else
          raise WebSocketError, "Cannot test whether pingable before onopen callback"
        end
      end

      def supports_close_codes?
        if @handler
          @handler.supports_close_codes?
        else
          raise WebSocketError, "Cannot test before onopen callback"
        end
      end

      def state
        @handler ? @handler.state : :handshake
      end

      # Returns the IP address for the remote peer
      def remote_ip
        get_peername[2,6].unpack('nC4')[1..4].join('.')
      end

      # Returns the maximum frame size which this connection is configured to
      # accept. This can be set globally or on a per connection basis, and
      # defaults to a value of 10MB if not set.
      #
      # The behaviour when a too large frame is received varies by protocol,
      # but in the newest protocols the connection will be closed with the
      # correct close code (1009) immediately after receiving the frame header
      #
      def max_frame_size
        defined?(@max_frame_size) ? @max_frame_size : WebSocket.max_frame_size
      end

      def close_timeout
        @close_timeout || WebSocket.close_timeout
      end

      private

      # As definited in draft 06 7.2.2, some failures require that the server
      # abort the websocket connection rather than close cleanly
      def abort(reason)
        debug [:abort, reason]
        close_connection
      end

      def close_websocket_private(code, body)
        if @handler
          debug [:closing, code]
          @handler.close_websocket(code, body)
        else
          # The handshake hasn't completed - should be safe to terminate
          abort(:handshake_incomplete)
        end
      end

      # Allow applications to close with 1000, 1003, 1008, 1011, 3xxx or 4xxx.
      #
      # em-websocket uses a few other codes internally which should not be
      # used by applications
      #
      # Browsers generally allow connections to be closed with code 1000,
      # 3xxx, and 4xxx. em-websocket allows closing with a few other codes
      # which seem reasonable (for discussion see
      # https://github.com/igrigorik/em-websocket/issues/98)
      #
      # Usage from the rfc:
      #
      # 1000 indicates a normal closure
      #
      # 1003 indicates that an endpoint is terminating the connection
      # because it has received a type of data it cannot accept
      #
      # 1008 indicates that an endpoint is terminating the connection because
      # it has received a message that violates its policy
      #
      # 1011 indicates that a server is terminating the connection because it
      # encountered an unexpected condition that prevented it from fulfilling
      # the request
      #
      # Status codes in the range 3000-3999 are reserved for use by libraries,
      # frameworks, and applications
      #
      # Status codes in the range 4000-4999 are reserved for private use and
      # thus can't be registered
      #
      def acceptable_close_code?(code)
        case code
        when 1000, 1003, 1008, 1011, (3000..4999)
          true
        else
          false
        end
      end
    end
  end
end
