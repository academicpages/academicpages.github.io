# frozen_string_literal: true

module GitHubPages
  module HealthCheck
    module Errors
      class InvalidAAAARecordError < GitHubPages::HealthCheck::Error
        DOCUMENTATION_PATH = "/articles/setting-up-a-custom-domain-with-github-pages/"

        def message
          <<-MSG
             Your site's DNS settings are using a custom subdomain, #{domain.host},
             that's set up with an AAAA record. GitHub Pages currently does not support
             IPv6.
          MSG
        end
      end
    end
  end
end
