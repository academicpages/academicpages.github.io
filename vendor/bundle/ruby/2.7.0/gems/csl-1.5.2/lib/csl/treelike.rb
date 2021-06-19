module CSL

  module Treelike

    attr_accessor :parent
    attr_reader :children
    attr_writer :nodename

    protected :parent=

    def self.included(base)
      base.extend(ClassMethods)
    end

    # @return [String] the node's name.
    def nodename
      @nodename ||= self.class.name.split(/::/)[-1].gsub(/([[:lower:]])([[:upper:]])/, '\1-\2').downcase
    end

    def each_child(&block)
      if block_given?
        children.each(&block)
        self
      else
        enum_for :each_child
      end
    end

    def delete_children(*nodes)
      nodes.flatten.each do |node|
        delete_child node
      end
    end
    alias delete delete_children

    # Deletes child nodes that are equal to the passed-in node. Returns all
    # deleted children. If no children were deleted, returns nil. If the
    # optional block is given, returns the result block if no children were
    # deleted.
    def delete_child(child)
      deleted = children.delete child

      case
      when deleted.nil? && block_given?
        yield
      when deleted.nil?
        nil
      else
        deleted.parent = nil

        deleted_child deleted
        deleted.deleted_from self

        deleted
      end
    rescue => e
      # TODO rollback
      raise e
    end

    def add_children(*nodes)
      nodes.each do |node|
        add_child node
      end
      self
    end

    def add_child(node)
      node.unlink

      node.parent = self
      children << node

      added_child node
      node.added_to self

      node
    rescue => e
      # TODO rollback
      raise e
    end

    def <<(node)
      add_child node
      self
    end

    # Returns the first immediate child node whose nodename matches the
    # passed-in name/pattern and attribute conditions.
    #
    # @param name [String,Regexp] the node name to match
    # @param conditions [Hash] the attributes to match
    #
    # @return [Node,nil] the first matching child node
    def find_child(name, conditions = {})
      children.detect do |child|
        child.match?(name, conditions)
      end
    end
    alias > find_child

    # Returns all immediate child nodes whose nodename matches the passed-in
    # name/pattern and attribute conditions; returns an empty array if there
    # is no match.
    #
    # @param name [String,Regexp] the node name to match
    # @param conditions [Hash] the attributes to match
    #
    # @return [Array<Node>] all matching child nodes
    def find_children(name, conditions = {})
      children.select do |child|
        child.match?(name, conditions)
      end
    end
    alias >> find_children

    def closest(name, conditions = {})
      case
      when root?
        nil
      when parent.match?(name, conditions)
        parent
      else
        parent.closest(name, conditions)
      end
    end

    # @return [Boolean] true if this node has child nodes; false otherwise.
    def has_children?
      !empty?
    end

    # @return [Boolean] true if this node has no child nodes; false otherwise.
    def empty?
      children.empty?
    end

    # Unlinks the node and all its children from its parent node. Returns
    # the old parent node or nil.
    def unlink
      return nil if root?

      other = parent
      other.delete_child self

      self.parent = nil

      other
    end

    def each_sibling
      if block_given?
        unless root?
          parent.children.each do |node|
            yield node unless node.equal?(self)
          end
        end

        self
      else
        enum_for :each_sibling
      end
    end

    def siblings
      @siblings = each_sibling.to_a
    end

    # Traverses the node's sub-tree in depth-first order.
    def each_descendant(&block)
      if block_given?
        each_child do |child|
          yield child
          child.each_descendant(&block)
        end

        self
      else
        enum_for :each_descendant
      end
    end

    # Returns all descendants of the node. See {#descendants!}
    # for a memoized version.
    def descendants
      @descendants = each_descendant.to_a
    end

    def each_ancestor
      if block_given?
        p = parent

        until p.nil?
          yield p
          p = p.parent
        end

        self
      else
        enum_for :each_ancestor
      end
    end

    # @returns this node's ancestors as an array
    def ancestors
      @ancestors = each_ancestor.to_a
    end

    # @return [Fixnum] the node's current depth in the tree
    def depth
      @depth = ancestors.length
    end

    # @return [Node] the root node
    def root
      @root = root? ? self : parent.root!
    end

    # @returns [Boolean] whether or not the node is the tree's root node
    def root?
      parent.nil?
    end


    # Add memoized methods. When processing citations, styles will
    # typically remain stable; therefore cite processors may opt
    # to use memoized versions of the following methods. These
    # versions are marked with an exclamation mark as a reminder
    # that the return values are cached and potentially outdated.
    %w{ ancestors descendants siblings root depth }.each do |name|
      ivar = "@#{name}"
      define_method("#{name}!") do
        if instance_variable_defined?(ivar)
          instance_variable_get(ivar) 
        else 
          send(name)
        end
      end
    end

    protected

    # @abstract
    # Called after the node was added to another node.
    def added_to(node)
    end

    # @abstract
    # Called when the node was deleted from an other node.
    def deleted_from(node)
    end

    private

    # @abstract
    # Called when the passed-in node was added to this node as a child.
    def added_child(node)
    end

    # @abstract
    # Called when the passed-in node was deleted from this node's child nodes.
    def deleted_child(node)
    end


    module ClassMethods

      # Returns a new instance of an Array or Struct to manage the Node's
      # children. This method is called automatically by the Node's
      # constructor.
      def create_children
        if const?(:Children)
          const_get(:Children).new
        else
          []
        end
      end

      def constantize_nodename(name)
        return constantize(name) if respond_to?(:constantize)

        klass = name.to_s.capitalize.gsub(/(\w)-(\w)/) { [$1, $2.upcase].join }

        if const_defined?(klass)
          const_get(klass)
        else
          nil
        end
      end


      private

      def attr_child_names_for(name)
        reader = name.to_s.downcase.tr('-', '_')
        [name.to_sym, reader, "set_child_#{reader}", "has_#{reader}?"]
      end

      # Creates a Struct for the passed-in child node names that will be
      # used internally by the Node to manage its children. The Struct
      # will be automatically initialized and is used similarly to the
      # standard Array that normally holds the child nodes. The benefit of
      # using the Struct is that all child nodes are accessible by name and
      # need not be looked up; this improves performance, however, note that
      # a node defining its children that way can only contain nodes of the
      # given types.
      #
      # This method also generates accessors for each child. The writer
      # method will try to coerce the passed-in value into the correct
      # node type automatically.
      def attr_children(*names)

        names.each do |name|
          name, reader, writer, predicate = attr_child_names_for(name)

          define_method(reader) do
            children[name]
          end unless method_defined?(reader)

          define_method(predicate) do
            c = children[name]
            !(c.nil? || c.is_a?(Array) && c.empty?)
          end unless method_defined?(predicate)

          unless method_defined?(writer)
            define_method(writer) do |value|
              begin
                klass = self.class.constantize_nodename(name)

                if klass
                  value = klass.new(value)
                else
                  # try to force convert value
                  value = (value.is_a?(String) ? TextNode : Node).new(value)
                  value.nodename = name.to_s
                end

              rescue => e
                raise ArgumentError, "failed to convert #{value.inspect} to node: #{e.message}"
              end unless value.respond_to?(:nodename)

              add_child value
              value
            end

            alias_method :"#{reader}=", writer unless method_defined?(:"#{reader}=")
          end
        end

        const_set(:Children, Struct.new(*names) {

          # 1.8 Compatibility
          @keys = members.map(&:to_sym).freeze

          class << self
            attr_reader :keys
          end

          def initialize(attrs = {})
            super(*attrs.symbolize_keys.values_at(*keys))
            @order = []
          end

          def index(node, &block)
            @order.index(node, &block)
          end

          # @return [<Symbol>] a list of symbols representing the names/keys
          #   of the attribute variables.
          def keys
            __class__.keys
          end


          def count
            values.reject { |c| c.nil? || c.is_a?(Array) && c.empty? }.length
          end

          alias original_each each

          # Iterates through all children. Nil values are skipped and Arrays
          # expanded.
          def each(&block)
            if block_given?
              order.each(&block)
              self
            else
              to_enum
            end
          end

          def empty?
            all?(&:nil?)
          end

          def select(&block)
            each.select(&block)
          end

          # Adds the node as a child node. Raises ValidationError if none
          # of the Struct members matches the node's name. If there is
          # already a node set with this node name, the node will be pushed
          # to an array for that name.
          def push(node)
            unless node.respond_to?(:nodename) && keys.include?(node.nodename.to_sym)
              raise ValidationError, "not allowed to add #{node.inspect} to #{inspect}"
            end

            current = self[node.nodename]
            case current
            when Array
              current.push(node)
            when nil
              self[node.nodename] = node
            else
              self[node.nodename] = [current, node]
            end

            # Add to @order to keep track of node ordering
            @order << node

            self
          end

          alias << push

          # Delete items from self that are equal to node. If any items are
          # found, returns the deleted items. If the items is not found,
          # returns nil. If the optional code block is given, returns the
          # result og block if the item is not found.
          def delete(node)
            return nil unless node.respond_to?(:nodename)

            deleted = resolve(node.nodename)
            if deleted.kind_of?(Array)
              deleted = deleted.delete(node)
            else
              if deleted == node
                self[node.nodename] = nil
              else
                deleted = nil
              end
            end

            # Delete node from ordered list as well
            @order.delete(node)

            if deleted.nil? && block_given?
              yield
            else
              deleted
            end
          end

          def fetch(name, default = nil)
            if block_given?
              resolve(name) || yield(key)
            else
              resolve(name) || default
            end
          end

          protected

          attr_reader :order

          private

          def resolve(nodename)
            keys.include?(nodename.to_sym) && self[nodename]
          end
        })
      end

      def alias_child(new_name, old_name)
        attr_child_names_for(new_name).zip(attr_child_names_for(old_name)).each do |nn, on|
          alias_method nn, on if method_defined?(on)
        end
      end

      # Turns the node into a leaf-node.
      def has_no_children
        undef_method :add_child
        undef_method :added_child
        undef_method :add_children
        undef_method :<<

        undef_method :delete_child
        undef_method :deleted_child
        undef_method :delete_children

        private :children

        define_method(:has_children?) do
          false
        end

        define_method(:empty?) do
          true
        end

      end

    end

  end
end
