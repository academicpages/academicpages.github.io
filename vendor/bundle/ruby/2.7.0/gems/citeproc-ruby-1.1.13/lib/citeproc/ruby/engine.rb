module CiteProc
  module Ruby

    class Engine < CiteProc::Engine

      include SortItems

      @name = 'citeproc-ruby'.freeze
      @type = 'CSL'.freeze
      @version = CSL::Schema.version
      @priority = 1

      attr_reader :renderer, :style

      def_delegators :renderer,
        :format, :format=, :locale, :locale=

      def initialize(*arguments)
        super(*arguments)
        @renderer = Renderer.new(self)

        update! unless processor.nil?
      end

      def style=(new_style)
        @style = CSL::Style.load new_style
      end

      def process(data)
        node = style.citation

        return unless node
        return '' if data.empty?

        # populate item data
        data.each do |item|
          item.data = processor[item.id].dup
        end

        # TODO implement sort in citation data
        sort!(data, node.sort_keys) unless !node.sort?

        # TODO citation number (after sorting?)

        renderer.render_citation data, node
      end

      def append
        raise NotImplementedByEngine
      end

      def bibliography(selector)
        node = style.bibliography
        return unless node

        selection = processor.data.select do |item|
          selector.matches?(item) && !selector.skip?(item)
        end

        sort!(selection, node.sort_keys) unless selection.empty? || !node.sort?

        Bibliography.new(node.bibliography_options) do |bib|
          format.bibliography(bib)

          idx = 1

          selection.each do |item|
            begin
              bib.push item.id, renderer.render_bibliography(item.cite(idx), node)
            rescue => error
              bib.errors << [item.id.to_s, error]
            ensure
              idx += 1 unless error
            end
          end
        end
      end

      def update_items
        raise NotImplementedByEngine
      end

      def update_uncited_items
        raise NotImplementedByEngine
      end

      # @return [String, Array<String>]
      def render(mode, data)
        case mode
        when :bibliography
          node = style.bibliography

          data.map do |item|
            item.data = processor[item.id].dup
            renderer.render item, node
          end

        when :citation
          node = style.citation

          data.each do |item|
            item.data = processor[item.id].dup
          end

          renderer.render_citation data, node

        else
          raise ArgumentError, "cannot render unknown mode: #{mode.inspect}"
        end
      end


      def update!
        renderer.format = processor.options[:format]
        renderer.locale = processor.options[:locale]

        if processor.options[:style].is_a? CSL::Style
          @style = processor.options[:style]
        else
          @style = CSL::Style.load processor.options[:style]
        end

        # Preliminary locale override implementation!
        # Does not yet reverse merge default region and default locale.
        @style.locales.sort.reverse.each do |locale|
          renderer.locale.merge! locale if renderer.locale.like?(locale)
        end

        self
      end

    end
  end
end
