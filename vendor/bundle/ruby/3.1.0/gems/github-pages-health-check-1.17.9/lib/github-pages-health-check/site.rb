# frozen_string_literal: true

module GitHubPages
  module HealthCheck
    class Site < Checkable
      attr_reader :repository, :domain

      def initialize(repository_or_domain, access_token: nil)
        @repository = Repository.new(repository_or_domain, :access_token => access_token)
        @domain = @repository.domain
      rescue GitHubPages::HealthCheck::Errors::InvalidRepositoryError
        @repository = nil
        @domain = Domain.redundant(repository_or_domain)
      end

      def check!
        [domain, repository].compact.each(&:check!)
        true
      end

      def to_hash
        hash = (domain || {}).to_hash.dup
        hash = hash.merge(repository.to_hash) unless repository.nil?
        hash[:valid?] = valid?
        hash[:reason] = reason
        hash
      end
      alias to_h to_hash
      alias as_json to_hash
    end
  end
end
