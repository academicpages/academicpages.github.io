module CiteProc
  module Ruby

    class Renderer

      # @param item [CiteProc::CitationItem]
      # @param node [CSL::Style::Group]
      # @return [String]
      def render_group(item, node)
        return '' unless node.has_children?

        observer = ItemObserver.new(item.data)
        observer.start

        begin
          rendition = node.each_child.map { |child|
            render item, child
          }.reject(&:empty?)

          rendition = join(rendition, node.delimiter)

        ensure
          observer.stop
        end

        return '' if observer.skip?

        rendition
      end

    end

  end
end
