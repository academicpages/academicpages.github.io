require 'set'
require 'stringio'

module CommonMarker
  class Renderer
    attr_accessor :in_tight, :warnings, :in_plain
    def initialize(options: :DEFAULT, extensions: [])
      @opts = Config.process_options(options, :render)
      @stream = StringIO.new("".force_encoding("utf-8"))
      @need_blocksep = false
      @warnings = Set.new []
      @in_tight = false
      @in_plain = false
      @tagfilter = extensions.include?(:tagfilter)
    end

    def out(*args)
      args.each do |arg|
        if arg == :children
          @node.each { |child| out(child) }
        elsif arg.is_a?(Array)
          arg.each { |x| render(x) }
        elsif arg.is_a?(Node)
          render(arg)
        else
          @stream.write(arg)
        end
      end
    end

    def render(node)
      @node = node
      if node.type == :document
        document(node)
        return @stream.string
      elsif @in_plain && node.type != :text && node.type != :softbreak
        node.each { |child| render(child) }
      else
        begin
          send(node.type, node)
        rescue NoMethodError => e
          @warnings.add("WARNING: #{node.type} not implemented.")
          raise e
        end
      end
    end

    def document(_node)
      out(:children)
    end

    def code_block(node)
      code_block(node)
    end

    def reference_def(_node)
    end

    def cr
      return if @stream.string.empty? || @stream.string[-1] == "\n"
      out("\n")
    end

    def blocksep
      out("\n")
    end

    def containersep
      cr unless @in_tight
    end

    def block
      cr
      yield
      cr
    end

    def container(starter, ender)
      out(starter)
      yield
      out(ender)
    end

    def plain
      old_in_plain = @in_plain
      @in_plain = true
      yield
      @in_plain = old_in_plain
    end

    private

    def escape_href(str)
      @node.html_escape_href(str)
    end

    def escape_html(str)
      @node.html_escape_html(str)
    end

    def tagfilter(str)
      if @tagfilter
        str.gsub(
          %r{
            <
            (
            title|textarea|style|xmp|iframe|
            noembed|noframes|script|plaintext
            )
            (?=\s|>|/>)
          }xi,
          '&lt;\1')
      else
        str
      end
    end

    def sourcepos(node)
      return "" unless option_enabled?(:SOURCEPOS)
      s = node.sourcepos
      " data-sourcepos=\"#{s[:start_line]}:#{s[:start_column]}-" \
        "#{s[:end_line]}:#{s[:end_column]}\""
    end

    def option_enabled?(opt)
      (@opts & CommonMarker::Config::Render.value(opt)) != 0
    end
  end
end
