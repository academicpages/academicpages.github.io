# frozen_string_literal: true

HTML::Pipeline.require_dependency('escape_utils', 'TableOfContentsFilter')

module HTML
  class Pipeline
    # HTML filter that adds an 'id' attribute to all headers
    # in a document, so they can be accessed from a table of contents.
    #
    # Generates the Table of Contents, with links to each header.
    #
    # Examples
    #
    #  TocPipeline =
    #    HTML::Pipeline.new [
    #      HTML::Pipeline::TableOfContentsFilter
    #    ]
    #  # => #<HTML::Pipeline:0x007fc13c4528d8...>
    #  orig = %(<h1>Ice cube</h1><p>is not for the pop chart</p>)
    #  # => "<h1>Ice cube</h1><p>is not for the pop chart</p>"
    #  result = {}
    #  # => {}
    #  TocPipeline.call(orig, {}, result)
    #  # => {:toc=> ...}
    #  result[:toc]
    #  # => "<ul class=\"section-nav\">\n<li><a href=\"#ice-cube\">...</li><ul>"
    #  result[:output].to_s
    #  # => "<h1>\n<a id=\"ice-cube\" class=\"anchor\" href=\"#ice-cube\">..."
    class TableOfContentsFilter < Filter
      PUNCTUATION_REGEXP = RUBY_VERSION > '1.9' ? /[^\p{Word}\- ]/u : /[^\w\- ]/

      # The icon that will be placed next to an anchored rendered markdown header
      def anchor_icon
        context[:anchor_icon] || '<span aria-hidden="true" class="octicon octicon-link"></span>'
      end

      def call
        result[:toc] = String.new('')

        headers = Hash.new(0)
        doc.css('h1, h2, h3, h4, h5, h6').each do |node|
          text = node.text
          id = ascii_downcase(text)
          id.gsub!(PUNCTUATION_REGEXP, '') # remove punctuation
          id.tr!(' ', '-') # replace spaces with dash

          uniq = headers[id] > 0 ? "-#{headers[id]}" : ''
          headers[id] += 1
          if header_content = node.children.first
            result[:toc] << %(<li><a href="##{id}#{uniq}">#{EscapeUtils.escape_html(text)}</a></li>\n)
            header_content.add_previous_sibling(%(<a id="#{id}#{uniq}" class="anchor" href="##{id}#{uniq}" aria-hidden="true">#{anchor_icon}</a>))
          end
        end
        result[:toc] = %(<ul class="section-nav">\n#{result[:toc]}</ul>) unless result[:toc].empty?
        doc
      end

      if RUBY_VERSION >= '2.4'
        def ascii_downcase(str)
          str.downcase(:ascii)
        end
      else
        def ascii_downcase(str)
          str.downcase
        end
      end
    end
  end
end
