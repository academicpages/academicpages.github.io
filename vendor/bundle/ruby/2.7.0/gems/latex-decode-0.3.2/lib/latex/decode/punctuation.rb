# -*- coding: utf-8 -*-

module LaTeX
  module Decode

    class Punctuation < Decoder

      @macros = Hash[*%w{
        textendash         –
        textemdash         —
        textquoteleft      ‘
        textquoteright     ’
        quotesinglbase     ‚
        textquotedblleft   “
        textquotedblright  ”
        quotedblbase       „
        dag                †
        ddag               ‡
        textbullet         •
        dots               …
        textperthousand    ‰
        textpertenthousand ‱
        guilsinglleft      ‹
        guilsinglright     ›
        textreferencemark  ※
        textinterrobang    ‽
        textoverline       ‾
        langle             ⟨
        rangle             ⟩
        textasciicircum    ^
        textbackslash      \\
        textasciitilde     ~
        textquotesingle    '
      }].freeze

      @symbols = Hash[*%w[
        -     -
        --    –
        ---   —
        ``    “
        `     ‘
        ''    ”
        '     ’
      ]].freeze

      @map = @macros.merge(@symbols).freeze

      @patterns = [
        /\\(#{ @macros.keys.map { |k| Regexp.escape(k) }.compact.join('|') })(?:\{\}|\s+|\b|$)/ou,
        /(-+|`{1,2}|'{1,2})/,
        /()\\([$%;#_&])(\{\})?/,
        /()\\(~)\{\}/,
        /()\\( )/
      ].freeze

    end

  end
end
