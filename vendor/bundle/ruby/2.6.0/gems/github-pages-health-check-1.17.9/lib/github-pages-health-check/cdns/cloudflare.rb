# frozen_string_literal: true

module GitHubPages
  module HealthCheck
    # Instance of the CloudFlare CDN for checking IP ownership
    # Specifically not namespaced to avoid a breaking change
    class CloudFlare < CDN
    end
  end
end
