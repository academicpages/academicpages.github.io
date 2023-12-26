# frozen_string_literal: true

module GitHubPages
  module HealthCheck
    class CDN
      include Singleton

      # Internal: The path of the config file.
      attr_reader :name, :path

      # Public: Does cloudflare control this address?
      def self.controls_ip?(address)
        instance.controls_ip?(address)
      end

      # Internal: Create a new CDN info instance.
      def initialize(options = {})
        @name = options.fetch(:name) { self.class.name.split("::").last.downcase }
        @path = options.fetch(:path) { default_config_path }
      end

      # Internal: Does this CDN control this address?
      def controls_ip?(address)
        ranges.any? { |range| range.include?(address.to_s) }
      end

      private

      # Internal: The IP address ranges that cloudflare controls.
      def ranges
        @ranges ||= load_ranges
      end

      # Internal: Load IPAddr ranges from #path
      def load_ranges
        File.read(path).lines.map { |line| IPAddr.new(line.chomp) }
      end

      def default_config_path
        File.expand_path("../../config/#{name}-ips.txt", File.dirname(__FILE__))
      end
    end
  end
end
