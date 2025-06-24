# -*- coding: utf-8 -*- #

module Rouge
  module Lexers
    class Solidity < RegexLexer
      title "Solidity"
      desc "Solidity, an Ethereum smart contract programming language"
      tag 'solidity'
      filenames '*.sol', '*.solidity'
      mimetypes 'text/x-solidity'

      # optional comment or whitespace
      ws = %r((?:\s|//.*?\n|/[*].*?[*]/)+)
      id = /[a-zA-Z$_][\w$_]*/

      def self.detect?(text)
        return true if text.start_with? 'pragma solidity'
      end

      # TODO: seperate by "type"
      def self.keywords
        @keywords ||= Set.new %w(
          abstract anonymous as assembly break catch calldata constant
          constructor continue contract do delete else emit enum event
          external fallback for function hex if indexed interface
          internal import is library mapping memory modifier new
          override payable public pure pragma private receive return
          returns storage struct throw try type using var view virtual
          while
        )
      end

      def self.builtins
        return @builtins if @builtins

        @builtins = Set.new %w(
          now
          false true
          balance now selector super this
          blockhash gasleft
          assert require revert
          selfdestruct suicide
          call callcode delegatecall
          send transfer
          addmod ecrecover keccak256 mulmod sha256 sha3 ripemd160
        )

        # TODO: use (currently shadowed by catch-all in :statements)
        abi = %w(decode encode encodePacked encodeWithSelector encodeWithSignature)
        @builtins.merge( abi.map { |i| "abi.#{i}" } )
        block = %w(coinbase difficulty gaslimit hash number timestamp)
        @builtins.merge( block.map { |i| "block.#{i}" } )
        msg = %w(data gas sender sig value)
        @builtins.merge( msg.map { |i| "msg.#{i}" } )
        tx = %w(gasprice origin)
        @builtins.merge( tx.map { |i| "tx.#{i}" } )
      end

      def self.constants
        @constants ||= Set.new %w(
          wei finney szabo ether
          seconds minutes hours days weeks years
        )
      end

      def self.keywords_type
        @keywords_type ||= Set.new %w(
          address bool byte bytes int string uint
        )
      end

      def self.reserved
        @reserved ||= Set.new %w(
          alias after apply auto case copyof default define final fixed
          immutable implements in inline let macro match mutable null of
          partial promise reference relocatable sealed sizeof static
          supports switch typedef typeof ufixed unchecked
        )
      end

      start { push :bol }

      state :expr_bol do
        mixin :inline_whitespace

        rule(//) { pop! }
      end

      # :expr_bol is the same as :bol but without labels, since
      # labels can only appear at the beginning of a statement.
      state :bol do
        mixin :expr_bol
      end

      # TODO: natspec in comments
      state :inline_whitespace do
        rule %r/[ \t\r]+/, Text
        rule %r/\\\n/, Text # line continuation
        rule %r(/\*), Comment::Multiline, :comment_multi
      end

      state :whitespace do
        rule %r/\n+/m, Text, :bol
        rule %r(//(\\.|.)*?\n), Comment::Single, :bol
        mixin :inline_whitespace
      end

      state :expr_whitespace do
        rule %r/\n+/m, Text, :expr_bol
        mixin :whitespace
      end

      state :statements do
        mixin :whitespace
        rule %r/(hex)?\"/, Str, :string_double
        rule %r/(hex)?\'/, Str, :string_single
        rule %r('(\\.|\\[0-7]{1,3}|\\x[a-f0-9]{1,2}|[^\\'\n])')i, Str::Char
        rule %r/\d\d*\.\d+([eE]\d+)?/i, Num::Float
        rule %r/0x[0-9a-f]+/i, Num::Hex
        rule %r/\d+([eE]\d+)?/i, Num::Integer
        rule %r(\*/), Error
        rule %r([~!%^&*+=\|?:<>/-]), Operator
        rule %r/[()\[\],.]/, Punctuation
        rule %r/u?fixed\d+x\d+/, Keyword::Reserved
        rule %r/bytes\d+/, Keyword::Type
        rule %r/u?int\d+/, Keyword::Type
        rule id do |m|
          name = m[0]

          if self.class.keywords.include? name
            token Keyword
          elsif self.class.builtins.include? name
            token Name::Builtin
          elsif self.class.constants.include? name
            token Keyword::Constant
          elsif self.class.keywords_type.include? name
            token Keyword::Type
          elsif self.class.reserved.include? name
            token Keyword::Reserved
          else
            token Name
          end
        end
      end

      state :root do
        mixin :expr_whitespace
        rule(//) { push :statement }
        # TODO: function declarations
      end

      state :statement do
        rule %r/;/, Punctuation, :pop!
        mixin :expr_whitespace
        mixin :statements
        rule %r/[{}]/, Punctuation
      end

      state :string_common do
        rule %r/\\(u[a-fA-F0-9]{4}|x..|[^x])/, Str::Escape
        rule %r/[^\\\"\'\n]+/, Str
        rule %r/\\\n/, Str # line continuation
        rule %r/\\/, Str # stray backslash
      end

      state :string_double do
        mixin :string_common
        rule %r/\"/, Str, :pop!
        rule %r/\'/, Str
      end

      state :string_single do
        mixin :string_common
        rule %r/\'/, Str, :pop!
        rule %r/\"/, Str
      end

       state :comment_multi do
         rule %r(\*/), Comment::Multiline, :pop!
         rule %r([^*/]+), Comment::Multiline
         rule %r([*/]), Comment::Multiline
       end
    end
  end
end
