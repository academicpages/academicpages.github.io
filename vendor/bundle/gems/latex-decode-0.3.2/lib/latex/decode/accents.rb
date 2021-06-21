# -*- coding: utf-8 -*-

module LaTeX
  module Decode
    
    class Accents < Decoder
      @map = Hash[*%W{
        `  \u0300
        '  \u0301
        ^  \u0302
        ~  \u0303
        =  \u0304
        .  \u0307
        '' \u0308
        "  \u0308  
      }.map { |s| LaTeX.to_unicode(s) }].freeze

      @patterns = [
        ruby_18 {
          /\\(#{ map.keys.map { |k| Regexp.escape(k) }.join('|') })\{([[:alpha:]]+)\}/ou
        } ||
        ruby_19 {
          /\\(#{ map.keys.map { |k| Regexp.escape(k) }.join('|') })\{(\p{L}\p{M}*)\}/ou
        },
        ruby_18 {
          /\\(#{ map.keys.map { |k| Regexp.escape(k) }.join('|') })([[:alpha:]])/ou          
        } ||
        ruby_19 {
          /\\(#{ map.keys.map { |k| Regexp.escape(k) }.join('|') })(\p{L}\p{M}*)/ou
        }
      ].freeze
      
    end

  end
end