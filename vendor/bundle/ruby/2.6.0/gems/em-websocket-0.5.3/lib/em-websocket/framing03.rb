# encoding: BINARY

module EventMachine
  module WebSocket
    module Framing03
      def initialize_framing
        @data = ''
        @application_data_buffer = '' # Used for MORE frames
        @frame_type = nil
      end
      
      def process_data
        error = false

        while !error && @data.size > 1
          pointer = 0

          more = ((@data.getbyte(pointer) & 0b10000000) == 0b10000000) ^ fin
          # Ignoring rsv1-3 for now
          opcode = @data.getbyte(0) & 0b00001111
          pointer += 1

          # Ignoring rsv4
          length = @data.getbyte(pointer) & 0b01111111
          pointer += 1

          payload_length = case length
          when 127 # Length defined by 8 bytes
            # Check buffer size
            if @data.getbyte(pointer+8-1) == nil
              debug [:buffer_incomplete, @data]
              error = true
              next
            end
            
            # Only using the last 4 bytes for now, till I work out how to
            # unpack 8 bytes. I'm sure 4GB frames will do for now :)
            l = @data[(pointer+4)..(pointer+7)].unpack('N').first
            pointer += 8
            l
          when 126 # Length defined by 2 bytes
            # Check buffer size
            if @data.getbyte(pointer+2-1) == nil
              debug [:buffer_incomplete, @data]
              error = true
              next
            end
            
            l = @data[pointer..(pointer+1)].unpack('n').first
            pointer += 2
            l
          else
            length
          end

          if payload_length > @connection.max_frame_size
            raise WSMessageTooBigError, "Frame length too long (#{payload_length} bytes)"
          end

          # Check buffer size
          if @data.getbyte(pointer+payload_length-1) == nil
            debug [:buffer_incomplete, @data]
            error = true
            next
          end

          # Throw away data up to pointer
          @data.slice!(0...pointer)

          # Read application data
          application_data = @data.slice!(0...payload_length)

          frame_type = opcode_to_type(opcode)

          if frame_type == :continuation && !@frame_type
            raise WSProtocolError, 'Continuation frame not expected'
          end

          if more
            debug [:moreframe, frame_type, application_data]
            @application_data_buffer << application_data
            # The message type is passed in the first frame
            @frame_type ||= frame_type
          else
            # Message is complete
            if frame_type == :continuation
              @application_data_buffer << application_data
              message(@frame_type, '', @application_data_buffer)
              @application_data_buffer = ''
              @frame_type = nil
            else
              message(frame_type, '', application_data)
            end
          end
        end # end while
      end
      
      def send_frame(frame_type, application_data)
        debug [:sending_frame, frame_type, application_data]

        if @state == :closing && data_frame?(frame_type)
          raise WebSocketError, "Cannot send data frame since connection is closing"
        end

        frame = ''

        opcode = type_to_opcode(frame_type)
        byte1 = opcode # since more, rsv1-3 are 0
        frame << byte1

        length = application_data.size
        if length <= 125
          byte2 = length # since rsv4 is 0
          frame << byte2
        elsif length < 65536 # write 2 byte length
          frame << 126
          frame << [length].pack('n')
        else # write 8 byte length
          frame << 127
          frame << [length >> 32, length & 0xFFFFFFFF].pack("NN")
        end

        frame << application_data

        @connection.send_data(frame)
      end

      def send_text_frame(data)
        send_frame(:text, data)
      end

      private

      # This allows flipping the more bit to fin for draft 04
      def fin; false; end

      FRAME_TYPES = {
        :continuation => 0,
        :close => 1,
        :ping => 2,
        :pong => 3,
        :text => 4,
        :binary => 5
      }
      FRAME_TYPES_INVERSE = FRAME_TYPES.invert
      # Frames are either data frames or control frames
      DATA_FRAMES = [:text, :binary, :continuation]

      def type_to_opcode(frame_type)
        FRAME_TYPES[frame_type] || raise("Unknown frame type")
      end

      def opcode_to_type(opcode)
        FRAME_TYPES_INVERSE[opcode] || raise(WSProtocolError, "Unknown opcode #{opcode}")
      end

      def data_frame?(type)
        DATA_FRAMES.include?(type)
      end
    end
  end
end
