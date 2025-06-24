# frozen_string_literal: true

module GitHubPages
  module HealthCheck
    module Errors
      class DeprecatedIPError < GitHubPages::HealthCheck::Error
        DOCUMENTATION_PATH = "/articles/setting-up-a-custom-domain-with-github-pages/"

        def message
          <<-MSG
            The custom domain for your GitHub Pages site is pointed at an outdated IP address.
            You must update your site's DNS records if you'd like it to be available via your custom domain.
          MSG
        end
      end
    end
  end
end
