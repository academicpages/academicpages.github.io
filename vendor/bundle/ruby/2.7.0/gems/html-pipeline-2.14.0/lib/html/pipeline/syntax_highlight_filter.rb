# frozen_string_literal: true

HTML::Pipeline.require_dependency('rouge', 'SyntaxHighlightFilter')

module HTML
  class Pipeline
    # HTML Filter that syntax highlights text inside code blocks.
    #
    # Context options:
    #
    #   :highlight => String represents the language to pick lexer. Defaults to empty string.
    #   :scope => String represents the class attribute adds to pre element after.
    #             Defaults to "highlight highlight-css" if highlights a css code block.
    #
    # This filter does not write any additional information to the context hash.
    class SyntaxHighlightFilter < Filter
      def initialize(*args)
        super(*args)
        @formatter = Rouge::Formatters::HTML.new
      end

      def call
        doc.search('pre').each do |node|
          default = context[:highlight] && context[:highlight].to_s
          next unless lang = node['lang'] || default
          next unless lexer = lexer_for(lang)

          text = node.inner_text
          html = highlight_with_timeout_handling(text, lexer)
          next if html.nil?

          node.inner_html = html
          scope = context.fetch(:scope) { 'highlight' }
          node['class'] = "#{scope} #{scope}-#{lang}"
        end
        doc
      end

      def highlight_with_timeout_handling(text, lexer)
        Rouge.highlight(text, lexer, @formatter)
      rescue Timeout::Error => _
        nil
      end

      def lexer_for(lang)
        Rouge::Lexer.find(lang)
      end
    end
  end
end
