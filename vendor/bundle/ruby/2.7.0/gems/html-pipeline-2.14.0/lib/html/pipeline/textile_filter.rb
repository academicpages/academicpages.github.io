# frozen_string_literal: true

HTML::Pipeline.require_dependency('redcloth', 'RedCloth')

module HTML
  class Pipeline
    # HTML Filter that converts Textile text into HTML and converts into a
    # DocumentFragment. This is different from most filters in that it can take a
    # non-HTML as input. It must be used as the first filter in a pipeline.
    #
    # Context options:
    #   :autolink => false    Disable autolinking URLs
    #
    # This filter does not write any additional information to the context hash.
    #
    # NOTE This filter is provided for really old comments only. It probably
    # shouldn't be used for anything new.
    class TextileFilter < TextFilter
      # Convert Textile to HTML and convert into a DocumentFragment.
      def call
        RedCloth.new(@text).to_html
      end
    end
  end
end
