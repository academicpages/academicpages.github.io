module CiteProc
  module Ruby
    module Formats

      class Latex < Format

        @defaults = {
          :italic    => 'emph',   # em
          :bold      => 'textbf', # strong
          :container => '',   # inner container
          :display   => ''    # display container
        }

        @vertical_align = Hash.new { |_,k| k }
        @vertical_align['sup'] = 'super'

        class << self
          attr_reader :defaults
        end

        attr_reader :config

        def initialize(config = nil)
          if config.nil?
            @config = Latex.defaults.dup
          else
            @config = Latex.defaults.merge(config)
          end
        end

        def bibliography(bibliography)
          bibliography.header = "\\begin{enumerate}"
          bibliography.footer = "\\end{enumerate}"

          bibliography.prefix = "\\item  "
          bibliography.suffix = ""

          bibliography.connector = "\n"
          bibliography
        end

        def apply_font_style
          if options[:'font-style'] == 'italic'
            output.replace content_tag(config[:italic], output)
          end
        end

        def apply_font_variant
        end

        def apply_font_weight
          if options[:'font-weight'] == 'bold'
            output.replace content_tag(config[:bold], output)
          end
        end

        def apply_text_decoration
        end

        def apply_vertical_align
        end

        def apply_display
          output.replace(
            content_tag(config[:display], output)
          )
        end

        def escape_quotes?
          false
        end

        protected

        def finalize!
          # TODO find a better solution for this (strip tags?)
          # For now make sure not to double encode entities
          # by matching spaces before or after.
          output.gsub!(/[$&#^_%~]/) do |c|
            case c
            # TODO: when "\\" then '\backslash{}'
            when "^" then '\^{}'
            when '~' then '\~{}'
            else "\\#{c}"
            end
          end
        end

        def cleanup!
          super
        end

        private

        def content_tag(name, content, options = nil)
          opening_tag(name, options) << content << closing_tag(name)
        end

        def style_for(options)
          return unless options && !options.empty?
          options.map { |*kv| kv.join(': ') }.join('; ')
        end

        def attribute_assignments(options)
          return unless options

          options = options.select { |_, v| !v.nil? }

          return unless !options.empty?

          ' ' << options.map { |k, v| [k, v.inspect].join('=') }.join(' ')
        end

        def opening_tag(name, options = nil)
          if options && options.key?('style')
            options['style'] = style_for(options['style'])
          end

          if name == ''
            ''
          else
            "\\#{name}{"
          end
        end

        def closing_tag(name)
          if name == ''
            ''
          else
            '}'
          end
        end
      end
    end
  end
end
