require 'helper'

describe "draft03" do
  include EM::SpecHelper
  default_timeout 1

  before :each do
    @request = {
      :port => 80,
      :method => "GET",
      :path => "/demo",
      :headers => {
        'Host' => 'example.com',
        'Connection' => 'Upgrade',
        'Sec-WebSocket-Key2' => '12998 5 Y3 1  .P00',
        'Sec-WebSocket-Protocol' => 'sample',
        'Upgrade' => 'WebSocket',
        'Sec-WebSocket-Key1' => '4 @1  46546xW%0l 1 5',
        'Origin' => 'http://example.com',
        'Sec-WebSocket-Draft' => '3'
      },
      :body => '^n:ds[4U'
    }

    @response = {
      :headers => {
        "Upgrade" => "WebSocket",
        "Connection" => "Upgrade",
        "Sec-WebSocket-Location" => "ws://example.com/demo",
        "Sec-WebSocket-Origin" => "http://example.com",
        "Sec-WebSocket-Protocol" => "sample"
      },
      :body => "8jKS\'y:G*Co,Wxa-"
    }
  end

  def start_client
    client = EM.connect('0.0.0.0', 12345, Draft03FakeWebSocketClient)
    client.send_data(format_request(@request))
    yield client if block_given?
    return client
  end

  it_behaves_like "a websocket server" do
    let(:version) { 3 }
  end

  it_behaves_like "a WebSocket server drafts 3 and above" do
    let(:version) { 3 }
  end

  # These examples are straight from the spec
  # http://tools.ietf.org/html/draft-ietf-hybi-thewebsocketprotocol-03#section-4.6
  describe "examples from the spec" do
    it "should accept a single-frame text message" do
      em {
        start_server { |ws|
          ws.onmessage { |msg|
            msg.should == 'Hello'
            done
          }
        }
        start_client { |client|
          client.onopen {
            client.send_data("\x04\x05Hello")
          }
        }
      }
    end
    
    it "should accept a fragmented text message" do
      em {
        start_server { |ws|
          ws.onmessage { |msg|
            msg.should == 'Hello'
            done
          }
        }

        connection = start_client

        # Send frame
        connection.onopen {
          connection.send_data("\x84\x03Hel")
          connection.send_data("\x00\x02lo")
        }
      }
    end
    
    it "should accept a ping request and respond with the same body" do
      em {
        start_server

        connection = start_client

        # Send frame
        connection.onopen {
          connection.send_data("\x02\x05Hello")
        }
        
        connection.onmessage { |frame|
          next if frame.nil?
          frame.should == "\x03\x05Hello"
          done
        }
      }
    end
    
    it "should accept a 256 bytes binary message in a single frame" do
      em {
        data = "a" * 256
        
        start_server { |ws|
          ws.onbinary { |msg|
            msg.encoding.should == Encoding.find("BINARY") if defined?(Encoding)
            msg.should == data
            done
          }
        }

        connection = start_client

        # Send frame
        connection.onopen {
          connection.send_data("\x05\x7E\x01\x00" + data)
        }
      }
    end
    
    it "should accept a 64KiB binary message in a single frame" do
      em {
        data = "a" * 65536
        
        start_server { |ws|
          ws.onbinary { |msg|
            msg.encoding.should == Encoding.find("BINARY") if defined?(Encoding)
            msg.should == data
            done
          }
        }

        connection = start_client

        # Send frame
        connection.onopen {
          connection.send_data("\x05\x7F\x00\x00\x00\x00\x00\x01\x00\x00" + data)
        }
      }
    end
  end

  describe "close handling" do
    it "should respond to a new close frame with a close frame" do
      em {
        start_server

        connection = start_client

        # Send close frame
        connection.onopen {
          connection.send_data("\x01\x00")
        }

        # Check that close ack received
        connection.onmessage { |frame|
          frame.should == "\x01\x00"
          done
        }
      }
    end

    it "should close the connection on receiving a close acknowlegement and call onclose with close code 1005 and was_clean=true (initiated by server)" do
      em {
        ack_received = false

        start_server { |ws|
          ws.onopen {
            # 2. Send a close frame
            EM.next_tick {
              ws.close
            }
          }

          # 5. Onclose event on server
          ws.onclose { |event|
            event.should == {
              :code => 1005,
              :reason => "",
              :was_clean => true,
            }
            done
          }
        }

        # 1. Create a fake client which sends draft 76 handshake
        connection = start_client

        # 3. Check that close frame recieved and acknowlege it
        connection.onmessage { |frame|
          frame.should == "\x01\x00"
          ack_received = true
          connection.send_data("\x01\x00")
        }

        # 4. Check that connection is closed _after_ the ack
        connection.onclose {
          ack_received.should == true
        }
      }
    end

    # it "should repur"
    #
    it "should return close code 1005 and was_clean=true after closing handshake (initiated by client)" do
      em {
        start_server { |ws|
          ws.onclose { |event|
            event.should == {
              :code => 1005,
              :reason => "",
              :was_clean => true,
            }
            done
          }
        }
        start_client { |client|
          client.onopen {
            client.send_data("\x01\x00")
          }
        }
      }
    end

    it "should not allow data frame to be sent after close frame sent" do
      em {
        start_server { |ws|
          ws.onopen {
            # 2. Send a close frame
            EM.next_tick {
              ws.close
            }

            # 3. Check that exception raised if I attempt to send more data
            EM.add_timer(0.1) {
              lambda {
                ws.send('hello world')
              }.should raise_error(EM::WebSocket::WebSocketError, 'Cannot send data frame since connection is closing')
              done
            }
          }
        }

        # 1. Create a fake client which sends draft 76 handshake
        start_client
      }
    end

    it "should still respond to control frames after close frame sent" do
      em {
        start_server { |ws|
          ws.onopen {
            # 2. Send a close frame
            EM.next_tick {
              ws.close
            }
          }
        }

        # 1. Create a fake client which sends draft 76 handshake
        connection = start_client

        connection.onmessage { |frame|
          if frame == "\x01\x00"
            # 3. After the close frame is received send a ping frame, but
            # don't respond with a close ack
            connection.send_data("\x02\x05Hello")
          else
            # 4. Check that the pong is received
            frame.should == "\x03\x05Hello"
            done
          end
        }
      }
    end

    it "should report that close codes are not supported" do
      em {
        start_server { |ws|
          ws.onopen {
            ws.supports_close_codes?.should == false
            done
          }
        }
        start_client
      }
    end
  end
end
