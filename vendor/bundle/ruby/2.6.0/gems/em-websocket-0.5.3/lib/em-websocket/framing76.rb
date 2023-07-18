# encoding: BINARY

module EventMachine
  module WebSocket
    module Framing76
      def initialize_framing
        @data = ''
      end
      
      def process_data
        debug [:message, @data]

        # This algorithm comes straight from the spec
        # http://tools.ietf.org/html/draft-hixie-thewebsocketprotocol-76#section-5.3

        error = false

        while !error
          return if @data.size == 0

          pointer = 0
          frame_type = @data.getbyte(pointer)
          pointer += 1

          if (frame_type & 0x80) == 0x80
            # If the high-order bit of the /frame type/ byte is set
            length = 0

            loop do
              return false if !@data.getbyte(pointer)
              b = @data.getbyte(pointer)
              pointer += 1
              b_v = b & 0x7F
              length = length * 128 + b_v
              break unless (b & 0x80) == 0x80
            end

            if length > @connection.max_frame_size
              raise WSMessageTooBigError, "Frame length too long (#{length} bytes)"
            end

            if @data.getbyte(pointer+length-1) == nil
              debug [:buffer_incomplete, @data]
              # Incomplete data - leave @data to accumulate
              error = true
            else
              # Straight from spec - I'm sure this isn't crazy...
              # 6. Read /length/ bytes.
              # 7. Discard the read bytes.
              @data = @data[(pointer+length)..-1]

              # If the /frame type/ is 0xFF and the /length/ was 0, then close
              if length == 0
                @connection.send_data("\xff\x00")
                @state = :closing
                @connection.close_connection_after_writing
              else
                error = true
              end
            end
          else
            # If the high-order bit of the /frame type/ byte is _not_ set

            if @data.getbyte(0) != 0x00
              # Close the connection since this buffer can never match
              raise WSProtocolError, "Invalid frame received"
            end

            # Addition to the spec to protect against malicious requests
            if @data.size > @connection.max_frame_size
              raise WSMessageTooBigError, "Frame length too long (#{@data.size} bytes)"
            end

            msg = @data.slice!(/\A\x00[^\xff]*\xff/)
            if msg
              msg.gsub!(/\A\x00|\xff\z/, '')
              if @state == :closing
                debug [:ignored_message, msg]
              else
                msg.force_encoding('UTF-8') if msg.respond_to?(:force_encoding)
                @connection.trigger_on_message(msg)
              end
            else
              error = true
            end
          end
        end

        false
      end
      
      # frames need to start with 0x00-0x7f byte and end with
      # an 0xFF byte. Per spec, we can also set the first
      # byte to a value betweent 0x80 and 0xFF, followed by
      # a leading length indicator
      def send_text_frame(data)
        debug [:sending_text_frame, data]
        ary = ["\x00", data, "\xff"]
        ary.collect{ |s| s.force_encoding('UTF-8') if s.respond_to?(:force_encoding) }
        @connection.send_data(ary.join)
      end

    end
  end
end