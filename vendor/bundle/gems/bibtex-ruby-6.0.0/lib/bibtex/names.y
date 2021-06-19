#--
# BibTeX-Ruby
# Copyright (C) 2010-2011  Sylvester Keil <http://sylvester.keil.or.at>
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
#
# A BibTeX Names grammar for the parser generator +racc+
#

# -*- racc -*-

class BibTeX::NameParser

token COMMA UWORD LWORD PWORD ANDFL ANDLF ERROR

expect 0

rule

  result : { result = [] } | names

  names : name       { result = [val[0]] }
        | names name { result << val[1] }

  name : ANDFL flname { result = Name.new(val[1]) }
       | ANDLF lfname { result = Name.new(val[1]) }

  flname : word
         {
           result = { :last => val[0] }
         }
         | u_words word
         {
           result = { :first => val[0].join(' '), :last => val[1] }
         }
         | u_words von last
         {
           result = { :first => val[0].join(' '), :von => val[1], :last => val[2] }
         }
         | von last
         {
           result = { :von => val[0], :last => val[1] }
         }
         | comma

  lfname : lastfirst
         {
           result = { :last => val[0][0], :first => val[0][1] }
         }
         | von lastfirst
         {
           result = { :von => val[0], :last => val[1][0], :first => val[1][1] }
         }
         | u_words von lastfirst
         {
           result = { :von => val[0..1].join(' '), :last => val[2][0], :first => val[2][1] }
         }
         | comma

  comma : last COMMA first
        {
          result = { :last => val[0], :jr => val[2][0], :first => val[2][1] }
        }
        | von last COMMA first
        {
          result = { :von => val[0], :last => val[1], :jr => val[3][0], :first => val[3][1] }
        }
        | u_words von last COMMA first
        {
          result = { :von => val[0..1].join(' '), :last => val[2], :jr => val[4][0], :first => val[4][1] }
        }

  von : LWORD
      | von LWORD         { result = val.join(' ') }
      | von u_words LWORD { result = val.join(' ') }

  lastfirst : LWORD         { result = [val[0], nil] }
            | u_words       { result = [val[0][0], val[0][1] ? val[0][1..-1].join(' ') : nil] }
            | u_words LWORD { result = [val[0][0], (val[0][1..-1] << val[1]).join(' ')] }

  last : LWORD | u_words { result = val[0].join(' ') }

  first : opt_words                 { result = [nil,val[0]] }
        | opt_words COMMA opt_words { result = [val[0],val[2]] }

  u_words : u_word         { result = [val[0]] }
          | u_words u_word { result << val[1] }

  u_word : UWORD | PWORD

  words : word
        | words word { result = val.join(' ') }

  opt_words : /* empty */ | words

  word : LWORD | UWORD | PWORD

end

---- header
require 'strscan'

---- inner

  @patterns = {
    :and => /,?\s+and\s+/io,
    :space => /\s+/o,
    :comma => /,/o,
    :lower => /[[:lower:]][[:lower:][:upper:]]*/uo,
    :upper => /[[:upper:]][[:lower:][:upper:].]*/uo,
    :other => /[^\s,\{\}\\[:upper:][:lower:]]+/uo,
    :lbrace => /\{/o,
    :rbrace => /\}/o,
    :braces => /[\{\}]/o,
    :escape => /\\./o,
    :last_first => /[\p{Han}\p{Hiragana}\p{Katakana}\p{Hangul}]/uo
  }

  class << self
    attr_reader :patterns
  end

  def initialize(options = {})
    self.options.merge!(options)
  end

  def options
    @options ||= { :debug => ENV['DEBUG'] == true }
  end

  def parse(input)
    @yydebug = options[:debug]
    scan(input)
    do_parse
  end

  def next_token
    @stack.shift
  end

  def on_error(tid, val, vstack)
    BibTeX.log.debug("Failed to parse BibTeX Name on value %s (%s) %s" % [val.inspect, token_to_str(tid) || '?', vstack.inspect])
  end

  def scan(input)
    @src = StringScanner.new(input)
    @brace_level = 0
    @last_and = 0
    @stack = [[:ANDFL,'(^start)']]
    @word = [:PWORD,'']
    do_scan
  end

  private

  def do_scan
    until @src.eos?
      case
      when @src.scan(NameParser.patterns[:and])
        push_word
        @last_and = @stack.length
        @stack.push([:ANDFL,@src.matched])

      when @src.skip(NameParser.patterns[:space])
        push_word

      when @src.scan(NameParser.patterns[:comma])
        push_word
        @stack.push([:COMMA,@src.matched])

      when @src.scan(NameParser.patterns[:lower])
        is_lowercase
        @word[1] << @src.matched

      when @src.scan(NameParser.patterns[:upper])
        is_uppercase
        @word[1] << @src.matched

      when @src.scan(NameParser.patterns[:other])
        check_name_order
        @word[1] << @src.matched

      when @src.scan(NameParser.patterns[:lbrace])
        @word[1] << @src.matched
        scan_literal

      when @src.scan(NameParser.patterns[:rbrace])
        error_unbalanced

      when @src.scan(NameParser.patterns[:escape])
        @word[1] << @src.matched

      else
        error_invalid
      end
    end

    push_word
    @stack
  end

  def push_word
    unless @word[1].empty?
      @stack.push(@word)
      @word = [:PWORD,'']
    end
  end

  def is_lowercase
    @word[0] = :LWORD if @word[0] == :PWORD
  end

  def is_uppercase
    @word[0] = :UWORD if @word[0] == :PWORD
  end

  def check_name_order
    return if RUBY_VERSION < '1.9'
    @stack[@last_and][0] = :ANDLF if @stack[@last_and][0] != :ANDLF && @src.matched =~ NameParser.patterns[:last_first]
  end

  def scan_literal
    @brace_level = 1

    while @brace_level > 0
      @word[1] << @src.scan_until(NameParser.patterns[:braces]).to_s

      case @src.matched
      when '{'
        @brace_level += 1
      when '}'
        @brace_level -= 1
      else
        @brace_level = 0
        error_unbalanced
      end
    end
  end

  def error_unexpected
    @stack.push [:ERROR,@src.matched]
    BibTeX.log.warn("NameParser: unexpected token `#{@src.matched}' at position #{@src.pos}; brace level #{@brace_level}.")
  end

  def error_unbalanced
    @stack.push [:ERROR,'}']
    BibTeX.log.warn("NameParser: unbalanced braces at position #{@src.pos}; brace level #{@brace_level}.")
  end

  def error_invalid
    @stack.push [:ERROR,@src.getch]
    BibTeX.log.warn("NameParser: invalid character at position #{@src.pos}; brace level #{@brace_level}.")
  end

# -*- racc -*-
