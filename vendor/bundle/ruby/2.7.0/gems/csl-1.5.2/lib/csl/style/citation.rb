module CSL
  class Style

    class Citation < Node

      include InheritableNameOptions

      attr_struct(*Schema.attr(:citation, :names, :name))

      attr_children :sort, :layout

      alias sort? has_sort?

      def sort_keys
        return [] unless sort?
        children[:sort].sort_keys
      end
    end

  end
end
