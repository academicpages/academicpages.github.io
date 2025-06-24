require "jekyll"
require "uri"

module Jekyll
  module GitHubMetadata
    class SiteGitHubMunger
      extend Forwardable

      class << self
        attr_accessor :global_munger
      end

      def_delegators Jekyll::GitHubMetadata, :site, :repository
      private :repository

      def initialize(site)
        Jekyll::GitHubMetadata.site = site
        @original_config = site.config["github"]
      end

      def munge!
        Jekyll::GitHubMetadata.log :debug, "Initializing..."

        add_title_and_description_fallbacks!
        add_url_and_baseurl_fallbacks! if should_add_url_fallbacks?
      end

      def inject_metadata!(payload)
        payload.site["github"] = github_namespace
      end

      def uninject_metadata!(payload)
        payload.site["github"] = @original_config
      end

      private

      def github_namespace
        case @original_config
        when nil
          drop
        when Hash
          drop.merge(@original_config)
        else
          @original_config
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
          site.config["title"] ||= Value.new("title", proc { |_context, repository|
            if repository.project_page?
              repository.name
            else
              repository.owner_display_name || repository.owner
            end
          })
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

    Jekyll::Hooks.register :site, :after_init do |site|
      SiteGitHubMunger.global_munger = SiteGitHubMunger.new(site)
      SiteGitHubMunger.global_munger.munge!
    end

    Jekyll::Hooks.register :site, :pre_render do |_site, payload|
      SiteGitHubMunger.global_munger.inject_metadata!(payload)
    end

    Jekyll::Hooks.register :site, :post_render do |_site, payload|
      SiteGitHubMunger.global_munger.uninject_metadata!(payload)
    end
  end
end
