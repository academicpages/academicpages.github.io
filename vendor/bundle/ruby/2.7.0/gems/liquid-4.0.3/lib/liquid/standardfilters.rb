require 'cgi'
require 'bigdecimal'

module Liquid
  module StandardFilters
    HTML_ESCAPE = {
      '&'.freeze => '&amp;'.freeze,
      '>'.freeze => '&gt;'.freeze,
      '<'.freeze => '&lt;'.freeze,
      '"'.freeze => '&quot;'.freeze,
      "'".freeze => '&#39;'.freeze
    }.freeze
    HTML_ESCAPE_ONCE_REGEXP = /["><']|&(?!([a-zA-Z]+|(#\d+));)/
    STRIP_HTML_BLOCKS = Regexp.union(
      /<script.*?<\/script>/m,
      /<!--.*?-->/m,
      /<style.*?<\/style>/m
    )
    STRIP_HTML_TAGS = /<.*?>/m

    # Return the size of an array or of an string
    def size(input)
      input.respond_to?(:size) ? input.size : 0
    end

    # convert an input string to DOWNCASE
    def downcase(input)
      input.to_s.downcase
    end

    # convert an input string to UPCASE
    def upcase(input)
      input.to_s.upcase
    end

    # capitalize words in the input centence
    def capitalize(input)
      input.to_s.capitalize
    end

    def escape(input)
      CGI.escapeHTML(input.to_s).untaint unless input.nil?
    end
    alias_method :h, :escape

    def escape_once(input)
      input.to_s.gsub(HTML_ESCAPE_ONCE_REGEXP, HTML_ESCAPE)
    end

    def url_encode(input)
      CGI.escape(input.to_s) unless input.nil?
    end

    def url_decode(input)
      return if input.nil?

      result = CGI.unescape(input.to_s)
      raise Liquid::ArgumentError, "invalid byte sequence in #{result.encoding}" unless result.valid_encoding?

      result
    end

    def slice(input, offset, length = nil)
      offset = Utils.to_integer(offset)
      length = length ? Utils.to_integer(length) : 1

      if input.is_a?(Array)
        input.slice(offset, length) || []
      else
        input.to_s.slice(offset, length) || ''
      end
    end

    # Truncate a string down to x characters
    def truncate(input, length = 50, truncate_string = "...".freeze)
      return if input.nil?
      input_str = input.to_s
      length = Utils.to_integer(length)
      truncate_string_str = truncate_string.to_s
      l = length - truncate_string_str.length
      l = 0 if l < 0
      input_str.length > length ? input_str[0...l] + truncate_string_str : input_str
    end

    def truncatewords(input, words = 15, truncate_string = "...".freeze)
      return if input.nil?
      wordlist = input.to_s.split
      words = Utils.to_integer(words)
      l = words - 1
      l = 0 if l < 0
      wordlist.length > l ? wordlist[0..l].join(" ".freeze) + truncate_string.to_s : input
    end

    # Split input string into an array of substrings separated by given pattern.
    #
    # Example:
    #   <div class="summary">{{ post | split '//' | first }}</div>
    #
    def split(input, pattern)
      input.to_s.split(pattern.to_s)
    end

    def strip(input)
      input.to_s.strip
    end

    def lstrip(input)
      input.to_s.lstrip
    end

    def rstrip(input)
      input.to_s.rstrip
    end

    def strip_html(input)
      empty = ''.freeze
      result = input.to_s.gsub(STRIP_HTML_BLOCKS, empty)
      result.gsub!(STRIP_HTML_TAGS, empty)
      result
    end

    # Remove all newlines from the string
    def strip_newlines(input)
      input.to_s.gsub(/\r?\n/, ''.freeze)
    end

    # Join elements of the array with certain character between them
    def join(input, glue = ' '.freeze)
      InputIterator.new(input).join(glue)
    end

    # Sort elements of the array
    # provide optional property with which to sort an array of hashes or drops
    def sort(input, property = nil)
      ary = InputIterator.new(input)

      return [] if ary.empty?

      if property.nil?
        ary.sort do |a, b|
          nil_safe_compare(a, b)
        end
      elsif ary.all? { |el| el.respond_to?(:[]) }
        begin
          ary.sort { |a, b| nil_safe_compare(a[property], b[property]) }
        rescue TypeError
          raise_property_error(property)
        end
      end
    end

    # Sort elements of an array ignoring case if strings
    # provide optional property with which to sort an array of hashes or drops
    def sort_natural(input, property = nil)
      ary = InputIterator.new(input)

      return [] if ary.empty?

      if property.nil?
        ary.sort do |a, b|
          nil_safe_casecmp(a, b)
        end
      elsif ary.all? { |el| el.respond_to?(:[]) }
        begin
          ary.sort { |a, b| nil_safe_casecmp(a[property], b[property]) }
        rescue TypeError
          raise_property_error(property)
        end
      end
    end

    # Filter the elements of an array to those with a certain property value.
    # By default the target is any truthy value.
    def where(input, property, target_value = nil)
      ary = InputIterator.new(input)

      if ary.empty?
        []
      elsif ary.first.respond_to?(:[]) && target_value.nil?
        begin
          ary.select { |item| item[property] }
        rescue TypeError
          raise_property_error(property)
        end
      elsif ary.first.respond_to?(:[])
        begin
          ary.select { |item| item[property] == target_value }
        rescue TypeError
          raise_property_error(property)
        end
      end
    end

    # Remove duplicate elements from an array
    # provide optional property with which to determine uniqueness
    def uniq(input, property = nil)
      ary = InputIterator.new(input)

      if property.nil?
        ary.uniq
      elsif ary.empty? # The next two cases assume a non-empty array.
        []
      elsif ary.first.respond_to?(:[])
        begin
          ary.uniq { |a| a[property] }
        rescue TypeError
          raise_property_error(property)
        end
      end
    end

    # Reverse the elements of an array
    def reverse(input)
      ary = InputIterator.new(input)
      ary.reverse
    end

    # map/collect on a given property
    def map(input, property)
      InputIterator.new(input).map do |e|
        e = e.call if e.is_a?(Proc)

        if property == "to_liquid".freeze
          e
        elsif e.respond_to?(:[])
          r = e[property]
          r.is_a?(Proc) ? r.call : r
        end
      end
    rescue TypeError
      raise_property_error(property)
    end

    # Remove nils within an array
    # provide optional property with which to check for nil
    def compact(input, property = nil)
      ary = InputIterator.new(input)

      if property.nil?
        ary.compact
      elsif ary.empty? # The next two cases assume a non-empty array.
        []
      elsif ary.first.respond_to?(:[])
        begin
          ary.reject { |a| a[property].nil? }
        rescue TypeError
          raise_property_error(property)
        end
      end
    end

    # Replace occurrences of a string with another
    def replace(input, string, replacement = ''.freeze)
      input.to_s.gsub(string.to_s, replacement.to_s)
    end

    # Replace the first occurrences of a string with another
    def replace_first(input, string, replacement = ''.freeze)
      input.to_s.sub(string.to_s, replacement.to_s)
    end

    # remove a substring
    def remove(input, string)
      input.to_s.gsub(string.to_s, ''.freeze)
    end

    # remove the first occurrences of a substring
    def remove_first(input, string)
      input.to_s.sub(string.to_s, ''.freeze)
    end

    # add one string to another
    def append(input, string)
      input.to_s + string.to_s
    end

    def concat(input, array)
      unless array.respond_to?(:to_ary)
        raise ArgumentError.new("concat filter requires an array argument")
      end
      InputIterator.new(input).concat(array)
    end

    # prepend a string to another
    def prepend(input, string)
      string.to_s + input.to_s
    end

    # Add <br /> tags in front of all newlines in input string
    def newline_to_br(input)
      input.to_s.gsub(/\n/, "<br />\n".freeze)
    end

    # Reformat a date using Ruby's core Time#strftime( string ) -> string
    #
    #   %a - The abbreviated weekday name (``Sun'')
    #   %A - The  full  weekday  name (``Sunday'')
    #   %b - The abbreviated month name (``Jan'')
    #   %B - The  full  month  name (``January'')
    #   %c - The preferred local date and time representation
    #   %d - Day of the month (01..31)
    #   %H - Hour of the day, 24-hour clock (00..23)
    #   %I - Hour of the day, 12-hour clock (01..12)
    #   %j - Day of the year (001..366)
    #   %m - Month of the year (01..12)
    #   %M - Minute of the hour (00..59)
    #   %p - Meridian indicator (``AM''  or  ``PM'')
    #   %s - Number of seconds since 1970-01-01 00:00:00 UTC.
    #   %S - Second of the minute (00..60)
    #   %U - Week  number  of the current year,
    #           starting with the first Sunday as the first
    #           day of the first week (00..53)
    #   %W - Week  number  of the current year,
    #           starting with the first Monday as the first
    #           day of the first week (00..53)
    #   %w - Day of the week (Sunday is 0, 0..6)
    #   %x - Preferred representation for the date alone, no time
    #   %X - Preferred representation for the time alone, no date
    #   %y - Year without a century (00..99)
    #   %Y - Year with century
    #   %Z - Time zone name
    #   %% - Literal ``%'' character
    #
    #   See also: http://www.ruby-doc.org/core/Time.html#method-i-strftime
    def date(input, format)
      return input if format.to_s.empty?

      return input unless date = Utils.to_date(input)

      date.strftime(format.to_s)
    end

    # Get the first element of the passed in array
    #
    # Example:
    #    {{ product.images | first | to_img }}
    #
    def first(array)
      array.first if array.respond_to?(:first)
    end

    # Get the last element of the passed in array
    #
    # Example:
    #    {{ product.images | last | to_img }}
    #
    def last(array)
      array.last if array.respond_to?(:last)
    end

    # absolute value
    def abs(input)
      result = Utils.to_number(input).abs
      result.is_a?(BigDecimal) ? result.to_f : result
    end

    # addition
    def plus(input, operand)
      apply_operation(input, operand, :+)
    end

    # subtraction
    def minus(input, operand)
      apply_operation(input, operand, :-)
    end

    # multiplication
    def times(input, operand)
      apply_operation(input, operand, :*)
    end

    # division
    def divided_by(input, operand)
      apply_operation(input, operand, :/)
    rescue ::ZeroDivisionError => e
      raise Liquid::ZeroDivisionError, e.message
    end

    def modulo(input, operand)
      apply_operation(input, operand, :%)
    rescue ::ZeroDivisionError => e
      raise Liquid::ZeroDivisionError, e.message
    end

    def round(input, n = 0)
      result = Utils.to_number(input).round(Utils.to_number(n))
      result = result.to_f if result.is_a?(BigDecimal)
      result = result.to_i if n == 0
      result
    rescue ::FloatDomainError => e
      raise Liquid::FloatDomainError, e.message
    end

    def ceil(input)
      Utils.to_number(input).ceil.to_i
    rescue ::FloatDomainError => e
      raise Liquid::FloatDomainError, e.message
    end

    def floor(input)
      Utils.to_number(input).floor.to_i
    rescue ::FloatDomainError => e
      raise Liquid::FloatDomainError, e.message
    end

    def at_least(input, n)
      min_value = Utils.to_number(n)

      result = Utils.to_number(input)
      result = min_value if min_value > result
      result.is_a?(BigDecimal) ? result.to_f : result
    end

    def at_most(input, n)
      max_value = Utils.to_number(n)

      result = Utils.to_number(input)
      result = max_value if max_value < result
      result.is_a?(BigDecimal) ? result.to_f : result
    end

    def default(input, default_value = ''.freeze)
      if !input || input.respond_to?(:empty?) && input.empty?
        default_value
      else
        input
      end
    end

    private

    def raise_property_error(property)
      raise Liquid::ArgumentError.new("cannot select the property '#{property}'")
    end

    def apply_operation(input, operand, operation)
      result = Utils.to_number(input).send(operation, Utils.to_number(operand))
      result.is_a?(BigDecimal) ? result.to_f : result
    end

    def nil_safe_compare(a, b)
      if !a.nil? && !b.nil?
        a <=> b
      else
        a.nil? ? 1 : -1
      end
    end

    def nil_safe_casecmp(a, b)
      if !a.nil? && !b.nil?
        a.to_s.casecmp(b.to_s)
      else
        a.nil? ? 1 : -1
      end
    end

    class InputIterator
      include Enumerable

      def initialize(input)
        @input = if input.is_a?(Array)
          input.flatten
        elsif input.is_a?(Hash)
          [input]
        elsif input.is_a?(Enumerable)
          input
        else
          Array(input)
        end
      end

      def join(glue)
        to_a.join(glue.to_s)
      end

      def concat(args)
        to_a.concat(args)
      end

      def reverse
        reverse_each.to_a
      end

      def uniq(&block)
        to_a.uniq(&block)
      end

      def compact
        to_a.compact
      end

      def empty?
        @input.each { return false }
        true
      end

      def each
        @input.each do |e|
          yield(e.respond_to?(:to_liquid) ? e.to_liquid : e)
        end
      end
    end
  end

  Template.register_filter(StandardFilters)
end
