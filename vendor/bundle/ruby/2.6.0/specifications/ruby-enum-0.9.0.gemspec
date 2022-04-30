# -*- encoding: utf-8 -*-
# stub: ruby-enum 0.9.0 ruby lib

Gem::Specification.new do |s|
  s.name = "ruby-enum".freeze
  s.version = "0.9.0"

  s.required_rubygems_version = Gem::Requirement.new(">= 1.3.6".freeze) if s.respond_to? :required_rubygems_version=
  s.require_paths = ["lib".freeze]
  s.authors = ["Daniel Doubrovkine".freeze]
  s.date = "2021-01-31"
  s.email = "dblock@dblock.org".freeze
  s.homepage = "http://github.com/dblock/ruby-enum".freeze
  s.licenses = ["MIT".freeze]
  s.rubygems_version = "3.0.3.1".freeze
  s.summary = "Enum-like behavior for Ruby.".freeze

  s.installed_by_version = "3.0.3.1" if s.respond_to? :installed_by_version

  if s.respond_to? :specification_version then
    s.specification_version = 4

    if Gem::Version.new(Gem::VERSION) >= Gem::Version.new('1.2.0') then
      s.add_runtime_dependency(%q<i18n>.freeze, [">= 0"])
    else
      s.add_dependency(%q<i18n>.freeze, [">= 0"])
    end
  else
    s.add_dependency(%q<i18n>.freeze, [">= 0"])
  end
end
