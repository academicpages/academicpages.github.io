module Jekyll
  class Scholar

    class CiteTag < Liquid::Tag
      include Scholar::Utilities

      attr_reader :pages

      def initialize(tag_name, arguments, tokens)
        super

        @config = Scholar.defaults.dup
        @keys, arguments = split_arguments(arguments)

        optparse(arguments)
      end

      def render(context)
        set_context_to context
        cite keys
      end

    end

  end
end

Liquid::Template.register_tag('cite', Jekyll::Scholar::CiteTag)
