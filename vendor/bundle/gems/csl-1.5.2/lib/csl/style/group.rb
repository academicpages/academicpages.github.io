module CSL
  class Style
    
    # The Group rendering element must contain one or more rendering
    # element (with the exception of {Layout}). Group nodes may carry the
    # delimiter attribute to separate their child elements, as well as
    # affixes and display attributes and text formatting (applied to the
    # output of the group as a whole).
    #
    # Groups implicitly act as a conditionals: a Group and its child
    # elements are suppressed if a) at least one rendering element in
    # the Group calls a variable (either directly or via a macro), and
    # b) all variables that are called are empty.
    class Group < Node
      attr_struct(*Schema.attr(:formatting, :delimiter))
      
      def delimiter
        attributes.fetch(:delimiter, '')
      end
    end
    
  end
end
