# frozen_string_literal: true

module GitHubPages
  module HealthCheck
    class Resolver
      DEFAULT_RESOLVER_OPTIONS = {
        :retry_times => 2,
        :query_timeout => 5,
        :dnssec => false,
        :do_caching => false
      }.freeze
      PUBLIC_NAMESERVERS = %w(
        8.8.8.8
        1.1.1.1
      ).freeze

      class << self
        def default_resolver
          @default_resolver ||= Dnsruby::Resolver.new(DEFAULT_RESOLVER_OPTIONS)
        end
      end

      attr_reader :domain, :nameservers

      # Create a new resolver.
      #
      # domain - the domain we're getting answers for
      # nameserver - (optional) a case
      def initialize(domain, nameservers: :default)
        @domain = domain
        @nameservers = nameservers
      end

      def query(type)
        resolver.query(Addressable::IDNA.to_ascii(domain), type).answer
      end

      private

      def resolver
        @resolver ||= case nameservers
                      when :default
                        self.class.default_resolver
                      when :authoritative
                        Dnsruby::Resolver.new(DEFAULT_RESOLVER_OPTIONS.merge(
                          :nameservers => authoritative_nameservers
                        ))
                      when :public
                        Dnsruby::Resolver.new(DEFAULT_RESOLVER_OPTIONS.merge(
                          :nameservers => PUBLIC_NAMESERVERS
                        ))
                      when Array
                        Dnsruby::Resolver.new(DEFAULT_RESOLVER_OPTIONS.merge(
                          :nameservers => nameservers
                        ))
                      else
                        raise "Invalid nameserver type: #{nameservers.inspect}"
                      end
      end

      def authoritative_nameservers
        @authoritative_nameservers ||= begin
          self.class.default_resolver.query(domain, Dnsruby::Types::NS).answer.map do |rr|
            next rr.nsdname.to_s if rr.type == Dnsruby::Types::NS
          end.compact
        end
      end
    end
  end
end
