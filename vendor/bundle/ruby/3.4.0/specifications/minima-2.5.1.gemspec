# -*- encoding: utf-8 -*-
# stub: minima 2.5.1 ruby lib

Gem::Specification.new do |s|
  s.name = "minima".freeze
  s.version = "2.5.1".freeze

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.metadata = { "plugin_type" => "theme" } if s.respond_to? :metadata=
  s.require_paths = ["lib".freeze]
  s.authors = ["Joel Glovier".freeze]
  s.date = "2019-08-16"
  s.email = ["jglovier@github.com".freeze]
  s.homepage = "https://github.com/jekyll/minima".freeze
  s.licenses = ["MIT".freeze]
  s.rubygems_version = "3.0.4".freeze
  s.summary = "A beautiful, minimal theme for Jekyll.".freeze

  s.installed_by_version = "3.6.9".freeze

  s.specification_version = 4

  s.add_runtime_dependency(%q<jekyll>.freeze, [">= 3.5".freeze, "< 5.0".freeze])
  s.add_runtime_dependency(%q<jekyll-feed>.freeze, ["~> 0.9".freeze])
  s.add_runtime_dependency(%q<jekyll-seo-tag>.freeze, ["~> 2.1".freeze])
  s.add_development_dependency(%q<bundler>.freeze, [">= 1.15".freeze])
end
