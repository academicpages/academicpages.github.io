require 'digest/sha1'
require 'base64'

module EventMachine
  module WebSocket
    module Handshake04
      def self.handshake(headers, _, __)
        # Required
        unless key = headers['sec-websocket-key']
          raise HandshakeError, "sec-websocket-key header is required"
        end

        string_to_sign = "#{key}258EAFA5-E914-47DA-95CA-C5AB0DC85B11"
        signature = Base64.encode64(Digest::SHA1.digest(string_to_sign)).chomp

        upgrade = ["HTTP/1.1 101 Switching Protocols"]
        upgrade << "Upgrade: websocket"
        upgrade << "Connection: Upgrade"
        upgrade << "Sec-WebSocket-Accept: #{signature}"
        if protocol = headers['sec-websocket-protocol']
          validate_protocol!(protocol)
          upgrade << "Sec-WebSocket-Protocol: #{protocol}"
        end

        # TODO: Support sec-websocket-protocol selection
        # TODO: sec-websocket-extensions

        return upgrade.join("\r\n") + "\r\n\r\n"
      end

      def self.validate_protocol!(protocol)
        raise HandshakeError, "Invalid WebSocket-Protocol: empty" if protocol.empty?
        # TODO: Validate characters
      end
    end
  end
end
