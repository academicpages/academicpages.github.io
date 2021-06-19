module Jekyll
  class Scholar

    class BibliographyTag < Liquid::Tag
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

        items = cited_entries

        if group?
          groups = group(items)
          bibliography = render_groups(groups)
        else
          items = items[offset..max] if limit_entries?
          bibliography = render_items(items)
        end

        bibliography
      end

      def render_groups(groups)
        def group_renderer(groupsOrItems,keys,order,tags)
          if keys.count == 0
            renderer(true)
            render_items(groupsOrItems)
          else
            groupsOrItems
              .sort do |e1,e2|
                if (order.first || group_order.last) =~ /^(desc|reverse)/i
                  group_compare(keys.first,e2[0],e1[0])
                else
                  group_compare(keys.first,e1[0],e2[0])
                end
              end
              .map do |e|
                bibhead = content_tag(tags.first || group_tags.last,
                                      group_name(keys.first, e[0]),
                                      :class => config['bibliography_class'])
                bibentries = group_renderer(e[1], keys.drop(1), order.drop(1), tags.drop(1))
                bibhead + "\n" + bibentries
              end
              .join("\n")
          end
        end
        group_renderer(groups,group_keys,group_order,group_tags)
      end

      def render_items(items)
        bibliography = items.compact.each_with_index.map { |entry, index|
          reference = bibliography_tag(entry, index + 1)

          if generate_details?
            reference << link_to(details_link_for(entry),
              config['details_link'], :class => config['details_link_class'])
          end

          content_tag config['bibliography_item_tag'], reference, config['bibliography_item_attributes']
        }.join("\n")

        content_tag bibliography_list_tag, bibliography,
          { :class => config['bibliography_class'] }.merge(config['bibliography_list_attributes'])

      end

    end

  end
end

Liquid::Template.register_tag('bibliography', Jekyll::Scholar::BibliographyTag)
