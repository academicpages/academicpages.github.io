# frozen_string_literal: true

module GitHubPages
  module HealthCheck
    module Errors
      class MissingAccessTokenError < GitHubPages::HealthCheck::Error
        LOCAL_ONLY = true
        def message
          "Cannot retrieve repository information with a valid access token"
        end
      end
    end
  end
end
