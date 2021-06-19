# frozen_string_literal: true

require 'uri'

module HTML
  class Pipeline
    class AbsoluteSourceFilter < Filter
      # HTML Filter for replacing relative and root relative image URLs with
      # fully qualified URLs
      #
      # This is useful if an image is root relative but should really be going
      # through a cdn, or if the content for the page assumes the host is known
      # i.e. scraped webpages and some RSS feeds.
      #
      # Context options:
      #   :image_base_url - Base URL for image host for root relative src.
      #   :image_subpage_url - For relative src.
      #
      # This filter does not write additional information to the context.
      # This filter would need to be run before CamoFilter.
      def call
        doc.search('img').each do |element|
          next if element['src'].nil? || element['src'].empty?
          src = element['src'].strip
          next if src.start_with? 'http'
          base = if src.start_with? '/'
                   image_base_url
                 else
                   image_subpage_url
                 end
          element['src'] = URI.join(base, src).to_s
        end
        doc
      end

      # Private: the base url you want to use
      def image_base_url
        context[:image_base_url] || raise("Missing context :image_base_url for #{self.class.name}")
      end

      # Private: the relative url you want to use
      def image_subpage_url
        context[:image_subpage_url] || raise("Missing context :image_subpage_url for #{self.class.name}")
      end
    end
  end
end
