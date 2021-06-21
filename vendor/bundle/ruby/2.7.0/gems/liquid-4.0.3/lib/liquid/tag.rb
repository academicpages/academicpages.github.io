module Liquid
  class Tag
    attr_reader :nodelist, :tag_name, :line_number, :parse_context
    alias_method :options, :parse_context
    include ParserSwitching

    class << self
      def parse(tag_name, markup, tokenizer, options)
        tag = new(tag_name, markup, options)
        tag.parse(tokenizer)
        tag
      end

      private :new
    end

    def initialize(tag_name, markup, parse_context)
      @tag_name   = tag_name
      @markup     = markup
      @parse_context = parse_context
      @line_number = parse_context.line_number
    end

    def parse(_tokens)
    end

    def raw
      "#{@tag_name} #{@markup}"
    end

    def name
      self.class.name.downcase
    end

    def render(_context)
      ''.freeze
    end

    def blank?
      false
    end
  end
end
