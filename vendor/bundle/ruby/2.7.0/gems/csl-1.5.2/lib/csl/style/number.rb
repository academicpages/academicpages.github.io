module CSL
  class Style

    # Numbers are CSL rendering elements which output the number variable
    # selected with the required variable attribute.
    class Number < Node
      attr_struct :variable, :form, *Schema.attr(:formatting)

      has_no_children

      def has_variable?
        attribute?(:variable)
      end

      def variable
        attributes[:variable]
      end

      def has_form?
        attribute?(:form)
      end

      def form
        attributes[:form].to_s
      end

      # @return [Boolean] whether or not the number's format is set to
      #   :numeric; also returns true if the number's form attribute is not
      #   set or nil.
      def numeric?
        !has_form? || form == 'numeric'
      end

      # @return [Boolean] whether or not the number's format is set to 'ordinal
      def ordinal?
        has_form? && form == 'ordinal'
      end

      # @return [Boolean] whether or not the number's format is set to 'long-ordinal'
      def long_ordinal?
        has_form? && form == 'long-ordinal'
      end

      # @return [Boolean] whether or not the number's format is set to 'roman'
      def roman?
        has_form? && form == 'roman'
      end
    end

  end
end