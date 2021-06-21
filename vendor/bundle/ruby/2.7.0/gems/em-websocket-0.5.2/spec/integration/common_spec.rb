require 'helper'

# These tests are not specific to any particular draft of the specification
#
describe "WebSocket server" do
  include EM::SpecHelper
  default_timeout 1

  it "should fail on non WebSocket requests" do
    em {
      EM.add_timer(0.1) do
        http = EM::HttpRequest.new('http://127.0.0.1:12345/').get :timeout => 0
        http.errback { done }
        http.callback { fail }
      end

      start_server
    }
  end

  it "should expose the WebSocket request headers, path and query params" do
    em {
      EM.add_timer(0.1) do
        ws = EventMachine::WebSocketClient.connect('ws://127.0.0.1:12345/',
                                                   :origin => 'http://example.com')
        ws.errback { fail }
        ws.callback { ws.close_connection }
        ws.stream { |msg| }
      end

      start_server do |ws|
        ws.onopen { |handshake|
          headers = handshake.headers
          headers["Connection"].should == "Upgrade"
          headers["Upgrade"].should == "websocket"
          headers["Host"].to_s.should == "127.0.0.1:12345"
          handshake.path.should == "/"
          handshake.query.should == {}
          handshake.origin.should == 'http://example.com'
        }
        ws.onclose {
          ws.state.should == :closed
          done
        }
      end
    }
  end

  it "should expose the WebSocket path and query params when nonempty" do
    em {
      EM.add_timer(0.1) do
        ws = EventMachine::WebSocketClient.connect('ws://127.0.0.1:12345/hello?foo=bar&baz=qux')
        ws.errback { fail }
        ws.callback {
          ws.close_connection
        }
        ws.stream { |msg| }
      end

      start_server do |ws|
        ws.onopen { |handshake|
          handshake.path.should == '/hello'
          handshake.query_string.split('&').sort.
            should == ["baz=qux", "foo=bar"]
          handshake.query.should == {"foo"=>"bar", "baz"=>"qux"}
        }
        ws.onclose {
          ws.state.should == :closed
          done
        }
      end
    }
  end

  it "should raise an exception if frame sent before handshake complete" do
    em {
      # 1. Start WebSocket server
      start_server { |ws|
        # 3. Try to send a message to the socket
        lambda {
          ws.send('early message')
        }.should raise_error('Cannot send data before onopen callback')
        done
      }

      # 2. Connect a dumb TCP connection (will not send handshake)
      EM.connect('0.0.0.0', 12345, EM::Connection)
    }
  end

  it "should allow the server to be started inside an existing EM" do
    em {
      EM.add_timer(0.1) do
        http = EM::HttpRequest.new('http://127.0.0.1:12345/').get :timeout => 0
        http.errback { |e| done }
        http.callback { fail }
      end

      start_server do |ws|
        ws.onopen { |handshake|
          headers = handshake.headers
          headers["Host"].to_s.should == "127.0.0.1:12345"
        }
        ws.onclose {
          ws.state.should == :closed
          done
        }
      end
    }
  end

  context "outbound limit set" do
    it "should close the connection if the limit is reached" do
      em {
        start_server(:outbound_limit => 150) do |ws|
          # Increase the message size by one on each loop
          ws.onmessage{|msg| ws.send(msg + "x") }
          ws.onclose{|status|
            status[:code].should == 1006 # Unclean
            status[:was_clean].should be false
          }
        end

        EM.add_timer(0.1) do
          ws = EventMachine::WebSocketClient.connect('ws://127.0.0.1:12345/')
          ws.callback { ws.send_msg "hello" }
          ws.disconnect { done } # Server closed the connection
          ws.stream { |msg|
            # minus frame size ? (getting 146 max here)
            msg.data.size.should <= 150
            # Return back the message
            ws.send_msg(msg.data)
          }
        end
      }
    end
  end
end
