# frozen_string_literal: true

module GitHubPages
  module HealthCheck
    module Errors
      class InvalidDomainError < GitHubPages::HealthCheck::Error
        DOCUMENTATION_PATH = "/articles/setting-up-a-custom-domain-with-github-pages/"

        def message
          "Domain is not a valid domain"
        end
      end
    end
  end
end
