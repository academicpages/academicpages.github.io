# -*- encoding: utf-8 -*-
# stub: rexml 3.2.4 ruby lib

Gem::Specification.new do |s|
  s.name = "rexml".freeze
  s.version = "3.2.4"

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.require_paths = ["lib".freeze]
  s.authors = ["Kouhei Sutou".freeze]
  s.bindir = "exe".freeze
  s.date = "2020-01-31"
  s.description = "An XML toolkit for Ruby".freeze
  s.email = ["kou@cozmixng.org".freeze]
  s.homepage = "https://github.com/ruby/rexml".freeze
  s.licenses = ["BSD-2-Clause".freeze]
  s.rubygems_version = "3.1.2".freeze
  s.summary = "An XML toolkit for Ruby".freeze

  s.installed_by_version = "3.1.2" if s.respond_to? :installed_by_version

  if s.respond_to? :specification_version then
    s.specification_version = 4
  end

  if s.respond_to? :add_runtime_dependency then
    s.add_development_dependency(%q<bundler>.freeze, [">= 0"])
    s.add_development_dependency(%q<rake>.freeze, [">= 0"])
  else
    s.add_dependency(%q<bundler>.freeze, [">= 0"])
    s.add_dependency(%q<rake>.freeze, [">= 0"])
  end
end
