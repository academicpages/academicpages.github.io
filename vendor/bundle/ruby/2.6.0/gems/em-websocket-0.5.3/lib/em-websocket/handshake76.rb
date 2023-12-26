require 'digest/md5'

module EventMachine::WebSocket
  module Handshake76
    class << self
      def handshake(headers, path, secure)
        challenge_response = solve_challenge(
          headers['sec-websocket-key1'],
          headers['sec-websocket-key2'],
          headers['third-key']
        )

        scheme = (secure ? "wss" : "ws")
        location = "#{scheme}://#{headers['host']}#{path}"

        upgrade =  "HTTP/1.1 101 WebSocket Protocol Handshake\r\n"
        upgrade << "Upgrade: WebSocket\r\n"
        upgrade << "Connection: Upgrade\r\n"
        upgrade << "Sec-WebSocket-Location: #{location}\r\n"
        upgrade << "Sec-WebSocket-Origin: #{headers['origin']}\r\n"
        if protocol = headers['sec-websocket-protocol']
          validate_protocol!(protocol)
          upgrade << "Sec-WebSocket-Protocol: #{protocol}\r\n"
        end
        upgrade << "\r\n"
        upgrade << challenge_response

        return upgrade
      end

      private

      def solve_challenge(first, second, third)
        # Refer to 5.2 4-9 of the draft 76
        sum = [numbers_over_spaces(first)].pack("N*") +
          [numbers_over_spaces(second)].pack("N*") +
          third
        Digest::MD5.digest(sum)
      end

      def numbers_over_spaces(string)
        unless string
          raise HandshakeError, "WebSocket key1 or key2 is missing"
        end

        numbers = string.scan(/[0-9]/).join.to_i

        spaces = string.scan(/ /).size
        # As per 5.2.5, abort the connection if spaces are zero.
        raise HandshakeError, "Websocket Key1 or Key2 does not contain spaces - this is a symptom of a cross-protocol attack" if spaces == 0

        # As per 5.2.6, abort if numbers is not an integral multiple of spaces
        if numbers % spaces != 0
          raise HandshakeError, "Invalid Key #{string.inspect}"
        end

        quotient = numbers / spaces

        if quotient > 2**32-1
          raise HandshakeError, "Challenge computation out of range for key #{string.inspect}"
        end

        return quotient
      end

      def validate_protocol!(protocol)
        raise HandshakeError, "Invalid WebSocket-Protocol: empty" if protocol.empty?
        # TODO: Validate characters
      end
    end
  end
end
