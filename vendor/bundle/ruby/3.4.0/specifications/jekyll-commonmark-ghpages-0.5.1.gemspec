# -*- encoding: utf-8 -*-
# stub: jekyll-commonmark-ghpages 0.5.1 ruby lib

Gem::Specification.new do |s|
  s.name = "jekyll-commonmark-ghpages".freeze
  s.version = "0.5.1".freeze

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.require_paths = ["lib".freeze]
  s.authors = ["GitHub, Inc.".freeze]
  s.date = "2024-07-18"
  s.email = "support@github.com".freeze
  s.homepage = "https://github.com/github/jekyll-commonmark-ghpages".freeze
  s.licenses = ["MIT".freeze]
  s.rubygems_version = "3.5.11".freeze
  s.summary = "CommonMark generator for Jekyll".freeze

  s.installed_by_version = "3.6.9".freeze

  s.specification_version = 4

  s.add_runtime_dependency(%q<jekyll>.freeze, [">= 3.9".freeze, "< 4.0".freeze])
  s.add_runtime_dependency(%q<jekyll-commonmark>.freeze, ["~> 1.4.0".freeze])
  s.add_runtime_dependency(%q<commonmarker>.freeze, [">= 0.23.7".freeze, "< 1.1.0".freeze])
  s.add_runtime_dependency(%q<rouge>.freeze, [">= 2.0".freeze, "< 5.0".freeze])
  s.add_development_dependency(%q<rspec>.freeze, ["~> 3.0".freeze])
  s.add_development_dependency(%q<rake>.freeze, [">= 0".freeze])
end
