module CSL
  class Locale

    # A localized Date comprises a set of formatting rules for dates.
    class Date < Node

      attr_struct :form, *Schema.attr(:formatting, :delimiter)
      attr_children :'date-part'

      alias parts  date_part
      alias locale parent

      def initialize(attributes = {})
        super(attributes)
        children[:'date-part'] = []

        yield self if block_given?
      end
      
      def added_to(node)
        raise ValidationError, "parent must be locale node: was #{node.inspect}" unless node.is_a?(Locale)
      end

      def delimiter
        attributes.fetch(:delimiter, '')
      end

      def has_form?
        attribute?(:form)
      end

      def form
        attributes[:form].to_s
      end

      def text?
        !numeric?
      end

      def numeric?
        attributes[:form].to_s =~ /^numeric$/i
      end

      def has_date_parts?
        !date_parts.empty?
      end
      alias has_parts? has_date_parts?
      
    end

    # DatePart represent the localized formatting options for an individual
    # date part (day, month, or year).
    class DatePart < Node
      has_no_children

      attr_struct :name, :form, :'range-delimiter',
        :'strip-periods', *Schema.attr(:formatting)

      include CSL::DatePart
    end


  end
end
