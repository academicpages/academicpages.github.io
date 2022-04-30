# frozen_string_literal: true

require "jekyll"
require "octokit"

if Jekyll.env == "development"
  begin
    require "dotenv"
    Dotenv.load
  rescue LoadError
    Jekyll.logger.debug "Dotenv not found. Skipping"
  end
end

module Jekyll
  module GitHubMetadata
    autoload :Client,           "jekyll-github-metadata/client"
    autoload :EditLinkTag,      "jekyll-github-metadata/edit-link-tag"
    autoload :MetadataDrop,     "jekyll-github-metadata/metadata_drop"
    autoload :Owner,            "jekyll-github-metadata/owner"
    autoload :Pages,            "jekyll-github-metadata/pages"
    autoload :Repository,       "jekyll-github-metadata/repository"
    autoload :RepositoryFinder, "jekyll-github-metadata/repository_finder"
    autoload :RepositoryCompat, "jekyll-github-metadata/repository_compat"
    autoload :Sanitizer,        "jekyll-github-metadata/sanitizer"
    autoload :Value,            "jekyll-github-metadata/value"
    autoload :VERSION,          "jekyll-github-metadata/version"

    NoRepositoryError = RepositoryFinder::NoRepositoryError

    require_relative "jekyll-github-metadata/site_github_munger" if Jekyll.const_defined? :Site

    class << self
      attr_reader :repository_finder
      attr_writer :client, :logger

      def site
        repository_finder.site
      end

      def environment
        Jekyll.env
      end

      def logger
        @logger ||= Jekyll.logger
      end

      def log(severity, message)
        if logger.method(severity).arity.abs >= 2
          logger.public_send(severity, "GitHub Metadata:", message.to_s)
        else
          logger.public_send(severity, "GitHub Metadata: #{message}")
        end
      end

      def client
        @client ||= Client.new
      end

      def repository
        @repository ||= GitHubMetadata::Repository.new(repository_finder.nwo).tap do |repo|
          log :debug, "Generating for #{repo.nwo}"
        end
      end

      def site=(new_site)
        reset!
        @repository_finder = GitHubMetadata::RepositoryFinder.new(new_site)
      end

      def reset!
        @logger = @client = @repository = @nwo = @site = nil
      end
    end
  end
end

Liquid::Template.register_tag("github_edit_link", Jekyll::GitHubMetadata::EditLinkTag)
