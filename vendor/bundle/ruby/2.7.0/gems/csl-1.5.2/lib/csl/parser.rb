module CSL
  #
  # A relatively straightforward XML parser that parses CSL using either
  # Nokogiri or REXML.
  #
  class Parser
    include Singleton

    attr_accessor :parser

    @engines = {
      :nokogiri => lambda { |source|
        Nokogiri::XML::Document.parse(source, nil, nil,
          Nokogiri::XML::ParseOptions::DEFAULT_XML |
          Nokogiri::XML::ParseOptions::NOBLANKS |
          Nokogiri::XML::ParseOptions::NOENT)
      },
      :default  => lambda { |source|
        REXML::Document.new(source, :compress_whitespace => :all, :ignore_whitespace_nodes => :all)
      }
    }

    class << self
      attr_reader :engines
    end

    def initialize
      require 'nokogiri'
      @parser = Parser.engines[:nokogiri]
    rescue LoadError
      require 'rexml/document'
      @parser = Parser.engines[:default]
    end

    def parse(*arguments)
      parse!(*arguments)
    rescue
      nil
    end

    def parse!(source, scope = Node)
      root = parser[source].children.detect { |child| !skip?(child) }
      parse_tree root, scope
    end

    private

    def parse_node(node, scope = Node)
      attributes, text = parse_attributes(node), parse_text(node)

      if text
        n = TextNode.create node.name, attributes
        n.text = text
        n
      else
        scope.create node.name, attributes
      end
    end

    def parse_attributes(node)
      Hash[*node.attributes.map { |n, a|
        [n.to_sym, a.respond_to?(:value) ? a.value : a.to_s]
      }.flatten]
    end

    def parse_tree(node, scope = Node)
      return nil if node.nil?

      root = parse_node node, scope
      scope = specialize_scope(root, scope)

      node.children.each do |child|
        root << parse_tree(child, scope) unless skip?(child)
      end unless root.textnode?

      root
    end

    def parse_text(node)
      if node.respond_to?(:has_text?)
        node.has_text? && node.text
      else
        child = node.children[0]
        return unless child && child.respond_to?(:text?) && child.text?

        text = child.text
        return if text.to_s.strip.empty?

        text
      end
    end

    def comment?(node)
      node.respond_to?(:comment?) && node.comment? ||
        node.respond_to?(:node_type) &&
        [:comment, :xmldecl, :processing_instruction, 7].include?(node.node_type)
    end

    def text?(node)
      if defined?(Nokogiri)
        node.is_a?(Nokogiri::XML::Text)
      else
        false
      end
    end

    def skip?(node)
      comment?(node) || text?(node)
    end

    def specialize_scope(root, scope = Node)
      case root
      when Style
        Style
      when Locale
        Locale
      when Info
        Info
      else
        scope
      end
    end
  end

end
