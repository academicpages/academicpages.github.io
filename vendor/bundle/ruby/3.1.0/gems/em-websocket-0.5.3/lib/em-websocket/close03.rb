module EventMachine
  module WebSocket
    module Close03
      def close_websocket(code, body)
        # TODO: Ideally send body data and check that it matches in ack
        send_frame(:close, '')
        @state = :closing
        start_close_timeout
      end

      def supports_close_codes?; false; end
    end
  end
end
