# -*- encoding: utf-8 -*-
# stub: jekyll-optional-front-matter 0.3.2 ruby lib

Gem::Specification.new do |s|
  s.name = "jekyll-optional-front-matter".freeze
  s.version = "0.3.2".freeze

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.require_paths = ["lib".freeze]
  s.authors = ["Ben Balter".freeze]
  s.date = "2019-10-23"
  s.email = ["ben.balter@github.com".freeze]
  s.homepage = "https://github.com/benbalter/jekyll-optional-front-matter".freeze
  s.licenses = ["MIT".freeze]
  s.rubygems_version = "3.0.6".freeze
  s.summary = "A Jekyll plugin to make front matter optional for Markdown files".freeze

  s.installed_by_version = "3.6.9".freeze

  s.specification_version = 4

  s.add_runtime_dependency(%q<jekyll>.freeze, [">= 3.0".freeze, "< 5.0".freeze])
  s.add_development_dependency(%q<rspec>.freeze, ["~> 3.5".freeze])
  s.add_development_dependency(%q<rubocop>.freeze, ["~> 0.71".freeze])
  s.add_development_dependency(%q<rubocop-jekyll>.freeze, ["~> 0.10".freeze])
end
