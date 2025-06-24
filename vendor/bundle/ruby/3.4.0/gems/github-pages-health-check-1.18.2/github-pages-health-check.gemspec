# frozen_string_literal: true

require File.expand_path("lib/github-pages-health-check/version", __dir__)

Gem::Specification.new do |s|
  s.required_ruby_version = ">= 2.2.0"

  s.name                  = "github-pages-health-check"
  s.version               = GitHubPages::HealthCheck::VERSION
  s.summary               = "Checks your GitHub Pages site for commons DNS configuration issues"
  s.description           = "Checks your GitHub Pages site for commons DNS configuration issues."
  s.authors               = "GitHub, Inc."
  s.email                 = "support@github.com"
  s.homepage              = "https://github.com/github/github-pages-health-check"
  s.license               = "MIT"
  s.files                 = `git ls-files -z`.split("\x0").reject { |f| f.match(%r{^(test|spec|features)/}) }
  s.require_paths         = ["lib"]

  s.add_dependency("addressable", "~> 2.3")
  s.add_dependency("dnsruby", "~> 1.60")
  s.add_dependency("octokit", ">= 4", "< 8")
  s.add_dependency("public_suffix", ">= 3.0", "< 6.0")
  s.add_dependency("typhoeus", "~> 1.3")
end
