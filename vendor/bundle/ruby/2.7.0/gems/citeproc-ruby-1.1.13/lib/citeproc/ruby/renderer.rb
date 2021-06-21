module CiteProc
  module Ruby

    class Renderer

      attr_reader :state

      attr_accessor :engine

      def initialize(options_or_engine = nil)
        @state = State.new

        case options_or_engine
        when Engine
          @engine = options_or_engine
        when Hash
          locale, format = options_or_engine.values_at(:locale, :format)
          @locale = locale.is_a?(CSL::Locale) ? locale : CSL::Locale.load(locale)
          @format = Format.load(format)
        end
      end

      def abbreviate(*arguments)
        return unless engine
        engine.abbreviate(*arguments)
      end
      alias abbrev abbreviate

      def allow_locale_overrides?
        return false unless engine
        engine.options[:allow_locale_overrides]
      end

      # @param item [CiteProc::CitationItem]
      # @param node [CSL::Node]
      # @return [String] the rendered and formatted string
      def render(item, node)
        raise ArgumentError, "no CSL node: #{node.inspect}" unless
          node.respond_to?(:nodename)

        specialize = "render_#{node.nodename.tr('-', '_')}"

        raise ArgumentError, "#{specialize} not implemented" unless
          respond_to?(specialize, true)

        format! send(specialize, item, node), node
      end

      # @param data [CiteProc::CitationData]
      # @param node [CSL::Style::Citation]
      # @return [String] the rendered and formatted string
      def render_citation(data, node)
        state.store! data, node

        citations = join data.map { |item|
          render_single_citation item, node.layout
        }, node.layout.delimiter || ''

        result = format! citations, node.layout
      ensure
        state.clear! result
      end

      # @param data [CiteProc::CitationItem]
      # @param node [CSL::Style::Layout]
      # @return [String] the rendered and string
      def render_single_citation(item, node)
        # TODO author_only
        item.suppress! 'author' if item.suppress_author?

        join [item.prefix, render_layout(item, node), item.suffix].compact
      end

      # @param item [CiteProc::CitationItem]
      # @param node [CSL::Style::Bibliography]
      # @return [String] the rendered and formatted string
      def render_bibliography(item, node)
        state.store! item, node

        if allow_locale_overrides? && item.language != locale.language
          begin
            new_locale = CSL::Locale.load(item.language)

            unless new_locale.nil?
              original_locale, @locale = @locale, new_locale
            end
          rescue ParseError
            # locale not found
          end
        end

        result = render item, node.layout

      ensure
        unless original_locale.nil?
          @locale = original_locale
        end

        state.clear! result
      end

      def render_sort(a, b, node, key)
        state.store! nil, key

        original_format = @format
        @format = Formats::Sort.new

        if a.is_a?(CiteProc::Names)
          [render_name(a, node), render_name(b, node)]

        else
          # We need to clear any items that are suppressed
          # because they were used as substitutes during
          # rendering for sorting purposes!
          a_rendered = render a.cite, node
          a.suppressed.clear

          b_rendered = render b.cite, node
          b.suppressed.clear

          [a_rendered, b_rendered]
        end

      ensure
        @format = original_format
        state.clear!
      end

    end

  end
end
