module Jekyll
  class Scholar

    class DetailsLinkTag < Liquid::Tag
      include Scholar::Utilities

      def initialize(tag_name, arguments, tokens)
        super

        @config = Scholar.defaults.dup
        @keys, arguments = split_arguments arguments

        optparse(arguments)
      end

      def render(context)
        set_context_to context
        details_link keys[0]
      end
    end

  end
end

Liquid::Template.register_tag('details_link', Jekyll::Scholar::DetailsLinkTag)
