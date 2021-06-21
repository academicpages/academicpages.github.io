module CSL
  class Style

    class Text < Node
      attr_struct :variable, :macro, :term, :form, :plural, :value,
				:quotes, :'strip-periods', *Schema.attr(:formatting)

      has_no_children

      def has_variable?
        attribute?(:variable)
      end

      def variable
        attributes[:variable]
      end

      def variable_options
        attributes_for :form
      end

      def has_macro?
        attribute?(:macro)
      end

      # @return [Macro, nil]
      def macro
        raise "failed to resolve macro #{attributes[:macro].inspect}" unless
          !root? && root.respond_to?(:macros)

        root.macros[attributes[:macro]]
      end

      def has_term?
        attribute?(:term)
      end

      def has_value?
        attribute?(:value)
      end

      def value
        attributes[:value]
      end
    end

  end
end
