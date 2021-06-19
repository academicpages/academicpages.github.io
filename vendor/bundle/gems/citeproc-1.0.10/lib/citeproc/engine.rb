module CiteProc

  # @abstract
  class Engine
    extend Forwardable

    include Converters

    @subclasses ||= []

    class << self

      attr_reader :subclasses, :type, :version

      attr_writer :default

      private :new

      def inherited(subclass)
        subclass.public_class_method :new
        @subclasses << subclass
        @subclasses = subclasses.sort_by { |engine| -1 * engine.priority }
      end

      def default
        @default ||= autodetect or warn 'no citeproc engine found'
      end

      # Returns the engine class for the given name or nil. If no suitable
      # class is found and a block is given, executes the block and returns
      # the result. The list of available engines will be passed to the block.
      def detect(name)
        subclasses.detect { |e| e.name == name } ||
          block_given? ? yield(subclasses) : nil
      end

      # Loads the engine with the given name and returns the engine class.
      def detect!(name, &block)
        load(name)
        block_given? ? detect(name, &block) : detect(name)
      end

      # Returns the best available engine class or nil.
      def autodetect(options = {})
        load('citeproc-ruby') if subclasses.empty?

        subclasses.detect { |e|
          !options.has_key?(:engine) || e.name == options[:engine] and
          !options.has_key?(:name) || e.name == options[:name]
        } || subclasses.first
      end

      # Loads the engine by requiring the engine name.
      def load(name)
        require name.gsub(/-/,'/')
      rescue LoadError
        warn "failed to load #{name} engine: try to gem install #{name}"
      end

      # Returns a list of all available engine names.
      def available
        subclasses.map(&:engine_name)
      end

      def engine_name
        @name ||= name.gsub(/::/, '-').downcase # returns class name as fallback
      end

      def priority
        @priority ||= 0
      end
    end

    attr_accessor :processor

    def_delegators :@processor, :options, :abbreviate

    def initialize(processor = nil)
      @processor = processor
      yield self if block_given?
    end

    [[:name, :engine_name], :type, :version].each do |method_id, target|
      define_method(method_id) do
        self.class.send(target || method_id)
      end
    end

    def process
      raise NotImplementedByEngine
    end

    def append
      raise NotImplementedByEngine
    end

    def bibliography
      raise NotImplementedByEngine
    end

    def render
      raise NotImplementedByEngine
    end

    def update_items
      raise NotImplementedByEngine
    end

    def update_uncited_items
      raise NotImplementedByEngine
    end

    def inspect
      "#<CiteProc::Engine #{name}-#{type}-#{version}>"
    end
  end

end
