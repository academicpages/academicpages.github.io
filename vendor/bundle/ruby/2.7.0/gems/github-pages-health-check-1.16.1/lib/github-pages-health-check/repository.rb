# frozen_string_literal: true

module GitHubPages
  module HealthCheck
    class Repository < Checkable
      attr_reader :name, :owner

      REPO_REGEX = %r{\A[a-z0-9_\-]+/[a-z0-9_\-\.]+\z}i.freeze

      HASH_METHODS = %i[
        name_with_owner built? last_built build_duration build_error
      ].freeze

      def initialize(name_with_owner, access_token: nil)
        unless name_with_owner.match(REPO_REGEX)
          raise Errors::InvalidRepositoryError
        end

        parts = name_with_owner.split("/")
        @owner = parts.first
        @name  = parts.last
        @access_token = access_token || ENV["OCTOKIT_ACCESS_TOKEN"]
      end

      def name_with_owner
        @name_with_owner ||= [owner, name].join("/")
      end
      alias nwo name_with_owner

      def check!
        raise Errors::BuildError.new(:repository => self), build_error unless built?

        true
      end

      def last_build
        @last_build ||= client.latest_pages_build(name_with_owner)
      end

      def built?
        last_build && last_build.status == "built"
      end

      def build_error
        last_build.error["message"] unless built?
      end
      alias reason build_error

      def build_duration
        last_build && last_build.duration
      end

      def last_built
        last_build && last_build.updated_at
      end

      def domain
        return if cname.nil?

        @domain ||= GitHubPages::HealthCheck::Domain.redundant(cname)
      end

      private

      def client
        raise Errors::MissingAccessTokenError if @access_token.nil?

        @client ||= Octokit::Client.new(:access_token => @access_token)
      end

      def pages_info
        @pages_info ||= client.pages(name_with_owner)
      end

      def cname
        pages_info.cname
      end
    end
  end
end
