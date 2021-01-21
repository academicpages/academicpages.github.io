# frozen_string_literal: true

require "dnsruby"
require "addressable/idna"
require "addressable/uri"
require "ipaddr"
require "public_suffix"
require "singleton"
require "net/http"
require "typhoeus"
require "resolv"
require "timeout"
require "octokit"
require_relative "github-pages-health-check/version"

if File.exist?(File.expand_path("../.env", File.dirname(__FILE__)))
  require "dotenv"
  Dotenv.load
end

module GitHubPages
  module HealthCheck
    autoload :CDN,            "github-pages-health-check/cdn"
    autoload :CloudFlare,     "github-pages-health-check/cdns/cloudflare"
    autoload :Fastly,         "github-pages-health-check/cdns/fastly"
    autoload :Error,          "github-pages-health-check/error"
    autoload :Errors,         "github-pages-health-check/errors"
    autoload :CAA,            "github-pages-health-check/caa"
    autoload :Checkable,      "github-pages-health-check/checkable"
    autoload :Domain,         "github-pages-health-check/domain"
    autoload :RedundantCheck, "github-pages-health-check/redundant_check"
    autoload :Repository,     "github-pages-health-check/repository"
    autoload :Resolver,       "github-pages-health-check/resolver"
    autoload :Site,           "github-pages-health-check/site"
    autoload :Printer,        "github-pages-health-check/printer"

    # DNS and HTTP timeout, in seconds
    TIMEOUT = 7

    HUMAN_NAME = "GitHub Pages Health Check".freeze
    URL = "https://github.com/github/pages-health-check".freeze
    USER_AGENT = "Mozilla/5.0 (compatible; #{HUMAN_NAME}/#{VERSION}; +#{URL})".freeze

    TYPHOEUS_OPTIONS = {
      :followlocation => true,
      :timeout => TIMEOUT,
      :accept_encoding => "gzip",
      :method => :head,
      :headers => {
        "User-Agent" => USER_AGENT
      }
    }.freeze

    # surpress warn-level feedback due to unsupported record types
    def self.without_warnings(&block)
      warn_level = $VERBOSE
      $VERBOSE = nil
      result = block.call
      $VERBOSE = warn_level
      result
    end

    def self.check(repository_or_domain, access_token: nil)
      Site.new repository_or_domain, :access_token => access_token
    end
  end
end
