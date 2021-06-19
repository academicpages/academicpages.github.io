# -*- coding: utf-8 -*-

module LaTeX
  module Decode
    
    class Diacritics < Decoder
      @macros = Hash[*%W{
        r \u030A
        H \u030B
        u \u0306
        v \u030C
        G \u030F
        M \u0322
        d \u0323
        c \u0327
        k \u0328
        b \u0331
        B \u0335
        t \u0361
      }.map { |s| LaTeX.to_unicode(s) }].freeze

      @map = @macros.merge(Hash[*%w{
        l  ł
        L  Ł
        o  ø
        O  Ø
        AA Å
        aa å
        AE Æ
        ae æ
      }]).freeze
      
      @patterns = [
        ruby_18 {
          /\\(#{ @macros.keys.map { |k| Regexp.escape(k) }.join('|') })\{([[:alpha:]]?)([[:alpha:]]*)\}/ou          
        } ||
        ruby_19 {
          /\\(#{ @macros.keys.map { |k| Regexp.escape(k) }.join('|') })\{(\p{L}\p{M}*)([[:alpha:]]*)\}/ou
        },
        /\\(o|O|l|L|aa|AA|ae|AE)\b/,
      ].freeze
      
    end
    
  end
end