module CiteProc
  module Ruby

    class Renderer

      private

      # @param item [CiteProc::CitationItem]
      # @param node [CSL::Style::Layout]
      # @return [String]
      def render_layout(item, node)
        join node.each_child.map { |child|
          render item, child
        }.reject(&:empty?), node.delimiter
      end

    end

  end
end
