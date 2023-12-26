require "webrick"
require "jekyll/commands/serve/servlet"

module Hawkins
  module Commands
    class LiveServe
      class SkipAnalyzer
        BAD_USER_AGENTS = [%r{MSIE}].freeze

        def self.skip_processing?(req, res, options)
          new(req, res, options).skip_processing?
        end

        def initialize(req, res, options)
          @options = options
          @req = req
          @res = res
        end

        def skip_processing?
          !html? || chunked? || inline? || bad_browser?
        end

        def chunked?
          @res['Transfer-Encoding'] == 'chunked'
        end

        def inline?
          @res['Content-Disposition'] =~ %r{^inline}
        end

        def bad_browser?
          BAD_USER_AGENTS.any? { |pattern| @req['User-Agent'] =~ pattern }
        end

        def html?
          @res['Content-Type'] =~ %r{text/html}
        end
      end

      class BodyProcessor
        HEAD_TAG_REGEX = /<head>|<head[^(er)][^<]*>/

        attr_reader :content_length, :new_body, :livereload_added

        def initialize(body, options)
          @body = body
          @options = options
          @processed = false
        end

        def with_swf?
          @options["swf"]
        end

        def processed?
          @processed
        end

        def process!
          # @body will usually be a File object but Strings occur in rare cases
          # that occur for reasons unknown to me.
          @new_body = []
          if @body.respond_to?(:each)
            begin
              @body.each { |line| @new_body << line.to_s }
            ensure
              @body.close
            end
          else
            @new_body = @body.lines
          end

          @content_length = 0
          @livereload_added = false

          @new_body.each do |line|
            if !@livereload_added && line['<head']
              line.gsub!(HEAD_TAG_REGEX) { |match| %(#{match}#{template.result(binding)}) }

              @livereload_added = true
            end

            @content_length += line.bytesize
            @processed = true
          end
          @new_body = @new_body.join
        end

        def template
          # Unclear what "snipver" does. Doc at
          # https://github.com/livereload/livereload-js states that the recommended
          # setting is 1.

          # Complicated JavaScript to ensure that livereload.js is loaded from the
          # same origin as the page.  Mostly useful for dealing with the browser's
          # distinction between 'localhost' and 127.0.0.1

          # Use 'src="//..."' to mirror the protocol used to load the page itself.
          template = <<-TEMPLATE
          <% if with_swf? %>
            <script type="text/javascript">
              WEB_SOCKET_SWF_LOCATION = "<%= @options["baseurl"] %>/__livereload/WebSocketMain.swf";
              WEB_SOCKET_FORCE_FLASH = false;
            </script>
            <script type="text/javascript" src="<%= @options["baseurl"] %>/__livereload/swfobject.js"></script>
            <script type="text/javascript" src="<%= @options["baseurl"] %>/__livereload/web_socket.js"></script>
          <% end %>
          <script>
            document.write(
              '<script src="//' +
              (location.host || 'localhost').split(':')[0] +
              ':<%=@options["reload_port"] %>/livereload.js?snipver=1<%= livereload_args %>"' +
              '></' +
              'script>');
          </script>
          TEMPLATE
          ERB.new(Jekyll::Utils.strip_heredoc(template))
        end

        def livereload_args
          src = ''
          # XHTML standard requires ampersands to be encoded as entities when in attributes
          # See http://stackoverflow.com/a/2190292
          src << "&amp;mindelay=#{@options['min_delay']}" if @options["min_delay"]
          src << "&amp;maxdelay=#{@options['max_delay']}" if @options["max_delay"]
          src << "&amp;port=#{@options['reload_port']}" if @options["reload_port"]
          src
        end
      end

      class ReloadServlet < Jekyll::Commands::Serve::Servlet
        def do_GET(req, res) # rubocop:disable MethodName
          rtn = super
          return rtn if SkipAnalyzer.skip_processing?(req, res, @jekyll_opts)

          processor = BodyProcessor.new(res.body, @jekyll_opts)
          processor.process!
          res.body = processor.new_body
          res.content_length = processor.content_length.to_s

          if processor.livereload_added
            res['X-Rack-LiveReload'] = '1'
          end

          rtn
        end
      end
    end
  end
end
