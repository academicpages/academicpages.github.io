# frozen_string_literal: true

HTML::Pipeline.require_dependency('commonmarker', 'MarkdownFilter')

module HTML
  class Pipeline
    # HTML Filter that converts Markdown text into HTML and converts into a
    # DocumentFragment. This is different from most filters in that it can take a
    # non-HTML as input. It must be used as the first filter in a pipeline.
    #
    # Context options:
    #   :gfm      => false    Disable GFM line-end processing
    #   :commonmarker_extensions => [ :table, :strikethrough,
    #      :tagfilter, :autolink ] Commonmarker extensions to include
    #
    # This filter does not write any additional information to the context hash.
    class MarkdownFilter < TextFilter
      DEFAULT_COMMONMARKER_EXTENSIONS = %i[table strikethrough tagfilter autolink].freeze

      def initialize(text, context = nil, result = nil)
        super text, context, result
        @text = @text.delete "\r"
      end

      # Convert Markdown to HTML using the best available implementation
      # and convert into a DocumentFragment.
      def call
        extensions = context.fetch(
          :commonmarker_extensions,
          DEFAULT_COMMONMARKER_EXTENSIONS
        )
        html = if (renderer = context[:commonmarker_renderer])
          unless renderer < CommonMarker::HtmlRenderer
            raise ArgumentError, "`commonmark_renderer` must be derived from `CommonMarker::HtmlRenderer`"
          end
          parse_options = :DEFAULT
          parse_options = [:UNSAFE] if context[:unsafe]

          render_options = [:GITHUB_PRE_LANG]
          render_options << :HARDBREAKS if context[:gfm] != false
          render_options << :UNSAFE if context[:unsafe]

          doc = CommonMarker.render_doc(@text, parse_options, extensions)
          renderer.new(options: render_options, extensions: extensions).render(doc)
        else
          options = [:GITHUB_PRE_LANG]
          options << :HARDBREAKS if context[:gfm] != false
          options << :UNSAFE if context[:unsafe]
          CommonMarker.render_html(@text, options, extensions)
        end
        html.rstrip!
        html
      end
    end
  end
end
