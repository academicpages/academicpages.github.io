module EventMachine
  module WebSocket
    module Handshake75
      def self.handshake(headers, path, secure)
        scheme = (secure ? "wss" : "ws")
        location = "#{scheme}://#{headers['host']}#{path}"

        upgrade =  "HTTP/1.1 101 Web Socket Protocol Handshake\r\n"
        upgrade << "Upgrade: WebSocket\r\n"
        upgrade << "Connection: Upgrade\r\n"
        upgrade << "WebSocket-Origin: #{headers['origin']}\r\n"
        upgrade << "WebSocket-Location: #{location}\r\n"
        if protocol = headers['sec-websocket-protocol']
          validate_protocol!(protocol)
          upgrade << "Sec-WebSocket-Protocol: #{protocol}\r\n"
        end
        upgrade << "\r\n"

        return upgrade
      end

      def self.validate_protocol!(protocol)
        raise HandshakeError, "Invalid WebSocket-Protocol: empty" if protocol.empty?
        # TODO: Validate characters
      end
    end
  end
end
