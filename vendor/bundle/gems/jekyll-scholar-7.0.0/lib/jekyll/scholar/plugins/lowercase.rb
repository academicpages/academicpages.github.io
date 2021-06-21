module Jekyll
  class Scholar
    class Lowercase < BibTeX::Filter
      def apply(value)
        # Use of \g<1> pattern back-reference to allow for capturing nested {} groups.
        # The first (outermost) capture of $1 is used.
        value.to_s.gsub(/\\lowercase(\{(?:[^{}]|\g<1>)*\})/) {
          "#{$1[1..-2].downcase}"
        }
      end
    end
  end
end
