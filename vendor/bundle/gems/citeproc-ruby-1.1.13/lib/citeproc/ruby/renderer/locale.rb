module CiteProc
  module Ruby

    class Renderer

      def locale
        @locale ||= CSL::Locale.load
      end

      def locale=(locale)
        @locale = CSL::Locale.load(locale)
      end

      def translate(name, options = {})
        locale.translate(name, options)
      end

      # @return [String] number as an ordinal
      def ordinalize(number, options = {})
        locale.ordinalize(number, options)
      end

    end

  end
end
