require 'json'
require 'em-websocket'
require 'http/parser'

module Hawkins
  # The LiveReload protocol requires the server to serve livereload.js over HTTP
  # despite the fact that the protocol itself uses WebSockets.  This custom connection
  # class addresses the dual protocols that the server needs to understand.
  class HttpAwareConnection < EventMachine::WebSocket::Connection
    attr_reader :reload_body, :reload_size

    def initialize(opts)
      em_opts = {}
      @ssl_enabled = opts['ssl_cert'] && opts['ssl_key']
      if @ssl_enabled
        em_opts[:tls_options] = {
          :private_key_file => Jekyll.sanitized_path(opts['source'], opts['ssl_key']),
          :cert_chain_file => Jekyll.sanitized_path(opts['source'], opts['ssl_cert']),
        }
        em_opts[:secure] = true
      end

      # Too noisy even for debug level logging.
      # em_opts[:debug] = true

      super(em_opts)

      reload_file = File.join(LIVERELOAD_DIR, "livereload.js")
      @reload_body = File.read(reload_file)
      @reload_size = @reload_body.bytesize
    end

    def dispatch(data)
      parser = Http::Parser.new
      parser << data

      # WebSockets requests will have a Connection: Upgrade header
      if parser.http_method != 'GET' || parser.upgrade?
        super
      elsif parser.request_url =~ /^\/livereload.js/
        headers = [
          'HTTP/1.1 200 OK',
          'Content-Type: application/javascript',
          "Content-Length: #{reload_size}",
          '',
          '',
        ].join("\r\n")
        send_data(headers)
        send_data(reload_body)
        close_connection_after_writing
      else
        body = "This port only serves livereload.js over HTTP.\n"
        headers = [
          'HTTP/1.1 400 Bad Request',
          'Content-Type: text/plain',
          "Content-Length: #{body.bytesize}",
          '',
          '',
        ].join("\r\n")
        send_data(headers)
        send_data(body)
        close_connection_after_writing
      end
    end
  end

  class LiveReloadReactor
    attr_reader :thread
    attr_reader :opts
    attr_reader :reactor_mutex, :reactor_running_cond

    def initialize
      @thread = nil
      @websockets = []
      @connections_count = 0
      @reactor_mutex = Mutex.new
      @reactor_running_cond = ConditionVariable.new
    end

    def stop
      EM.stop if EM.reactor_running?
      Jekyll.logger.debug("LiveReload Server:", "halted")
    end

    def running?
      EM.reactor_running?
    end

    def start(opts)
      @thread = Thread.new do
        # Use epoll if the kernel supports it
        EM.epoll
        EM.run do
          Jekyll.logger.info("LiveReload Server:", "#{opts['host']}:#{opts['reload_port']}")
          EM.start_server(opts['host'], opts['reload_port'], HttpAwareConnection, opts) do |ws|
            ws.onopen do |handshake|
              connect(ws, handshake)
            end

            ws.onclose do
              disconnect(ws)
            end

            ws.onmessage do |msg|
              print_message(msg)
            end
          end

          # Notify blocked threads that EventMachine has started or shutdown
          EM.schedule do
            @reactor_mutex.synchronize do
              @reactor_running_cond.broadcast
            end
          end

          EM.add_shutdown_hook do
            @reactor_mutex.synchronize do
              @reactor_running_cond.broadcast
            end
          end
        end
      end
      @thread.abort_on_exception = true
    end

    # For a description of the protocol see http://feedback.livereload.com/knowledgebase/articles/86174-livereload-protocol
    def reload(pages)
      pages.each do |p|
        msg = {
          :command => 'reload',
          :path => p.path,
          :liveCSS => true,
        }

        # TODO Add support for override URL?
        # See http://feedback.livereload.com/knowledgebase/articles/86220-preview-css-changes-against-a-live-site-then-uplo

        Jekyll.logger.debug("LiveReload:", "Reloading #{p.path}")
        @websockets.each do |ws|
          ws.send(JSON.dump(msg))
        end
      end
    end

    def connect(ws, _handshake)
      @connections_count += 1
      Jekyll.logger.info("LiveReload:", "Browser connected") if @connections_count == 1
      ws.send(
        JSON.dump(
          :command => 'hello',
          :protocols => ['http://livereload.com/protocols/official-7'],
          :serverName => 'jekyll livereload',
        ))

      @websockets << ws
    end

    def disconnect(ws)
      @websockets.delete(ws)
    end

    def print_message(json_message)
      msg = JSON.parse(json_message)
      # Not sure what the 'url' command even does in LiveReload
      Jekyll.logger.info("LiveReload:", "Browser URL: #{msg['url']}") if msg['command'] == 'url'
    end
  end
end
