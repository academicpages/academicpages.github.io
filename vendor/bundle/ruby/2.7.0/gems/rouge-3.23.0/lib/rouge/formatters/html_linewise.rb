# -*- coding: utf-8 -*- #
# frozen_string_literal: true

module Rouge
  module Formatters
    class HTMLLinewise < Formatter
      def initialize(formatter, opts={})
        @formatter = formatter
        @tag_name = opts.fetch(:tag_name, 'div')
        @class_format = opts.fetch(:class, 'line-%i')
      end

      def stream(tokens, &b)
        lineno = 0
        token_lines(tokens) do |line_tokens|
          yield %(<#{@tag_name} class="#{sprintf @class_format, lineno += 1}">)
          @formatter.stream(line_tokens) {|formatted| yield formatted }
          yield %(\n</#{@tag_name}>)
        end
      end
    end
  end
end
