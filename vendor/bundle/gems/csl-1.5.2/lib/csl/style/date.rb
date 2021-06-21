module CSL
  class Style

    class Date < Node
      attr_defaults :'date-parts' => 'year-month-day'

      attr_struct :name, :form, :'range-delimiter', :'date-parts',
				:variable, *Schema.attr(:formatting, :delimiter)

      attr_children :'date-part'

      alias date_parts date_part
      alias parts date_part

      private :date_part

      def initialize(attributes = {})
        super(attributes, &nil)
        children[:'date-part'] = []

        yield self if block_given?
      end

      # @return [Array<String>] the localized date parts to be used
      def date_parts_filter
        attributes[:'date-parts'].to_s.split(/-/)
      end
      alias parts_filter date_parts_filter

      def delimiter
        attributes.fetch(:delimiter, '')
      end

      def has_variable?
        attribute?(:variable)
      end

      def variable
        attributes[:variable]
      end

      def has_form?
        attribute?(:form)
      end
      alias localized? has_form?

      def form
        attributes[:form].to_s
      end

      def numeric?
        form =~ /^numeric$/i
      end

      def text?
        form =~ /^text$/i
      end

      def has_date_parts?
        !date_parts.empty?
      end
      alias has_parts? has_date_parts?

      def has_overrides?
        localized? && has_parts?
      end
    end

    class DatePart < Node
      has_no_children

      attr_struct :name, :form, :'range-delimiter', :'strip-periods',
        *Schema.attr(:formatting)

      include CSL::DatePart
    end

  end
end