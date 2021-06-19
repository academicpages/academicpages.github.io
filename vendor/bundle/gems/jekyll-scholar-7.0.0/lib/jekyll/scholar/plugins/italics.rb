module Jekyll
  class Scholar
    class Italics < BibTeX::Filter
      def apply(value)
        # Use of \g<1> pattern back-reference to allow for capturing nested {} groups.
        # The first (outermost) capture of $1 is used.
        value.to_s.gsub(/\\emph(\{(?:[^{}]|\g<1>)*\})/) {
          "<i>#{$1[1..-2]}</i>"
        }
      end
    end
  end
end
