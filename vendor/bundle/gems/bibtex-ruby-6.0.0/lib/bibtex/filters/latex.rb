require 'latex/decode'

module BibTeX
  module Filters
    class LaTeX < Filter
      def apply(value)
        ::LaTeX.decode(value)
      end
    end
  end
end
