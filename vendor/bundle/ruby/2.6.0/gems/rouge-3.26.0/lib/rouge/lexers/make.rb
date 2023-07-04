# -*- coding: utf-8 -*- #
# frozen_string_literal: true

module Rouge
  module Lexers
    class Make < RegexLexer
      title "Make"
      desc "Makefile syntax"
      tag 'make'
      aliases 'makefile', 'mf', 'gnumake', 'bsdmake'
      filenames '*.make', '*.mak', '*.mk', 'Makefile', 'makefile', 'Makefile.*', 'GNUmakefile', '*,fe1'
      mimetypes 'text/x-makefile'

      def self.functions
        @functions ||= %w(
          abspath addprefix addsuffix and basename call dir error eval file
          filter filter-out findstring firstword flavor foreach if join lastword
          notdir or origin patsubst realpath shell sort strip subst suffix value
          warning wildcard word wordlist words
        )
      end

      # TODO: Add support for special keywords
      # bsd_special = %w(
      #   include undef error warning if else elif endif for endfor
      # )

      def initialize(opts={})
        super
        @shell = Shell.new(opts)
      end

      start { @shell.reset! }

      state :root do
        rule %r/\s+/, Text

        rule %r/#.*?\n/, Comment

        rule %r/([-s]?include)((?:[\t ]+[^\t\n #]+)+)/ do
          groups Keyword, Literal::String::Other
        end

        rule %r/(ifn?def|ifn?eq)([\t ]+)([^#\n]+)/ do
          groups Keyword, Text, Name::Variable
        end

        rule %r/(?:else|endif)[\t ]*(?=[#\n])/, Keyword

        rule %r/(export)([\t ]+)(?=[\w\${}()\t -]+\n)/ do
          groups Keyword, Text
          push :export
        end

        rule %r/export[\t ]+/, Keyword

        # assignment
        rule %r/([\w${}().-]+)([\t ]*)([!?:+]?=)/m do |m|
          token Name::Variable, m[1]
          token Text, m[2]
          token Operator, m[3]
          push :shell_line
        end

        rule %r/"(\\\\|\\.|[^"\\])*"/, Str::Double
        rule %r/'(\\\\|\\.|[^'\\])*'/, Str::Single
        rule %r/([^\n:]+)(:+)([ \t]*)/ do
          groups Name::Label, Operator, Text
          push :block_header
        end
      end

      state :export do
        rule %r/[\w\${}()-]/, Name::Variable
        rule %r/\n/, Text, :pop!
        rule %r/[\t ]+/, Text
      end

      state :block_header do
        rule %r/[^,\\\n#]+/, Name::Function
        rule %r/,/, Punctuation
        rule %r/#.*?/, Comment
        rule %r/\\\n/, Text
        rule %r/\\./, Text
        rule %r/\n/ do
          token Text
          goto :block_body
        end
      end

      state :block_body do
        rule %r/(ifn?def|ifn?eq)([\t ]+)([^#\n]+)(#.*)?(\n)/ do
          groups Keyword, Text, Name::Variable, Comment, Text
        end

        rule %r/(else|endif)([\t ]*)(#.*)?(\n)/ do
          groups Keyword, Text, Comment, Text
        end

        rule %r/(\t[\t ]*)([@-]?)/ do
          groups Text, Punctuation
          push :shell_line
        end

        rule(//) { @shell.reset!; pop! }
      end

      state :shell do
        # macro interpolation
        rule %r/\$[({][\t ]*\w[\w:=%.]*[\t ]*[)}]/i, Name::Variable
        # function invocation
        rule %r/(\$[({])([\t ]*)(#{Make.functions.join('|')})([\t ]+)/m do
          groups Name::Function, Text, Name::Builtin, Text
          push :shell_expr
        end

        rule(/\\./m) { delegate @shell }
        stop = /\$\(|\$\{|\(|\)|\}|\\|$/
        rule(/.+?(?=#{stop})/m) { delegate @shell }
        rule(stop) { delegate @shell }
      end

      state :shell_expr do
        rule(/[({]/) { delegate @shell; push }
        rule %r/[)}]/, Name::Function, :pop!
        mixin :shell
      end

      state :shell_line do
        rule %r/\n/, Text, :pop!
        mixin :shell
      end
    end
  end
end
