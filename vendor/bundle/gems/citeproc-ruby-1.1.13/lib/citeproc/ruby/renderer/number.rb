module CiteProc
  module Ruby

    class Renderer

      # @param item [CiteProc::CitationItem]
      # @param node [CSL::Style::Number]
      # @return [String]
      def render_number(item, node)
        return '' unless node.has_variable?

        variable = item.data[node.variable]
        return variable.to_s unless variable && variable.numeric?

        numbers = variable.tokenize

        case
        when node.ordinal? || node.long_ordinal?
          options = node.attributes_for :form
          # TODO lookup term of variable to check gender

          numbers.map! do |num|
            num =~ /^\d+$/ ? ordinalize(num, options) : num
          end

        when node.roman?
          numbers.map! do |num|
            num =~ /^\d+$/ ? romanize(num) : num
          end

        else
					# nothing
        end

				numbers.join('')
      end

    end

  end
end
