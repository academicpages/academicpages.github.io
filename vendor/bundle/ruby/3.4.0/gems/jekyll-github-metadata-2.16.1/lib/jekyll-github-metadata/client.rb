# frozen_string_literal: true

require "digest"

module Jekyll
  module GitHubMetadata
    class Client
      InvalidMethodError = Class.new(NoMethodError)
      BadCredentialsError = Class.new(StandardError)

      # Whitelisted API calls.
      API_CALLS = Set.new(%w(
        repository
        organization
        user
        repository?
        pages
        contributors
        releases
        latest_release
        list_repos
        organization_public_members
      ))

      def initialize(options = nil)
        @client = build_octokit_client(options)
      end

      def safe_require(gem_name)
        require gem_name
        true
      rescue LoadError
        false
      end

      def default_octokit_options
        {
          :api_endpoint  => Jekyll::GitHubMetadata::Pages.api_url,
          :web_endpoint  => Jekyll::GitHubMetadata::Pages.github_url,
          :auto_paginate => true,
        }
      end

      def build_octokit_client(options = nil)
        options ||= {}
        options.merge!(pluck_auth_method) unless options.key?(:access_token)
        Octokit::Client.new(default_octokit_options.merge(options))
      end

      def accepts_client_method?(method_name)
        API_CALLS.include?(method_name.to_s) && @client.respond_to?(method_name)
      end

      def respond_to_missing?(method_name, include_private = false)
        accepts_client_method?(method_name) || super
      end

      def method_missing(method_name, *args, &block)
        method = method_name.to_s
        if accepts_client_method?(method_name)
          key = cache_key(method_name, args)
          GitHubMetadata.log :debug, "Calling @client.#{method}(#{args.map(&:inspect).join(", ")})"
          cache[key] ||= save_from_errors { @client.public_send(method_name, *args, &block) }
        elsif @client.respond_to?(method_name)
          raise InvalidMethodError, "#{method_name} is not whitelisted on #{inspect}"
        else
          super
        end
      end

      # NOTE: Faraday's error classes have been simplified from v1.0.0.
      #
      # In older versions, both `Faraday::Error::ConnectionFailed` and `Faraday::ConnectionFailed`
      # were valid and equivalent to each other.
      # From v1.0.0 onwards, `Faraday::Error::ConnectionFailed` no longer exists.
      #
      # TODO: Remove in v2.0 of this plugin.
      FARADAY_FAILED_CONNECTION =
        begin
          Faraday::Error::ConnectionFailed
        rescue NameError
          Faraday::ConnectionFailed
        end
      deprecate_constant :FARADAY_FAILED_CONNECTION

      def save_from_errors(default = false)
        unless internet_connected?
          GitHubMetadata.log :warn, "No internet connection. GitHub metadata may be missing or incorrect."
          return default
        end

        yield @client
      rescue Octokit::Unauthorized
        raise BadCredentialsError, "The GitHub API credentials you provided aren't valid."
      rescue Faraday::ConnectionFailed, Octokit::TooManyRequests => e
        GitHubMetadata.log :warn, e.message
        default
      rescue Octokit::NotFound
        default
      end

      def inspect
        "#<#{self.class.name} @client=#{client_inspect} @internet_connected=#{internet_connected?}>"
      end

      def authenticated?
        !@client.access_token.to_s.empty?
      end

      def internet_connected?
        return @internet_connected if defined?(@internet_connected)

        require "resolv"
        begin
          Resolv::DNS.open do |dns|
            dns.timeouts = 2
            dns.getaddress("api.github.com")
          end
          @internet_connected = true
        rescue Resolv::ResolvError
          @internet_connected = false
        end
      end

      private

      def client_inspect
        if @client.nil?
          "nil"
        else
          "#<#{@client.class.name} (#{"un" unless authenticated?}authenticated)>"
        end
      end

      # rubocop:disable Metrics/CyclomaticComplexity
      def pluck_auth_method
        if ENV["JEKYLL_GITHUB_TOKEN"] || Octokit.access_token
          { :access_token => ENV["JEKYLL_GITHUB_TOKEN"] || Octokit.access_token }
        elsif !ENV["NO_NETRC"] && File.exist?(File.join(Dir.home, ".netrc")) && safe_require("netrc")
          { :netrc => true }
        else
          GitHubMetadata.log :warn, "No GitHub API authentication could be found. " \
                                    "Some fields may be missing or have incorrect data."
          {}.freeze
        end
      end
      # rubocop:enable Metrics/CyclomaticComplexity

      def cache_key(method, *args)
        Digest::SHA1.hexdigest(method.to_s + args.join(", "))
      end

      def cache
        @cache ||= {}
      end
    end
  end
end
