# frozen_string_literal: true

module Jekyll
  module GitHubMetadata
    class RepositoryCompat
      attr_reader :repo

      def initialize(repo)
        @repo = repo
      end

      # In enterprise, the site's scheme will be the same as the instance's
      # In dotcom, this will be `https` for GitHub-owned sites that end with
      # `.github.com` and will be `http` for all other sites.
      # Note: This is not the same as *instance*'s scheme, which may differ
      def url_scheme
        if Pages.enterprise?
          Pages.scheme
        elsif repo.owner == "github" && domain.end_with?(".github.com")
          "https"
        else
          "http"
        end
      end

      def user_domain
        domain = repo.default_user_domain
        repo.user_page_domains.each do |user_repo|
          candidate_nwo = "#{repo.owner}/#{user_repo}"
          next unless Jekyll::GitHubMetadata.client.repository?(candidate_nwo)

          domain = Jekyll::GitHubMetadata::Repository.new(candidate_nwo).repo_compat.domain
        end
        domain
      end

      def pages_url
        return enterprise_url unless Pages.custom_domains_enabled?

        if repo.cname || repo.primary?
          "#{url_scheme}://#{domain}"
        else
          URI.join("#{url_scheme}://#{domain}", repo.name).to_s
        end
      end
      alias_method :html_url, :pages_url

      def domain
        @domain ||=
          if !Pages.custom_domains_enabled?
            Pages.github_hostname
          elsif repo.cname # explicit CNAME
            repo.cname
          elsif repo.primary? # user/org repo
            repo.default_user_domain
          else # project repo
            user_domain
          end
      end

      def source
        {
          "branch" => (repo.user_page? ? "master" : "gh-pages"),
          "path"   => "/",
        }
      end

      private

      def enterprise_url
        path = repo.user_page? ? repo.owner : repo.nwo
        if Pages.subdomain_isolation?
          URI.join("#{Pages.scheme}://#{Pages.pages_hostname}/", path).to_s
        else
          URI.join("#{Pages.github_url}/pages/", path).to_s
        end
      end
    end
  end
end
