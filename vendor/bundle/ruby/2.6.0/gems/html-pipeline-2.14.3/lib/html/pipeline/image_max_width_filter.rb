# frozen_string_literal: true

module HTML
  class Pipeline
    # This filter rewrites image tags with a max-width inline style and also wraps
    # the image in an <a> tag that causes the full size image to be opened in a
    # new tab.
    #
    # The max-width inline styles are especially useful in HTML email which
    # don't use a global stylesheets.
    class ImageMaxWidthFilter < Filter
      def call
        doc.search('img').each do |element|
          # Skip if there's already a style attribute. Not sure how this
          # would happen but we can reconsider it in the future.
          next if element['style']

          # Bail out if src doesn't look like a valid http url. trying to avoid weird
          # js injection via javascript: urls.
          next if element['src'].to_s.strip =~ /\Ajavascript/i

          element['style'] = 'max-width:100%;'

          link_image element unless has_ancestor?(element, %w[a])
        end

        doc
      end

      def link_image(element)
        link = doc.document.create_element('a', href: element['src'], target: '_blank')
        link.add_child(element.dup)
        element.replace(link)
      end
    end
  end
end
