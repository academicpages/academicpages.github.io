# -*- encoding: utf-8 -*-
# stub: jekyll-remote-theme 0.4.3 ruby lib

Gem::Specification.new do |s|
  s.name = "jekyll-remote-theme".freeze
  s.version = "0.4.3".freeze

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.require_paths = ["lib".freeze]
  s.authors = ["Ben Balter".freeze]
  s.date = "2021-03-10"
  s.email = ["ben.balter@github.com".freeze]
  s.homepage = "https://github.com/benbalter/jekyll-remote-theme".freeze
  s.licenses = ["MIT".freeze]
  s.required_ruby_version = Gem::Requirement.new(">= 2.3.0".freeze)
  s.rubygems_version = "3.2.14".freeze
  s.summary = "Jekyll plugin for building Jekyll sites with any GitHub-hosted theme".freeze

  s.installed_by_version = "3.6.9".freeze

  s.specification_version = 4

  s.add_runtime_dependency(%q<addressable>.freeze, ["~> 2.0".freeze])
  s.add_runtime_dependency(%q<jekyll>.freeze, [">= 3.5".freeze, "< 5.0".freeze])
  s.add_runtime_dependency(%q<jekyll-sass-converter>.freeze, [">= 1.0".freeze, "<= 3.0.0".freeze, "!= 2.0.0".freeze])
  s.add_runtime_dependency(%q<rubyzip>.freeze, [">= 1.3.0".freeze, "< 3.0".freeze])
  s.add_development_dependency(%q<jekyll-theme-primer>.freeze, ["~> 0.5".freeze])
  s.add_development_dependency(%q<jekyll_test_plugin_malicious>.freeze, ["~> 0.2".freeze])
  s.add_development_dependency(%q<kramdown-parser-gfm>.freeze, ["~> 1.0".freeze])
  s.add_development_dependency(%q<pry>.freeze, ["~> 0.11".freeze])
  s.add_development_dependency(%q<rspec>.freeze, ["~> 3.0".freeze])
  s.add_development_dependency(%q<rubocop>.freeze, ["~> 0.71".freeze])
  s.add_development_dependency(%q<rubocop-jekyll>.freeze, ["~> 0.10".freeze])
  s.add_development_dependency(%q<webmock>.freeze, ["~> 3.0".freeze])
end
