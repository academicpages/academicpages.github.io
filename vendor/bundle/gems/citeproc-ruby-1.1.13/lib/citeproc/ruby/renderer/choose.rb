module CiteProc
  module Ruby

    class Renderer

      # @param item [CiteProc::CitationItem]
      # @param node [CSL::Style::Choose]
      # @return [String]
      def render_choose(item, node)
        return '' unless node.has_children?

        node.each_child do |child|
          return render_block(item, child) if evaluates?(item, child)
        end

        '' # no block was rendered
      end

      # @param item [CiteProc::CitationItem]
      # @param node [CSL::Style::Choose::Block]
      # @return [String]
      def render_block(item, node)
        return '' unless node.has_children?

        join node.each_child.map { |child|
          render item, child
        }
      end


      # Evaluates the conditions of the passed-in Choose::Block
      # against the passed-in CitationItem using the Block's matcher.
      #
      # @param item [CiteProc::CitationItem]
      # @param node [CSL::Style::Choose::Block]
      #
      # @return [Boolean] whether or not the node's conditions
      #   are true for the passed-in item
      def evaluates?(item, node)

        # subtle: else-nodes have no conditions. since the default
        # matcher :all? returns true for an empty list we do not
        # need to check for an else node specifically.

        # return true if node.nodename == 'else'

        node.conditions.send(node.matcher) do |type, matcher, values|
          case type
          when :disambiguate
            false # TODO not implemented yet

          when :'is-numeric'
            evaluates_condition? matcher, values do |value|
              v = item.data.unobservable_read_attribute(value)
              v.respond_to?(:numeric?) && v.numeric?
            end

          when :'is-uncertain-date'
            evaluates_condition? matcher, values do |value|
              v = item.data.unobservable_read_attribute(value)
              v.respond_to?(:uncertain?) && v.uncertain?
            end


          when :locator
            locator = item.locator.to_s.tr(' ', '-')

            evaluates_condition? matcher, values do |value|
              value.to_s == locator
            end

          when :position
            false # TODO not implemented yet

          when :type
            type = item.data.unobservable_read_attribute(:type).to_s

            evaluates_condition? matcher, values do |value|
              value.to_s == type
            end

          when :variable
            evaluates_condition? matcher, values do |value|
              item.data.attribute?(value)
            end

          else
            fail "unknown condition type: #{type}"
          end
        end
      end

      # Evaluates the passed-in block for each value in values,
      # negating the result if the value is prefixed with 'not:'
      def evaluates_condition?(matcher, values, &condition)
        values.send(matcher) do |value|
          value, negate = value.split(/^not:/, 2).reverse
          result = condition.call(value)

          negate ? !result : result
        end
      end
    end

  end
end
