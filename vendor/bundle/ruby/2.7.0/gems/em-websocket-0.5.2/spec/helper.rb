# encoding: BINARY

require 'rubygems'
require 'rspec'
require 'em-spec/rspec'
require 'em-http'

require 'em-websocket'
require 'em-websocket-client'

require 'integration/shared_examples'
require 'integration/gte_03_examples'

RSpec.configure do |c|
  c.mock_with :rspec
end

class FakeWebSocketClient < EM::Connection
  attr_reader :handshake_response, :packets

  def onopen(&blk);     @onopen = blk;    end
  def onclose(&blk);    @onclose = blk;   end
  def onerror(&blk);    @onerror = blk;   end
  def onmessage(&blk);  @onmessage = blk; end

  def initialize
    @state = :new
    @packets = []
  end

  def receive_data(data)
    # puts "RECEIVE DATA #{data}"
    if @state == :new
      @handshake_response = data
      @onopen.call if defined? @onopen
      @state = :open
    else
      @onmessage.call(data) if defined? @onmessage
      @packets << data
    end
  end

  def send(application_data)
    send_frame(:text, application_data)
  end

  def send_frame(type, application_data)
    send_data construct_frame(type, application_data)
  end

  def unbind
    @onclose.call if defined? @onclose
  end

  private

  def construct_frame(type, data)
    "\x00#{data}\xff"
  end
end

class Draft03FakeWebSocketClient < FakeWebSocketClient
  private

  def construct_frame(type, data)
    frame = ""
    frame << EM::WebSocket::Framing03::FRAME_TYPES[type]
    frame << encoded_length(data.size)
    frame << data
  end

  def encoded_length(length)
    if length <= 125
      [length].pack('C') # since rsv4 is 0
    elsif length < 65536 # write 2 byte length
      "\126#{[length].pack('n')}"
    else # write 8 byte length
      "\127#{[length >> 32, length & 0xFFFFFFFF].pack("NN")}"
    end
  end
end

class Draft05FakeWebSocketClient < Draft03FakeWebSocketClient
  private

  def construct_frame(type, data)
    frame = ""
    frame << "\x00\x00\x00\x00" # Mask with nothing for simplicity
    frame << (EM::WebSocket::Framing05::FRAME_TYPES[type] | 0b10000000)
    frame << encoded_length(data.size)
    frame << data
  end
end

class Draft07FakeWebSocketClient < Draft05FakeWebSocketClient
  private

  def construct_frame(type, data)
    frame = ""
    frame << (EM::WebSocket::Framing07::FRAME_TYPES[type] | 0b10000000)
    # Should probably mask the data, but I get away without bothering since
    # the server doesn't enforce that incoming frames are masked
    frame << encoded_length(data.size)
    frame << data
  end
end

# Wrapper around em-websocket-client
class Draft75WebSocketClient
  def onopen(&blk);     @onopen = blk;    end
  def onclose(&blk);    @onclose = blk;   end
  def onerror(&blk);    @onerror = blk;   end
  def onmessage(&blk);  @onmessage = blk; end

  def initialize
    @ws = EventMachine::WebSocketClient.connect('ws://127.0.0.1:12345/',
                                                :version => 75,
                                                :origin => 'http://example.com')
    @ws.errback { |err| @onerror.call if defined? @onerror }
    @ws.callback { @onopen.call if defined? @onopen }
    @ws.stream { |msg| @onmessage.call(msg) if defined? @onmessage }
    @ws.disconnect { @onclose.call if defined? @onclose }
  end

  def send(message)
    @ws.send_msg(message)
  end

  def close_connection
    @ws.close_connection
  end
end

def start_server(opts = {})
  EM::WebSocket.run({:host => "0.0.0.0", :port => 12345}.merge(opts)) { |ws|
    yield ws if block_given?
  }
end

def format_request(r)
  data = "#{r[:method]} #{r[:path]} HTTP/1.1\r\n"
  header_lines = r[:headers].map { |k,v| "#{k}: #{v}" }
  data << [header_lines, '', r[:body]].join("\r\n")
  data
end

def format_response(r)
  data = r[:protocol] || "HTTP/1.1 101 WebSocket Protocol Handshake\r\n"
  header_lines = r[:headers].map { |k,v| "#{k}: #{v}" }
  data << [header_lines, '', r[:body]].join("\r\n")
  data
end

RSpec::Matchers.define :succeed_with_upgrade do |response|
  match do |actual|
    success = nil
    actual.callback { |upgrade_response, handler_klass|
      success = (upgrade_response.lines.sort == format_response(response).lines.sort)
    }
    success
  end
end

RSpec::Matchers.define :fail_with_error do |error_klass, error_message|
  match do |actual|
    success = nil
    actual.errback { |e|
      success = (e.class == error_klass)
      success &= (e.message == error_message) if error_message
    }
    success
  end
end
