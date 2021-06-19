#--
# BibTeX-Ruby
# Copyright (C) 2010-2015 Sylvester Keil <http://sylvester.keil.or.at>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#++

require 'strscan'

module BibTeX
  #
  # The BibTeX::Lexer handles the lexical analysis of BibTeX bibliographies.
  #
  class Lexer
    extend Forwardable

    attr_reader :options, :stack, :mode, :scanner
    attr_writer :mode

    def_delegator :@scanner, :string, :data

    @defaults = {
      include: [:errors],
      strict: true,
      allow_missing_keys: false,
      strip: true
    }

    # Patterns Cache (#37: MacRuby does not cache regular expressions)
    @patterns = {
      space: /[\s]+/o,
      lbrace: /\s*\{/o,
      rbrace: /\s*\}\s*/o,
      braces: /\{|\}/o,
      eq: /\s*=\s*/o,
      comma: /\s*,\s*/o,
      number: /[[:digit:]]+/o,
      name: %r{[[:alpha:][:digit:]/:_!$\?\.%+&\*-]+}io,
      quote: /\s*"/o,
      unquote: /[\{\}"]/o,
      sharp: /\s*#\s*/o,
      object: /@/o,
      period: /./o,
      strict_next: /@[\t ]*/o,
      next: /(^|\n)[\t ]*@[\t ]*/o,
      entry: /[a-z\d:_!\.$%&*-]+/io,
      string: /string/io,
      comment: /comment\b/io,
      preamble: /preamble\b/io,
      key: %r{\s*[[:alpha:][:digit:] /:_!$\?\.%+;&\*'"-]+,}io,
      optional_key: %r{\s*[[:alpha:][:digit:] /:_!$\?\.%+;&\*'"-]*,}io
    }

    MODE = Hash.new(:meta).merge(
      bibtex: :bibtex, entry: :bibtex,
      string: :bibtex, preamble: :bibtex,
      comment: :bibtex,  meta: :meta,
      literal: :literal, content: :content
    ).freeze

    class << self
      attr_reader :defaults, :patterns
    end

    #
    # Creates a new instance. Possible options and their respective
    # default values are:
    #
    # - :include => [:errors] A list that may contain :meta_content, and
    #   :errors; depending on whether or not these are present, the respective
    #   tokens are included in the parse tree.
    # - :strict => true In strict mode objects can start anywhere; therefore
    #   the `@' symbol is not possible except inside literals or @comment
    #   objects; for a more lenient lexer set to false and objects are
    #   expected to start after a new line (leading white space is permitted).
    # - :strip => true When enabled, newlines will be stripped from quoted
    #   string values.
    #
    def initialize(options = {})
      @options = Lexer.defaults.merge(options)
      reset
    end

    def reset
      @stack = []
      @brace_level = 0
      @mode = :meta
      @active_object = nil

      # cache options for speed
      @include_meta_content = @options[:include].include?(:meta_content)
      @include_errors = @options[:include].include?(:errors)

      self
    end

    # Sets the source for the lexical analysis and resets the internal state.
    def data=(data)
      @scanner = StringScanner.new(data)
      reset
    end

    def symbols
      @stack.map(&:first)
    end

    # Returns the next token from the parse stack.
    def next_token
      @stack.shift
    end

    # Returns true if the lexer is currenty parsing a BibTeX object.
    def bibtex_mode?
      MODE[@mode] == :bibtex
    end

    %i[meta literal content].each do |m|
      define_method("#{m}_mode?") { @mode == m }
    end

    # Returns true if the lexer is currently parsing the given object type.
    def active?(object)
      @active_object == object
    end

    # Returns true if the lexer is currently in strict mode.
    def strict?
      !!@options[:strict]
    end

    def allow_missing_keys?
      !!@options[:allow_missing_keys]
    end

    def strip_line_breaks?
      !!options[:strip] && !active?(:comment)
    end

    # Pushes a value onto the parse stack. Returns the Lexer.
    def push(value)
      case value[0]
      when :CONTENT, :STRING_LITERAL
        value[1].gsub!(/\n\s*/, ' ') if strip_line_breaks?

        if !@stack.empty? && value[0] == @stack[-1][0]
          @stack[-1][1] << value[1]
        else
          @stack.push(value)
        end
      when :ERROR
        @stack.push(value) if @include_errors
        leave_object
      when :META_CONTENT
        @stack.push(value) if @include_meta_content
      else
        @stack.push(value)
      end

      self
    end

    # Start the lexical analysis.
    def analyse(string = nil)
      raise(ArgumentError, 'Lexer: failed to start analysis: no source given!') unless
        string || @scanner

      self.data = string || @scanner.string

      send("parse_#{MODE[@mode]}") until @scanner.eos?

      push([false, '$end'])
    end

    private

    def parse_bibtex
      case
      when @scanner.scan(Lexer.patterns[:lbrace])
        @brace_level += 1
        push([:LBRACE, '{'])
        @mode = :content if @brace_level > 1 || @brace_level == 1 && active?(:comment)
      when @scanner.scan(Lexer.patterns[:rbrace])
        @brace_level -= 1
        push([:RBRACE, '}'])
        return leave_object if @brace_level == 0
        return error_unbalanced_braces if @brace_level < 0
      when @scanner.scan(Lexer.patterns[:eq])
        push([:EQ, '='])
      when @scanner.scan(Lexer.patterns[:comma])
        push([:COMMA, ','])
      when @scanner.scan(Lexer.patterns[:number])
        push([:NUMBER, @scanner.matched])
      when @scanner.scan(Lexer.patterns[:name])
        push([:NAME, @scanner.matched.rstrip])
      when @scanner.scan(Lexer.patterns[:quote])
        @mode = :literal
      when @scanner.scan(Lexer.patterns[:sharp])
        push([:SHARP, '#'])
      when @scanner.scan(Lexer.patterns[:object])
        enter_object
      when @scanner.scan(Lexer.patterns[:space])
        # skip
      when @scanner.scan(Lexer.patterns[:period])
        error_unexpected_token
      end
    end

    def parse_meta
      match = @scanner.scan_until(Lexer.patterns[strict? ? :strict_next : :next])
      if @scanner.matched
        push([:META_CONTENT, match.chop])
        enter_object
      else
        push([:META_CONTENT, @scanner.rest])
        @scanner.terminate
      end
    end

    def parse_content
      match = @scanner.scan_until(Lexer.patterns[:braces])
      case @scanner.matched
      when '{'
        @brace_level += 1
        push([:CONTENT, match])
      when '}'
        @brace_level -= 1
        if @brace_level == 0
          push([:CONTENT, match.chop])
          push([:RBRACE, '}'])
          leave_object
        elsif @brace_level == 1 && !active?(:comment)
          push([:CONTENT, match.chop])
          push([:RBRACE, '}'])
          @mode = :bibtex
        elsif @brace_level < 0
          push([:CONTENT, match.chop])
          error_unbalanced_braces
        else
          push([:CONTENT, match])
        end
      else
        push([:CONTENT, @scanner.rest])
        @scanner.terminate
        error_unterminated_content
      end
    end

    def parse_literal
      match = @scanner.scan_until(Lexer.patterns[:unquote])
      case @scanner.matched
      when '{'
        @brace_level += 1
        push([:STRING_LITERAL, match])
      when '}'
        @brace_level -= 1
        if @brace_level < 1
          push([:STRING_LITERAL, match.chop])
          error_unbalanced_braces
        else
          push([:STRING_LITERAL, match])
        end
      when '"'
        if @brace_level == 1
          push([:STRING_LITERAL, match.chop])
          @mode = :bibtex
        else
          push([:STRING_LITERAL, match])
        end
      else
        push([:STRING_LITERAL, @scanner.rest])
        @scanner.terminate
        error_unterminated_string
      end
    end

    # Called when the lexer encounters a new BibTeX object.
    def enter_object
      @brace_level = 0
      push [:AT, '@']

      if @scanner.scan(Lexer.patterns[:string])
        @mode = @active_object = :string
        push [:STRING, @scanner.matched]
      elsif @scanner.scan(Lexer.patterns[:preamble])
        @mode = @active_object = :preamble
        push [:PREAMBLE, @scanner.matched]
      elsif @scanner.scan(Lexer.patterns[:comment])
        @mode = @active_object = :comment
        push [:COMMENT, @scanner.matched]
      elsif @scanner.scan(Lexer.patterns[:entry])
        @mode = @active_object = :entry
        push [:NAME, @scanner.matched]

        # TODO: DRY - try to parse key
        if @scanner.scan(Lexer.patterns[:lbrace])
          @brace_level += 1
          push([:LBRACE, '{'])
          @mode = :content if @brace_level > 1 || @brace_level == 1 && active?(:comment)

          push [:KEY, @scanner.matched.chop.strip] if @scanner.scan(Lexer.patterns[allow_missing_keys? ? :optional_key : :key])
        end

      else
        error_unexpected_object
      end
    end

    # Called when parser leaves a BibTeX object.
    def leave_object
      @mode = :meta
      @active_object = nil
      @brace_level = 0
    end

    def error_unbalanced_braces
      BibTeX.log.warn("Lexer: unbalanced braces at #{@scanner.pos}; brace level #{@brace_level}; mode #{@mode.inspect}.")
      backtrace [:E_UNBALANCED, @scanner.matched]
    end

    def error_unterminated_string
      BibTeX.log.warn("Lexer: unterminated string at #{@scanner.pos}; brace level #{@brace_level}; mode #{@mode.inspect}.")
      backtrace [:E_UNTERMINATED_STRING, @scanner.matched]
    end

    def error_unterminated_content
      BibTeX.log.warn("Lexer: unterminated content at #{@scanner.pos}; brace level #{@brace_level}; mode #{@mode.inspect}.")
      backtrace [:E_UNTERMINATED_CONTENT, @scanner.matched]
    end

    def error_unexpected_token
      BibTeX.log.warn("Lexer: unexpected token `#{@scanner.matched}' at #{@scanner.pos}; brace level #{@brace_level}; mode #{@mode.inspect}.")
      backtrace [:E_UNEXPECTED_TOKEN, @scanner.matched]
    end

    def error_unexpected_object
      BibTeX.log.warn("Lexer: unexpected object at #{@scanner.pos}; brace level #{@brace_level}; mode #{@mode.inspect}.")
      backtrace [:E_UNEXPECTED_OBJECT, '@']
    end

    def backtrace(error)
      bt = []
      bt.unshift(@stack.pop) until @stack.empty? || (!bt.empty? && %i[AT META_CONTENT].include?(bt[0][0]))
      bt << error
      push [:ERROR, bt]
    end
  end
end
