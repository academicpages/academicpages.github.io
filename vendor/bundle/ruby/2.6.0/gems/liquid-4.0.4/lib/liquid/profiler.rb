require 'liquid/profiler/hooks'

module Liquid
  # Profiler enables support for profiling template rendering to help track down performance issues.
  #
  # To enable profiling, first require 'liquid/profiler'.
  # Then, to profile a parse/render cycle, pass the <tt>profile: true</tt> option to <tt>Liquid::Template.parse</tt>.
  # After <tt>Liquid::Template#render</tt> is called, the template object makes available an instance of this
  # class via the <tt>Liquid::Template#profiler</tt> method.
  #
  #   template = Liquid::Template.parse(template_content, profile: true)
  #   output  = template.render
  #   profile = template.profiler
  #
  # This object contains all profiling information, containing information on what tags were rendered,
  # where in the templates these tags live, and how long each tag took to render.
  #
  # This is a tree structure that is Enumerable all the way down, and keeps track of tags and rendering times
  # inside of <tt>{% include %}</tt> tags.
  #
  #   profile.each do |node|
  #     # Access to the node itself
  #     node.code
  #
  #     # Which template and line number of this node.
  #     # If top level, this will be "<root>".
  #     node.partial
  #     node.line_number
  #
  #     # Render time in seconds of this node
  #     node.render_time
  #
  #     # If the template used {% include %}, this node will also have children.
  #     node.children.each do |child2|
  #       # ...
  #     end
  #   end
  #
  # Profiler also exposes the total time of the template's render in <tt>Liquid::Profiler#total_render_time</tt>.
  #
  # All render times are in seconds. There is a small performance hit when profiling is enabled.
  #
  class Profiler
    include Enumerable

    class Timing
      attr_reader :code, :partial, :line_number, :children

      def initialize(node, partial)
        @code        = node.respond_to?(:raw) ? node.raw : node
        @partial     = partial
        @line_number = node.respond_to?(:line_number) ? node.line_number : nil
        @children    = []
      end

      def self.start(node, partial)
        new(node, partial).tap(&:start)
      end

      def start
        @start_time = Time.now
      end

      def finish
        @end_time = Time.now
      end

      def render_time
        @end_time - @start_time
      end
    end

    def self.profile_node_render(node)
      if Profiler.current_profile && node.respond_to?(:render)
        Profiler.current_profile.start_node(node)
        output = yield
        Profiler.current_profile.end_node(node)
        output
      else
        yield
      end
    end

    def self.profile_children(template_name)
      if Profiler.current_profile
        Profiler.current_profile.push_partial(template_name)
        output = yield
        Profiler.current_profile.pop_partial
        output
      else
        yield
      end
    end

    def self.current_profile
      Thread.current[:liquid_profiler]
    end

    def initialize
      @partial_stack = ["<root>"]

      @root_timing = Timing.new("", current_partial)
      @timing_stack = [@root_timing]

      @render_start_at = Time.now
      @render_end_at = @render_start_at
    end

    def start
      Thread.current[:liquid_profiler] = self
      @render_start_at = Time.now
    end

    def stop
      Thread.current[:liquid_profiler] = nil
      @render_end_at = Time.now
    end

    def total_render_time
      @render_end_at - @render_start_at
    end

    def each(&block)
      @root_timing.children.each(&block)
    end

    def [](idx)
      @root_timing.children[idx]
    end

    def length
      @root_timing.children.length
    end

    def start_node(node)
      @timing_stack.push(Timing.start(node, current_partial))
    end

    def end_node(_node)
      timing = @timing_stack.pop
      timing.finish

      @timing_stack.last.children << timing
    end

    def current_partial
      @partial_stack.last
    end

    def push_partial(partial_name)
      @partial_stack.push(partial_name)
    end

    def pop_partial
      @partial_stack.pop
    end
  end
end
