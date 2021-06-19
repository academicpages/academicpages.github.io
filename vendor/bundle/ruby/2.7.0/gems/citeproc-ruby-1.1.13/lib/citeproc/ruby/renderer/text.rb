module CiteProc
  module Ruby

    class Renderer

      # @param item [CiteProc::CitationItem]
      # @param node [CSL::Style::Text]
      # @return [String]
      def render_text(item, node)
        case
        when node.has_variable?

          if node.variable == 'locator'

            # Subtle: when there is no locator we also look
            # in item.data; there should be no locator there
            # either but the read access will be noticed by
            # observers (if any).
            text = item.locator || item.data[:locator].to_s

          else
            text = item.data.variable(node.variable, node.variable_options).to_s

            # Check for abbreviations or short-form fallbacks!
            context, was_short_form = node.variable.split(/-short$/, 2)

            if !was_short_form.nil? || node[:form] == 'short'
              if text.empty? && context != node.variable
                text = item.data.variable(context, node.variable_options).to_s
              end

              text = abbreviate(context, text) || text
            end
          end


          case
          when node.variable == 'page'
            format_page_range!(text, node.page_range_format)

          when node.variable == 'page-first' && text.empty?
            text = item.data[:'page'].to_s[/\d+/].to_s

          end

          text

        when node.has_macro?
          render item, node.macro

        when node.has_term?
          translate node[:term], node.attributes_for(:plural, :form)

        else
          node.value.to_s
        end
      end

    end

  end
end
