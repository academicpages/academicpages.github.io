require "jekyll"
require "uri"

module Jekyll
  module GitHubMetadata
    class SiteGitHubMunger
      extend Forwardable

      def_delegators Jekyll::GitHubMetadata, :site, :repository
      private :repository

      def initialize(site)
        Jekyll::GitHubMetadata.site = site
      end

      def munge!
        Jekyll::GitHubMetadata.log :debug, "Initializing..."

        # This is the good stuff.
        site.config["github"] = github_namespace

        add_title_and_description_fallbacks!
        add_url_and_baseurl_fallbacks! if should_add_url_fallbacks?
      end

      private

      def github_namespace
        case site.config["github"]
        when nil
          drop
        when Hash
          Jekyll::Utils.deep_merge_hashes(drop, site.config["github"])
        else
          site.config["github"]
        end
      end

      def drop
        @drop ||= MetadataDrop.new(GitHubMetadata.site)
      end

      # Set `site.url` and `site.baseurl` if unset.
      def add_url_and_baseurl_fallbacks!
        site.config["url"] ||= Value.new("url", proc { |_c, r| r.url_without_path })
        return unless should_set_baseurl?

        site.config["baseurl"] = Value.new("baseurl", proc { |_c, r| r.baseurl })
      end

      def add_title_and_description_fallbacks!
        if should_warn_about_site_name?
          msg =  "site.name is set in _config.yml, but many plugins and themes expect "
          msg << "site.title to be used instead. To avoid potential inconsistency, "
          msg << "Jekyll GitHub Metadata will not set site.title to the repository's name."
          Jekyll::GitHubMetadata.log :warn, msg
        else
          site.config["title"] ||= Value.new("title", proc { |_c, r| r.name })
        end
        site.config["description"] ||= Value.new("description", proc { |_c, r| r.tagline })
      end

      # Set the baseurl only if it is `nil` or `/`
      # Baseurls should never be "/". See http://bit.ly/2s1Srid
      def should_set_baseurl?
        site.config["baseurl"].nil? || site.config["baseurl"] == "/"
      end

      def should_add_url_fallbacks?
        Jekyll.env == "production" || Pages.page_build?
      end

      def should_warn_about_site_name?
        site.config["name"] && !site.config["title"]
      end
    end
  end
end

Jekyll::Hooks.register :site, :after_init do |site|
  Jekyll::GitHubMetadata::SiteGitHubMunger.new(site).munge!
end
