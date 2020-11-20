# -*- coding: utf-8 -*- #
# frozen_string_literal: true

module Rouge
  module Lexers
    class Rust < RegexLexer
      title "Rust"
      desc 'The Rust programming language (rust-lang.org)'
      tag 'rust'
      aliases 'rs',
        # So that directives from https://github.com/budziq/rust-skeptic
        # do not prevent highlighting.
        'rust,no_run', 'rs,no_run',
        'rust,ignore', 'rs,ignore',
        'rust,should_panic', 'rs,should_panic'
      filenames '*.rs'
      mimetypes 'text/x-rust'

      def self.detect?(text)
        return true if text.shebang? 'rustc'
      end

      def self.keywords
        @keywords ||= %w(
          as assert async await break const copy do drop else enum extern fail false
          fn for if impl let log loop match mod move mut priv pub pure
          ref return self static struct true trait type unsafe use where
          while box
        )
      end

      def self.builtins
        @builtins ||= Set.new %w(
          Add BitAnd BitOr BitXor bool c_char c_double c_float char
          c_int clock_t c_long c_longlong Cons Const Copy c_schar c_short
          c_uchar c_uint c_ulong c_ulonglong c_ushort c_void dev_t DIR
          dirent Div Either Eq Err f32 f64 Failure FILE float fpos_t
          i16 i32 i64 i8 isize Index ino_t int intptr_t Left mode_t Modulo Mul
          Neg Nil None Num off_t Ok Option Ord Owned pid_t Ptr ptrdiff_t
          Right Send Shl Shr size_t Some ssize_t str Sub Success time_t
          u16 u32 u64 u8 usize uint uintptr_t
          Box Vec String Gc Rc Arc
        )
      end

      def macro_closed?
        @macro_delims.values.all?(&:zero?)
      end

      start {
        @macro_delims = { ']' => 0, ')' => 0, '}' => 0 }
        push :bol
      }

      delim_map = { '[' => ']', '(' => ')', '{' => '}' }

      id = /[a-z_]\w*/i
      hex = /[0-9a-f]/i
      escapes = %r(
        \\ ([nrt'"\\0] | x#{hex}{2} | u#{hex}{4} | U#{hex}{8})
      )x
      size = /8|16|32|64/

      # Although not officially part of Rust, the rustdoc tool allows code in
      # comments to begin with `#`. Code like this will be evaluated but not
      # included in the HTML output produced by rustdoc. So that code intended
      # for these comments can be higlighted with Rouge, the  Rust lexer needs
      # to check if the beginning of the line begins with a `# `.
      state :bol do
        mixin :whitespace
        rule %r/#\s[^\n]*/, Comment::Special
        rule(//) { pop! }
      end

      state :attribute do
        mixin :whitespace
        mixin :has_literals
        rule %r/[(,)=:]/, Name::Decorator
        rule %r/\]/, Name::Decorator, :pop!
        rule id, Name::Decorator
      end

      state :whitespace do
        rule %r/\s+/, Text
        rule %r(//[^\n]*), Comment
        rule %r(/[*].*?[*]/)m, Comment::Multiline
      end

      state :root do
        rule %r/\n/, Text, :bol
        mixin :whitespace
        rule %r/#!?\[/, Name::Decorator, :attribute
        rule %r/\b(?:#{Rust.keywords.join('|')})\b/, Keyword
        mixin :has_literals

        rule %r([=-]>), Keyword
        rule %r(<->), Keyword
        rule %r/[()\[\]{}|,:;]/, Punctuation
        rule %r/[*\/!@~&+%^<>=\?-]|\.{2,3}/, Operator

        rule %r/([.]\s*)?#{id}(?=\s*[(])/m, Name::Function
        rule %r/[.]\s*#{id}/, Name::Property
        rule %r/[.]\s*\d+/, Name::Attribute
        rule %r/(#{id})(::)/m do
          groups Name::Namespace, Punctuation
        end

        # macros
        rule %r/\bmacro_rules!/, Name::Decorator, :macro_rules
        rule %r/#{id}!/, Name::Decorator, :macro

        rule %r/'#{id}/, Name::Variable
        rule %r/#{id}/ do |m|
          name = m[0]
          if self.class.builtins.include? name
            token Name::Builtin
          else
            token Name
          end
        end
      end

      state :macro do
        mixin :has_literals

        rule %r/[\[{(]/ do |m|
          @macro_delims[delim_map[m[0]]] += 1
          puts "    macro_delims: #{@macro_delims.inspect}" if @debug
          token Punctuation
        end

        rule %r/[\]})]/ do |m|
          @macro_delims[m[0]] -= 1
          puts "    macro_delims: #{@macro_delims.inspect}" if @debug
          pop! if macro_closed?
          token Punctuation
        end

        # same as the rule in root, but don't push another macro state
        rule %r/#{id}!/, Name::Decorator
        mixin :root

        # No syntax errors in macros
        rule %r/./, Text
      end

      state :macro_rules do
        rule %r/[$]#{id}(:#{id})?/, Name::Variable
        rule %r/[$]/, Name::Variable

        mixin :macro
      end

      state :has_literals do
        # constants
        rule %r/\b(?:true|false|nil)\b/, Keyword::Constant
        # characters
        rule %r(
          ' (?: #{escapes} | [^\\] ) '
        )x, Str::Char

        rule %r/"/, Str, :string
        rule %r/r(#*)".*?"\1/m, Str

        # numbers
        dot = /[.][0-9_]+/
        exp = /e[-+]?[0-9_]+/
        flt = /f32|f64/

        rule %r(
          [0-9_]+
          (#{dot}  #{exp}? #{flt}?
          |#{dot}? #{exp}  #{flt}?
          |#{dot}? #{exp}? #{flt}
          )
        )x, Num::Float

        rule %r(
          ( 0b[10_]+
          | 0x[0-9a-fA-F_]+
          | [0-9_]+
          ) (u#{size}?|i#{size})?
        )x, Num::Integer

      end

      state :string do
        rule %r/"/, Str, :pop!
        rule escapes, Str::Escape
        rule %r/[^"\\]+/m, Str
      end
    end
  end
end
