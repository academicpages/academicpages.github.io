# frozen_string_literal: true

module Jekyll
  class SeoTag
    # A drop representing the current page's author
    #
    # Author name will be pulled from:
    #
    # 1. The page's `author` key
    # 2. The first author in the page's `authors` key
    # 3. The `author` key in the site config
    #
    # If the result from the name search is a string, we'll also check
    # for additional author metadata in `site.data.authors`
    class AuthorDrop < Jekyll::Drops::Drop
      # Initialize a new AuthorDrop
      #
      # page - The page hash (e.g., Page#to_liquid)
      # site - The Jekyll::Drops::SiteDrop
      def initialize(page: nil, site: nil)
        raise ArgumentError unless page && site

        @mutations = {}
        @page = page
        @site = site
      end

      # AuthorDrop#to_s should return name, allowing the author drop to safely
      # replace `page.author`, if necessary, and remain backwards compatible
      def name
        author_hash["name"]
      end
      alias_method :to_s, :name

      def twitter
        return @twitter if defined? @twitter

        twitter = author_hash["twitter"] || author_hash["name"]
        @twitter = twitter.is_a?(String) ? twitter.sub(%r!^@!, "") : nil
      end

      private

      attr_reader :page
      attr_reader :site

      # Finds the page author in the page.author, page.authors, or site.author
      #
      # Returns a string or hash representing the author
      def resolved_author
        return @resolved_author if defined? @resolved_author

        sources = [page["author"]]
        sources << page["authors"].first if page["authors"].is_a?(Array)
        sources << site["author"]
        @resolved_author = sources.find { |s| !s.to_s.empty? }
      end

      # If resolved_author is a string, attempts to find coresponding author
      # metadata in `site.data.authors`
      #
      # Returns a hash representing additional metadata or an empty hash
      def site_data_hash
        @site_data_hash ||= begin
          return {} unless resolved_author.is_a?(String)
          return {} unless site.data["authors"].is_a?(Hash)

          author_hash = site.data["authors"][resolved_author]
          author_hash.is_a?(Hash) ? author_hash : {}
        end
      end

      # Returns the normalized author hash representing the page author,
      # including site-wide metadata if the author is provided as a string,
      # or an empty hash, if the author cannot be resolved
      def author_hash
        @author_hash ||= begin
          if resolved_author.is_a? Hash
            resolved_author
          elsif resolved_author.is_a? String
            { "name" => resolved_author }.merge!(site_data_hash)
          else
            {}
          end
        end
      end

      # Since author_hash is aliased to fallback_data, any values in the hash
      # will be exposed via the drop, allowing support for arbitrary metadata
      alias_method :fallback_data, :author_hash
    end
  end
end
