# -*- coding: utf-8 -*- #
# frozen_string_literal: true

module Rouge
  module Lexers
    class TOML < RegexLexer
      title "TOML"
      desc 'the TOML configuration format (https://github.com/mojombo/toml)'
      tag 'toml'

      filenames '*.toml', 'Pipfile'
      mimetypes 'text/x-toml'

      identifier = /\S+/

      state :basic do
        rule %r/\s+/, Text
        rule %r/#.*?$/, Comment
        rule %r/(true|false)/, Keyword::Constant

        rule %r/(\S+)(\s*)(=)(\s*)(\{)/ do |m|
          groups Name::Namespace, Text, Operator, Text, Punctuation
          push :inline
        end

        rule %r/(?<!=)\s*\[[\S]+\]/, Name::Namespace

        rule %r/\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z/, Literal::Date

        rule %r/(\d+\.\d*|\d*\.\d+)([eE][+-]?[0-9]+)?j?/, Num::Float
        rule %r/\d+[eE][+-]?[0-9]+j?/, Num::Float
        rule %r/\-?\d+/, Num::Integer
      end

      state :root do
        mixin :basic

        rule %r/(#{identifier})(\s*)(=)/ do
          groups Name::Property, Text, Punctuation
          push :value
        end
      end

      state :value do
        rule %r/\n/, Text, :pop!
        mixin :content
      end

      state :content do
        mixin :basic
        rule %r/"""/, Str, :mdq
        rule %r/"/, Str, :dq
        rule %r/'''/, Str, :msq
        rule %r/'/, Str, :sq
        mixin :esc_str
        rule %r/\,/, Punctuation
        rule %r/\[/, Punctuation, :array
      end

      state :dq do
        rule %r/"/, Str, :pop!
        rule %r/\n/, Error, :pop!
        mixin :esc_str
        rule %r/[^\\"\n]+/, Str
      end

      state :mdq do
        rule %r/"""/, Str, :pop!
        mixin :esc_str
        rule %r/[^\\"]+/, Str
        rule %r/"+/, Str
      end

      state :sq do
        rule %r/'/, Str, :pop!
        rule %r/\n/, Error, :pop!
        rule %r/[^'\n]+/, Str
      end

      state :msq do
        rule %r/'''/, Str, :pop!
        rule %r/[^']+/, Str
        rule %r/'+/, Str
      end

      state :esc_str do
        rule %r/\\[0t\tn\n "\\r]/, Str::Escape
      end

      state :array do
        mixin :content
        rule %r/\]/, Punctuation, :pop!
      end

      state :inline do
        mixin :content

        rule %r/(#{identifier})(\s*)(=)/ do
          groups Name::Property, Text, Punctuation
        end

        rule %r/\}/, Punctuation, :pop!
      end
    end
  end
end
