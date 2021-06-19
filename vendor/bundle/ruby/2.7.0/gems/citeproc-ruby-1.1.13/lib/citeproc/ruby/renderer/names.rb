module CiteProc
  module Ruby

    class Renderer

      # @param item [CiteProc::CitationItem]
      # @param node [CSL::Style::Names]
      # @return [String]
      def render_names(item, node)
        return '' unless node.has_variable?

        names = node.variable.split(/\s+/).map do |role|
          [role.to_sym, item.data[role]]
        end

        suppressed = names.reject! { |n| item.suppressed? n[0] }

        names.reject! { |n| n[1].nil? || n[1].empty? }

        if names.empty?
          # We also return when the list is empty because
          # of a suppression, because we do not want to
          # substitute suppressed items!
          return '' unless suppressed.nil? && node.has_substitute?

          rendered_names = render_substitute item, node.substitute

          if substitute_subsequent_authors_completely? &&
            completely_substitute?(rendered_names)

            rendered_names = state.node.subsequent_author_substitute
          end

          rendered_names

        else

          resolve_editor_translator_exception! names

          # Pick the names node that will be used for
          # formatting; if we are currently in substiution
          # mode, the node that is being substituted for
          # will take precedence if the current node is
          # a descendant of it.
          #
          # This makes sure that nodes in macros do not
          # use the original names node.
          #
          # When the current node has children the names
          # will not be substituted either.
          if substitution_mode? && !node.has_children? &&
            node.ancestors.include?(state.substitute)

            names_node = state.substitute

          else
            names_node = node
          end

          name = name_node_for(names_node)

          return count_names(names, name).to_s if name.count?

          names.map! do |role, ns|
            if names_node.has_label?
              label = render_label item, names_node.label, role
              label = format! label, names_node.label

              rendered_names = render_name(ns, name)

              if rendered_names.empty?
                rendered_names
              else
                if names_node.prefix_label?
                  concat label, rendered_names
                else
                  concat rendered_names, label
                end
              end

            else
              render_name ns, name
            end
          end

          join names, names_node.delimiter(state.node)
        end

      ensure
        state.rendered_names!
      end

      def count_names(names, node)
        names.reduce(0) do |count, (_, ns)|
          if node.truncate?(ns)
            count + node.truncate(ns).length
          else
            count + ns.length
          end
        end
      end

      def substitute_subsequent_authors?
        bibliography_mode? && state.node.substitute_subsequent_authors?
      end

      def substitute_subsequent_authors_completely?
        substitute_subsequent_authors? &&
          state.node.substitute_subsequent_authors_completely?
      end

      def substitute_subsequent_authors_individually?
        substitute_subsequent_authors? &&
          state.node.substitute_subsequent_authors_individually?
      end

      def completely_substitute?(names)
        # Substitution applies only to the first names
        # node being rendered!
        return false if state.rendered_names?

        state.store_authors! names
        previous_names = state.previous_authors

        return false unless previous_names

        names == previous_names[0]
      end

      def individually_substitute!(names)
      end

      # Formats one or more names according to the
      # configuration of the passed-in node.
      # Returns the formatted name(s) as a string.
      #
      # @param names [CiteProc::Names]
      # @param node [CSL::Style::Name]
      # @return [String]
      def render_name(names, node)

        # TODO handle subsequent citation rules

        delimiter = node.delimiter

        connector = node.connector
        connector = translate('and') if connector == 'text'

        # Add spaces around connector
        connector = " #{connector} " unless connector.nil?

        rendered_names =
          case
          when node.truncate?(names)
            truncated = node.truncate(names)

            return '' if truncated.empty?

            if node.delimiter_precedes_last?(truncated)
              connector = join [delimiter, connector].compact
            end

            if node.ellipsis? && names.length - truncated.length > 1
              join [
                join(truncated.map.with_index { |name, idx|
                  render_individual_name name, node, idx + 1
                }, delimiter),

                render_individual_name(names[-1], node, truncated.length + 1)

              ], node.ellipsis

            else
              others = node.et_al ?
                format!(translate(node.et_al[:term]), node.et_al) :
                translate('et-al')

              connector = node.delimiter_precedes_et_al?(truncated) ?
                delimiter : ' '

              join [
                join(truncated.map.with_index { |name, idx|
                  render_individual_name name, node, idx + 1
                }, delimiter),

                others

              ], connector

            end

          when names.length < 3
            if node.delimiter_precedes_last?(names)
              connector = [delimiter, connector].compact.join('').squeeze(' ')
            end

            join names.map.with_index { |name, idx|
              render_individual_name name, node, idx + 1
            }, connector || delimiter

          else
            if node.delimiter_precedes_last?(names)
              connector = [delimiter, connector].compact.join('').squeeze(' ')
            end

            join [
              join(names[0...-1].map.with_index { |name, idx|
                render_individual_name name, node, idx + 1
              }, delimiter),

              render_individual_name(names[-1], node, names.length)

            ], connector || delimiter
          end


        if substitute_subsequent_authors_completely? &&
          completely_substitute?(rendered_names)

          rendered_names = state.node.subsequent_author_substitute
        end

        format! rendered_names, node
      end

      # @param names [CiteProc::Name]
      # @param node [CSL::Style::Name]
      # @param position [Fixnum]
      # @return [String]
      def render_individual_name(name, node, position = 1)
        if name.personal?
          name = name.dup

          # TODO move parts of the formatting logic here
          # because name parts may include particles etc.


          # Strip away some unusual characters to normalize
          # sort order for names.
          if sort_mode?
            name.family = name.family.to_s.gsub(/[\[\]]|^\W+/, '')
          end

          name.options.merge! node.name_options
          name.sort_order! node.name_as_sort_order_at?(position)

          name.initialize_without_hyphen! if node.initialize_without_hyphen?

          if style && style.demote_particle?
            name.options[:'demote-non-dropping-particle'] = style.demote_particle
          end

          # Strip away (hyphenated) particles in sort mode!
          if sort_mode? && name.demote_particle?
            name.family = name.family.to_s.sub(/^[[:lower:]]+[\s-]/, '')
          end

          node.name_part.each do |part|
            case part[:name]
            when 'family'
              if !name.particle? || name.demote_particle?
                name.family = format!(name.family, part)
              else
                name.family = format!("#{name.particle} #{name.family}", part)
                name.particle = nil
              end

              # Name suffix must be enclosed by family-part
              # suffix in display order!
              if name.has_suffix? && !name.sort_order? && part.attribute?(:suffix)
                comma = name.comma_suffix? ? name.comma : ' '
                suffix = part[:suffix]

                name.family.chomp! suffix
                name.family.concat "#{comma}#{name.suffix}#{suffix}"
                name.suffix = nil
              end

            when 'given'
              if name.dropping_particle?
                name.given = format!("#{name.initials} #{name.dropping_particle}", part)
                name.dropping_particle = nil
              else
                name.given = format!(name.initials, part)
              end

              # Demoted particles must be enclosed by
              # given-part affixes in sort order!
              if name.particle? && name.demote_particle? &&
                name.sort_order? && part.attribute?(:suffix)

                suffix = part[:suffix]

                name.given.chomp! suffix
                name.given.concat " #{name.particle}#{suffix}"

                name.particle = nil
              end

            end
          end

        end

        format! name.format, node
      end

      # @param item [CiteProc::CitationItem]
      # @param node [CSL::Style::Substitute]
      # @return [String]
      def render_substitute(item, node)
        return '' unless node.has_children?

        if substitution_mode?
          saved_substitute = state.substitute
        end

        state.substitute! node.parent
        observer = ItemObserver.new(item.data)

        node.each_child do |child|
          observer.start

          begin
            string = render(item, child)

            unless string.empty?
              # Variables rendered as substitutes
              # must be suppressed during the remainder
              # of the rendering process!
              item.suppress!(*observer.accessed)

              # Report a read-access using the substitution string
              # for the name variable being substituted, or the first
              # name variable (if there are more than one).
              variable = node.parent.variable[/\w+/]
              item.data.simulate_read_attribute variable, string

              return string # break out of each loop!
            end

          ensure
            observer.stop
            observer.clear!
          end

        end

        '' # no substitute was rendered
      ensure
        state.clear_substitute! saved_substitute
      end


      private

      def name_node_for(names_node)
        # Make a copy of the name node and inherit
        # options from root and citation/bibliography
        # depending on current rendering mode.
        if names_node.has_name?
          name = names_node.name.deep_copy
        else
          name = CSL::Style::Name.new
        end

        # Inherit name options from style and the
        # current rendering node. We pass both in,
        # because this is now an unlinked node!
        options = name.inherited_name_options(state.node, names_node.root)

        name.reverse_merge! options
        name.et_al = names_node.et_al if names_node.has_et_al?

        # Override options if we are rendering a sort key!
        if sort_mode?
          name.merge! state.node.name_options
          name.all_names_as_sort_order!
        end

        name
      end

      def resolve_editor_translator_exception!(names)

        i = names.index { |role, _| role == :translator }
        return names if i.nil?

        j = names.index { |role, _| role == :editor }
        return names if j.nil?

        return names unless names[i][1] == names[j][1]

        # rename the first instance and drop the second one
        i, j = j, i if j < i

        names[i][0] = :editortranslator
        names.slice!(j)

        names
      end
    end

  end
end
