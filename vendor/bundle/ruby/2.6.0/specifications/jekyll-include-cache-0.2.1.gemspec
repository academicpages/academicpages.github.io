# -*- encoding: utf-8 -*-
# stub: jekyll-include-cache 0.2.1 ruby lib

Gem::Specification.new do |s|
  s.name = "jekyll-include-cache".freeze
  s.version = "0.2.1"

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.require_paths = ["lib".freeze]
  s.authors = ["Ben Balter".freeze]
  s.date = "2020-10-08"
  s.email = ["ben.balter@github.com".freeze]
  s.homepage = "https://github.com/benbalter/jekyll-include-cache".freeze
  s.licenses = ["MIT".freeze]
  s.rubygems_version = "3.0.3.1".freeze
  s.summary = "A Jekyll plugin to cache the rendering of Liquid includes".freeze

  s.installed_by_version = "3.0.3.1" if s.respond_to? :installed_by_version

  if s.respond_to? :specification_version then
    s.specification_version = 4

    if Gem::Version.new(Gem::VERSION) >= Gem::Version.new('1.2.0') then
      s.add_runtime_dependency(%q<jekyll>.freeze, [">= 3.7", "< 5.0"])
      s.add_development_dependency(%q<rspec>.freeze, ["~> 3.5"])
      s.add_development_dependency(%q<rubocop>.freeze, ["~> 0.51"])
      s.add_development_dependency(%q<rubocop-jekyll>.freeze, ["~> 0.3"])
    else
      s.add_dependency(%q<jekyll>.freeze, [">= 3.7", "< 5.0"])
      s.add_dependency(%q<rspec>.freeze, ["~> 3.5"])
      s.add_dependency(%q<rubocop>.freeze, ["~> 0.51"])
      s.add_dependency(%q<rubocop-jekyll>.freeze, ["~> 0.3"])
    end
  else
    s.add_dependency(%q<jekyll>.freeze, [">= 3.7", "< 5.0"])
    s.add_dependency(%q<rspec>.freeze, ["~> 3.5"])
    s.add_dependency(%q<rubocop>.freeze, ["~> 0.51"])
    s.add_dependency(%q<rubocop-jekyll>.freeze, ["~> 0.3"])
  end
end
