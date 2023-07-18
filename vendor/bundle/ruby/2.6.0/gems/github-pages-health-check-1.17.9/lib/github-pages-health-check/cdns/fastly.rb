# frozen_string_literal: true

module GitHubPages
  module HealthCheck
    # Instance of the Fastly CDN for checking IP ownership
    # Specifically not namespaced to avoid a breaking change
    class Fastly < CDN
      # Fastly maps used by GitHub Pages.
      HOSTNAMES = %w(
        github.map.fastly.net
        github.map.fastly.net.
        sni.github.map.fastly.net
        sni.github.map.fastly.net.
      ).freeze
    end
  end
end
