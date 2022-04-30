require 'thread'

module Hawkins
  module Commands
    class LiveServe < Jekyll::Command
      # Based on pattern described in
      # https://emptysqua.re/blog/an-event-synchronization-primitive-for-ruby/
      @mutex = Mutex.new
      @running_cond = ConditionVariable.new
      @is_running = false

      class << self
        COMMAND_OPTIONS = {
          "swf"      => ["--swf", "Use Flash for WebSockets support"],
          "ignore"   => ["--ignore GLOB1[,GLOB2[,...]]", "Files not to reload"],
          "min_delay" => ["--min-delay [SECONDS]", "Minimum reload delay"],
          "max_delay" => ["--max-delay [SECONDS]", "Maximum reload delay"],
          "reload_port" => ["--reload-port [PORT]", Integer, "Port for LiveReload to listen on"],
        }.merge(Jekyll::Commands::Serve.singleton_class::COMMAND_OPTIONS).freeze

        LIVERELOAD_PORT = 35729

        attr_reader :mutex, :running_cond, :is_running

        #

        def init_with_program(prog)
          prog.command(:liveserve) do |cmd|
            cmd.description "Serve your site locally with LiveReload"
            cmd.syntax "liveserve [options]"
            cmd.alias :liveserver
            cmd.alias :l

            add_build_options(cmd)
            COMMAND_OPTIONS.each do |key, val|
              cmd.option(key, *val)
            end

            cmd.action do |_, opts|
              opts["reload_port"] ||= LIVERELOAD_PORT
              opts["serving"] = true
              opts["watch"] = true unless opts.key?("watch")
              start(opts)
            end
          end
        end

        def start(opts)
          config = opts["config"]
          @reload_reactor = nil
          register_reload_hooks(opts)
          Jekyll::Commands::Build.process(opts)
          opts["config"] = config
          LiveServe.process(opts)
        end

        def process(opts)
          opts = configuration_from_options(opts)
          destination = opts["destination"]
          setup(destination)

          @reload_reactor.start(opts)
          @server = WEBrick::HTTPServer.new(webrick_opts(opts)).tap { |o| o.unmount("") }

          @server.mount("#{opts['baseurl']}/__livereload",
            WEBrick::HTTPServlet::FileHandler, LIVERELOAD_DIR)
          @server.mount(opts["baseurl"], ReloadServlet, destination, file_handler_opts)

          Jekyll.logger.info "Server address:", server_address(@server, opts)
          launch_browser(@server, opts) if opts["open_url"]
          boot_or_detach(@server, opts)
        end

        def shutdown
          @server.shutdown if @is_running
        end

        private
        def register_reload_hooks(opts)
          require_relative "websockets"
          @reload_reactor = LiveReloadReactor.new

          Jekyll::Hooks.register(:site, :post_render) do |site|
            regenerator = Jekyll::Regenerator.new(site)
            @changed_pages = site.pages.select do |p|
              regenerator.regenerate?(p)
            end
          end

          # A note on ignoring files: LiveReload errs on the side of reloading when it
          # comes to the message it gets.  If, for example, a page is ignored but a CSS
          # file linked in the page isn't, the page will still be reloaded if the CSS
          # file is contained in the message sent to LiveReload.  Additionally, the
          # path matching is very loose so that a message to reload "/" will always
          # lead the page to reload since every page starts with "/".
          Jekyll::Hooks.register(:site, :post_write) do
            if @changed_pages && @reload_reactor && @reload_reactor.running?
              ignore, @changed_pages = @changed_pages.partition do |p|
                Array(opts["ignore"]).any? do |filter|
                  File.fnmatch(filter, Jekyll.sanitized_path(p.relative_path))
                end
              end
              Jekyll.logger.debug "LiveReload:", "Ignoring #{ignore.map(&:relative_path)}"
              @reload_reactor.reload(@changed_pages)
            end
            @changed_pages = nil
          end
        end

        # Do a base pre-setup of WEBRick so that everything is in place
        # when we get ready to party, checking for an setting up an error page
        # and making sure our destination exists.

        private
        def setup(destination)
          require_relative "./servlet"

          FileUtils.mkdir_p(destination)
          if File.exist?(File.join(destination, "404.html"))
            WEBrick::HTTPResponse.class_eval do
              def create_error_page
                @header["Content-Type"] = "text/html; charset=UTF-8"
                @body = IO.read(File.join(@config[:DocumentRoot], "404.html"))
              end
            end
          end
        end

        #

        private
        def webrick_opts(opts)
          opts = {
            :JekyllOptions      => opts,
            :DoNotReverseLookup => true,
            :MimeTypes          => mime_types,
            :DocumentRoot       => opts["destination"],
            :StartCallback      => start_callback(opts["detach"]),
            :StopCallback       => stop_callback(opts["detach"]),
            :BindAddress        => opts["host"],
            :Port               => opts["port"],
            :DirectoryIndex     => %w(
              index.htm
              index.html
              index.rhtml
              index.cgi
              index.xml
            ),
          }

          enable_ssl(opts)
          enable_logging(opts)
          opts
        end

        # Recreate NondisclosureName under utf-8 circumstance

        private
        def file_handler_opts
          WEBrick::Config::FileHandler.merge(
            :FancyIndexing     => true,
            :NondisclosureName => [
              '.ht*', '~*'
            ]
          )
        end

        #

        private
        def server_address(server, opts)
          address = server.config[:BindAddress]
          baseurl = "#{opts['baseurl']}/" if opts["baseurl"]
          port = server.config[:Port]

          if opts['ssl_cert'] && opts['ssl_key']
            protocol = "https"
          else
            protocol = "http"
          end

          "#{protocol}://#{address}:#{port}#{baseurl}"
        end

        #

        private
        def launch_browser(server, opts)
          command =
            if Jekyll::Utils::Platforms.windows?
              "start"
            elsif Jekyll::Utils::Platforms.osx?
              "open"
            else
              "xdg-open"
            end
          system command, server_address(server, opts)
        end

        # Keep in our area with a thread or detach the server as requested
        # by the user.  This method determines what we do based on what you
        # ask us to do.

        private
        def boot_or_detach(server, opts)
          if opts["detach"]
            pid = Process.fork do
              server.start
            end

            Process.detach(pid)
            Jekyll.logger.info "Server detached with pid '#{pid}'.", \
              "Run `pkill -f jekyll' or `kill -9 #{pid}' to stop the server."
          else
            t = Thread.new { server.start }
            trap("INT") { server.shutdown }
            t.join
          end
        end

        # Make the stack verbose if the user requests it.

        private
        def enable_logging(opts)
          opts[:AccessLog] = []
          level = WEBrick::Log.const_get(opts[:JekyllOptions]["verbose"] ? :DEBUG : :WARN)
          opts[:Logger] = WEBrick::Log.new($stdout, level)
        end

        # Add SSL to the stack if the user triggers --enable-ssl and they
        # provide both types of certificates commonly needed.  Raise if they
        # forget to add one of the certificates.

        private
        def enable_ssl(opts)
          jekyll_opts = opts[:JekyllOptions]
          return if !jekyll_opts['ssl_cert'] && !jekyll_opts['ssl_key']
          if !jekyll_opts['ssl_cert'] || !jekyll_opts['ssl_key']
            raise "--ssl-cert or --ssl-key missing."
          end

          Jekyll.logger.info("LiveReload:", "Serving over SSL/TLS.  If you are using a "\
            "certificate signed by an unknown CA, you will need to add an exception for both "\
            "#{jekyll_opts['host']}:#{jekyll_opts['port']} and "\
            "#{jekyll_opts['host']}:#{jekyll_opts['reload_port']}")

          require "openssl"
          require "webrick/https"
          source_key = Jekyll.sanitized_path(jekyll_opts['source'], jekyll_opts['ssl_key'])
          source_certificate = Jekyll.sanitized_path(jekyll_opts['source'], jekyll_opts['ssl_cert'])
          opts[:SSLCertificate] = OpenSSL::X509::Certificate.new(File.read(source_certificate))
          opts[:SSLPrivateKey] = OpenSSL::PKey::RSA.new(File.read(source_key))
          opts[:SSLEnable] = true
        end

        private
        def start_callback(detached)
          unless detached
            proc do
              mutex.synchronize do
                unless @reload_reactor.nil?
                  @reload_reactor.reactor_mutex.synchronize do
                    unless EM.reactor_running?
                      @reload_reactor.reactor_running_cond.wait(@reload_reactor.reactor_mutex)
                    end
                  end
                end
                @is_running = true
                Jekyll.logger.info("Server running...", "press ctrl-c to stop.")
                running_cond.signal
              end
            end
          end
        end

        private
        def stop_callback(detached)
          unless detached
            proc do
              mutex.synchronize do
                unless @reload_reactor.nil?
                  @reload_reactor.stop
                  @reload_reactor.reactor_mutex.synchronize do
                    if EM.reactor_running?
                      @reload_reactor.reactor_running_cond.wait(@reload_reactor.reactor_mutex)
                    end
                  end
                end
                @is_running = false
                running_cond.signal
              end
            end
          end
        end

        private
        def mime_types
          file = File.expand_path('../mime.types', File.dirname(__FILE__))
          WEBrick::HTTPUtils.load_mime_types(file)
        end
      end
    end
  end
end
