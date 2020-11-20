# frozen_string_literal: true

module HTML
  class Pipeline
    # HTML Filter for replacing http references to :http_url with https versions.
    # Subdomain references are not rewritten.
    #
    # Context options:
    #   :http_url - The HTTP url to force HTTPS. Falls back to :base_url
    class HttpsFilter < Filter
      def call
        doc.css(%(a[href^="#{http_url}"])).each do |element|
          element['href'] = element['href'].sub(/^http:/, 'https:')
        end
        doc
      end

      # HTTP url to replace. Falls back to :base_url
      def http_url
        context[:http_url] || context[:base_url]
      end

      # Raise error if :http_url undefined
      def validate
        needs :http_url unless http_url
      end
    end
  end
end
