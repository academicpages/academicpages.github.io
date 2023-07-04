# encoding: BINARY

require 'helper'

describe EM::WebSocket::Framing03 do
  class FramingContainer
    include EM::WebSocket::Framing03
    
    def initialize
      @connection = Object.new
      def @connection.max_frame_size
        1000000
      end
    end

    def <<(data)
      @data << data
      process_data
    end
    
    def debug(*args); end
  end
  
  before :each do
    @f = FramingContainer.new
    @f.initialize_framing
  end
  
  describe "basic examples" do
    it "connection close" do
      @f.should_receive(:message).with(:close, '', '')
      @f << 0b00000001
      @f << 0b00000000
    end
    
    it "ping" do
      @f.should_receive(:message).with(:ping, '', '')
      @f << 0b00000010
      @f << 0b00000000
    end
    
    it "pong" do
      @f.should_receive(:message).with(:pong, '', '')
      @f << 0b00000011
      @f << 0b00000000
    end
    
    it "text" do
      @f.should_receive(:message).with(:text, '', 'foo')
      @f << 0b00000100
      @f << 0b00000011
      @f << 'foo'
    end
    
    it "Text in two frames" do
      @f.should_receive(:message).with(:text, '', 'hello world')
      @f << 0b10000100
      @f << 0b00000110
      @f << "hello "
      @f << 0b00000000
      @f << 0b00000101
      @f << "world"
    end
    
    it "2 byte extended payload length text frame" do
      data = 'a' * 256
      @f.should_receive(:message).with(:text, '', data)
      @f << 0b00000100 # Single frame, text
      @f << 0b01111110 # Length 126 (so read 2 bytes)
      @f << 0b00000001 # Two bytes in network byte order (256)
      @f << 0b00000000
      @f << data
    end
  end
  
  # These examples are straight from the spec
  # http://tools.ietf.org/html/draft-ietf-hybi-thewebsocketprotocol-03#section-4.6
  describe "examples from the spec" do
    it "a single-frame text message" do
      @f.should_receive(:message).with(:text, '', 'Hello')
      @f << "\x04\x05Hello"
    end
    
    it "a fragmented text message" do
      @f.should_receive(:message).with(:text, '', 'Hello')
      @f << "\x84\x03Hel"
      @f << "\x00\x02lo"
    end
    
    it "Ping request and response" do
      @f.should_receive(:message).with(:ping, '', 'Hello')
      @f << "\x02\x05Hello"
    end
    
    it "256 bytes binary message in a single frame" do
      data = "a"*256
      @f.should_receive(:message).with(:binary, '', data)
      @f << "\x05\x7E\x01\x00" + data
    end
    
    it "64KiB binary message in a single frame" do
      data = "a"*65536
      @f.should_receive(:message).with(:binary, '', data)
      @f << "\x05\x7F\x00\x00\x00\x00\x00\x01\x00\x00" + data
    end
  end

  describe "other tests" do
    it "should accept a fragmented unmasked text message in 3 frames" do
      @f.should_receive(:message).with(:text, '', 'Hello world')
      @f << "\x84\x03Hel"
      @f << "\x80\x02lo"
      @f << "\x00\x06 world"
    end
  end

  describe "error cases" do
    it "should raise an exception on continuation frame without preceeding more frame" do
      lambda {
        @f << 0b00000000 # Single frame, continuation
        @f << 0b00000001 # Length 1
        @f << 'f'
      }.should raise_error(EM::WebSocket::WebSocketError, 'Continuation frame not expected')
    end
  end
end

# These examples are straight from the spec
# http://tools.ietf.org/html/draft-ietf-hybi-thewebsocketprotocol-03#section-4.6
describe EM::WebSocket::Framing04 do
  class FramingContainer04
    include EM::WebSocket::Framing04

    def initialize
      @connection = Object.new
      def @connection.max_frame_size
        1000000
      end
    end

    def <<(data)
      @data << data
      process_data
    end

    def debug(*args); end
  end

  before :each do
    @f = FramingContainer04.new
    @f.initialize_framing
  end

  describe "examples from the spec" do
    it "a single-frame text message" do
      @f.should_receive(:message).with(:text, '', 'Hello')
      @f << "\x84\x05\x48\x65\x6c\x6c\x6f" # "\x84\x05Hello"
    end

    it "a fragmented text message" do
      @f.should_receive(:message).with(:text, '', 'Hello')
      @f << "\x04\x03Hel"
      @f << "\x80\x02lo"
    end

    it "Ping request" do
      @f.should_receive(:message).with(:ping, '', 'Hello')
      @f << "\x82\x05Hello"
    end

    it "a pong response" do
      @f.should_receive(:message).with(:pong, '', 'Hello')
      @f << "\x83\x05Hello"
    end

    it "256 bytes binary message in a single frame" do
      data = "a"*256
      @f.should_receive(:message).with(:binary, '', data)
      @f << "\x85\x7E\x01\x00" + data
    end

    it "64KiB binary message in a single frame" do
      data = "a"*65536
      @f.should_receive(:message).with(:binary, '', data)
      @f << "\x85\x7F\x00\x00\x00\x00\x00\x01\x00\x00" + data
    end
  end

  describe "other tests" do
    it "should accept a fragmented unmasked text message in 3 frames" do
      @f.should_receive(:message).with(:text, '', 'Hello world')
      @f << "\x04\x03Hel"
      @f << "\x00\x02lo"
      @f << "\x80\x06 world"
    end
  end
end

describe EM::WebSocket::Framing07 do
  class FramingContainer07
    include EM::WebSocket::Framing07

    def initialize
      @connection = Object.new
      def @connection.max_frame_size
        1000000
      end
    end

    def <<(data)
      @data << data
      process_data
    end

    def debug(*args); end
  end

  before :each do
    @f = FramingContainer07.new
    @f.initialize_framing
  end

  # These examples are straight from the spec
  # http://tools.ietf.org/html/draft-ietf-hybi-thewebsocketprotocol-07#section-4.6
  describe "examples from the spec" do
    it "a single-frame unmakedtext message" do
      @f.should_receive(:message).with(:text, '', 'Hello')
      @f << "\x81\x05\x48\x65\x6c\x6c\x6f" # "\x84\x05Hello"
    end

    it "a single-frame masked text message" do
      @f.should_receive(:message).with(:text, '', 'Hello')
      @f << "\x81\x85\x37\xfa\x21\x3d\x7f\x9f\x4d\x51\x58" # "\x84\x05Hello"
    end

    it "a fragmented unmasked text message" do
      @f.should_receive(:message).with(:text, '', 'Hello')
      @f << "\x01\x03Hel"
      @f << "\x80\x02lo"
    end

    it "Ping request" do
      @f.should_receive(:message).with(:ping, '', 'Hello')
      @f << "\x89\x05Hello"
    end

    it "a pong response" do
      @f.should_receive(:message).with(:pong, '', 'Hello')
      @f << "\x8a\x05Hello"
    end

    it "256 bytes binary message in a single unmasked frame" do
      data = "a"*256
      @f.should_receive(:message).with(:binary, '', data)
      @f << "\x82\x7E\x01\x00" + data
    end

    it "64KiB binary message in a single unmasked frame" do
      data = "a"*65536
      @f.should_receive(:message).with(:binary, '', data)
      @f << "\x82\x7F\x00\x00\x00\x00\x00\x01\x00\x00" + data
    end
  end

  describe "other tests" do
    it "should raise a WSProtocolError if an invalid frame type is requested" do
      lambda {
        # Opcode 3 is not supported by this draft
        @f << "\x83\x05Hello"
      }.should raise_error(EventMachine::WebSocket::WSProtocolError, "Unknown opcode 3")
    end

    it "should accept a fragmented unmasked text message in 3 frames" do
      @f.should_receive(:message).with(:text, '', 'Hello world')
      @f << "\x01\x03Hel"
      @f << "\x00\x02lo"
      @f << "\x80\x06 world"
    end

    it "should raise if non-fin frame is followed by a non-continuation data frame (continuation frame would be expected)" do
      lambda {
        @f << 0b00000001 # Not fin, text
        @f << 0b00000001 # Length 1
        @f << 'f'
        @f << 0b10000001 # fin, text (continutation expected)
        @f << 0b00000001 # Length 1
        @f << 'b'
      }.should raise_error(EM::WebSocket::WebSocketError, 'Continuation frame expected')
    end

    it "should raise on non-fin control frames (control frames must not be fragmented)" do
      lambda {
        @f << 0b00001010 # Not fin, pong (opcode 10)
        @f << 0b00000000 # Length 1
      }.should raise_error(EM::WebSocket::WebSocketError, 'Control frames must not be fragmented')
    end
  end
end
