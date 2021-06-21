module BibTeX
  module Filters

    class LineBreaks < Filter
      def apply(value)
        value.to_s.gsub(/\n\s*/, ' ')
      end
    end

  end
end
