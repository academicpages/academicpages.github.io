# coding: utf-8
# frozen_string_literal: true

module Nokogiri
  class << self
    ###
    # Create a Nokogiri::XSLT::Stylesheet with +stylesheet+.
    #
    # Example:
    #
    #   xslt = Nokogiri::XSLT(File.read(ARGV[0]))
    #
    def XSLT(stylesheet, modules = {})
      XSLT.parse(stylesheet, modules)
    end
  end

  ###
  # See Nokogiri::XSLT::Stylesheet for creating and manipulating
  # Stylesheet object.
  module XSLT
    class << self
      ###
      # Parse the stylesheet in +string+, register any +modules+
      def parse(string, modules = {})
        modules.each do |url, klass|
          XSLT.register(url, klass)
        end

        doc = XML::Document.parse(string, nil, nil, XML::ParseOptions::DEFAULT_XSLT)
        if Nokogiri.jruby?
          Stylesheet.parse_stylesheet_doc(doc, string)
        else
          Stylesheet.parse_stylesheet_doc(doc)
        end
      end

      # :call-seq:
      #   quote_params(params) → Array
      #
      # Quote parameters in +params+ for stylesheet safety.
      # See Nokogiri::XSLT::Stylesheet.transform for example usage.
      #
      # [Parameters]
      # - +params+ (Hash, Array) XSLT parameters (key->value, or tuples of [key, value])
      #
      # [Returns] Array of string parameters, with quotes correctly escaped for use with XSLT::Stylesheet.transform
      #
      def quote_params(params)
        params.flatten.each_slice(2).each_with_object([]) do |kv, quoted_params|
          key, value = kv.map(&:to_s)
          value = if /'/.match?(value)
            "concat('#{value.gsub(/'/, %q{', "'", '})}')"
          else
            "'#{value}'"
          end
          quoted_params << key
          quoted_params << value
        end
      end
    end
  end
end

require_relative "xslt/stylesheet"
