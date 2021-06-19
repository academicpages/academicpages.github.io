module EventMachine
  module WebSocket
    class << self
      attr_accessor :max_frame_size
      attr_accessor :close_timeout
    end
    @max_frame_size = 10 * 1024 * 1024 # 10MB
    # Connections are given 60s to close after being sent a close handshake
    @close_timeout = 60

    # All errors raised by em-websocket should descend from this class
    class WebSocketError < RuntimeError; end

    # Used for errors that occur during WebSocket handshake
    class HandshakeError < WebSocketError; end

    # Used for errors which should cause the connection to close.
    # See RFC6455 §7.4.1 for a full description of meanings
    class WSProtocolError < WebSocketError
      def code; 1002; end
    end

    class InvalidDataError < WSProtocolError
      def code; 1007; end
    end

    # 1009: Message too big to process
    class WSMessageTooBigError < WSProtocolError
      def code; 1009; end
    end

    # Start WebSocket server, including starting eventmachine run loop
    def self.start(options, &blk)
      EM.epoll
      EM.run {
        trap("TERM") { stop }
        trap("INT")  { stop }

        run(options, &blk)
      }
    end

    # Start WebSocket server inside eventmachine run loop
    def self.run(options)
      host, port = options.values_at(:host, :port)
      EM.start_server(host, port, Connection, options) do |c|
        yield c
      end
    end

    def self.stop
      puts "Terminating WebSocket Server"
      EM.stop
    end
  end
end
