module Liquid
  # Templates are central to liquid.
  # Interpretating templates is a two step process. First you compile the
  # source code you got. During compile time some extensive error checking is performed.
  # your code should expect to get some SyntaxErrors.
  #
  # After you have a compiled template you can then <tt>render</tt> it.
  # You can use a compiled template over and over again and keep it cached.
  #
  # Example:
  #
  #   template = Liquid::Template.parse(source)
  #   template.render('user_name' => 'bob')
  #
  class Template
    attr_accessor :root
    attr_reader :resource_limits, :warnings

    @@file_system = BlankFileSystem.new

    class TagRegistry
      include Enumerable

      def initialize
        @tags = {}
        @cache = {}
      end

      def [](tag_name)
        return nil unless @tags.key?(tag_name)
        return @cache[tag_name] if Liquid.cache_classes

        lookup_class(@tags[tag_name]).tap { |o| @cache[tag_name] = o }
      end

      def []=(tag_name, klass)
        @tags[tag_name]  = klass.name
        @cache[tag_name] = klass
      end

      def delete(tag_name)
        @tags.delete(tag_name)
        @cache.delete(tag_name)
      end

      def each(&block)
        @tags.each(&block)
      end

      private

      def lookup_class(name)
        name.split("::").reject(&:empty?).reduce(Object) { |scope, const| scope.const_get(const) }
      end
    end

    attr_reader :profiler

    class << self
      # Sets how strict the parser should be.
      # :lax acts like liquid 2.5 and silently ignores malformed tags in most cases.
      # :warn is the default and will give deprecation warnings when invalid syntax is used.
      # :strict will enforce correct syntax.
      attr_writer :error_mode

      # Sets how strict the taint checker should be.
      # :lax is the default, and ignores the taint flag completely
      # :warn adds a warning, but does not interrupt the rendering
      # :error raises an error when tainted output is used
      attr_writer :taint_mode

      attr_accessor :default_exception_renderer
      Template.default_exception_renderer = lambda do |exception|
        exception
      end

      def file_system
        @@file_system
      end

      def file_system=(obj)
        @@file_system = obj
      end

      def register_tag(name, klass)
        tags[name.to_s] = klass
      end

      def tags
        @tags ||= TagRegistry.new
      end

      def error_mode
        @error_mode ||= :lax
      end

      def taint_mode
        @taint_mode ||= :lax
      end

      # Pass a module with filter methods which should be available
      # to all liquid views. Good for registering the standard library
      def register_filter(mod)
        Strainer.global_filter(mod)
      end

      def default_resource_limits
        @default_resource_limits ||= {}
      end

      # creates a new <tt>Template</tt> object from liquid source code
      # To enable profiling, pass in <tt>profile: true</tt> as an option.
      # See Liquid::Profiler for more information
      def parse(source, options = {})
        template = Template.new
        template.parse(source, options)
      end
    end

    def initialize
      @rethrow_errors = false
      @resource_limits = ResourceLimits.new(self.class.default_resource_limits)
    end

    # Parse source code.
    # Returns self for easy chaining
    def parse(source, options = {})
      @options = options
      @profiling = options[:profile]
      @line_numbers = options[:line_numbers] || @profiling
      parse_context = options.is_a?(ParseContext) ? options : ParseContext.new(options)
      @root = Document.parse(tokenize(source), parse_context)
      @warnings = parse_context.warnings
      self
    end

    def registers
      @registers ||= {}
    end

    def assigns
      @assigns ||= {}
    end

    def instance_assigns
      @instance_assigns ||= {}
    end

    def errors
      @errors ||= []
    end

    # Render takes a hash with local variables.
    #
    # if you use the same filters over and over again consider registering them globally
    # with <tt>Template.register_filter</tt>
    #
    # if profiling was enabled in <tt>Template#parse</tt> then the resulting profiling information
    # will be available via <tt>Template#profiler</tt>
    #
    # Following options can be passed:
    #
    #  * <tt>filters</tt> : array with local filters
    #  * <tt>registers</tt> : hash with register variables. Those can be accessed from
    #    filters and tags and might be useful to integrate liquid more with its host application
    #
    def render(*args)
      return ''.freeze if @root.nil?

      context = case args.first
      when Liquid::Context
        c = args.shift

        if @rethrow_errors
          c.exception_renderer = ->(e) { raise }
        end

        c
      when Liquid::Drop
        drop = args.shift
        drop.context = Context.new([drop, assigns], instance_assigns, registers, @rethrow_errors, @resource_limits)
      when Hash
        Context.new([args.shift, assigns], instance_assigns, registers, @rethrow_errors, @resource_limits)
      when nil
        Context.new(assigns, instance_assigns, registers, @rethrow_errors, @resource_limits)
      else
        raise ArgumentError, "Expected Hash or Liquid::Context as parameter"
      end

      case args.last
      when Hash
        options = args.pop

        registers.merge!(options[:registers]) if options[:registers].is_a?(Hash)

        apply_options_to_context(context, options)
      when Module, Array
        context.add_filters(args.pop)
      end

      # Retrying a render resets resource usage
      context.resource_limits.reset

      begin
        # render the nodelist.
        # for performance reasons we get an array back here. join will make a string out of it.
        result = with_profiling(context) do
          @root.render(context)
        end
        result.respond_to?(:join) ? result.join : result
      rescue Liquid::MemoryError => e
        context.handle_error(e)
      ensure
        @errors = context.errors
      end
    end

    def render!(*args)
      @rethrow_errors = true
      render(*args)
    end

    private

    def tokenize(source)
      Tokenizer.new(source, @line_numbers)
    end

    def with_profiling(context)
      if @profiling && !context.partial
        raise "Profiler not loaded, require 'liquid/profiler' first" unless defined?(Liquid::Profiler)

        @profiler = Profiler.new
        @profiler.start

        begin
          yield
        ensure
          @profiler.stop
        end
      else
        yield
      end
    end

    def apply_options_to_context(context, options)
      context.add_filters(options[:filters]) if options[:filters]
      context.global_filter = options[:global_filter] if options[:global_filter]
      context.exception_renderer = options[:exception_renderer] if options[:exception_renderer]
      context.strict_variables = options[:strict_variables] if options[:strict_variables]
      context.strict_filters = options[:strict_filters] if options[:strict_filters]
    end
  end
end
