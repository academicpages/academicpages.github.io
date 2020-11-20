# -*- coding: utf-8 -*- #
# frozen_string_literal: true

module Rouge
  module Lexers
    class JSL < RegexLexer
      title "JSL"
      desc "The JMP Scripting Language (JSL) (jmp.com)"

      tag 'jsl'
      filenames '*.jsl'

      state :root do
        rule %r/\s+/m, Text::Whitespace

        rule %r(//.*?$), Comment::Single
        rule %r(/\*.*?\*/)m, Comment::Multiline

        # messages
        rule %r/(<<)(.*?)(\(|;)/ do |m|
          groups Operator, Name::Function, Punctuation
        end

        # covers built-in and custom functions
        rule %r/([a-z_][\w\s'%.\\]*)(\()/i do |m|
          groups Keyword, Punctuation
        end

        rule %r/\b[+-]?(?:[0-9]+(?:\.[0-9]+)?|\.[0-9]+|\.)(?:e[+-]?[0-9]+)?i?\b/i, Num

        rule %r/\d{2}(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\d{2}(\d{2})?(:\d{2}:\d{2}(:\d{2}(\.\d*)?)?)?/i, Literal::Date

        rule %r/::[a-z_][\w\s'%.\\]*/i, Name::Variable
        rule %r/:\w+/, Name
        rule %r/[a-z_][\w\s'%.\\]*/i, Name::Variable
        rule %r/"(?:\\!"|[^"])*?"n/m, Name::Variable

        rule %r/(")(\\\[)(.*?)(\]\\)(")/m do
          groups Str::Double, Str::Escape, Str::Double, Str::Escape, Str::Double  # escaped string
        end
        rule %r/"/, Str::Double, :dq

        rule %r/[-+*\/!%&<>\|=:]/, Operator
        rule %r/[\[\](){},;]/, Punctuation
      end

      state :dq do
        rule %r/\\![btrnNf0\\"]/, Str::Escape
        rule %r/\\/, Str::Double
        rule %r/"/, Str::Double, :pop!
        rule %r/[^\\"]*/m, Str::Double
      end
    end
  end
end
