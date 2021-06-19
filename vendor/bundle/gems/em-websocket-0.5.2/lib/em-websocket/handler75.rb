module EventMachine
  module WebSocket
    class Handler75 < Handler
      include Handshake75
      include Framing76
      include Close75
    end
  end
end
