# frozen_string_literal: true

module GitHubPages
  module HealthCheck
    module Errors
      class InvalidAAAARecordError < GitHubPages::HealthCheck::Error
        DOCUMENTATION_PATH = "/articles/setting-up-a-custom-domain-with-github-pages/"

        def message
          <<-MSG
          Your site's DNS settings are using a custom subdomain, #{domain.host},
          that's set up as an AAAA record. We recommend you change this to a CNAME
          record pointing at #{username}.github.io.
          MSG
        end
      end
    end
  end
end
