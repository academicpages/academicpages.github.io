# frozen_string_literal: true

module Nokogiri
  module XML
    class DocumentFragment < Nokogiri::XML::Node
      ####
      # Create a Nokogiri::XML::DocumentFragment from +tags+
      def self.parse(tags, options = ParseOptions::DEFAULT_XML, &block)
        new(XML::Document.new, tags, nil, options, &block)
      end

      ##
      #  Create a new DocumentFragment from +tags+.
      #
      #  If +ctx+ is present, it is used as a context node for the
      #  subtree created, e.g., namespaces will be resolved relative
      #  to +ctx+.
      def initialize(document, tags = nil, ctx = nil, options = ParseOptions::DEFAULT_XML)
        return self unless tags

        options = Nokogiri::XML::ParseOptions.new(options) if Integer === options
        yield options if block_given?

        children = if ctx
          # Fix for issue#490
          if Nokogiri.jruby?
            # fix for issue #770
            ctx.parse("<root #{namespace_declarations(ctx)}>#{tags}</root>", options).children
          else
            ctx.parse(tags, options)
          end
        else
          wrapper_doc = XML::Document.parse("<root>#{tags}</root>", nil, nil, options)
          self.errors = wrapper_doc.errors
          wrapper_doc.xpath("/root/node()")
        end
        children.each { |child| child.parent = self }
      end

      if Nokogiri.uses_libxml?
        def dup
          new_document = document.dup
          new_fragment = self.class.new(new_document)
          children.each do |child|
            child.dup(1, new_document).parent = new_fragment
          end
          new_fragment
        end
      end

      ###
      # return the name for DocumentFragment
      def name
        "#document-fragment"
      end

      ###
      # Convert this DocumentFragment to a string
      def to_s
        children.to_s
      end

      ###
      # Convert this DocumentFragment to html
      # See Nokogiri::XML::NodeSet#to_html
      def to_html(*args)
        if Nokogiri.jruby?
          options = args.first.is_a?(Hash) ? args.shift : {}
          unless options[:save_with]
            options[:save_with] = Node::SaveOptions::NO_DECLARATION | Node::SaveOptions::NO_EMPTY_TAGS | Node::SaveOptions::AS_HTML
          end
          args.insert(0, options)
        end
        children.to_html(*args)
      end

      ###
      # Convert this DocumentFragment to xhtml
      # See Nokogiri::XML::NodeSet#to_xhtml
      def to_xhtml(*args)
        if Nokogiri.jruby?
          options = args.first.is_a?(Hash) ? args.shift : {}
          unless options[:save_with]
            options[:save_with] = Node::SaveOptions::NO_DECLARATION | Node::SaveOptions::NO_EMPTY_TAGS | Node::SaveOptions::AS_XHTML
          end
          args.insert(0, options)
        end
        children.to_xhtml(*args)
      end

      ###
      # Convert this DocumentFragment to xml
      # See Nokogiri::XML::NodeSet#to_xml
      def to_xml(*args)
        children.to_xml(*args)
      end

      ###
      # call-seq: css *rules, [namespace-bindings, custom-pseudo-class]
      #
      # Search this fragment for CSS +rules+. +rules+ must be one or more CSS
      # selectors. For example:
      #
      # For more information see Nokogiri::XML::Searchable#css
      def css(*args)
        if children.any?
          children.css(*args) # 'children' is a smell here
        else
          NodeSet.new(document)
        end
      end

      #
      #  NOTE that we don't delegate #xpath to children ... another smell.
      #  def xpath ; end
      #

      ###
      # call-seq: search *paths, [namespace-bindings, xpath-variable-bindings, custom-handler-class]
      #
      # Search this fragment for +paths+. +paths+ must be one or more XPath or CSS queries.
      #
      # For more information see Nokogiri::XML::Searchable#search
      def search(*rules)
        rules, handler, ns, binds = extract_params(rules)

        rules.inject(NodeSet.new(document)) do |set, rule|
          set + if Searchable::LOOKS_LIKE_XPATH.match?(rule)
            xpath(*[rule, ns, handler, binds].compact)
          else
            children.css(*[rule, ns, handler].compact) # 'children' is a smell here
          end
        end
      end

      alias_method :serialize, :to_s

      # A list of Nokogiri::XML::SyntaxError found when parsing a document
      def errors
        document.errors
      end

      def errors=(things) # :nodoc:
        document.errors = things
      end

      def fragment(data)
        document.fragment(data)
      end

      private

      # fix for issue 770
      def namespace_declarations(ctx)
        ctx.namespace_scopes.map do |namespace|
          prefix = namespace.prefix.nil? ? "" : ":#{namespace.prefix}"
          %{xmlns#{prefix}="#{namespace.href}"}
        end.join(" ")
      end
    end
  end
end
