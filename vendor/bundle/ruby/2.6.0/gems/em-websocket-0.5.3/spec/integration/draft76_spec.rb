# encoding: BINARY

require 'helper'

describe "WebSocket server draft76" do
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
        'Origin' => 'http://example.com'
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
    client = EM.connect('0.0.0.0', 12345, FakeWebSocketClient)
    client.send_data(format_request(@request))
    yield client if block_given?
    return client
  end

  it_behaves_like "a websocket server" do
    let(:version) { 76 }
  end

  it "should send back the correct handshake response" do
    em {
      start_server

      start_client { |connection|
        connection.onopen {
          connection.handshake_response.lines.sort.
            should == format_response(@response).lines.sort
          done
        }
      }
    }
  end
  
  it "should send closing frame back and close the connection after recieving closing frame" do
    em {
      start_server

      connection = start_client

      # Send closing frame after handshake complete
      connection.onopen {
        connection.send_data(EM::WebSocket::Handler76::TERMINATE_STRING)
      }

      # Check that this causes a termination string to be returned and the
      # connection close
      connection.onclose {
        connection.packets[0].should ==
          EM::WebSocket::Handler76::TERMINATE_STRING
        done
      }
    }
  end
  
  it "should ignore any data received after the closing frame" do
    em {
      start_server { |ws|
        # Fail if foobar message is received
        ws.onmessage { |msg|
          fail
        }
      }

      connection = start_client

      # Send closing frame after handshake complete, followed by another msg
      connection.onopen {
        connection.send_data(EM::WebSocket::Handler76::TERMINATE_STRING)
        connection.send('foobar')
      }

      connection.onclose {
        done
      }
    }
  end

  it "should accept null bytes within the frame after a line return" do
    em {
      start_server { |ws|
        ws.onmessage { |msg|
          msg.should == "\n\000"
        }
      }

      connection = start_client

      # Send closing frame after handshake complete
      connection.onopen {
        connection.send_data("\000\n\000\377")
        connection.send_data(EM::WebSocket::Handler76::TERMINATE_STRING)
      }

      connection.onclose {
        done
      }
    }
  end

  it "should handle unreasonable frame lengths by calling onerror callback" do
    em {
      start_server { |server|
        server.onerror { |error|
          error.should be_an_instance_of EM::WebSocket::WSMessageTooBigError
          error.message.should == "Frame length too long (1180591620717411303296 bytes)"
          done
        }
      }

      client = start_client

      # This particular frame indicates a message length of
      # 1180591620717411303296 bytes. Such a message would previously cause
      # a "bignum too big to convert into `long'" error.
      # However it is clearly unreasonable and should be rejected.
      client.onopen {
        client.send_data("\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00")
      }
    }
  end
  
  it "should handle impossible frames by calling onerror callback" do
    em {
      start_server { |server|
        server.onerror { |error|
          error.should be_an_instance_of EM::WebSocket::WSProtocolError
          error.message.should == "Invalid frame received"
          done
        }
      }

      client = start_client

      client.onopen {
        client.send_data("foobar") # Does not start with \x00 or \xff
      }
    }
  end

  it "should handle invalid http requests by raising HandshakeError passed to onerror callback" do
    em {
      start_server { |server|
        server.onerror { |error|
          error.should be_an_instance_of EM::WebSocket::HandshakeError
          error.message.should == "Invalid HTTP header: Could not parse data entirely (1 != 29)"
          done
        }
      }
      
      client = EM.connect('0.0.0.0', 12345, FakeWebSocketClient)
      client.send_data("This is not a HTTP header\r\n\r\n")
    }
  end

  it "should handle handshake request split into two TCP packets" do
    em {
      start_server

      # Create a fake client which sends draft 76 handshake
      connection = EM.connect('0.0.0.0', 12345, FakeWebSocketClient)
      data = format_request(@request)
      # Sends first half of the request
      connection.send_data(data[0...(data.length / 2)])

      connection.onopen {
        connection.handshake_response.lines.sort.
          should == format_response(@response).lines.sort
        done
      }

      EM.add_timer(0.1) do
        # Sends second half of the request
        connection.send_data(data[(data.length / 2)..-1])
      end
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

  it "should call onclose when the server closes the connection [antiregression]" do
    em {
      start_server { |ws|
        ws.onopen {
          EM.add_timer(0.1) {
            ws.close()
          }
        }
        ws.onclose {
          done
        }
      }
      start_client
    }
  end
end
