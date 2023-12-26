# encoding: BINARY

module EventMachine
  module WebSocket
    module MessageProcessor03
      def message(message_type, extension_data, application_data)
        case message_type
        when :close
          @close_info = {
            :code => 1005,
            :reason => "",
            :was_clean => true,
          }
          if @state == :closing
            # TODO: Check that message body matches sent data
            # We can close connection immediately since there is no more data
            # is allowed to be sent or received on this connection
            @connection.close_connection
          else
            # Acknowlege close
            # The connection is considered closed
            send_frame(:close, application_data)
            @connection.close_connection_after_writing
          end
        when :ping
          # Pong back the same data
          send_frame(:pong, application_data)
          @connection.trigger_on_ping(application_data)
        when :pong
          @connection.trigger_on_pong(application_data)
        when :text
          if application_data.respond_to?(:force_encoding)
            application_data.force_encoding("UTF-8")
          end
          @connection.trigger_on_message(application_data)
        when :binary
          @connection.trigger_on_binary(application_data)
        end
      end

      # Ping & Pong supported
      def pingable?
        true
      end
    end
  end
end
