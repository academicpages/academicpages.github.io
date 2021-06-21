# -*- coding: utf-8 -*- #
# frozen_string_literal: true

module Rouge
  module Lexers
    load_lexer 'jsx.rb'
    load_lexer 'typescript/common.rb'

    class TSX < JSX
      extend TypescriptCommon

      title 'TSX'
      desc 'TypeScript-compatible JSX (www.typescriptlang.org/docs/handbook/jsx.html)'

      tag 'tsx'
      filenames '*.tsx'

      prepend :element_name do
        rule %r/(\w+)(,)/ do
          groups Name::Other, Punctuation
          pop! 3
        end
      end
    end
  end
end

