# encoding: BINARY

module EventMachine
  module WebSocket
    # The only difference between draft 03 framing and draft 04 framing is 
    # that the MORE bit has been changed to a FIN bit
    module Framing04
      include Framing03

      private
      
      def fin; true; end
    end
  end
end