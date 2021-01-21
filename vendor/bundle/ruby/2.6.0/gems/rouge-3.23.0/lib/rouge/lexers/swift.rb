# -*- coding: utf-8 -*- #
# frozen_string_literal: true

module Rouge
  module Lexers
    class Swift < RegexLexer
      tag 'swift'
      filenames '*.swift'

      title "Swift"
      desc 'Multi paradigm, compiled programming language developed by Apple for iOS and OS X development. (developer.apple.com/swift)'

      id_head = /_|(?!\p{Mc})\p{Alpha}|[^\u0000-\uFFFF]/
      id_rest = /[\p{Alnum}_]|[^\u0000-\uFFFF]/
      id = /#{id_head}#{id_rest}*/

      keywords = Set.new %w(
        break case continue default do else fallthrough if in for return switch where while try catch throw guard defer repeat

        as dynamicType is new super self Self Type __COLUMN__ __FILE__ __FUNCTION__ __LINE__

        associativity didSet get infix inout mutating none nonmutating operator override postfix precedence prefix set unowned weak willSet throws rethrows precedencegroup

        #available #colorLiteral #column #else #elseif #endif #error #file #fileLiteral #function #if #imageLiteral #line #selector #sourceLocation #warning
      )

      declarations = Set.new %w(
        class deinit enum convenience extension final func import init internal lazy let optional private protocol public required static struct subscript typealias var dynamic indirect associatedtype open fileprivate some
      )

      constants = Set.new %w(
        true false nil
      )

      start { push :bol }

      # beginning of line
      state :bol do
        rule %r/#.*/, Comment::Preproc

        mixin :inline_whitespace

        rule(//) { pop! }
      end

      state :inline_whitespace do
        rule %r/\s+/m, Text
        mixin :has_comments
      end

      state :whitespace do
        rule %r/\n+/m, Text, :bol
        rule %r(\/\/.*?$), Comment::Single, :bol
        mixin :inline_whitespace
      end

      state :has_comments do
        rule %r(/[*]), Comment::Multiline, :nested_comment
      end

      state :nested_comment do
        mixin :has_comments
        rule %r([*]/), Comment::Multiline, :pop!
        rule %r([^*/]+)m, Comment::Multiline
        rule %r/./, Comment::Multiline
      end

      state :root do
        mixin :whitespace
        
        rule %r/\$(([1-9]\d*)?\d)/, Name::Variable

        rule %r{[()\[\]{}:;,?\\]}, Punctuation
        rule %r([-/=+*%<>!&|^.~]+), Operator
        rule %r/@?"/, Str, :dq
        rule %r/'(\\.|.)'/, Str::Char
        rule %r/(\d+(?:_\d+)*\*|(?:\d+(?:_\d+)*)*\.\d+(?:_\d)*)(e[+-]?\d+(?:_\d)*)?/i, Num::Float
        rule %r/\d+e[+-]?[0-9]+/i, Num::Float
        rule %r/0o?[0-7]+(?:_[0-7]+)*/, Num::Oct
        rule %r/0x[0-9A-Fa-f]+(?:_[0-9A-Fa-f]+)*((\.[0-9A-F]+(?:_[0-9A-F]+)*)?p[+-]?\d+)?/, Num::Hex
        rule %r/0b[01]+(?:_[01]+)*/, Num::Bin
        rule %r{[\d]+(?:_\d+)*}, Num::Integer

        rule %r/@#{id}/, Keyword::Declaration

        rule %r/(private|internal)(\([ ]*)(\w+)([ ]*\))/ do |m|
          if m[3] == 'set'
            token Keyword::Declaration
          else
            groups Keyword::Declaration, Keyword::Declaration, Error, Keyword::Declaration
          end
        end

        rule %r/(unowned\([ ]*)(\w+)([ ]*\))/ do |m|
          if m[2] == 'safe' || m[2] == 'unsafe'
            token Keyword::Declaration
          else
            groups Keyword::Declaration, Error, Keyword::Declaration
          end
        end

        rule %r/#available\([^)]+\)/, Keyword::Declaration

        rule %r/(#(?:selector|keyPath)\()([^)]+?(?:[(].*?[)])?)(\))/ do
          groups Keyword::Declaration, Name::Function, Keyword::Declaration
        end

        rule %r/#(line|file|column|function|dsohandle)/, Keyword::Declaration

        rule %r/(let|var)\b(\s*)(#{id})/ do
          groups Keyword, Text, Name::Variable
        end

        rule %r/(let|var)\b(\s*)([(])/ do
          groups Keyword, Text, Punctuation
          push :tuple
        end

        rule %r/(?!\b(if|while|for|private|internal|unowned|switch|case)\b)\b#{id}(?=(\?|!)?\s*[(])/ do |m|
          if m[0] =~ /^[[:upper:]]/
            token Keyword::Type
          else
            token Name::Function
          end
        end

        rule %r/as[?!]?(?=\s)/, Keyword
        rule %r/try[!]?(?=\s)/, Keyword

        rule %r/(#?(?!default)(?![[:upper:]])#{id})(\s*)(:)/ do
          groups Name::Variable, Text, Punctuation
        end

        rule id do |m|
          if keywords.include? m[0]
            token Keyword
          elsif declarations.include? m[0]
            token Keyword::Declaration
          elsif constants.include? m[0]
            token Keyword::Constant
          elsif m[0] =~ /^[[:upper:]]/
            token Keyword::Type
          else
            token Name
          end
        end

        rule %r/(`)(#{id})(`)/ do
          groups Punctuation, Name::Variable, Punctuation
        end
      end

      state :tuple do
        rule %r/(#{id})/, Name::Variable
        rule %r/(`)(#{id})(`)/ do
            groups Punctuation, Name::Variable, Punctuation
        end
        rule %r/,/, Punctuation
        rule %r/[(]/, Punctuation, :push
        rule %r/[)]/, Punctuation, :pop!
        mixin :inline_whitespace
      end

      state :dq do
        rule %r/\\[\\0tnr'"]/, Str::Escape
        rule %r/\\[(]/, Str::Escape, :interp
        rule %r/\\u\{\h{1,8}\}/, Str::Escape
        rule %r/[^\\"]+/, Str
        rule %r/"""/, Str, :pop!
        rule %r/"/, Str, :pop!
      end

      state :interp do
        rule %r/[(]/, Punctuation, :interp_inner
        rule %r/[)]/, Str::Escape, :pop!
        mixin :root
      end

      state :interp_inner do
        rule %r/[(]/, Punctuation, :push
        rule %r/[)]/, Punctuation, :pop!
        mixin :root
      end
    end
  end
end
