module CSL
  class Style

    class Bibliography < Node

      include InheritableNameOptions

      attr_struct :'subsequent-author-substitute',
        :'subsequent-author-substitute-rule',
        *Schema.attr(:bibliography, :name, :names)

      attr_children :sort, :layout

      attr_defaults :'line-spacing' => 1, :'entry-spacing' => 1,
        :'subsequent-author-substitute-rule' => 'complete-all'

      alias sort? has_sort?

      def bibliography_options
        attributes_for(*Schema.attr(:bibliography))
      end

      def sort_keys
        return [] unless sort?
        children[:sort].sort_keys
      end

      def substitute_subsequent_authors?
        attribute?(:'subsequent-author-substitute')
      end

      def subsequent_author_substitute
        attributes[:'subsequent-author-substitute'].to_s
      end

      def subsequent_author_substitute_rule
        attributes[:'subsequent-author-substitute-rule'].to_s
      end

      def substitute_subsequent_authors_completely?
        return false unless substitute_subsequent_authors?
        subsequent_author_substitute_rule == 'complete-all'
      end

      def substitute_subsequent_authors_individually?
        return false unless substitute_subsequent_authors?
        subsequent_author_substitute_rule != 'complete-all'
      end
    end

  end
end
