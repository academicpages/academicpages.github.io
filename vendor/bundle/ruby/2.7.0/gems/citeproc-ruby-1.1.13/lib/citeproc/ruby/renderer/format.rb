# -*- encoding: utf-8 -*-

module CiteProc
  module Ruby

    class Renderer

      def format
       @format ||= Format.load
      end

      def format=(format)
        @format = Format.load(format)
      end

      # Applies the current format on the string using the
      # node's formatting options.
      def format!(string, node)
        format.apply(string, node, locale)
      end

      def join(list, delimiter = nil)
        format.join(list, delimiter)
      end

      # Concatenates two strings, making sure that squeezable
      # characters are not duplicated between string and suffix.
      #
      # @param [String] string
      # @param [String] suffix
      #
      # @return [String] new string consisting of string
      #   and suffix
      def concat(string, suffix)
        format.concat(string, suffix)
      end


      # @return [String] the roman numeral of number
			def romanize(number)
				CiteProc::Number.romanize(number)
			end


      # Formats pages accoring to format. Valid formats are:
      #
      # * "chicago": page ranges are abbreviated according to
      #   the Chicago Manual of Style rules.
      # * "expanded": Abbreviated page ranges are expanded to
      #   their non-abbreviated form: 42-45, 321-328, 2787-2816.
      # * "minimal": All digits repeated in the second number
      #   are left out: 42-45, 321-8, 2787-816.
      #
      # @param [String] pages to be formatted
      # @param [String] format to use for formatting
      def format_page_range(pages, format)
        return if pages.nil?
        format_page_range!(pages.dup, format)
      end

      def format_page_range!(pages, format)
        return if pages.nil?
        return pages if pages.empty?

        dash = translate('page-range-delimiter') || '–' # en-dash

        pages.gsub! PAGE_RANGE_PATTERN do
          affixes, f, t = [$1, $3, $4, $6], $2, $5

          # When there are affixes or no format was
          # specified we skip this part. As a result,
          # only the delimiter will be replaced!

          if affixes.all?(&:empty?) && !format.nil?

            dim = f.length
            delta = dim - t.length

            if delta >= 0
              t.prepend f[0, delta] unless delta.zero?

              if format == 'chicago'
                changes = dim - f.chars.zip(t.chars).
                  take_while { |a,b| a == b }.length if dim == 4

                format = case
                  when dim < 3
                    'expanded'
                  when dim == 4 && changes > 2
                    'expanded'
                  when f[-2, 2] == '00'
                    'expanded'
                  when f[-2] == '0'
                    'minimal'
                  else
                    'minimal-two'
                  end
              end

              case format
              when 'expanded'
                # nothing to do
              when 'minimal'
                t = t.each_char.drop_while.with_index { |c, i| c == f[i] }.join('')
              when 'minimal-two'
                if dim > 2
                  t = t.each_char.drop_while.with_index { |c, i|
                    c == f[i] && dim - i > 2
                  }.join('')
                end
              else
                raise ArgumentError, "unknown page range format: #{format}"
              end
            end
          end

          affixes.zip([f, dash, t]).flatten.compact.join('')
        end

        pages
      end

      PAGE_RANGE_PATTERN =
        #   ------------  -2-  ------------             ------------  -5-  ------------
        /\b([[:alpha:]]*)(\d+)([[:alpha:]]*)\s*[–-]+\s*([[:alpha:]]*)(\d+)([[:alpha:]]*)\b/

    end

  end
end
