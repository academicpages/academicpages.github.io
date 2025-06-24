# frozen_string_literal: true

module Jekyll
  module GitHubMetadata
    class Repository
      attr_reader :nwo, :owner, :name

      # Defines an instance method that delegates to a hash's key
      #
      # hash   - a symbol representing the instance method to delegate to. The
      #          instance method should return a hash or respond to #[]
      # key    - the key to call within the hash
      # method - (optional) the instance method the key should be aliased to.
      #          If not specified, defaults to the hash key
      #
      # Returns a symbol representing the instance method
      def self.def_hash_delegator(hash, key, method)
        define_method(method) do
          public_send(hash)[key.to_s]
        end
      end

      extend Forwardable
      def_hash_delegator :repo_info,      :license,       :license
      def_hash_delegator :repo_info,      :language,      :language
      def_hash_delegator :repo_info,      :description,   :tagline
      def_hash_delegator :repo_info,      :has_downloads, :show_downloads?
      def_hash_delegator :repo_info,      :private,       :private?
      def_hash_delegator :repo_info,      :archived,      :archived?
      def_hash_delegator :repo_info,      :disabled,      :disabled?
      def_hash_delegator :latest_release, :url,           :latest_release_url
      def_hash_delegator :source,         :branch,        :git_ref

      def_delegator :uri, :host,   :domain
      def_delegator :uri, :scheme, :url_scheme
      def_delegator :uri, :path,   :baseurl

      def initialize(name_with_owner)
        @nwo   = name_with_owner
        @owner = nwo.split("/").first
        @name  = nwo.split("/").last
      end

      def repo_compat
        @repo_compat ||= Jekyll::GitHubMetadata::RepositoryCompat.new(self)
      end

      def repo_info
        @repo_info ||= begin
          options = { :accept => "application/vnd.github.drax-preview+json" }
          (Value.new("repo_info", proc { |c| c.repository(nwo, options) }).render || {})
        end
      end

      def repo_pages_info
        @repo_pages_info ||= (Value.new("repo_pages_info", proc { |c| c.pages(nwo, repo_pages_info_opts) }).render || {})
      end

      def repo_pages_info_opts
        if Pages.repo_pages_html_url_preview?
          { :accept => "application/vnd.github.mister-fantastic-preview+json" }
        else
          {}
        end
      end

      def owner_display_name
        owner_metadata.name
      end

      def owner_metadata
        @owner_metadata ||= Jekyll::GitHubMetadata::Owner.new(owner)
      end

      def owner_url
        "#{Pages.github_url}/#{owner}"
      end

      def owner_gravatar_url
        "#{owner_url}.png"
      end

      def repo_clone_url
        "#{repository_url}.git"
      end

      def repository_url
        "#{owner_url}/#{name}"
      end

      def zip_url
        "#{repository_url}/zipball/#{git_ref}"
      end

      def tar_url
        "#{repository_url}/tarball/#{git_ref}"
      end

      def releases_url
        "#{repository_url}/releases"
      end

      def issues_url
        "#{repository_url}/issues" if repo_info["has_issues"]
      end

      def wiki_url
        "#{repository_url}/wiki" if repo_info["has_wiki"]
      end

      def organization_repository?
        memoize_value :@is_organization_repository, Value.new("organization_repository?", proc { |c| !!c.organization(owner) })
      end

      def owner_public_repositories
        options = {
          :type   => "public",
          :accept => "application/vnd.github.mercy-preview+json",
        }
        memoize_value :@owner_public_repositories, Value.new("owner_public_repositories", proc do |c|
          repos = c.list_repos(owner, options) || []
          repos.map do |r|
            r[:releases] = Value.new("owner_public_repositories_releases", proc { c.releases(r[:full_name]) })
            r[:contributors] = Value.new("owner_public_repositories_contributors", proc { c.contributors(r[:full_name]) })
            r
          end
        end)
      end

      def organization_public_members
        memoize_value :@organization_public_members, Value.new("organization_public_members", proc do |c|
          c.organization_public_members(owner) if organization_repository?
        end)
      end

      def contributors
        memoize_value :@contributors, Value.new("contributors", proc { |c| c.contributors(nwo) })
      end

      def releases
        memoize_value :@releases, Value.new("releases", proc { |c| c.releases(nwo) })
      end

      def latest_release
        memoize_value :@latest_release, Value.new("latest_release", proc { |c| c.latest_release(nwo) })
      end

      def source
        repo_pages_info["source"] || repo_compat.source
      end

      def project_page?
        !user_page?
      end

      def github_repo?
        !Pages.enterprise? && owner.eql?("github")
      end

      def primary?
        if Pages.enterprise?
          name.downcase == "#{owner.to_s.downcase}.#{Pages.github_hostname}"
        else
          user_page_domains.include? name.downcase
        end
      end
      alias_method :user_page?, :primary?

      def user_page_domains
        domains = [default_user_domain]
        domains.push "#{owner}.github.com".downcase unless Pages.enterprise?
        domains
      end

      def default_user_domain
        if github_repo?
          "#{owner}.#{Pages.github_hostname}".downcase
        elsif Pages.enterprise?
          Pages.pages_hostname.downcase
        else
          "#{owner}.#{Pages.pages_hostname}".downcase
        end
      end

      def cname
        return nil unless Pages.custom_domains_enabled?

        repo_pages_info["cname"]
      end

      def html_url
        @html_url ||= (repo_pages_info["html_url"] || repo_compat.pages_url).chomp("/")
      end

      def uri
        @uri ||= URI(html_url)
      end

      def url_without_path
        uri.dup.tap { |u| u.path = "" }.to_s
      end

      def stargazers_count
        repo_pages_info["stargazers_count"] || 0
      end

      def forks_count
        repo_pages_info["forks_count"] || 0
      end

      private

      def memoize_value(var_name, value)
        return instance_variable_get(var_name) if instance_variable_defined?(var_name)

        instance_variable_set(var_name, value.render)
      end
    end
  end
end
