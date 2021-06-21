# -*- coding: utf-8 -*-

module LaTeX
  module Decode

    class Decoder
      class << self
        attr_reader :patterns, :map

        def inherited(base)
          subclasses << base
        end

        def subclasses
          @subclasses ||= []
        end

        def decode(string)
          decode!(string.dup)
        end

        def decode!(string)
          patterns.each do |pattern|
            string.gsub!(pattern) { |m| [$2,map[$1],$3].compact.join }
          end
          string
        end
      end
    end

    module Base

      module_function

      def normalize(string)
        string.gsub!(/\\(?:i|j)\b/) { |m| m == '\\i' ? 'ı' : 'ȷ' }

        # \foo\ bar -> \foo{} bar
        string.gsub!(/(\\[a-zA-Z]+)\\(\s+)/, '\1{}\2')

        # Aaaa\o, -> Aaaa\o{},
        string.gsub!(/([^{]\\\w)([;,.:%])/, '\1{}\2')

        # \c cb -> \c{cb}
        string.gsub!(/(\\[^\sij&#\$\{\}_~%])\s+([[:alpha:]]+)\b/i, '\1{\2}')

        # non-breaking spaces
        string.gsub!(/(\A|[^\\])~/, LaTeX.to_unicode("\\1\u00a0"))

        string
      end

      def strip_braces(string)
        string.gsub!(/(^|[^\\])([\{\}]+)/, '\1')
        string.gsub!(/\\(\{|\})/, '\1')
        string
      end

    end

  end
end
