module Liquid
  class Tokenizer
    attr_reader :line_number

    def initialize(source, line_numbers = false)
      @source = source
      @line_number = line_numbers ? 1 : nil
      @tokens = tokenize
    end

    def shift
      token = @tokens.shift
      @line_number += token.count("\n") if @line_number && token
      token
    end

    private

    def tokenize
      @source = @source.source if @source.respond_to?(:source)
      return [] if @source.to_s.empty?

      tokens = @source.split(TemplateParser)

      # removes the rogue empty element at the beginning of the array
      tokens.shift if tokens[0] && tokens[0].empty?

      tokens
    end
  end
end
