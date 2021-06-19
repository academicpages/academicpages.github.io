module EventMachine
  module WebSocket
    module Close75
      def close_websocket(code, body)
        @connection.close_connection_after_writing
      end

      def supports_close_codes?; false; end
    end
  end
end
