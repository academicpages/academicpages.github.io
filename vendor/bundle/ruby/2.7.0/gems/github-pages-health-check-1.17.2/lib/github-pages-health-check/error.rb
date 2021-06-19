# frozen_string_literal: true

module GitHubPages
  module HealthCheck
    class Error < StandardError
      DOCUMENTATION_BASE = "https://help.github.com"
      DOCUMENTATION_PATH = "/categories/github-pages-basics/"
      LOCAL_ONLY = false # Error is only used when running locally

      attr_reader :repository, :domain

      def initialize(repository: nil, domain: nil)
        super
        @repository = repository
        @domain     = domain
      end

      def self.inherited(base)
        subclasses << base
      end

      def self.subclasses
        @subclasses ||= []
      end

      def message
        "Something's wrong with your GitHub Pages site."
      end

      # Error message, with get more info URL appended
      def message_with_url
        msg = message.gsub(/\s+/, " ").squeeze(" ").strip
        msg << "." unless msg.end_with?(".") # add trailing period if not there
        "#{msg} #{more_info}"
      end
      alias message_formatted message_with_url

      def to_s
        "#{message_with_url} (#{name})".tr("\n", " ").squeeze(" ").strip
      end

      private

      def name
        self.class.name.split("::").last
      end

      def username
        if repository.nil?
          "[YOUR USERNAME]"
        else
          repository.owner
        end
      end

      def more_info
        "For more information, see #{documentation_url}."
      end

      def documentation_url
        URI.join(Error::DOCUMENTATION_BASE, self.class::DOCUMENTATION_PATH).to_s
      end
    end
  end
end
