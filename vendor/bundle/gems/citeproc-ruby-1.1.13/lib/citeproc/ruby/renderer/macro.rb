module CiteProc
  module Ruby

    class Renderer

      private

      # @param item [CiteProc::CitationItem]
      # @param node [CSL::Style::Layout]
      # @return [String]
      def render_macro(item, node)
        node.each_child.map { |child|
          render item, child
        }.join('')
      end

    end

  end
end
