# frozen_string_literal: true

module Jekyll
  class SeoTag
    # This module is deprecated, but is included in the Gem to avoid a breaking
    # change and should be removed at the next major version bump
    module JSONLD
      METHODS_KEYS = {
        :json_context   => "@context",
        :type           => "@type",
        :name           => "name",
        :page_title     => "headline",
        :json_author    => "author",
        :json_image     => "image",
        :date_published => "datePublished",
        :date_modified  => "dateModified",
        :description    => "description",
        :publisher      => "publisher",
        :main_entity    => "mainEntityOfPage",
        :links          => "sameAs",
        :canonical_url  => "url",
      }.freeze

      # Self should be a Jekyll::SeoTag::Drop instance (when extending the module)
      def json_ld
        Jekyll.logger.warn "Jekyll::SeoTag::JSONLD is deprecated"
        @json_ld ||= JSONLDDrop.new(self)
      end
    end
  end
end
