module Jekyll
  class Scholar
    class Smallcaps < BibTeX::Filter
      def apply(value)
        # Use of \g<1> pattern back-reference to allow for capturing nested {} groups.
        # The first (outermost) capture of $1 is used.
        value.to_s.gsub(/\\textsc(\{(?:[^{}]|\g<1>)*\})/) {
          "<font style=\"font-variant: small-caps\">#{$1[1..-2]}</font>"
        }
      end
    end
  end
end
