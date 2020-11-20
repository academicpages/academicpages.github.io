# frozen_string_literal: true

module GitHubPages
  module HealthCheck
    class Printer
      PRETTY_LEFT_WIDTH = 11
      PRETTY_JOINER = " | ".freeze

      attr_reader :health_check

      def initialize(health_check)
        @health_check = health_check
      end

      def simple_string
        require "yaml"
        hash = health_check.to_hash
        hash[:reason] = hash[:reason].to_s if hash[:reason]
        hash.to_yaml.sub(/\A---\n/, "").gsub(/^:/, "")
      end

      def pretty_print
        values = health_check.to_hash
        output = StringIO.new

        # Header
        output.puts new_line "Domain", (values[:uri]).to_s
        output.puts "-" * (PRETTY_LEFT_WIDTH + 1) + "|" + "-" * 50

        output.puts new_line "DNS", "does not resolve" unless values[:dns_resolves?]

        # Valid?
        output.write new_line "State", (values[:valid?] ? "valid" : "invalid").to_s
        output.puts " - is #{"NOT " unless values[:served_by_pages?]}served by Pages"

        # What's wrong?
        output.puts new_line "Reason", (values[:reason]).to_s unless values[:valid?]

        if values[:pointed_to_github_user_domain?]
          output.puts new_line nil, "pointed to user domain"
        end

        if values[:pointed_to_github_pages_ip?]
          output.puts new_line nil, "pointed to pages IP"
        end

        # DNS Record info
        record_type = if values[:a_record?]
                        "A"
                      elsif values[:cname_record?]
                        "CNAME"
                      else
                        "other"
                      end
        output.write new_line "Record Type", record_type
        should_be = values[:should_be_a_record?] ? "A record" : "CNAME"
        output.puts ", should be #{should_be}"

        ip_problems = []
        ip_problems << "not apex domain" unless values[:apex_domain?]
        ip_problems << "invalid domain" unless values[:valid_domain?]
        ip_problems << "old ip address used" if values[:old_ip_address?]

        ip_problems_string = !ip_problems.empty? ? ip_problems.join(", ") : "none"
        output.puts new_line "IP Problems", ip_problems_string

        if values[:proxied?]
          proxy = values[:cloudflare_ip?] ? "CloudFlare" : "unknown"
          output.puts new_line "Proxied", "yes, through #{proxy}"
        end

        output.puts new_line "Domain", "*.github.com/io domain" if values[:pages_domain?]

        output.string
      end

      def new_line(left = nil, right = nil)
        if left && right
          ljust(left) + PRETTY_JOINER + right
        elsif left
          ljust(left)
        elsif right
          " " * (PRETTY_LEFT_WIDTH + PRETTY_JOINER.size) + right
        end
      end

      def ljust(line)
        line.ljust(PRETTY_LEFT_WIDTH)
      end
    end
  end
end
