# -*- encoding: utf-8 -*-
# stub: jekyll-commonmark-ghpages 0.1.6 ruby lib

Gem::Specification.new do |s|
  s.name = "jekyll-commonmark-ghpages".freeze
  s.version = "0.1.6"

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.require_paths = ["lib".freeze]
  s.authors = ["Ashe Connor".freeze]
  s.date = "2019-01-21"
  s.email = "kivikakk@github.com".freeze
  s.homepage = "https://github.com/github/jekyll-commonmark-ghpages".freeze
  s.licenses = ["MIT".freeze]
  s.rubygems_version = "3.1.2".freeze
  s.summary = "CommonMark generator for Jekyll".freeze

  s.installed_by_version = "3.1.2" if s.respond_to? :installed_by_version

  if s.respond_to? :specification_version then
    s.specification_version = 4
  end

  if s.respond_to? :add_runtime_dependency then
    s.add_runtime_dependency(%q<jekyll-commonmark>.freeze, ["~> 1.2"])
    s.add_runtime_dependency(%q<commonmarker>.freeze, ["~> 0.17.6"])
    s.add_runtime_dependency(%q<rouge>.freeze, [">= 2.0", "< 4.0"])
    s.add_development_dependency(%q<rspec>.freeze, ["~> 3.0"])
    s.add_development_dependency(%q<rake>.freeze, [">= 0"])
  else
    s.add_dependency(%q<jekyll-commonmark>.freeze, ["~> 1.2"])
    s.add_dependency(%q<commonmarker>.freeze, ["~> 0.17.6"])
    s.add_dependency(%q<rouge>.freeze, [">= 2.0", "< 4.0"])
    s.add_dependency(%q<rspec>.freeze, ["~> 3.0"])
    s.add_dependency(%q<rake>.freeze, [">= 0"])
  end
end
