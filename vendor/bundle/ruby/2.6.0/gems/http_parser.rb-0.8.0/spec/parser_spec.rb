if defined?(Encoding)
  Encoding.default_external = "UTF-8"
end
require "spec_helper"
require "json"

describe HTTP::Parser do
  before do
    @parser = HTTP::Parser.new

    @headers = nil
    @body = ""
    @started = false
    @done = false

    @parser.on_message_begin = proc{ @started = true }
    @parser.on_headers_complete = proc { |e| @headers = e }
    @parser.on_body = proc { |chunk| @body << chunk }
    @parser.on_message_complete = proc{ @done = true }
  end

  it "should have initial state" do
    expect(@parser.headers).to be_nil

    expect(@parser.http_version).to be_nil
    expect(@parser.http_method).to be_nil
    expect(@parser.status_code).to be_nil

    expect(@parser.request_url).to be_nil

    expect(@parser.header_value_type).to eq(:mixed)
  end

  it "should be able to run in non-main ractors" do
    skip unless Kernel.const_defined?(:Ractor)
    default_header_value_type = HTTP::Parser.default_header_value_type
    r = Ractor.new(default_header_value_type) { |type|
      parser = HTTP::Parser.new(default_header_value_type: type)
      done = false
      parser.on_message_complete = proc {
        done = true
      }
      parser <<
        "GET /ractor HTTP/1.1\r\n" +
        "Content-Length: 5\r\n" +
        "\r\n" +
        "World"
      done
    }
    expect(r.take).to be true
  end

  it "should allow us to set the header value type" do
    [:mixed, :arrays, :strings].each do |type|
      @parser.header_value_type = type
      expect(@parser.header_value_type).to eq(type)

      parser_tmp = HTTP::Parser.new(nil, type)
      expect(parser_tmp.header_value_type).to eq(type)

      parser_tmp2 = HTTP::Parser.new(default_header_value_type: type)
      expect(parser_tmp2.header_value_type).to eq(type)
    end
  end

  it "should allow us to set the default header value type" do
    [:mixed, :arrays, :strings].each do |type|
      HTTP::Parser.default_header_value_type = type

      parser = HTTP::Parser.new
      expect(parser.header_value_type).to eq(type)
    end
  end

  it "should throw an Argument Error if header value type is invalid" do
    expect{ @parser.header_value_type = 'bob' }.to raise_error(ArgumentError)
  end

  it "should throw an Argument Error if default header value type is invalid" do
    expect{ HTTP::Parser.default_header_value_type = 'bob' }.to raise_error(ArgumentError)
  end

  it "should implement basic api" do
    @parser <<
      "GET /test?ok=1 HTTP/1.1\r\n" +
      "User-Agent: curl/7.18.0\r\n" +
      "Host: 0.0.0.0:5000\r\n" +
      "Accept: */*\r\n" +
      "Content-Length: 5\r\n" +
      "\r\n" +
      "World"

    expect(@started).to be true
    expect(@done).to be true

    expect(@parser.http_major).to eq(1)
    expect(@parser.http_minor).to eq(1)
    expect(@parser.http_version).to eq([1,1])
    expect(@parser.http_method).to eq('GET')
    expect(@parser.status_code).to be_nil

    expect(@parser.request_url).to eq('/test?ok=1')

    expect(@parser.headers).to eq(@headers)
    expect(@parser.headers['User-Agent']).to eq('curl/7.18.0')
    expect(@parser.headers['Host']).to eq('0.0.0.0:5000')

    expect(@body).to eq("World")
  end

  it "should raise errors on invalid data" do
    expect{ @parser << "BLAH" }.to raise_error(HTTP::Parser::Error)
  end

  it "should abort parser via header complete callback with a body" do
    @parser.on_headers_complete = proc { |e| @headers = e; :stop }

    data =
      "GET / HTTP/1.0\r\n" +
      "Content-Length: 5\r\n" +
      "\r\n" +
      "World"

    bytes = @parser << data

    expect(bytes).to eq(37)
    expect(data[bytes..-1]).to eq('World')

    expect(@headers).to eq({'Content-Length' => '5'})
    expect(@body).to be_empty
    expect(@done).to be false
  end

  it "should abort parser via header complete callback without a body" do
    @parser.on_headers_complete = proc { |e| @headers = e; :stop }

    data =
      "GET / HTTP/1.0\r\n" +
      "Content-Length: 0\r\n" +
      "\r\n"

    bytes = @parser << data

    expect(bytes).to eq(37)
    expect(data[bytes..-1]).to eq('')

    expect(@headers).to eq({'Content-Length' => '0'})
    expect(@body).to be_empty
    expect(@done).to be false
  end

  it "should abort parser via message complete callback with a body" do
    @parser.on_message_complete = proc { :stop }

    data =
      "CONNECT www.example.com:443 HTTP/1.0\r\n" +
      "Connection: keep-alive\r\n" +
      "\r\n" +
      "World"

    bytes = @parser << data

    expect(bytes).to eq(64)
    expect(data[bytes..-1]).to eq('World')

    expect(@headers).to eq({'Connection' => 'keep-alive'})
    expect(@parser.upgrade_data).to eq('World')
    expect(@body).to be_empty
    expect(@done).to be false
  end

  it "should abort parser via message complete callback without a body" do
    @parser.on_message_complete = proc { :stop }

    data =
      "CONNECT www.example.com:443 HTTP/1.0\r\n" +
      "Connection: keep-alive\r\n" +
      "\r\n"

    bytes = @parser << data

    expect(bytes).to eq(64)
    expect(data[bytes..-1]).to eq('')

    expect(@headers).to eq({'Connection' => 'keep-alive'})
    expect(@parser.upgrade_data).to eq('')
    expect(@body).to be_empty
    expect(@done).to be false
  end

  it "should reset to initial state" do
    @parser << "GET / HTTP/1.0\r\n\r\n"

    expect(@parser.http_method).to eq('GET')
    expect(@parser.http_version).to eq([1,0])

    expect(@parser.request_url).to eq('/')

    expect(@parser.reset!).to be true

    expect(@parser.http_version).to be_nil
    expect(@parser.http_method).to be_nil
    expect(@parser.status_code).to be_nil

    expect(@parser.request_url).to be_nil
  end

  it "should optionally reset parser state on no-body responses" do
   expect(@parser.reset!).to be true

   @head, @complete = 0, 0
   @parser.on_headers_complete = proc {|h| @head += 1; :reset }
   @parser.on_message_complete = proc { @complete += 1 }
   @parser.on_body = proc {|b| fail }

   head_response = "HTTP/1.1 200 OK\r\nContent-Length:10\r\n\r\n"

   @parser << head_response
   expect(@head).to eq(1)
   expect(@complete).to eq(1)

   @parser << head_response
   expect(@head).to eq(2)
   expect(@complete).to eq(2)
  end

  it "should retain callbacks after reset" do
    expect(@parser.reset!).to be true

    @parser << "GET / HTTP/1.0\r\n\r\n"
    expect(@started).to be true
    expect(@headers).to eq({})
    expect(@done).to be true
  end

  it "should parse headers incrementally" do
    request =
      "GET / HTTP/1.0\r\n" +
      "Header1: value 1\r\n" +
      "Header2: value 2\r\n" +
      "\r\n"

    while chunk = request.slice!(0,2) and !chunk.empty?
      @parser << chunk
    end

    expect(@parser.headers).to eq({
      'Header1' => 'value 1',
      'Header2' => 'value 2'
    })
  end

  it "should handle multiple headers using strings" do
    @parser.header_value_type = :strings

    @parser <<
      "GET / HTTP/1.0\r\n" +
      "Set-Cookie: PREF=ID=a7d2c98; expires=Fri, 05-Apr-2013 05:00:45 GMT; path=/; domain=.bob.com\r\n" +
      "Set-Cookie: NID=46jSHxPM; path=/; domain=.bob.com; HttpOnly\r\n" +
      "\r\n"

    expect(@parser.headers["Set-Cookie"]).to eq("PREF=ID=a7d2c98; expires=Fri, 05-Apr-2013 05:00:45 GMT; path=/; domain=.bob.com, NID=46jSHxPM; path=/; domain=.bob.com; HttpOnly")
  end

  it "should handle multiple headers using strings" do
    @parser.header_value_type = :arrays

    @parser <<
      "GET / HTTP/1.0\r\n" +
      "Set-Cookie: PREF=ID=a7d2c98; expires=Fri, 05-Apr-2013 05:00:45 GMT; path=/; domain=.bob.com\r\n" +
      "Set-Cookie: NID=46jSHxPM; path=/; domain=.bob.com; HttpOnly\r\n" +
      "\r\n"

    expect(@parser.headers["Set-Cookie"]).to eq([
        "PREF=ID=a7d2c98; expires=Fri, 05-Apr-2013 05:00:45 GMT; path=/; domain=.bob.com",
        "NID=46jSHxPM; path=/; domain=.bob.com; HttpOnly"
    ])
  end

  it "should handle multiple headers using mixed" do
    @parser.header_value_type = :mixed

    @parser <<
      "GET / HTTP/1.0\r\n" +
      "Set-Cookie: PREF=ID=a7d2c98; expires=Fri, 05-Apr-2013 05:00:45 GMT; path=/; domain=.bob.com\r\n" +
      "Set-Cookie: NID=46jSHxPM; path=/; domain=.bob.com; HttpOnly\r\n" +
      "\r\n"

    expect(@parser.headers["Set-Cookie"]).to eq([
        "PREF=ID=a7d2c98; expires=Fri, 05-Apr-2013 05:00:45 GMT; path=/; domain=.bob.com",
        "NID=46jSHxPM; path=/; domain=.bob.com; HttpOnly"
    ])
  end

  it "should handle a single cookie using mixed" do
    @parser.header_value_type = :mixed

    @parser <<
      "GET / HTTP/1.0\r\n" +
      "Set-Cookie: PREF=ID=a7d2c98; expires=Fri, 05-Apr-2013 05:00:45 GMT; path=/; domain=.bob.com\r\n" +
      "\r\n"

    expect(@parser.headers["Set-Cookie"]).to eq("PREF=ID=a7d2c98; expires=Fri, 05-Apr-2013 05:00:45 GMT; path=/; domain=.bob.com")
  end

  it "should support alternative api" do
    callbacks = double('callbacks')
    allow(callbacks).to receive(:on_message_begin){ @started = true }
    allow(callbacks).to receive(:on_headers_complete){ |e| @headers = e }
    allow(callbacks).to receive(:on_body){ |chunk| @body << chunk }
    allow(callbacks).to receive(:on_message_complete){ @done = true }

    @parser = HTTP::Parser.new(callbacks)
    @parser << "GET / HTTP/1.0\r\n\r\n"

    expect(@started).to be true
    expect(@headers).to eq({})
    expect(@body).to eq('')
    expect(@done).to be true
  end

  it "should ignore extra content beyond specified length" do
    @parser <<
      "GET / HTTP/1.0\r\n" +
      "Content-Length: 5\r\n" +
      "\r\n" +
      "hello" +
      "  \n"

    expect(@body).to eq('hello')
    expect(@done).to be true
  end

  it 'sets upgrade_data if available' do
    @parser <<
      "GET /demo HTTP/1.1\r\n" +
      "Connection: Upgrade\r\n" +
      "Upgrade: WebSocket\r\n\r\n" +
      "third key data"

    expect(@parser.upgrade?).to be true
    expect(@parser.upgrade_data).to eq('third key data')
  end

  it 'sets upgrade_data to blank if un-available' do
    @parser <<
      "GET /demo HTTP/1.1\r\n" +
      "Connection: Upgrade\r\n" +
      "Upgrade: WebSocket\r\n\r\n"

    expect(@parser.upgrade?).to be true
    expect(@parser.upgrade_data).to eq('')
  end

  it 'should stop parsing headers when instructed' do
    request = "GET /websocket HTTP/1.1\r\n" +
      "host: localhost\r\n" +
      "connection: Upgrade\r\n" +
      "upgrade: websocket\r\n" +
      "sec-websocket-key: SD6/hpYbKjQ6Sown7pBbWQ==\r\n" +
      "sec-websocket-version: 13\r\n" +
      "\r\n"

    @parser.on_headers_complete = proc { |e| :stop }
    offset = (@parser << request)
    expect(@parser.upgrade?).to be true
    expect(@parser.upgrade_data).to eq('')
    expect(offset).to eq(request.length)
  end

  it "should execute on_body on requests with no content-length" do
   expect(@parser.reset!).to be true

   @head, @complete, @body = 0, 0, 0
   @parser.on_headers_complete = proc {|h| @head += 1 }
   @parser.on_message_complete = proc { @complete += 1 }
   @parser.on_body = proc {|b| @body += 1 }

   head_response = "HTTP/1.1 200 OK\r\n\r\nstuff"

   @parser << head_response
   @parser << ''
   expect(@head).to eq(1)
   expect(@complete).to eq(1)
   expect(@body).to eq(1)
  end


  %w[ request response ].each do |type|
    JSON.parse(File.read(File.expand_path("../support/#{type}s.json", __FILE__))).each do |test|
      test['headers'] ||= {}
      next if !defined?(JRUBY_VERSION) and HTTP::Parser.strict? != test['strict']

      it "should parse #{type}: #{test['name']}" do
        @parser << test['raw']

        expect(@parser.http_method).to eq(test['method'])
        expect(@parser.keep_alive?).to eq(test['should_keep_alive'])

        if test.has_key?('upgrade') and test['upgrade'] != 0
          expect(@parser.upgrade?).to be true
          expect(@parser.upgrade_data).to eq(test['upgrade'])
        end

        expect(@parser.send("http_major")).to eq(test["http_major"])
        expect(@parser.send("http_minor")).to eq(test["http_minor"])

        if test['type'] == 'HTTP_REQUEST'
          if defined?(JRUBY_VERSION)
            expect(@parser.send("request_url")).to eq(test["request_url"])
          else
            # It's created by rb_str_new(), so that encoding is Encoding::ASCII_8BIT a.k.a Encoding::BINARY
            expect(@parser.send("request_url")).to eq(test["request_url"].force_encoding(Encoding::ASCII_8BIT))
          end
        else
          expect(@parser.send("status_code")).to eq(test["status_code"])
          expect(@parser.send("status")).to eq(test["status"].force_encoding(Encoding::ASCII_8BIT)) if !defined?(JRUBY_VERSION)
        end

        expect(@headers.size).to eq(test['num_headers'])
        expect(@headers).to eq(test['headers'])

        expect(@body).to eq(test['body'])
        expect(@body.size).to eq(test['body_size']) if test['body_size']
      end
    end
  end
end
