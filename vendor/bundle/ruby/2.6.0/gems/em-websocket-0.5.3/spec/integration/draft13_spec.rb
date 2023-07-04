# encoding: BINARY

require 'helper'

describe "draft13" do
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
        'Sec-WebSocket-Version' => '13'
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
    client = EM.connect('0.0.0.0', 12345, Draft07FakeWebSocketClient)
    client.send_data(format_request(@request))
    yield client if block_given?
    return client
  end

  it_behaves_like "a websocket server" do
    let(:version) { 13 }
  end

  it_behaves_like "a WebSocket server drafts 3 and above" do
    let(:version) { 13 }
  end

  it "should send back the correct handshake response" do
    em {
      start_server

      connection = start_client

      connection.onopen {
        connection.handshake_response.lines.sort.
          should == format_response(@response).lines.sort
        done
      }
    }
  end

  # TODO: This test would be much nicer with a real websocket client...
  it "should support sending pings and binding to onpong" do
    em {
      start_server { |ws|
        ws.onopen {
          ws.should be_pingable
          EM.next_tick {
            ws.ping('hello').should == true
          }

        }
        ws.onpong { |data|
          data.should == 'hello'
          done
        }
      }

      connection = start_client

      # Confusing, fake onmessage means any data after the handshake
      connection.onmessage { |data|
        # This is what a ping looks like
        data.should == "\x89\x05hello"
        # This is what a pong looks like
        connection.send_data("\x8a\x05hello")
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
