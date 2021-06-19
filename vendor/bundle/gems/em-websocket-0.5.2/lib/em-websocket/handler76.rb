# encoding: BINARY

module EventMachine
  module WebSocket
    class Handler76 < Handler
      include Handshake76
      include Framing76
      include Close75

      # "\377\000" is octet version and "\xff\x00" is hex version
      TERMINATE_STRING = "\xff\x00"
    end
  end
end
