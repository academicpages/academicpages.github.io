module CiteProc
  module Ruby
    module Formats

      class Text < Format

        private

        def finalize!
          super
          output.gsub!(/&(amp|lt|gt);/i, {
            '&amp;' => '&',
            '&gt;'  => '>',
            '&lt;'  => '<'
          })
        end

      end

      class Sort < Text
        #A special format to use when sorting which prevents formatting of extraneous things like quotes

        def apply(input, node, locale = nil)
          return '' if input.nil?
          return input if input.empty? || node.nil?

          return ArgumentError unless node.respond_to?(:formatting_options)


          @input, @output, @node, @locale = input, input.dup, node, locale

          setup!

          # NB: Layout nodes apply formatting to
          # affixes; all other nodes do not!
          if node.is_a? CSL::Style::Layout
            apply_prefix if options.key?(:prefix)
            apply_suffix if options.key?(:suffix)
          end

          keys.each do |format|
            if options.key?(format)
              method = "apply_#{format}".tr('-', '_')
              send method if respond_to?(method)
            end
          end unless options.empty?

          output.gsub!(/\.+/, '') if node.strip_periods?

          #Do not apply quotes when sorting
          #apply_quotes if node.quotes? && !locale.nil?

          finalize_content!

          unless node.is_a? CSL::Style::Layout
            apply_prefix if options.key?(:prefix)
            apply_suffix if options.key?(:suffix)
          end

          apply_display if options.key?(:display)

          finalize!

          output
        ensure
          cleanup!
        end
      end

      class Debug < Format
      end

    end
  end
end
