module Jekyll
  class Scholar

    class BibliographyCountTag < Liquid::Tag
      include Scholar::Utilities

      def initialize(tag_name, arguments, tokens)
        super

        @config = Scholar.defaults.dup

        optparse(arguments)
      end

      def render(context)
        set_context_to context

        # Add bibtex files to dependency tree.
        update_dependency_tree

        cited_entries.size
      end

    end

  end
end

Liquid::Template.register_tag('bibliography_count', Jekyll::Scholar::BibliographyCountTag)
