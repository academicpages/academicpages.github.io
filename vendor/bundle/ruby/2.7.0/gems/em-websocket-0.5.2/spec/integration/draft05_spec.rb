require 'helper'

describe "draft05" do
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
        'Sec-WebSocket-Version' => '5'
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
    let(:version) { 5 }
  end

  it_behaves_like "a WebSocket server drafts 3 and above" do
    let(:version) { 5 }
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
