# frozen_string_literal: true

module GitHubPages
  module HealthCheck
    class RedundantCheck
      extend Forwardable

      TIMEOUT = 5 # seconds

      attr_reader :domain

      def initialize(domain)
        @domain = domain
      end

      def check
        @check ||= (checks.find(&:valid?) || check_with_default_nameservers)
      end

      def_delegator :check, :reason, :reason
      def_delegator :check, :valid?, :valid?

      def https_eligible?
        checks.any?(&:https_eligible?)
      end

      private

      def checks
        @checks ||= %i[default authoritative public].map do |ns|
          GitHubPages::HealthCheck::Domain.new(domain, :nameservers => ns)
        end
      end

      def check_with_default_nameservers
        @check_with_default_nameservers ||= checks.find { |c| c.nameservers == :default }
      end

      def check_with_public_nameservers
        @check_with_public_nameservers ||= checks.find { |c| c.nameservers == :public }
      end
    end
  end
end
