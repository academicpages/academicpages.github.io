module Jekyll
  class Scholar

    class BibTeXTag < Liquid::Block
      include Scholar::Utilities

      def initialize(tag_name, arguments, tokens)
        super

        @config = Scholar.defaults.dup
        @keys, arguments = split_arguments arguments

        optparse(arguments)
      end

      def render(context)
        set_context_to context
        
        BibTeX.parse(super, bibtex_options).map { |entry|
          reference_tag entry

        }.join("\n")
      end
    end

  end
end

Liquid::Template.register_tag('bibtex', Jekyll::Scholar::BibTeXTag)

