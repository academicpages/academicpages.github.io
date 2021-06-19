module CSL

  class Node

    extend Forwardable
    extend Extensions::Nesting

    include Enumerable
    include Comparable

    include Treelike
    include PrettyPrinter


    class << self

      def inherited(subclass)
        types << subclass
        subclass.nesting.each do |klass|
          klass.types << subclass if klass < Node
        end
      end

      def types
        @types ||= Set.new
      end

      def default_attributes
        @default_attributes ||= {}
      end

      def hide_default_attributes?
        !@show_default_attributes
      end

      def hide_default_attributes!
        @show_default_attributes = false
      end

      def show_default_attributes!
        @show_default_attributes = true
      end

      def constantize(name)
        pattern = /:#{name.to_s.tr('-', '')}$/i
        klass = types.detect { |t| t.matches?(pattern) }

        case
        when !klass.nil?
          klass
        when nesting[-2].respond_to?(:constantize)
          nesting[-2].constantize(name)
        else
          nil
        end
      end

      # @return [Boolean] whether or not the node's name matches the
      #   passed-in name pattern
      def match?(name_pattern)
        name_pattern === name
      end
      alias matches? match?

      # Returns a new node with the passed in name and attributes.
      def create(name, attributes = {}, &block)
        klass = constantize(name)

        node = (klass || Node).new(attributes, &block)
        node.nodename = name
        node
      end

      def create_attributes(attributes)
        if const?(:Attributes)
          const_get(:Attributes).new(default_attributes.merge(attributes))
        else
          default_attributes.merge(attributes)
        end
      end

      def parse(data)
        parse!(data)
      rescue
        nil
      end

      def parse!(data)
        node = CSL.parse!(data, self)

        raise ParseError, "root node not #{self.name}: #{node.inspect}" unless
          node.class == self || Node.equal?(self)

        node
      end

      private

      def has_language
        attr_accessor :language

        define_method :has_language? do
          !language.nil?
        end

        public :language, :language=, :has_language?

        alias_method :original_attribute_assignments, :attribute_assignments

        define_method :attribute_assignments do
          if has_language?
            original_attribute_assignments.unshift('xml:lang="%s"' % language)
          else
            original_attribute_assignments
          end
        end

        private :original_attribute_assignments, :attribute_assignments
      end

      def attr_defaults(attributes)
        default_attributes.merge! attributes
      end

      # Creates a new Struct for the passed-in attributes. Node instances
      # will create an instance of this struct to manage their respective
      # attributes.
      #
      # The new Struct will be available as Attributes in the current node's
      # class scope.
      def attr_struct(*attributes)
        const_set(:Attributes, Struct.new(*attributes) {

          # 1.8 Compatibility
          @keys = attributes.map(&:to_sym).freeze

          class << self
            attr_reader :keys
          end

          CSL.silence_warnings do
            def initialize(attrs = {})
              super(*attrs.symbolize_keys.values_at(*keys))
            end
          end

          # @return [<Symbol>] a list of symbols representing the names/keys
          #   of the attribute variables.
          def keys
            __class__.keys
          end

          def symbolize_keys
            self
          end

          def values
            super.compact
          end

          def to_hash
            Hash[keys.zip(values_at(*keys)).reject { |_, v| v.nil? }]
          end

          # @return [Boolean] true if all the attribute values are nil;
          #   false otherwise.
          def empty?
            values.compact.empty?
          end

          def fetch(key, default = nil)
            value = keys.include?(key.to_sym) && send(:'[]', key)

            if block_given?
              value || yield(key)
            else
              value || default
            end
          end

          # Merges the current with the passed-in attributes.
          #
          # @param other [#each_pair] the other attributes
          # @return [self]
          def merge(other)
            raise ArgumentError, "failed to merge #{other.class} into Attributes" unless
              other.respond_to?(:each_pair)

            other.each_pair do |part, value|
              part = part.to_sym
              send(:'[]=', part, value) if !value.nil? && keys.include?(part)
            end

            self
          end
          alias merge! merge

          # @overload values_at(selector, ... )
          #   Returns an array containing the attributes in self according
          #   to the given selector(s). The selectors may be either integer
          #   indices, ranges (functionality inherited from Struct) or
          #   symbols identifying valid keys (similar to Hash#values_at).
          #
          # @example
          #   attributes.values_at(:family, :nick) #=> ['Matsumoto', 'Matz']
          #
          # @see Struct#values_at
          # @return [Array] the list of values
          def values_at(*arguments)
            arguments.flatten.inject([]) do |values, key|
              if key.is_a?(Symbol)
                values.push fetch(key)
              else
                values.concat super(key)
              end
            end
          end

        })
      end

    end


    attr_reader :attributes

    def_delegators :attributes, :[], :[]=, :values, :values_at, :length, :size

    def initialize(attributes = {})
      @attributes = self.class.create_attributes(attributes)
      @children = self.class.create_children

      yield self if block_given?
    end

    def initialize_copy(other)
      @parent, @ancestors, @descendants, @siblings, @root, @depth = nil
      initialize(other.attributes)
    end

    def deep_copy
      copy = dup

      each_child do |child|
        copy.add_child child.deep_copy
      end

      copy
    end

    def merge!(options)
      attributes.merge!(options)
      self
    end

    def reverse_merge!(options)
      options.each_pair do |key, value|
        attributes[key] = value unless attribute? key
      end

      self
    end

    # @return [Boolean] whether or not the node has default attributes
    def has_default_attributes?
      !default_attributes.empty?
    end
    alias has_defaults? has_default_attributes?

    # Iterates through the Node's attributes
    def each(&block)
      if block_given?
        attributes.each_pair(&block)
        self
      else
        to_enum
      end
    end
    alias each_pair each

    # @param name [#to_sym] the name of the attribute
    # @return [Boolean] whether or not key is set to the default value
    def default_attribute?(name)
      defaults = self.class.default_attributes
      name, value = name.to_sym, attributes.fetch(name)

      return false unless !value.nil? || defaults.key?(name)
      defaults[name] == value
    end

    # @return [Hash] the attributes currently set to their default values
    def default_attributes
      attributes.to_hash.select do |name, _|
        default_attribute?(name)
      end
    end

    # @return [Hash] the attributes currently not set to their default values
    def custom_attributes
      attributes.to_hash.reject do |name, _|
        default_attribute?(name)
      end
    end

    # Returns true if the node contains an attribute with the passed-in name;
    # false otherwise.
    def attribute?(name)
      attributes.fetch(name, false)
    end

    # @param [[String]] names list of attribute names
    # @return [Boolean] true if the node contains attributes for all
    #   passed-in names; false otherwise.
    def attributes?(*names)
      names.flatten(1).all? do |name|
        attribute?(name)
      end
    end

    # Returns true if the node contains any attributes (ignores nil values);
    # false otherwise.
    def has_attributes?
      !attributes.empty?
    end

    def has_language?
      false
    end

    def textnode?
      false
    end
    alias has_text? textnode?

    def save_to(path, options = {})
      File.open(path, 'w:UTF-8') do |f|
        f << (options[:compact] ? to_xml : pretty_print)
      end

      self
    end

    # Tests whether or not the Name matches the passed-in node name and
    # attribute conditions; if a Hash is passed as a single argument,
    # it is taken as the conditions parameter (the name parameter
    # automatically matches in this case).
    #
    # Whether or not the arguments match the node is determined as
    # follows:
    #
    # 1. The name must match {#nodename}
    # 2. All attribute name/value pairs passed as conditions must match
    #    the corresponding attributes of the node
    #
    # Note that only attributes present in the passed-in conditions
    # influence the match – if you want to match only nodes that contain
    # no other attributes than specified by the conditions, {#exact_match?}
    # should be used instead.
    #
    # @see #exact_match?
    #
    # @example
    #   node.match?(name, conditions)
    #   node.match?(conditions)
    #   node.match?(other_node)
    #
    # @param name [String,Regexp,Node] must match the nodename; alternatively
    #   you can pass a node
    # @param conditions [Hash] the conditions
    #
    # @return [Boolean] whether or not the query matches the node
    def match?(name = nodename, conditions = {})
      name, conditions = match_conditions_for(name, conditions)

      return false unless name === nodename
      return true  if conditions.empty?

      conditions.values.zip(
        attributes.values_at(*conditions.keys)).all? do |condition, value|
          condition === value
        end
    end
    alias matches? match?

    # Tests whether or not the Name matches the passed-in node name and
    # attribute conditions exactly; if a Hash is passed as a single argument,
    # it is taken as the conditions parameter (the name parameter is
    # automatically matches in this case).
    #
    # Whether or not the arguments match the node is determined as
    # follows:
    #
    # 1. The name must match {#nodename}
    # 2. All attribute name/value pairs of the node must match the
    #    corresponding pairs in the passed-in Hash
    #
    # Note that all node attributes are used by this method – if you want
    # to match only a subset of attributes {#match?} should be used instead.
    #
    # @see #match?
    #
    # @example
    #   node.exact_match?(name, conditions)
    #   node.exact_match?(conditions)
    #   node.exact_match?(other_node)
    #
    # @param name [String,Regexp,Node] must match the nodename; alternatively
    #   you can pass a node
    # @param conditions [Hash] the conditions
    #
    # @return [Boolean] whether or not the query matches the node exactly
    def exact_match?(name = nodename, conditions = {})
      name, conditions = match_conditions_for(name, conditions)

      return false unless name === nodename
      return true  if conditions.empty?

      conditions.values_at(*attributes.keys).zip(
        attributes.values_at(*attributes.keys)).all? do |condition, value|
          condition === value
        end
    end
    alias matches_exactly? exact_match?

    # @option filter [Array] a list of attribute names
    # @return [Hash] the node's attributes matching the filter
    def attributes_for(*filter)
      filter.flatten!

      Hash[map { |name, value|
        !value.nil? && filter.include?(name) ? [name, value.to_s] : nil
      }.compact]
    end


    # The node's formatting options. If the node's parent responds
    # to `inheritable_formatting_options`, these will be included
    # in the result. This makes it easy for nodes to push formatting
    # options to their child nodes.
    #
    # @return [Hash] the node's formatting options
    def formatting_options
      options = attributes_for Schema.attr(:formatting)

      if !root? && parent.respond_to?(:inheritable_formatting_options)
        parent.inheritable_formatting_options.merge(options)
      else
        options
      end
    end

    # Whether or not page ranges should be formatted when
    # rendering this node.
    #
    # Page ranges must be formatted if the node is part of
    # a {Style} with a page-range-format value.
    #
    # @return [Boolean] whether or not page ranges should
    #   be formatted
    def format_page_ranges?
      root.respond_to?(:has_page_range_format?) && root.has_page_range_format?
    end

    def page_range_format
      return unless format_page_ranges?
      root.page_range_format
    end

    def strip_periods?
      attribute?(:'strip-periods') && !!(attributes[:'strip-periods'].to_s =~ /^true$/i)
    end

    def quotes?
      attribute?(:'quotes') && !!(attributes[:'quotes'].to_s =~ /^true$/i)
    end


    def <=>(other)
      return nil unless other.is_a?(Node)
      comparables <=> other.comparables
    rescue
      nil
    end

    # Returns the node' XML tags (including attribute assignments) as an
    # array of strings.
    def tags
      if has_children?
        tags = []
        tags << "<#{[nodename, *attribute_assignments].join(' ')}>"

        tags << children.map { |node|
          node.respond_to?(:tags) ? node.tags : [node.to_s]
        }.flatten(1)

        tags << "</#{nodename}>"
        tags
      else
        ["<#{[nodename, *attribute_assignments].join(' ')}/>"]
      end
    end

    def inspect
      "#<#{[self.class.name, *attribute_assignments].join(' ')} children=[#{children.count}]>"
    end

    alias to_s pretty_print


    protected

    def match_conditions
    end

    def comparables
      c = []

      c << nodename
      c << attributes

      c << (textnode? ? text : '')
      c << (has_children? ? children : [])

      c
    end

    private

    def attribute_assignments
      attrs = self.class.hide_default_attributes? ?
        custom_attributes : attributes.to_hash

      attrs.map { |name, value|
        value.nil? ? nil : [name, CSL.encode_xml_attr(value.to_s)].join('=')
      }.compact
    end

    def match_conditions_for(name, conditions)
      case name
      when Node
        conditions, name = name.attributes.to_hash, name.nodename
      when Hash
        conditions, name = name, nodename
      when Symbol
        name = name.to_s
      end

      [name, conditions.symbolize_keys]
    end

  end


  class TextNode < Node

    has_no_children

    class << self
      undef_method :attr_children

      # @override
      def create(name, attributes = {}, &block)
        klass = constantize(name)

        node = (klass || TextNode).new(attributes, &block)
        node.nodename = name
        node
      end
    end

    attr_accessor :text

    def to_s
      CSL.encode_xml_text text.to_s.strip
    end

    # TextNodes quack like a string.
    # def_delegators :to_s, *String.instance_methods(false).reject do |m|
    #   m.to_s =~ /^\W|!$|(?:^(?:hash|eql?|to_s|length|size|inspect)$)/
    # end
    #
    # String.instance_methods(false).select { |m| m.to_s =~ /!$/ }.each do |m|
    #   define_method(m) do
    #     content.send(m) if content.respond_to?(m)
    #   end
    # end

    def initialize(argument = '')
      case
      when argument.respond_to?(:each_pair)
        super
      when argument.respond_to?(:to_s)
        super({})
        @text = argument.to_s
        yield self if block_given?
      else
        raise ArgumentError, "failed to create text node from #{argument.inspect}"
      end
    end

    def initialize_copy(other)
      super
      @text = other.text
    end

    def textnode?
      true
    end

    remove_method :empty?

    def empty?
      text.nil? || text.empty?
    end

    def tags
      ["<#{attribute_assignments.unshift(nodename).join(' ')}>#{to_s}</#{nodename}>"]
    end

    def inspect
      "#<#{[self.class.name, text.inspect, *attribute_assignments].join(' ')}>"
    end

  end

end
