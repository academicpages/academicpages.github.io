# frozen_string_literal: true

module GitHubPages
  module HealthCheck
    module Errors
      class NotServedByPagesError < GitHubPages::HealthCheck::Error
        DOCUMENTATION_PATH = "/articles/setting-up-a-custom-domain-with-github-pages/"

        def message
          "Domain does not resolve to the GitHub Pages server"
        end
      end
    end
  end
end
