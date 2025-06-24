# frozen_string_literal: true

require "jekyll"
require "forwardable"

module Jekyll
  module GitHubMetadata
    class MetadataDrop < Jekyll::Drops::Drop
      extend Forwardable

      mutable true

      # See https://github.com/jekyll/jekyll/pull/6338
      alias_method :invoke_drop, :[]
      def key?(key)
        return false if key.nil?
        return true if self.class.mutable? && mutations.key?(key)

        respond_to?(key) || fallback_data.key?(key)
      end

      def to_s
        require "json"
        JSON.pretty_generate to_h
      end
      alias_method :to_str, :to_s

      def content_methods
        super - %w(to_s to_str)
      end

      def keys
        super.sort
      end

      def_delegator Jekyll::GitHubMetadata::Pages, :env,             :environment
      def_delegator Jekyll::GitHubMetadata::Pages, :env,             :pages_env
      def_delegator Jekyll::GitHubMetadata::Pages, :github_hostname, :hostname
      def_delegator Jekyll::GitHubMetadata::Pages, :pages_hostname,  :pages_hostname
      def_delegator Jekyll::GitHubMetadata::Pages, :api_url,         :api_url
      def_delegator Jekyll::GitHubMetadata::Pages, :help_url,        :help_url

      private def_delegator Jekyll::GitHubMetadata, :repository

      def_delegator :repository, :owner_public_repositories,   :public_repositories
      def_delegator :repository, :organization_public_members, :organization_members
      def_delegator :repository, :name,                        :project_title
      def_delegator :repository, :tagline,                     :project_tagline
      def_delegator :repository, :owner_metadata,              :owner
      def_delegator :repository, :owner,                       :owner_name
      def_delegator :repository, :owner_display_name,          :owner_display_name
      def_delegator :repository, :owner_url,                   :owner_url
      def_delegator :repository, :owner_gravatar_url,          :owner_gravatar_url
      def_delegator :repository, :repository_url,              :repository_url
      def_delegator :repository, :nwo,                         :repository_nwo
      def_delegator :repository, :name,                        :repository_name
      def_delegator :repository, :zip_url,                     :zip_url
      def_delegator :repository, :tar_url,                     :tar_url
      def_delegator :repository, :repo_clone_url,              :clone_url
      def_delegator :repository, :releases_url,                :releases_url
      def_delegator :repository, :issues_url,                  :issues_url
      def_delegator :repository, :wiki_url,                    :wiki_url
      def_delegator :repository, :language,                    :language
      def_delegator :repository, :user_page?,                  :is_user_page
      def_delegator :repository, :project_page?,               :is_project_page
      def_delegator :repository, :show_downloads?,             :show_downloads
      def_delegator :repository, :html_url,                    :url
      def_delegator :repository, :baseurl,                     :baseurl
      def_delegator :repository, :contributors,                :contributors
      def_delegator :repository, :releases,                    :releases
      def_delegator :repository, :latest_release,              :latest_release
      def_delegator :repository, :private?,                    :private
      def_delegator :repository, :archived?,                   :archived
      def_delegator :repository, :disabled?,                   :disabled
      def_delegator :repository, :license,                     :license
      def_delegator :repository, :source,                      :source

      def versions
        return @versions if defined?(@versions)

        begin
          require "github-pages"
          @versions = GitHubPages.versions
        rescue LoadError
          @versions = {}
        end
      end

      def build_revision
        @build_revision ||= begin
          ENV["JEKYLL_BUILD_REVISION"] || `git rev-parse HEAD`.strip
        end
      end

      private

      # Nothing to see here.
      def fallback_data
        @fallback_data ||= {}
      end

      def mutations
        @mutations ||= {}
      end
    end
  end
end
