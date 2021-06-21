# -*- coding: utf-8 -*- #
# frozen_string_literal: true

module Rouge
  module Lexers
    class Liquid < RegexLexer
      title "Liquid"
      desc 'Liquid is a templating engine for Ruby (liquidmarkup.org)'
      tag 'liquid'
      filenames '*.liquid'

      state :root do
        rule %r/[^\{]+/, Text

        rule %r/(\{%-?)(\s*)/ do
          groups Punctuation, Text::Whitespace
          push :tag_or_block
        end

        rule %r/(\{\{-?)(\s*)/ do
          groups Punctuation, Text::Whitespace
          push :output
        end

        rule %r/\{/, Text
      end

      state :tag_or_block do
        # builtin logic blocks
        rule %r/(if|elsif|unless|case)\b/, Keyword::Reserved, :condition
        rule %r/(when)\b/, Keyword::Reserved, :when

        rule %r/(else)(\s*)(-?%\})/ do
          groups Keyword::Reserved, Text::Whitespace, Punctuation
          pop!
        end

        # other builtin blocks
        rule %r/(capture|(?:in|de)crement)(\s+)([^\s%]+)(\s*)(-?%\})/ do
          groups Name::Tag, Text::Whitespace, Name::Variable, Text::Whitespace, Punctuation
          pop!
        end

        rule %r/(comment)(\s*)(-?%\})/ do
          groups Name::Tag, Text::Whitespace, Punctuation
          push :comment
        end

        rule %r/(raw)(\s*)(-?%\})/ do
          groups Name::Tag, Text::Whitespace, Punctuation
          push :raw
        end

        # end of block
        rule %r/(end(?:if|unless|case))(\s*)(-?%\})/ do
          groups Keyword::Reserved, Text::Whitespace, Punctuation
          pop!
        end

        rule %r/(end(?:[^\s%]+))(\s*)(-?%\})/ do
          groups Name::Tag, Text::Whitespace, Punctuation
          pop!
        end

        # builtin tags
        rule %r/(assign|echo)\b/, Name::Tag, :assign
        rule %r/(include|render)\b/, Name::Tag, :include

        rule %r/(cycle)(\s+)(?:([^\s:]*)(\s*)(:))?(\s*)/ do |m|
          token_class = case m[3]
                        when %r/'[^']*'/ then Str::Single
                        when %r/"[^"]*"/ then Str::Double
                        else
                          Name::Attribute
                        end

          groups Name::Tag, Text::Whitespace, token_class,
                 Text::Whitespace, Punctuation, Text::Whitespace

          push :variable_tag_markup
        end

        # iteration
        rule %r/
          (for|tablerow)(\s+)
          ([\w-]+)(\s+)
          (in)(\s+)
          (
            (?: [^\s%,\|'"] | (?:"[^"]*"|'[^']*') )+
          )(\s*)
        /x do |m|
          groups Name::Tag, Text::Whitespace, Name::Variable, Text::Whitespace,
                 Name::Tag, Text::Whitespace

          token_class = case m[7]
                        when %r/'[^']*'/ then Str::Single
                        when %r/"[^"]*"/ then Str::Double
                        else
                          Name::Variable
                        end
          token token_class, m[7]
          token Text::Whitespace, m[8]
          push :tag_markup
        end

        # other tags or blocks
        rule %r/([^\s%]+)(\s*)/ do
          groups Name::Tag, Text::Whitespace
          push :tag_markup
        end
      end

      state :output do
        rule %r/(\|)(\s*)([a-zA-Z_][^\s}\|:]*)/ do
          groups Punctuation, Text::Whitespace, Name::Function
          push :filters
        end

        mixin :end_of_tag
        mixin :generic
      end

      state :filters do
        rule %r/(\|)(\s*)([a-zA-Z_][^\s%}\|:]*)/ do
          groups Punctuation, Text::Whitespace, Name::Function
        end

        mixin :end_of_tag
        mixin :end_of_block
        mixin :variable_param_markup
      end

      state :condition do
        rule %r/([=!]=|[<>]=?)/, Operator
        rule %r/(and|or|contains)\b/, Operator::Word

        mixin :end_of_block
        mixin :generic
      end

      state :when do
        mixin :end_of_block
        mixin :generic
      end

      state :end_of_tag do
        rule(/-?\}\}/) { token Punctuation; reset_stack }
      end

      state :end_of_block do
        rule(/-?%\}/) { token Punctuation; reset_stack }
      end

      # states for unknown markup
      state :param_markup do
        mixin :whitespace
        mixin :keyword
        mixin :string
        mixin :number

        rule %r/([^\s=:]+)(\s*)(=|:)/ do
          groups Name::Attribute, Text::Whitespace, Operator
        end

        rule %r/[,:]/, Punctuation
      end

      state :default_param_markup do
        mixin :param_markup

        rule %r/\S+/, Text
      end

      state :variable_param_markup do
        mixin :param_markup
        mixin :variable

        rule %r/\S+/, Text
      end

      state :tag_markup do
        rule %r/(reversed)\b/, Name::Attribute

        mixin :end_of_block
        mixin :default_param_markup
      end

      state :variable_tag_markup do
        mixin :end_of_block
        mixin :variable_param_markup
      end

      # states for different values types
      state :keyword do
        rule %r/(false|true|nil)\b/, Keyword::Constant
      end

      state :variable do
        rule %r/(empty|blank|forloop\.[^\s%}\|:]+)\b/, Name::Builtin
        rule %r/\.(?=\w)|\[|\]/, Punctuation
        rule %r/(first|last|size)\b/, Name::Function
        rule %r/[a-zA-Z_][\w-]*\??/, Name::Variable
      end

      state :string do
        rule %r/'[^']*'/, Str::Single
        rule %r/"[^"]*"/, Str::Double
      end

      state :number do
        rule %r/-/, Operator
        rule %r/\d+\.\d+/, Num::Float
        rule %r/\d+/, Num::Integer
      end

      state :generic do
        mixin :whitespace
        mixin :keyword
        mixin :string
        mixin :number
        mixin :variable
      end

      state :whitespace do
        rule %r/[ \t]+/, Text::Whitespace
      end

      state :comment do
        rule %r/[^\{]+/, Comment

        rule %r/(\{%-?)(\s*)(endcomment)(\s*)(-?%\})/ do
          groups Punctuation, Text::Whitespace, Name::Tag, Text::Whitespace, Punctuation
          reset_stack
        end

        rule %r/\{/, Comment
      end

      state :raw do
        rule %r/[^\{]+/, Text

        rule %r/(\{%-?)(\s*)(endraw)(\s*)(-?%\})/ do
          groups Punctuation, Text::Whitespace, Name::Tag, Text::Whitespace, Punctuation
          reset_stack
        end

        rule %r/\{/, Text
      end

      state :assign do
        rule %r/=/, Operator

        rule %r/(\|)(\s*)([a-zA-Z_][^\s%\|:]*)/ do
          groups Punctuation, Text::Whitespace, Name::Function
          push :filters
        end

        mixin :end_of_block
        mixin :generic
      end

      state :include do
        rule %r/(\{\{-?)(\s*)/ do
          groups Punctuation, Text::Whitespace
          push :output_embed
        end

        rule %r/(with|for)\b/, Name::Tag
        rule %r/[\/\w-]+(\.[\w-]+)+\b/, Text

        mixin :variable_tag_markup
      end

      state :output_embed do
        rule %r/(\|)(\s*)([a-zA-Z_][^\s}\|:]*)/ do
          groups Punctuation, Text::Whitespace, Name::Function
        end

        rule %r/-?\}\}/, Punctuation, :pop!

        mixin :variable_param_markup
      end
    end
  end
end
