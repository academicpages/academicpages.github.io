module Jekyll
  class Scholar
    class Textregistered < BibTeX::Filter
      def apply(value)
        # Use of \g<1> pattern back-reference to allow for capturing nested {} groups.
        # The first (outermost) capture of $1 is used.
        value.to_s.gsub(/\\textregistered/) {
          "&#0174"
        }
      end
    end
  end
end
