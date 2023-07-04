# -*- encoding: utf-8 -*-
# stub: jekyll-readme-index 0.3.0 ruby lib

Gem::Specification.new do |s|
  s.name = "jekyll-readme-index".freeze
  s.version = "0.3.0"

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.require_paths = ["lib".freeze]
  s.authors = ["Ben Balter".freeze]
  s.date = "2019-11-05"
  s.email = ["ben.balter@github.com".freeze]
  s.homepage = "https://github.com/benbalter/jekyll-readme-index".freeze
  s.licenses = ["MIT".freeze]
  s.rubygems_version = "3.0.3.1".freeze
  s.summary = "A Jekyll plugin to render a project's README as the site's index.".freeze

  s.installed_by_version = "3.0.3.1" if s.respond_to? :installed_by_version

  if s.respond_to? :specification_version then
    s.specification_version = 4

    if Gem::Version.new(Gem::VERSION) >= Gem::Version.new('1.2.0') then
      s.add_runtime_dependency(%q<jekyll>.freeze, [">= 3.0", "< 5.0"])
      s.add_development_dependency(%q<rspec>.freeze, ["~> 3.5"])
      s.add_development_dependency(%q<rubocop>.freeze, ["~> 0.40"])
      s.add_development_dependency(%q<rubocop-jekyll>.freeze, ["~> 0.10.0"])
      s.add_development_dependency(%q<rubocop-performance>.freeze, ["~> 1.5"])
      s.add_development_dependency(%q<rubocop-rspec>.freeze, ["~> 1.3"])
    else
      s.add_dependency(%q<jekyll>.freeze, [">= 3.0", "< 5.0"])
      s.add_dependency(%q<rspec>.freeze, ["~> 3.5"])
      s.add_dependency(%q<rubocop>.freeze, ["~> 0.40"])
      s.add_dependency(%q<rubocop-jekyll>.freeze, ["~> 0.10.0"])
      s.add_dependency(%q<rubocop-performance>.freeze, ["~> 1.5"])
      s.add_dependency(%q<rubocop-rspec>.freeze, ["~> 1.3"])
    end
  else
    s.add_dependency(%q<jekyll>.freeze, [">= 3.0", "< 5.0"])
    s.add_dependency(%q<rspec>.freeze, ["~> 3.5"])
    s.add_dependency(%q<rubocop>.freeze, ["~> 0.40"])
    s.add_dependency(%q<rubocop-jekyll>.freeze, ["~> 0.10.0"])
    s.add_dependency(%q<rubocop-performance>.freeze, ["~> 1.5"])
    s.add_dependency(%q<rubocop-rspec>.freeze, ["~> 1.3"])
  end
end
