# frozen_string_literal: true

module Jekyll
  module GitHubMetadata
    class Pages
      class << self
        DEFAULTS = {
          "PAGES_ENV"              => "development",
          "PAGES_API_URL"          => "https://api.github.com",
          "PAGES_HELP_URL"         => "https://docs.github.com",
          "PAGES_GITHUB_HOSTNAME"  => "github.com",
          "PAGES_PAGES_HOSTNAME"   => "github.io",
          "SSL"                    => "false",
          "SUBDOMAIN_ISOLATION"    => "false",
          "PAGES_PREVIEW_HTML_URL" => nil,
          "PAGE_BUILD_ID"          => nil,
        }.freeze

        # Whether the GitHub instance supports HTTPS
        # Note: this will be the same as how sites are served in Enterprise,
        # but may be different from how sites are served on GitHub.com.
        # See Repository#url_scheme
        def ssl?
          env_var("SSL") == "true" || test?
        end

        def scheme
          ssl? ? "https" : "http"
        end

        def subdomain_isolation?
          env_var("SUBDOMAIN_ISOLATION").eql? "true"
        end

        def test?
          env == "test"
        end

        def dotcom?
          env == "dotcom"
        end

        def enterprise?
          env == "enterprise"
        end

        def development?
          env == "development"
        end

        def custom_domains_enabled?
          dotcom? || test?
        end

        def env
          env_var "PAGES_ENV", ENV["JEKYLL_ENV"]
        end

        def repo_pages_html_url_preview?
          env_var "PAGES_PREVIEW_HTML_URL"
        end

        def github_url
          if dotcom? || github_hostname == "github.com"
            "https://github.com"
          else
            "#{scheme}://#{github_hostname}"
          end
        end

        def api_url
          trim_last_slash env_var("PAGES_API_URL", ENV["API_URL"])
        end

        def help_url
          trim_last_slash env_var("PAGES_HELP_URL", ENV["HELP_URL"])
        end

        def github_hostname
          trim_last_slash env_var("PAGES_GITHUB_HOSTNAME", ENV["GITHUB_HOSTNAME"])
        end

        def pages_hostname
          intermediate_default = ENV["PAGES_HOSTNAME"]
          intermediate_default ||= "localhost:4000" if development?
          trim_last_slash env_var("PAGES_PAGES_HOSTNAME", intermediate_default)
        end

        def page_build?
          !env_var("PAGE_BUILD_ID").to_s.empty?
        end

        def configuration
          (methods - Object.methods - [:configuration]).sort.each_with_object({}) do |meth, memo|
            memo[meth.to_s] = public_send(meth)
          end
        end

        private

        def env_var(key, intermediate_default = nil)
          !ENV[key].to_s.empty? ? ENV[key] : (intermediate_default || DEFAULTS[key])
        end

        def trim_last_slash(url)
          if url[-1] == "/"
            url[0..-2]
          else
            url
          end
        end
      end
    end
  end
end
