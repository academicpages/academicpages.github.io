require 'helper'

describe EM::WebSocket::Handshake do
  def handshake(request, secure = false)
    handshake = EM::WebSocket::Handshake.new(secure)
    handshake.receive_data(format_request(request))
    handshake
  end
  
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
    @secure_request = @request.merge(:port => 443)

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
    @secure_response = @response.merge(:headers => @response[:headers].merge('Sec-WebSocket-Location' => "wss://example.com/demo"))
  end
  
  it "should handle good request" do
    handshake(@request).should succeed_with_upgrade(@response)
  end
  
  it "should handle good request to secure default port if secure mode is enabled" do
    handshake(@secure_request, true).
      should succeed_with_upgrade(@secure_response)
  end
  
  it "should not handle good request to secure default port if secure mode is disabled" do
    handshake(@secure_request, false).
      should_not succeed_with_upgrade(@secure_response)
  end
  
  it "should handle good request on nondefault port" do
    @request[:port] = 8081
    @request[:headers]['Host'] = 'example.com:8081'
    @response[:headers]['Sec-WebSocket-Location'] =
      'ws://example.com:8081/demo'

    handshake(@request).should succeed_with_upgrade(@response)
  end
  
  it "should handle good request to secure nondefault port" do
    @secure_request[:port] = 8081
    @secure_request[:headers]['Host'] = 'example.com:8081'
    @secure_response[:headers]['Sec-WebSocket-Location'] = 'wss://example.com:8081/demo'
    
    handshake(@secure_request, true).
      should succeed_with_upgrade(@secure_response)
  end
  
  it "should handle good request with no protocol" do
    @request[:headers].delete('Sec-WebSocket-Protocol')
    @response[:headers].delete("Sec-WebSocket-Protocol")

    handshake(@request).should succeed_with_upgrade(@response)
  end
  
  it "should handle extra headers by simply ignoring them" do
    @request[:headers]['EmptyValue'] = ""
    @request[:headers]['AKey'] = "AValue"

    handshake(@request).should succeed_with_upgrade(@response)
  end
  
  it "should raise error on HTTP request" do
    @request[:headers] = {
      'Host' => 'www.google.com',
      'User-Agent' => 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 GTB6 GTBA',
      'Accept' => 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
      'Accept-Language' => 'en-us,en;q=0.5',
      'Accept-Encoding' => 'gzip,deflate',
      'Accept-Charset' => 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
      'Keep-Alive' => '300',
      'Connection' => 'keep-alive',
    }
    
    handshake(@request).should fail_with_error(EM::WebSocket::HandshakeError)
  end
  
  it "should raise error on wrong method" do
    @request[:method] = 'POST'

    handshake(@request).should fail_with_error(EM::WebSocket::HandshakeError)
  end
  
  it "should raise error if upgrade header incorrect" do
    @request[:headers]['Upgrade'] = 'NonWebSocket'

    handshake(@request).should fail_with_error(EM::WebSocket::HandshakeError)
  end
  
  it "should raise error if Sec-WebSocket-Protocol is empty" do
    @request[:headers]['Sec-WebSocket-Protocol'] = ''

    handshake(@request).should fail_with_error(EM::WebSocket::HandshakeError)
  end
  
  %w[Sec-WebSocket-Key1 Sec-WebSocket-Key2].each do |header|
    it "should raise error if #{header} has zero spaces" do
      @request[:headers][header] = 'nospaces'

      handshake(@request).
        should fail_with_error(EM::WebSocket::HandshakeError, 'Websocket Key1 or Key2 does not contain spaces - this is a symptom of a cross-protocol attack')
    end
  end
  
  it "should raise error if Sec-WebSocket-Key1 is missing" do
    @request[:headers].delete("Sec-WebSocket-Key1")

    # The error message isn't correct since key1 is used to heuristically
    # determine the protocol version in use, however this test at least checks
    # that the handshake does correctly fail
    handshake(@request).
      should fail_with_error(EM::WebSocket::HandshakeError, 'Extra bytes after header')
  end

  it "should raise error if Sec-WebSocket-Key2 is missing" do
    @request[:headers].delete("Sec-WebSocket-Key2")

    handshake(@request).
      should fail_with_error(EM::WebSocket::HandshakeError, 'WebSocket key1 or key2 is missing')
  end

  it "should raise error if spaces do not divide numbers in Sec-WebSocket-Key* " do
    @request[:headers]['Sec-WebSocket-Key2'] = '12998 5 Y3 1.P00'

    handshake(@request).
      should fail_with_error(EM::WebSocket::HandshakeError, 'Invalid Key "12998 5 Y3 1.P00"')
  end
  
  it "should raise error if the HTTP header is empty" do
    handshake = EM::WebSocket::Handshake.new(false)
    handshake.receive_data("\r\n\r\nfoobar")
    
    handshake.
      should fail_with_error(EM::WebSocket::HandshakeError, 'Invalid HTTP header: Could not parse data entirely (4 != 10)')
  end

  # This might seems crazy, but very occasionally we saw multiple "Upgrade:
  # WebSocket" headers in the wild. RFC 4.2.1 isn't particularly clear on this
  # point, so for now I have decided not to accept --@mloughran
  it "should raise error on multiple upgrade headers" do
    handshake = EM::WebSocket::Handshake.new(false)

    # Add a duplicate upgrade header
    headers = format_request(@request)
    upgrade_header = "Upgrade: WebSocket\r\n"
    headers.gsub!(upgrade_header, "#{upgrade_header}#{upgrade_header}")

    handshake.receive_data(headers)

    handshake.errback { |e|
      e.class.should == EM::WebSocket::HandshakeError
      e.message.should == 'Invalid upgrade header: ["WebSocket", "WebSocket"]'
    }
  end
  
  it "should cope with requests where the header is split" do
    request = format_request(@request)
    incomplete_request = request[0...(request.length / 2)]
    rest = request[(request.length / 2)..-1]
    handshake = EM::WebSocket::Handshake.new(false)
    handshake.receive_data(incomplete_request)
    
    handshake.instance_variable_get(:@deferred_status).should == nil
    
    # Send the remaining header
    handshake.receive_data(rest)
    
    handshake(@request).should succeed_with_upgrade(@response)
  end
  
  it "should cope with requests where the third key is split" do
    request = format_request(@request)
    # Removes last two bytes of the third key
    incomplete_request = request[0..-3]
    rest = request[-2..-1]
    handshake = EM::WebSocket::Handshake.new(false)
    handshake.receive_data(incomplete_request)
    
    handshake.instance_variable_get(:@deferred_status).should == nil
    
    # Send the remaining third key
    handshake.receive_data(rest)
    
    handshake(@request).should succeed_with_upgrade(@response)
  end

  it "should fail if the request URI is invalid" do
    @request[:path] = "/%"
    handshake(@request).should \
      fail_with_error(EM::WebSocket::HandshakeError, 'Invalid request URI: /%')
  end
end
