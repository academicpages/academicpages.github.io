# -*- encoding: utf-8 -*-
# stub: jekyll-relative-links 0.6.1 ruby lib

Gem::Specification.new do |s|
  s.name = "jekyll-relative-links".freeze
  s.version = "0.6.1"

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.require_paths = ["lib".freeze]
  s.authors = ["Ben Balter".freeze]
  s.date = "2019-10-23"
  s.email = ["ben.balter@github.com".freeze]
  s.homepage = "https://github.com/benbalter/jekyll-relative-links".freeze
  s.licenses = ["MIT".freeze]
  s.rubygems_version = "3.0.3.1".freeze
  s.summary = "A Jekyll plugin to convert relative links to markdown files to their rendered equivalents.".freeze

  s.installed_by_version = "3.0.3.1" if s.respond_to? :installed_by_version

  if s.respond_to? :specification_version then
    s.specification_version = 4

    if Gem::Version.new(Gem::VERSION) >= Gem::Version.new('1.2.0') then
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
  else
    s.add_dependency(%q<jekyll>.freeze, [">= 3.3", "< 5.0"])
    s.add_dependency(%q<rspec>.freeze, ["~> 3.5"])
    s.add_dependency(%q<rubocop>.freeze, ["~> 0.71"])
    s.add_dependency(%q<rubocop-jekyll>.freeze, ["~> 0.10"])
  end
end
