# frozen_string_literal: true

module GitHubPages
  module HealthCheck
    class Domain < Checkable
      attr_reader :host, :resolver, :nameservers

      LEGACY_IP_ADDRESSES = [
        # Legacy GitHub Datacenter
        "207.97.227.245",
        "204.232.175.78",

        # Aug. 2016 Fastly datacenter deprecation
        "199.27.73.133",
        "199.27.76.133",

        # Feb. 2017 Fastly datacenter deprecation
        "103.245.222.133",
        "103.245.223.133",
        "103.245.224.133",
        "104.156.81.133",
        "104.156.82.133",
        "104.156.83.133",
        "104.156.85.133",
        "104.156.87.133",
        "104.156.88.133",
        "104.156.89.133",
        "104.156.90.133",
        "104.156.91.133",
        "104.156.92.133",
        "104.156.93.133",
        "104.156.94.133",
        "104.156.95.133",
        "104.37.95.133",
        "157.52.64.133",
        "157.52.66.133",
        "157.52.67.133",
        "157.52.68.133",
        "157.52.69.133",
        "157.52.96.133",
        "172.111.64.133",
        "172.111.96.133",
        "185.31.16.133",
        "185.31.17.133",
        "185.31.18.133",
        "185.31.19.133",
        "199.27.74.133",
        "199.27.75.133",
        "199.27.76.133",
        "199.27.78.133",
        "199.27.79.133",
        "23.235.33.133",
        "23.235.37.133",
        "23.235.39.133",
        "23.235.40.133",
        "23.235.41.133",
        "23.235.43.133",
        "23.235.44.133",
        "23.235.45.133",
        "23.235.46.133",
        "23.235.47.133",
        "23.235.47.133",
        "43.249.72.133",
        "43.249.73.133",
        "43.249.74.133",
        "43.249.75.133",

        # 2018 Move to GitHub assigned IP space
        "192.30.252.153",
        "192.30.252.154"
      ].freeze

      CURRENT_IP_ADDRESSES = %w(
        185.199.108.153
        185.199.109.153
        185.199.110.153
        185.199.111.153
      ).freeze

      CURRENT_IPV6_ADDRESSES = %w(
        2606:50c0:8000::153
        2606:50c0:8001::153
        2606:50c0:8002::153
        2606:50c0:8003::153
      ).freeze

      CURRENT_IP_ADDRESSES_ALL =
        (CURRENT_IP_ADDRESSES + CURRENT_IPV6_ADDRESSES).freeze

      HASH_METHODS = %i[
        host uri nameservers dns_resolves? proxied? cloudflare_ip?
        fastly_ip? old_ip_address? a_record? aaaa_record? a_record_present? aaaa_record_present?
        cname_record? mx_records_present? valid_domain? apex_domain?
        should_be_a_record? cname_to_github_user_domain?
        cname_to_pages_dot_github_dot_com? cname_to_fastly?
        pointed_to_github_pages_ip? non_github_pages_ip_present? pages_domain?
        served_by_pages? valid? reason valid_domain? https?
        enforces_https? https_error https_eligible? caa_error dns_zone_soa? dns_zone_ns?
      ].freeze

      def self.redundant(host)
        GitHubPages::HealthCheck::RedundantCheck.new(host).check
      end

      def initialize(host, nameservers: :default)
        unless host.is_a? String
          raise ArgumentError, "Expected string, got #{host.class}"
        end

        @host = normalize_host(host)
        @nameservers = nameservers
        @resolver = GitHubPages::HealthCheck::Resolver.new(self.host,
                                                           :nameservers => nameservers)
      end

      # Runs all checks, raises an error if invalid
      # rubocop:disable Metrics/AbcSize
      def check!
        raise Errors::InvalidDomainError.new :domain => self unless valid_domain?
        raise Errors::InvalidDNSError.new :domain => self    unless dns_resolves?
        raise Errors::DeprecatedIPError.new :domain => self  if deprecated_ip?
        return true if proxied?
        raise Errors::InvalidARecordError.new :domain => self    if invalid_a_record?
        raise Errors::InvalidCNAMEError.new :domain => self      if invalid_cname?
        raise Errors::InvalidAAAARecordError.new :domain => self if invalid_aaaa_record?
        raise Errors::NotServedByPagesError.new :domain => self  unless served_by_pages?

        true
      end
      # rubocop:enable Metrics/AbcSize

      def deprecated_ip?
        return @deprecated_ip if defined? @deprecated_ip

        @deprecated_ip = (valid_domain? && a_record? && old_ip_address?)
      end

      def invalid_aaaa_record?
        return @invalid_aaaa_record if defined? @invalid_aaaa_record

        @invalid_aaaa_record = (valid_domain? && aaaa_record_present? && !should_be_a_record?)
      end

      def invalid_a_record?
        return @invalid_a_record if defined? @invalid_a_record

        @invalid_a_record = (valid_domain? && a_record_present? && !should_be_a_record?)
      end

      def invalid_cname?
        return @invalid_cname if defined? @invalid_cname

        @invalid_cname = begin
          return false unless valid_domain?
          return false if github_domain? || apex_domain?
          return true  if cname_to_pages_dot_github_dot_com? || cname_to_fastly?

          !cname_to_github_user_domain? && should_be_cname_record?
        end
      end

      # Is this a valid domain that PublicSuffix recognizes?
      # Used as an escape hatch to prevent false positives on DNS checkes
      def valid_domain?
        return @valid if defined? @valid

        unicode_host = Addressable::IDNA.to_unicode(host)
        @valid = PublicSuffix.valid?(unicode_host,
                                     :default_rule => nil,
                                     :ignore_private => true)
      end

      # Is this domain an apex domain, meaning a CNAME would be innapropriate
      def apex_domain?
        return @apex_domain if defined?(@apex_domain)

        return false unless valid_domain?

        return true if dns_zone_soa? && dns_zone_ns?

        # PublicSuffix.domain pulls out the apex-level domain name.
        # E.g. PublicSuffix.domain("techblog.netflix.com") # => "netflix.com"
        # It's aware of multi-step top-level domain names:
        # E.g. PublicSuffix.domain("blog.digital.gov.uk") # => "digital.gov.uk"
        # For apex-level domain names, DNS providers do not support CNAME records.
        unicode_host = Addressable::IDNA.to_unicode(host)
        PublicSuffix.domain(unicode_host,
                            :default_rule => nil,
                            :ignore_private => true) == unicode_host
      end

      #
      # Does the domain have an associated SOA record?
      #
      def dns_zone_soa?
        return @soa_records if defined?(@soa_records)
        return false unless dns?

        @soa_records = dns.any? do |answer|
          answer.type == Dnsruby::Types::SOA && answer.name.to_s == host
        end
      end

      #
      # Does the domain have assoicated NS records?
      #
      def dns_zone_ns?
        return @ns_records if defined?(@ns_records)
        return false unless dns?

        @ns_records = dns.any? do |answer|
          answer.type == Dnsruby::Types::NS && answer.name.to_s == host
        end
      end

      # Should the domain use an A record?
      def should_be_a_record?
        !pages_io_domain? && (apex_domain? || mx_records_present?)
      end

      def should_be_cname_record?
        !should_be_a_record?
      end

      # Is the domain's first response an A or AAAA record to a valid GitHub Pages IP?
      def pointed_to_github_pages_ip?
        return false unless address_record?

        CURRENT_IP_ADDRESSES_ALL.include?(dns.first.address.to_s.downcase)
      end

      # Are any of the domain's A or AAAA records pointing elsewhere?
      def non_github_pages_ip_present?
        return unless dns?

        dns
          .select { |a| Dnsruby::Types::A == a.type || Dnsruby::Types::AAAA == a.type }
          .any? { |a| !github_pages_ip?(a.address.to_s) }
      end

      # Is the domain's first response a CNAME to a pages domain?
      def cname_to_github_user_domain?
        cname? && !cname_to_pages_dot_github_dot_com? && cname.pages_domain?
      end

      # Is the given domain a CNAME to pages.github.(io|com)
      # instead of being CNAME'd to the user's subdomain?
      #
      # domain - the domain to check, generaly the target of a cname
      def cname_to_pages_dot_github_dot_com?
        cname? && cname.pages_dot_github_dot_com?
      end

      # Is the given domain CNAME'd directly to our Fastly account?
      def cname_to_fastly?
        cname? && !pages_domain? && cname.fastly?
      end

      # Is the host a *.github.io domain?
      def pages_io_domain?
        !!host.match(/\A[\w-]+\.github\.(io)\.?\z/i)
      end

      # Is the host a *.github.(io|com) domain?
      def pages_domain?
        !!host.match(/\A[\w-]+\.github\.(io|com)\.?\z/i)
      end

      # Is the host pages.github.com or pages.github.io?
      def pages_dot_github_dot_com?
        !!host.match(/\Apages\.github\.(io|com)\.?\z/i)
      end

      # Is this domain owned by GitHub?
      def github_domain?
        !!host.downcase.end_with?("github.com")
      end

      # Is the host our Fastly CNAME?
      def fastly?
        !!host.match(/\A#{Regexp.union(Fastly::HOSTNAMES)}\z/i)
      end

      # Does the domain resolve to a CloudFlare-owned IP
      def cloudflare_ip?
        cdn_ip?(CloudFlare)
      end

      # Does the domain resolve to a Fastly-owned IP
      def fastly_ip?
        cdn_ip?(Fastly)
      end

      # Does this non-GitHub-pages domain proxy a GitHub Pages site?
      #
      # This can be:
      #   1. A Cloudflare-owned IP address
      #   2. A site that returns GitHub.com server headers, but
      #      isn't CNAME'd to a GitHub domain
      #   3. A site that returns GitHub.com server headers, but
      #      isn't CNAME'd to a GitHub IP
      def proxied?
        return unless dns?
        return true if cloudflare_ip?
        return false if pointed_to_github_pages_ip?
        return false if cname_to_github_user_domain?
        return false if cname_to_pages_dot_github_dot_com?
        return false if cname_to_fastly? || fastly_ip?

        served_by_pages?
      end

      REQUESTED_RECORD_TYPES = [
        Dnsruby::Types::A,
        Dnsruby::Types::AAAA,
        Dnsruby::Types::CNAME,
        Dnsruby::Types::MX,
        Dnsruby::Types::NS,
        Dnsruby::Types::SOA
      ].freeze

      # Returns an array of DNS answers
      def dns
        return @dns if defined? @dns
        return unless valid_domain?

        @dns = Timeout.timeout(TIMEOUT) do
          GitHubPages::HealthCheck.without_warnings do
            next if host.nil?

            REQUESTED_RECORD_TYPES
              .map { |type| resolver.query(type) }
              .flatten.uniq
          end
        end
      rescue StandardError
        @dns = nil
      end

      # Are we even able to get the DNS record?
      def dns?
        !(dns.nil? || dns.empty?)
      end
      alias dns_resolves? dns?

      # Does this domain have *any* A record that points to the legacy IPs?
      def old_ip_address?
        return unless dns?

        dns.any? do |answer|
          answer.type == Dnsruby::Types::A && legacy_ip?(answer.address.to_s)
        end
      end

      # Is this domain's first response an A record?
      def a_record?
        return @is_a_record if defined?(@is_a_record)
        return unless dns?

        @is_a_record = Dnsruby::Types::A == dns.first.type
      end

      # Is this domain's first response an AAAA record?
      def aaaa_record?
        return @is_aaaa_record if defined?(@is_aaaa_record)
        return unless dns?

        @is_aaaa_record = Dnsruby::Types::AAAA == dns.first.type
      end

      # Does this domain has an A record setup (not necessarily as the first record)?
      def a_record_present?
        return unless dns?

        dns.any? { |answer| answer.type == Dnsruby::Types::A && answer.name.to_s == host }
      end

      # Does this domain has an AAAA record setup (not necessarily as the first record)?
      def aaaa_record_present?
        return unless dns?

        dns.any? { |answer| answer.type == Dnsruby::Types::AAAA && answer.name.to_s == host }
      end

      # Is this domain's first response a CNAME record?
      def cname_record?
        return unless dns?
        return false unless cname

        cname.valid_domain?
      end
      alias cname? cname_record?

      # The domain to which this domain's CNAME resolves
      # Returns nil if the domain is not a CNAME
      def cname
        return unless dns?

        cnames = dns.take_while { |answer| answer.type == Dnsruby::Types::CNAME }
        return if cnames.empty?

        @cname ||= Domain.new(cnames.last.cname.to_s)
      end

      def mx_records_present?
        return unless dns?

        dns.any? { |answer| answer.type == Dnsruby::Types::MX }
      end

      def served_by_pages?
        return @served_by_pages if defined? @served_by_pages
        return unless dns_resolves?

        @served_by_pages = begin
          return true if response.headers["Server"] == "GitHub.com"

          # Typhoeus mangles the case of the header, compare insensitively
          response.headers.any? { |k, _v| k.downcase == "x-github-request-id" }
        end
      end

      def uri(overrides = {})
        options = { :host => host, :scheme => scheme, :path => "/" }
        options = options.merge(overrides)
        Addressable::URI.new(options).normalize.to_s
      end

      # Does this domain respond to HTTPS requests with a valid cert?
      def https?
        https_response.return_code == :ok
      end

      # The response code of the HTTPS request, if it failed.
      # Useful for diagnosing cert errors
      def https_error
        https_response.return_code unless https?
      end

      # Does this domain redirect HTTP requests to HTTPS?
      def enforces_https?
        return false unless https? && http_response.headers["Location"]

        redirect = Addressable::URI.parse(http_response.headers["Location"])
        redirect.scheme == "https" && redirect.host == host
      end

      # Can an HTTPS certificate be issued for this domain?
      def https_eligible?
        # Can't have any IP's which aren't GitHub's present.
        return false if non_github_pages_ip_present?
        # Must be a CNAME or point to our IPs.

        # Only check the one domain if a CNAME. Don't check the parent domain.
        return true if cname_to_github_user_domain?

        # Check CAA records for the full domain and its parent domain.
        pointed_to_github_pages_ip? && caa.lets_encrypt_allowed?
      end

      # Any errors querying CAA records
      def caa_error
        return nil unless caa&.errored?

        caa.error.class.name
      end

      private

      def address_record?
        a_record? || aaaa_record?
      end

      def caa
        @caa ||= GitHubPages::HealthCheck::CAA.new(
          :host => cname&.host || host,
          :nameservers => nameservers
        )
      end

      # The domain's response to HTTP(S) requests, following redirects
      def response
        return @response if defined? @response

        @response = Typhoeus.head(uri, TYPHOEUS_OPTIONS)

        # Workaround for webmock not playing nicely with Typhoeus redirects
        # See https://github.com/bblimke/webmock/issues/237
        if @response.mock? && @response.headers["Location"]
          @response = Typhoeus.head(response.headers["Location"], TYPHOEUS_OPTIONS)
        end

        @response
      end

      # The domain's response to HTTP requests, without following redirects
      def http_response
        options = TYPHOEUS_OPTIONS.merge(:followlocation => false)
        @http_response ||= Typhoeus.head(uri(:scheme => "http"), options)
      end

      # The domain's response to HTTPS requests, without following redirects
      def https_response
        options = TYPHOEUS_OPTIONS.merge(:followlocation => false)
        @https_response ||= Typhoeus.head(uri(:scheme => "https"), options)
      end

      # Parse the URI. Accept either domain names or full URI's.
      # Used by the initializer so we can be more flexible with inputs.
      #
      # domain - a URI or domain name.
      #
      # Examples
      #
      #   normalize_host("benbalter.github.com")
      #   # => 'benbalter.github.com'
      #   normalize_host("https://benbalter.github.com")
      #   # => 'benbalter.github.com'
      #   normalize_host("benbalter.github.com/help-me-im-a-path/")
      #   # => 'benbalter.github.com'
      #
      # Return the hostname.
      def normalize_host(domain)
        domain = domain.strip.chomp(".")
        host = Addressable::URI.parse(domain).normalized_host
        host ||= Addressable::URI.parse("http://#{domain}").normalized_host
        host unless host.to_s.empty?
      rescue Addressable::URI::InvalidURIError
        nil
      end

      # Adjust `domain` so that it won't be searched for with /etc/resolv.conf
      #
      #     GitHubPages::HealthCheck.new("anything.io").absolute_domain
      #     => "anything.io."
      def absolute_domain
        host.end_with?(".") ? host : "#{host}."
      end

      def scheme
        @scheme ||= github_domain? ? "https" : "http"
      end

      # Does the domain resolve to a CDN-owned IP
      def cdn_ip?(cdn)
        return unless dns?

        address_records = dns.select do |answer|
          Dnsruby::Types::A == answer.type || Dnsruby::Types::AAAA == answer.type
        end
        return false if !address_records || address_records.empty?

        address_records.all? do |answer|
          cdn.controls_ip?(answer.address)
        end
      end

      def legacy_ip?(ip_addr)
        LEGACY_IP_ADDRESSES.include?(ip_addr)
      end

      def github_pages_ip?(ip_addr)
        CURRENT_IP_ADDRESSES_ALL.include?(ip_addr&.to_s&.downcase)
      end
    end
  end
end
