module EventMachine
  module WebSocket
    module Close06
      def close_websocket(code, body)
        if code
          close_data = [code].pack('n')
          close_data << body if body
          send_frame(:close, close_data)
        else
          send_frame(:close, '')
        end
        @state = :closing
        start_close_timeout
      end

      def supports_close_codes?; true; end
    end
  end
end
