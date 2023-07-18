# frozen_string_literal: true

module Nokogiri
  module XML
    class Attr < Node
      alias_method :value, :content
      alias_method :to_s, :content
      alias_method :content=, :value=

      private

      def inspect_attributes
        [:name, :namespace, :value]
      end
    end
  end
end
