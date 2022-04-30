module EventMachine
  module WebSocket
    class Handler03 < Handler
      include Framing03
      include MessageProcessor03
      include Close03
    end
  end
end
