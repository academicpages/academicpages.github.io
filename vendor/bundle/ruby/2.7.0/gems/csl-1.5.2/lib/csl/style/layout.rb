module CSL
  class Style

    class Layout < Node
      attr_struct(*Schema.attr(:affixes, :font, :delimiter))

      def delimiter
        attributes.fetch(:delimiter, '')
      end
    end

  end
end
