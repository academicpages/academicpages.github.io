# frozen_string_literal: true

module GitHubPages
  module HealthCheck
    module Errors
      class BuildError < GitHubPages::HealthCheck::Error
        DOCUMENTATION_PATH = "/articles/troubleshooting-jekyll-builds/".freeze
        LOCAL_ONLY = true
      end
    end
  end
end
