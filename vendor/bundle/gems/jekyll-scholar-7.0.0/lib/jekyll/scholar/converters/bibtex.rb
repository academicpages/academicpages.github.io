module Jekyll
  class Scholar
    class BibTeXConverter < Converter
      include Scholar::Utilities

      safe true
      priority :highest

      attr_reader :config

      @pattern = (/bib(tex)?$/i).freeze
      @extension = '.html'.freeze

      class << self
        attr_reader :pattern, :extension
      end

      def initialize(config = {})
        super
        @config['scholar'] = Scholar.defaults.merge(@config['scholar'] || {})
        @markdown = Jekyll::Converters::Markdown.new(config)
      end

      def matches(extension)
        extension =~ BibTeXConverter.pattern
      end

      def output_ext(extension)
        BibTeXConverter.extension
      end

      def convert(content)
        content = BibTeX.parse(content, :strict => true, :include => [:meta_content],
                               :filter => @config['scholar']['bibtex_filters']).map do |b|
          if b.respond_to?(:to_citeproc)
            render_bibliography b
          else
            b.is_a?(BibTeX::MetaContent) ? b.to_s : ''
          end
        end

        @markdown.convert(content.join("\n"))
      end

    end
  end
end
