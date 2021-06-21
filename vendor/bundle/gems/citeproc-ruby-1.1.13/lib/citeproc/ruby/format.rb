# -*- encoding: utf-8 -*-

module CiteProc
  module Ruby

    class Format

      @available = []

      @squeezable = /^[\s\.,:;!?\)\(\[\]]+$/

      @stopwords = {
        :en => %w(a about above across afore after against along alongside amid amidst among amongst
          an and anenst apropos apud around as aside astride at athwart atop barring before behind
          below beneath beside besides between beyond but by circa despite d down during except for
          forenenst from given in inside into lest like modulo near next nor notwithstanding of off
          on onto or out over per plus pro qua sans since so than the through thru throughout thruout
          till to toward towards under underneath until unto up upon versus vs v via vis-à-vis with
          within without)
      }

      class << self
        attr_reader :available, :stopwords

        def inherited(base)
          Format.available << base
        end

        def load(name = nil)
          return new unless name
          return name if name.is_a?(Format)

          name = name.to_s.downcase

          klass = available.detect do |format|
            format.name.split('::')[-1].downcase == name
          end

          raise(Error, "unknown format: #{name}") unless klass

          klass.new
        end

        def stopword?(word, locale = :en)
          return unless stopwords.key?(locale)
          stopwords[locale].include?(word.downcase)
        end

        def squeezable?(string)
          squeezable === string
        end

        def squeezable
          @squeezable ||= Format.squeezable
        end
      end

      attr_reader :locale

      def keys
        @keys ||= (CSL::Schema.attr(:formatting) - [:prefix, :suffix, :display])
      end

      def squeezable?(string)
        self.class.squeezable?(string)
      end

      def squeeze_suffix(string, suffix)
        raise ArgumentError unless string.is_a?(::String)
        raise ArgumentError unless suffix.is_a?(::String)

        return string.dup if suffix.empty?
        return suffix.dup if string.empty?

        string, stripped = strip(string)
        string, quotes = split_closing_quotes(string)

        suffix = decode_entities(suffix)

        suffix = suffix.each_char.drop_while.with_index { |c, i|
          squeezable?(c) && string.end_with?(suffix[0, i + 1])
        }.join('')

        # Handle special cases like ?. or ;.
        if suffix.start_with?('.') && string.end_with?(';', ',', '!', '?', ':')
          suffix = suffix[1..-1]
        end

        # Handle special cases ;, and :,
        if suffix.start_with?(',') && string.end_with?(';', ':')
          suffix = suffix[1..-1]
        end

        # Handle special cases ,; and :;
        if suffix.start_with?(';') && string.end_with?(',', ':')
          suffix = suffix[1..-1]
        end

        # Handle punctiation-in-quote
        if !quotes.nil? && punctuation_in_quotes?
          if suffix.sub!(/^([\.,])/, '')
            punctuation = ($1).to_s
          end
        end

        "#{string}#{punctuation}#{quotes}#{stripped}#{suffix}"
      end

      def squeeze_prefix(string, prefix)
        raise ArgumentError unless string.is_a?(::String)
        raise ArgumentError unless prefix.is_a?(::String)

        prefix = prefix.reverse.each_char.drop_while.with_index { |c, i|
          squeezable?(c) && string.start_with?(prefix[-(i + 1) .. -1])
        }.join('').reverse

        "#{prefix}#{string}"
      end

      alias concat squeeze_suffix

      def join(list, delimiter = nil)
        raise ArgumentError unless list.is_a?(Enumerable)
        return '' if list.length.zero?
        return list[0] if list.length == 1

        if delimiter.nil? || delimiter.empty?
          list.inject do |m, n|
            concat(m, n)
          end
        else
          list.inject do |m, n|
            concat(concat(m, delimiter), n)
          end
        end
      end

      def bibliography(bibliography, locale = nil)
        bibliography.connector = "\n" * bibliography.entry_spacing
        bibliography
      end

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

        apply_quotes if node.quotes? && !locale.nil?

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

      def escape_quotes?
        false
      end

      def close_quote
        locale && locale.t('close-quote') ||  '"'
      end

      def close_inner_quote
        locale && locale.t('close-inner-quote') || "'"
      end

      def split_closing_quotes(string)
        string.split(/((#{Regexp.quote(close_inner_quote)}|#{Regexp.quote(close_quote)})+)$/, 2)
      end

      def apply_quotes
        output.replace locale.quote(output, escape_quotes?)
      end

      def apply_text_case
        case options[:'text-case']
        when 'lowercase'
          output.replace CiteProc.downcase output

        when 'uppercase'
          output.replace CiteProc.upcase output

        when 'capitalize-first'
          output.sub!(/^([^\p{L}]*)(\p{Ll})/) { "#{$1}#{CiteProc.upcase($2)}" }

        when 'capitalize-all'
          output.gsub!(/\b(\p{Ll})/) { CiteProc.upcase($1) }

        when 'sentence'
          output.sub!(/^([^\p{L}]*)(\p{Ll})/) { "#{$1}#{CiteProc.upcase($2)}" }
          output.gsub!(/\b(\p{Lu})(\p{Lu}+)\b/) { "#{$1}#{CiteProc.downcase($2)}" }

        when 'title'
          return if locale && locale.language != :en

          # TODO add support for stop words consisting of multiple words
          #output.gsub!(/\b(\p{Lu})(\p{Lu}+)\b/) { "#{$1}#{CiteProc.downcase($2)}" }

          # TODO exceptions: word followed by colon
          first = true
          output.gsub!(/\b(\p{L})([\p{L}\.]+)\b/) do |word|
            first_letter = $1
            rest_of_word = $2
            result = word

            if first_letter.match(/^\p{Ll}/) && (!Format.stopword?(word) || first)
              result = "#{CiteProc.upcase(first_letter)}#{rest_of_word}"
            end
            first = false
            result
          end

          output.gsub!(/(\.|\b)(\p{Ll})([\p{L}\.]+)\b$/) do |word|
            word_boundary = $1
            first_letter = $2
            rest_of_word = $3

            if word_boundary == '.'
              word
            else
              "#{CiteProc.upcase(first_letter)}#{rest_of_word}"
            end
          end
        end
      end

      def punctuation_in_quotes?
        !locale.nil? && locale.punctuation_in_quotes?
      end

      def apply_display
      end

      def apply_prefix
        output.replace(squeeze_prefix(output, prefix))
      end

      def apply_suffix
        output.replace(squeeze_suffix(output, suffix))
      end

      def prefix
        options[:prefix].to_s
      end

      def suffix
        options[:suffix].to_s
      end

      def strip(string)
        string
      end

      protected

      attr_reader :input, :output, :node

      def options
        @options ||= @node.formatting_options
      end

      def finalize!
      end

      def finalize_content!
      end

      def setup!
      end

      def decode_entities(string)
        string.gsub(/&#x([0-9a-f]);/i) do
          [Integer("0x#{$1}")].pack('U')
        end
      end

      def cleanup!
        @input, @output, @node, @options = nil
      end
    end

  end
end
