# frozen_string_literal: true

module GitHubPages
  module HealthCheck
    module Errors
      class InvalidRepositoryError < GitHubPages::HealthCheck::Error
        LOCAL_ONLY = true
        def message
          "Repository is not a valid repository"
        end
      end
    end
  end
end
