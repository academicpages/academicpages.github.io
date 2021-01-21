# frozen_string_literal: true

module Jekyll
  class SeoTag
    class Drop < Jekyll::Drops::Drop
      include Jekyll::SeoTag::UrlHelper

      TITLE_SEPARATOR = " | "
      FORMAT_STRING_METHODS = [
        :markdownify, :strip_html, :normalize_whitespace, :escape_once,
      ].freeze
      HOMEPAGE_OR_ABOUT_REGEX = %r!^/(about/)?(index.html?)?$!.freeze

      def initialize(text, context)
        @obj = {}
        @mutations = {}
        @text    = text
        @context = context
      end

      def version
        Jekyll::SeoTag::VERSION
      end

      # Should the `<title>` tag be generated for this page?
      def title?
        return false unless title
        return @display_title if defined?(@display_title)

        @display_title = (@text !~ %r!title=false!i)
      end

      def site_title
        @site_title ||= format_string(site["title"] || site["name"])
      end

      def site_description
        @site_description ||= format_string site["description"]
      end

      # Page title without site title or description appended
      def page_title
        @page_title ||= format_string(page["title"]) || site_title
      end

      # Page title with site title or description appended
      # rubocop:disable Metrics/CyclomaticComplexity
      def title
        @title ||= begin
          if site_title && page_title != site_title
            page_title + TITLE_SEPARATOR + site_title
          elsif site_description && site_title
            site_title + TITLE_SEPARATOR + site_description
          else
            page_title || site_title
          end
        end

        return page_number + @title if page_number

        @title
      end
      # rubocop:enable Metrics/CyclomaticComplexity

      def name
        return @name if defined?(@name)

        @name = if seo_name
                  seo_name
                elsif !homepage_or_about?
                  nil
                elsif site_social["name"]
                  format_string site_social["name"]
                elsif site_title
                  site_title
                end
      end

      def description
        @description ||= begin
          format_string(page["description"] || page["excerpt"]) || site_description
        end
      end

      # A drop representing the page author
      def author
        @author ||= AuthorDrop.new(:page => page, :site => site)
      end

      # A drop representing the JSON-LD output
      def json_ld
        @json_ld ||= JSONLDDrop.new(self)
      end

      # Returns a Drop representing the page's image
      # Returns nil if the image has no path, to preserve backwards compatability
      def image
        @image ||= ImageDrop.new(:page => page, :context => @context)
        @image if @image.path
      end

      def date_modified
        @date_modified ||= begin
          date = if page_seo["date_modified"]
                   page_seo["date_modified"]
                 elsif page["last_modified_at"]
                   page["last_modified_at"].to_liquid
                 else
                   page["date"]
                 end
          filters.date_to_xmlschema(date) if date
        end
      end

      def date_published
        @date_published ||= filters.date_to_xmlschema(page["date"]) if page["date"]
      end

      def type
        @type ||= begin
          if page_seo["type"]
            page_seo["type"]
          elsif homepage_or_about?
            "WebSite"
          elsif page["date"]
            "BlogPosting"
          else
            "WebPage"
          end
        end
      end

      def links
        @links ||= begin
          if page_seo["links"]
            page_seo["links"]
          elsif homepage_or_about? && site_social["links"]
            site_social["links"]
          end
        end
      end

      def logo
        @logo ||= begin
          return unless site["logo"]

          if absolute_url? site["logo"]
            filters.uri_escape site["logo"]
          else
            filters.uri_escape filters.absolute_url site["logo"]
          end
        end
      end

      def page_lang
        @page_lang ||= page["lang"] || site["lang"] || "en_US"
      end

      def canonical_url
        @canonical_url ||= begin
          if page["canonical_url"].to_s.empty?
            filters.absolute_url(page["url"]).to_s.gsub(%r!/index\.html$!, "/")
          else
            page["canonical_url"]
          end
        end
      end

      private

      def filters
        @filters ||= Jekyll::SeoTag::Filters.new(@context)
      end

      def page
        @page ||= @context.registers[:page].to_liquid
      end

      def site
        @site ||= @context.registers[:site].site_payload["site"].to_liquid
      end

      def homepage_or_about?
        page["url"] =~ HOMEPAGE_OR_ABOUT_REGEX
      end

      def page_number
        return unless @context["paginator"] && @context["paginator"]["page"]

        current = @context["paginator"]["page"]
        total = @context["paginator"]["total_pages"]

        return "Page #{current} of #{total} for " if current > 1
      end

      attr_reader :context

      def fallback_data
        @fallback_data ||= {}
      end

      def format_string(string)
        string = FORMAT_STRING_METHODS.reduce(string) do |memo, method|
          filters.public_send(method, memo)
        end

        string unless string.empty?
      end

      def seo_name
        @seo_name ||= format_string(page_seo["name"]) if page_seo["name"]
      end

      def page_seo
        @page_seo ||= sub_hash(page, "seo")
      end

      def site_social
        @site_social ||= sub_hash(site, "social")
      end

      # Safely returns a sub hash
      #
      # hash - the parent hash
      # key  - the key in the parent hash
      #
      # Returns the sub hash or an empty hash, if it does not exist
      def sub_hash(hash, key)
        if hash[key].is_a?(Hash)
          hash[key]
        else
          {}
        end
      end
    end
  end
end
