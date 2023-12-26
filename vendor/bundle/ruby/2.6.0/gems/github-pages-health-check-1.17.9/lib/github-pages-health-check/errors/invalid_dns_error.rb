# frozen_string_literal: true

module GitHubPages
  module HealthCheck
    module Errors
      class InvalidDNSError < GitHubPages::HealthCheck::Error
        DOCUMENTATION_PATH = "/articles/setting-up-a-custom-domain-with-github-pages/"

        def message
          "Domain's DNS record could not be retrieved"
        end
      end
    end
  end
end
