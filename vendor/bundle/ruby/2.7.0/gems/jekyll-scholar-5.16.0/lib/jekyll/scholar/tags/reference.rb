module Jekyll
  class Scholar

    class ReferenceTag < Liquid::Tag
      include Scholar::Utilities

      def initialize(tag_name, arguments, tokens)
        super

        @config = Scholar.defaults.dup
        @keys, arguments = split_arguments arguments

        optparse(arguments)
      end

      def render(context)
        set_context_to context
        keys.map { |key|
          reference_tag bibliography[key]
        }.join("\n")
      end
    end

  end
end

Liquid::Template.register_tag('reference', Jekyll::Scholar::ReferenceTag)
