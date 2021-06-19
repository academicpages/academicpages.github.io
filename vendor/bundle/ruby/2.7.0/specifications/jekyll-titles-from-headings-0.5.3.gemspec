# -*- encoding: utf-8 -*-
# stub: jekyll-titles-from-headings 0.5.3 ruby lib

Gem::Specification.new do |s|
  s.name = "jekyll-titles-from-headings".freeze
  s.version = "0.5.3"

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.require_paths = ["lib".freeze]
  s.authors = ["Ben Balter".freeze]
  s.date = "2019-10-23"
  s.email = ["ben.balter@github.com".freeze]
  s.homepage = "https://github.com/benbalter/jekyll-titles-from-headings".freeze
  s.licenses = ["MIT".freeze]
  s.rubygems_version = "3.1.2".freeze
  s.summary = "A Jekyll plugin to pull the page title from the first Markdown heading when none is specified.".freeze

  s.installed_by_version = "3.1.2" if s.respond_to? :installed_by_version

  if s.respond_to? :specification_version then
    s.specification_version = 4
  end

  if s.respond_to? :add_runtime_dependency then
    s.add_runtime_dependency(%q<jekyll>.freeze, [">= 3.3", "< 5.0"])
    s.add_development_dependency(%q<rspec>.freeze, ["~> 3.5"])
    s.add_development_dependency(%q<rubocop>.freeze, ["~> 0.71"])
    s.add_development_dependency(%q<rubocop-jekyll>.freeze, ["~> 0.10"])
  else
    s.add_dependency(%q<jekyll>.freeze, [">= 3.3", "< 5.0"])
    s.add_dependency(%q<rspec>.freeze, ["~> 3.5"])
    s.add_dependency(%q<rubocop>.freeze, ["~> 0.71"])
    s.add_dependency(%q<rubocop-jekyll>.freeze, ["~> 0.10"])
  end
end
