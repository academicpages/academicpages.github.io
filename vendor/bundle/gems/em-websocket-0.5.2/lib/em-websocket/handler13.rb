module EventMachine
  module WebSocket
    class Handler13 < Handler
      include Framing07
      include MessageProcessor06
      include Close06
    end
  end
end
