# -*- encoding: utf-8 -*-
# stub: mercenary 0.3.6 ruby lib

Gem::Specification.new do |s|
  s.name = "mercenary".freeze
  s.version = "0.3.6"

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.require_paths = ["lib".freeze]
  s.authors = ["Tom Preston-Werner".freeze, "Parker Moore".freeze]
  s.date = "2016-04-08"
  s.description = "Lightweight and flexible library for writing command-line apps in Ruby.".freeze
  s.email = ["tom@mojombo.com".freeze, "parkrmoore@gmail.com".freeze]
  s.homepage = "https://github.com/jekyll/mercenary".freeze
  s.licenses = ["MIT".freeze]
  s.rubygems_version = "3.1.2".freeze
  s.summary = "Lightweight and flexible library for writing command-line apps in Ruby.".freeze

  s.installed_by_version = "3.1.2" if s.respond_to? :installed_by_version

  if s.respond_to? :specification_version then
    s.specification_version = 4
  end

  if s.respond_to? :add_runtime_dependency then
    s.add_development_dependency(%q<bundler>.freeze, ["~> 1.3"])
    s.add_development_dependency(%q<rake>.freeze, [">= 0"])
    s.add_development_dependency(%q<rspec>.freeze, ["~> 3.0"])
  else
    s.add_dependency(%q<bundler>.freeze, ["~> 1.3"])
    s.add_dependency(%q<rake>.freeze, [">= 0"])
    s.add_dependency(%q<rspec>.freeze, ["~> 3.0"])
  end
end
