# -*- encoding: utf-8 -*-
# stub: mini_portile2 2.8.2 ruby lib

Gem::Specification.new do |s|
  s.name = "mini_portile2".freeze
  s.version = "2.8.2"

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.require_paths = ["lib".freeze]
  s.authors = ["Luis Lavena".freeze, "Mike Dalessio".freeze, "Lars Kanis".freeze]
  s.date = "2023-04-30"
  s.description = "Simplistic port-like solution for developers. It provides a standard and simplified way to compile against dependency libraries without messing up your system.".freeze
  s.email = "mike.dalessio@gmail.com".freeze
  s.homepage = "https://github.com/flavorjones/mini_portile".freeze
  s.licenses = ["MIT".freeze]
  s.required_ruby_version = Gem::Requirement.new(">= 2.3.0".freeze)
  s.rubygems_version = "3.0.3.1".freeze
  s.summary = "Simplistic port-like solution for developers".freeze

  s.installed_by_version = "3.0.3.1" if s.respond_to? :installed_by_version

  if s.respond_to? :specification_version then
    s.specification_version = 4

    if Gem::Version.new(Gem::VERSION) >= Gem::Version.new('1.2.0') then
      s.add_development_dependency(%q<bundler>.freeze, ["~> 2.2"])
      s.add_development_dependency(%q<minitar>.freeze, ["~> 0.9"])
      s.add_development_dependency(%q<minitest>.freeze, ["~> 5.15"])
      s.add_development_dependency(%q<minitest-hooks>.freeze, ["~> 1.5"])
      s.add_development_dependency(%q<rake>.freeze, ["~> 13.0"])
      s.add_development_dependency(%q<webrick>.freeze, ["~> 1.7"])
    else
      s.add_dependency(%q<bundler>.freeze, ["~> 2.2"])
      s.add_dependency(%q<minitar>.freeze, ["~> 0.9"])
      s.add_dependency(%q<minitest>.freeze, ["~> 5.15"])
      s.add_dependency(%q<minitest-hooks>.freeze, ["~> 1.5"])
      s.add_dependency(%q<rake>.freeze, ["~> 13.0"])
      s.add_dependency(%q<webrick>.freeze, ["~> 1.7"])
    end
  else
    s.add_dependency(%q<bundler>.freeze, ["~> 2.2"])
    s.add_dependency(%q<minitar>.freeze, ["~> 0.9"])
    s.add_dependency(%q<minitest>.freeze, ["~> 5.15"])
    s.add_dependency(%q<minitest-hooks>.freeze, ["~> 1.5"])
    s.add_dependency(%q<rake>.freeze, ["~> 13.0"])
    s.add_dependency(%q<webrick>.freeze, ["~> 1.7"])
  end
end
