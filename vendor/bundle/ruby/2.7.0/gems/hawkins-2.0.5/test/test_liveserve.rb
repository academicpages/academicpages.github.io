require 'tmpdir'
require 'httpclient'

require_relative './spec_helper'

module Hawkins
  RSpec.describe "Hawkins" do
    context "when running in liveserve mode" do
      let!(:temp_dir) do
        Dir.mktmpdir("hawkins_test")
      end

      let(:destination) do
        Dir.mkdir(File.join(temp_dir, "_site"))
        File.join(temp_dir, "_site")
      end

      let(:client) do
        HTTPClient.new
      end

      let(:standard_opts) do
        {
          "port" => 4000,
          "host" => "localhost",
          "baseurl" => "",
          "detach" => false,
          "source" => temp_dir,
          "destination" => destination,
          "reload_port" => Commands::LiveServe.singleton_class::LIVERELOAD_PORT,
        }
      end

      before(:each) do
        site = instance_double(Jekyll::Site)
        simple_page = <<-HTML.gsub(/^\s*/, '')
        <!DOCTYPE HTML>
        <html lang="en-US">
        <head>
          <meta charset="UTF-8">
          <title>Hello World</title>
        </head>
        <body>
          <p>Hello!  I am a simple web page.</p>
        </body>
        </html>
        HTML

        File.open(File.join(destination, "hello.html"), 'w') do |f|
          f.write(simple_page)
        end
        allow(Jekyll::Site).to receive(:new).and_return(site)
      end

      after(:each) do
        capture_io do
          Commands::LiveServe.shutdown
        end

        Commands::LiveServe.mutex.synchronize do
          if Commands::LiveServe.is_running
            Commands::LiveServe.running_cond.wait(Commands::LiveServe.mutex)
          end
        end

        FileUtils.remove_entry_secure(temp_dir, true)
      end

      def start_server(opts)
        @thread = Thread.new do
          Commands::LiveServe.start(opts)
        end
        @thread.abort_on_exception = true

        Commands::LiveServe.mutex.synchronize do
          unless Commands::LiveServe.is_running
            Commands::LiveServe.running_cond.wait(Commands::LiveServe.mutex)
          end
        end
      end

      def serve(opts)
        allow(Jekyll).to receive(:configuration).and_return(opts)
        allow(Jekyll::Commands::Build).to receive(:process)

        capture_io do
          start_server(opts)
        end

        opts
      end

      it "serves livereload.js over HTTP on the default LiveReload port" do
        opts = serve(standard_opts)
        content = client.get_content(
          "http://#{opts['host']}:#{opts['reload_port']}/livereload.js")
        expect(content).to include('LiveReload.on(')
      end

      it "serves livereload.js over HTTPS" do
        key = File.join(File.dirname(__FILE__), "resources", "test.key")
        cert = File.join(File.dirname(__FILE__), "resources", "test.crt")

        FileUtils.cp(key, temp_dir)
        FileUtils.cp(cert, temp_dir)
        opts = serve(standard_opts.merge('ssl_cert' => 'test.crt', 'ssl_key' => 'test.key'))

        client.ssl_config.add_trust_ca(cert)
        content = client.get_content(
          "https://#{opts['host']}:#{opts['reload_port']}/livereload.js")
        expect(content).to include('LiveReload.on(')
      end

      it "uses wss when SSL options are provided" do
        key = File.join(File.dirname(__FILE__), "resources", "test.key")
        cert = File.join(File.dirname(__FILE__), "resources", "test.crt")

        FileUtils.cp(key, temp_dir)
        FileUtils.cp(cert, temp_dir)
        opts = serve(standard_opts.merge('ssl_cert' => 'test.crt', 'ssl_key' => 'test.key'))

        client.ssl_config.add_trust_ca(cert)
        content = client.get_content(
          "https://#{opts['host']}:#{opts['port']}/#{opts['baseurl']}/hello.html")
        expect(content).to include(%q(src="//'))
      end

      it "serves nothing else over HTTP on the default LiveReload port" do
        opts = serve(standard_opts)
        res = client.get("http://#{opts['host']}:#{opts['reload_port']}/")
        expect(res.status_code).to eq(400)
        expect(res.content).to include('only serves livereload.js')
      end

      it "inserts the LiveReload script tags" do
        opts = serve(standard_opts)
        content = client.get_content(
          "http://#{opts['host']}:#{opts['port']}/#{opts['baseurl']}/hello.html")
        expect(content).to include("livereload.js?snipver=1&amp;port=#{opts['livereload_port']}")
        expect(content).to include("I am a simple web page")
      end

      it "applies the max and min delay options" do
        opts = serve(standard_opts.merge("max_delay" => "1066", "min_delay" => "3"))
        content = client.get_content(
          "http://#{opts['host']}:#{opts['port']}/#{opts['baseurl']}/hello.html")
        expect(content).to include("&amp;mindelay=3")
        expect(content).to include("&amp;maxdelay=1066")
      end

      it "inserts a SWF LiveReload when --swf is used" do
        opts = serve(standard_opts.merge("swf" => true))
        host = opts['host']
        port = opts['port']
        base = opts['baseurl']
        content = client.get_content(
          "http://#{host}:#{port}/#{base}/hello.html")
        expect(content).to include(
          "WEB_SOCKET_SWF_LOCATION = \"/__livereload/WebSocketMain.swf")
        expect(content).to include("__livereload/swfobject.js")
        expect(content).to include("__livereload/web_socket.js")

        res = client.get(
          "http://#{host}:#{port}/#{base}/__livereload/WebSocketMain.swf")
        expect(res.status_code).to eq(200)
      end
    end
  end
end
