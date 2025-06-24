# frozen_string_literal: true

require 'openssl'
require 'uri'

module HTML
  class Pipeline
    # HTML Filter for replacing http image URLs with camo versions. See:
    #
    # https://github.com/atmos/camo
    #
    # All images provided in user content should be run through this
    # filter so that http image sources do not cause mixed-content warnings
    # in browser clients.
    #
    # Context options:
    #   :asset_proxy (required) - Base URL for constructed asset proxy URLs.
    #   :asset_proxy_secret_key (required) - The shared secret used to encode URLs.
    #   :asset_proxy_allowlist - Array of host Strings or Regexps to skip
    #                            src rewriting.
    #
    # This filter does not write additional information to the context.
    class CamoFilter < Filter
      # Hijacks images in the markup provided, replacing them with URLs that
      # go through the github asset proxy.
      def call
        return doc unless asset_proxy_enabled?

        doc.search('img').each do |element|
          original_src = element['src']
          next unless original_src

          begin
            uri = URI.parse(original_src)
          rescue Exception
            next
          end

          next if uri.host.nil?
          next if asset_host_allowed?(uri.host)

          element['src'] = asset_proxy_url(original_src)
          element['data-canonical-src'] = original_src
        end
        doc
      end

      # Implementation of validate hook.
      # Errors should raise exceptions or use an existing validator.
      def validate
        needs :asset_proxy, :asset_proxy_secret_key
      end

      # The camouflaged URL for a given image URL.
      def asset_proxy_url(url)
        "#{asset_proxy_host}/#{asset_url_hash(url)}/#{hexencode(url)}"
      end

      # Private: calculate the HMAC digest for a image source URL.
      def asset_url_hash(url)
        OpenSSL::HMAC.hexdigest('sha1', asset_proxy_secret_key, url)
      end

      # Private: Return true if asset proxy filter should be enabled
      def asset_proxy_enabled?
        !context[:disable_asset_proxy]
      end

      # Private: the host to use for generated asset proxied URLs.
      def asset_proxy_host
        context[:asset_proxy]
      end

      def asset_proxy_secret_key
        context[:asset_proxy_secret_key]
      end

      def asset_proxy_whitelist
        warn "[DEPRECATION] 'asset_proxy_whitelist' is deprecated. Please use 'asset_proxy_allowlist' instead."
        asset_proxy_allowlist
      end

      def asset_proxy_allowlist
        context[:asset_proxy_allowlist] || context[:asset_proxy_whitelist] || []
      end

      def asset_host_whitelisted?(host)
        warn "[DEPRECATION] 'asset_host_whitelisted?' is deprecated. Please use 'asset_host_allowed?' instead."
        asset_host_allowed?(host)
      end

      def asset_host_allowed?(host)
        asset_proxy_allowlist.any? do |test|
          test.is_a?(String) ? host == test : test.match(host)
        end
      end

      # Private: helper to hexencode a string. Each byte ends up encoded into
      # two characters, zero padded value in the range [0-9a-f].
      def hexencode(str)
        str.unpack('H*').first
      end
    end
  end
end
