module LaTeX
  module Decode

    class Maths < Decoder
      @patterns = [
        /\$([^\$]+)\$/
      ].freeze

      def self.decode!(string)
        patterns.each do |pattern|
          string.gsub!(pattern) do
            LaTeX.to_math_ml($1)
          end
        end
        string
      end

    end

  end
end
