module Jekyll
  class Scholar
    class Superscript < BibTeX::Filter
      def apply(value)
        # Use of \g<1> pattern back-reference to allow for capturing nested {} groups.
        # The first (outermost) capture of $1 is used.
        value.to_s.gsub(/\\textsuperscript(\{(?:[^{}]|\g<1>)*\})/) {
          "<sup>#{$1[1..-2]}</sup>"
        }
      end
    end
  end
end
