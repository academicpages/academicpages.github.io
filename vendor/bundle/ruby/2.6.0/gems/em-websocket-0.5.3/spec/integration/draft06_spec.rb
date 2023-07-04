require 'helper'

describe "draft06" do
  include EM::SpecHelper
  default_timeout 1

  before :each do
    @request = {
      :port => 80,
      :method => "GET",
      :path => "/demo",
      :headers => {
        'Host' => 'example.com',
        'Upgrade' => 'websocket',
        'Connection' => 'Upgrade',
        'Sec-WebSocket-Key' => 'dGhlIHNhbXBsZSBub25jZQ==',
        'Sec-WebSocket-Protocol' => 'sample',
        'Sec-WebSocket-Origin' => 'http://example.com',
        'Sec-WebSocket-Version' => '6'
      }
    }

    @response = {
      :protocol => "HTTP/1.1 101 Switching Protocols\r\n",
      :headers => {
        "Upgrade" => "websocket",
        "Connection" => "Upgrade",
        "Sec-WebSocket-Accept" => "s3pPLMBiTxaQ9kYGzzhZRbK+xOo=",
        "Sec-WebSocket-Protocol" => "sample",
      }
    }
  end

  def start_client
    client = EM.connect('0.0.0.0', 12345, Draft05FakeWebSocketClient)
    client.send_data(format_request(@request))
    yield client if block_given?
    return client
  end
  
  it_behaves_like "a websocket server" do
    let(:version) { 6 }
  end

  it_behaves_like "a WebSocket server drafts 3 and above" do
    let(:version) { 6 }
  end

  it "should open connection" do
    em {
      start_server { |server|
        server.onopen {
          server.instance_variable_get(:@handler).class.should == EventMachine::WebSocket::Handler06
        }
      }
      
      start_client { |client|
        client.onopen {
          client.handshake_response.lines.sort.
            should == format_response(@response).lines.sort
          done
        }
      }
    }
  end
  
  it "should accept a single-frame text message (masked)" do
    em {
      start_server { |server|
        server.onmessage { |msg|
          msg.should == 'Hello'
          if msg.respond_to?(:encoding)
            msg.encoding.should == Encoding.find("UTF-8")
          end
          done
        }
        server.onerror {
          fail
        }
      }
  
      start_client { |client|
        client.onopen {
          client.send_data("\x00\x00\x01\x00\x84\x05Ielln")
        }
      }
    }
  end

  it "should return close code and reason if closed via handshake" do
    em {
      start_server { |ws|
        ws.onclose { |event|
          # 2. Receive close event in server
          event.should == {
            :code => 4004,
            :reason => "close reason",
            :was_clean => true,
          }
          done
        }
      }
      start_client { |client|
        client.onopen {
          # 1: Send close handshake
          close_data = [4004].pack('n')
          close_data << "close reason"
          client.send_frame(:close, close_data)
        }
      }
    }
  end

  it "should return close code 1005 if no code was specified" do
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
          client.send_frame(:close, '')
        }
      }
    }
  end

  it "should report that close codes are supported" do
    em {
      start_server { |ws|
        ws.onopen {
          ws.supports_close_codes?.should == true
          done
        }
      }
      start_client
    }
  end
end
