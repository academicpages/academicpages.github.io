module EventMachine
  module WebSocket
    class Handler
      def self.klass_factory(version)
        case version
        when 75
          Handler75
        when 76
          Handler76
        when 1..3
          # We'll use handler03 - I believe they're all compatible
          Handler03
        when 5
          Handler05
        when 6
          Handler06
        when 7
          Handler07
        when 8
          # drafts 9, 10, 11 and 12 should never change the version
          # number as they are all the same as version 08.
          Handler08
        when 13
          # drafts 13 to 17 all identify as version 13 as they are
          # only minor changes or text changes.
          Handler13
        else
          # According to spec should abort the connection
          raise HandshakeError, "Protocol version #{version} not supported"
        end
      end

      include Debugger

      attr_reader :request, :state

      def initialize(connection, debug = false)
        @connection = connection
        @debug = debug
        @state = :connected
        @close_timer = nil
        initialize_framing
      end

      def receive_data(data)
        @data << data
        process_data
      rescue WSProtocolError => e
        fail_websocket(e)
      end

      def close_websocket(code, body)
        # Implemented in subclass
      end

      # Used to avoid un-acked and unclosed remaining open indefinitely
      def start_close_timeout
        @close_timer = EM::Timer.new(@connection.close_timeout) {
          @connection.close_connection
          e = WSProtocolError.new("Close handshake un-acked after #{@connection.close_timeout}s, closing tcp connection")
          @connection.trigger_on_error(e)
        }
      end

      # This corresponds to "Fail the WebSocket Connection" in the spec.
      def fail_websocket(e)
        debug [:error, e]
        close_websocket(e.code, e.message)
        @connection.close_connection_after_writing
        @connection.trigger_on_error(e)
      end

      def unbind
        @state = :closed

        @close_timer.cancel if @close_timer

        @close_info = defined?(@close_info) ? @close_info : {
          :code => 1006,
          :was_clean => false,
        }

        @connection.trigger_on_close(@close_info)
      end

      def ping
        # Overridden in subclass
        false
      end

      def pingable?
        # Also Overridden
        false
      end
    end
  end
end
