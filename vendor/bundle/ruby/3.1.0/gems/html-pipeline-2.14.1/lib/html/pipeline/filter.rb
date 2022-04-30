# frozen_string_literal: true

module HTML
  class Pipeline
    # Base class for user content HTML filters. Each filter takes an
    # HTML string or Nokogiri::HTML::DocumentFragment, performs
    # modifications and/or writes information to the result hash. Filters must
    # return a DocumentFragment (typically the same instance provided to the call
    # method) or a String with HTML markup.
    #
    # Example filter that replaces all images with trollface:
    #
    #   class FuuuFilter < HTML::Pipeline::Filter
    #     def call
    #       doc.search('img').each do |img|
    #         img['src'] = "http://paradoxdgn.com/junk/avatars/trollface.jpg"
    #       end
    #     end
    #   end
    #
    # The context Hash passes options to filters and should not be changed in
    # place.  A Result Hash allows filters to make extracted information
    # available to the caller and is mutable.
    #
    # Common context options:
    #   :base_url   - The site's base URL
    #   :repository - A Repository providing context for the HTML being processed
    #
    # Each filter may define additional options and output values. See the class
    # docs for more info.
    class Filter
      class InvalidDocumentException < StandardError; end

      def initialize(doc, context = nil, result = nil)
        if doc.is_a?(String)
          @html = doc.to_str
          @doc = nil
        else
          @doc = doc
          @html = nil
        end
        @context = context || {}
        @result = result || {}
        validate
      end

      # Public: Returns a simple Hash used to pass extra information into filters
      # and also to allow filters to make extracted information available to the
      # caller.
      attr_reader :context

      # Public: Returns a Hash used to allow filters to pass back information
      # to callers of the various Pipelines.  This can be used for
      # #mentioned_users, for example.
      attr_reader :result

      # The Nokogiri::HTML::DocumentFragment to be manipulated. If the filter was
      # provided a String, parse into a DocumentFragment the first time this
      # method is called.
      def doc
        @doc ||= parse_html(html)
      end

      # The String representation of the document. If a DocumentFragment was
      # provided to the Filter, it is serialized into a String when this method is
      # called.
      def html
        raise InvalidDocumentException if @html.nil? && @doc.nil?
        @html || doc.to_html
      end

      # The main filter entry point. The doc attribute is guaranteed to be a
      # Nokogiri::HTML::DocumentFragment when invoked. Subclasses should modify
      # this document in place or extract information and add it to the context
      # hash.
      def call
        raise NotImplementedError
      end

      # Make sure the context has everything we need. Noop: Subclasses can override.
      def validate; end

      # The Repository object provided in the context hash, or nil when no
      # :repository was specified.
      #
      # It's assumed that the repository context has already been checked
      # for permissions
      def repository
        context[:repository]
      end

      # The User object provided in the context hash, or nil when no user
      # was specified
      def current_user
        context[:current_user]
      end

      # The site's base URL provided in the context hash, or '/' when no
      # base URL was specified.
      def base_url
        context[:base_url] || '/'
      end

      # Ensure the passed argument is a DocumentFragment. When a string is
      # provided, it is parsed and returned; otherwise, the DocumentFragment is
      # returned unmodified.
      def parse_html(html)
        HTML::Pipeline.parse(html)
      end

      # Helper method for filter subclasses used to determine if any of a node's
      # ancestors have one of the tag names specified.
      #
      # node - The Node object to check.
      # tags - An array of tag name strings to check. These should be downcase.
      #
      # Returns true when the node has a matching ancestor.
      def has_ancestor?(node, tags)
        while node = node.parent
          break true if tags.include?(node.name.downcase)
        end
      end

      # Perform a filter on doc with the given context.
      #
      # Returns a HTML::Pipeline::DocumentFragment or a String containing HTML
      # markup.
      def self.call(doc, context = nil, result = nil)
        new(doc, context, result).call
      end

      # Like call but guarantees that a DocumentFragment is returned, even when
      # the last filter returns a String.
      def self.to_document(input, context = nil)
        html = call(input, context)
        HTML::Pipeline.parse(html)
      end

      # Like call but guarantees that a string of HTML markup is returned.
      def self.to_html(input, context = nil)
        output = call(input, context)
        if output.respond_to?(:to_html)
          output.to_html
        else
          output.to_s
        end
      end

      # Validator for required context. This will check that anything passed in
      # contexts exists in @contexts
      #
      # If any errors are found an ArgumentError will be raised with a
      # message listing all the missing contexts and the filters that
      # require them.
      def needs(*keys)
        missing = keys.reject { |key| context.include? key }

        if missing.any?
          raise ArgumentError,
                "Missing context keys for #{self.class.name}: #{missing.map(&:inspect).join ', '}"
        end
      end
    end
  end
end
