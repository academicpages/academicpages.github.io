# -*- encoding: utf-8 -*-
# stub: citeproc 1.0.10 ruby lib

Gem::Specification.new do |s|
  s.name = "citeproc".freeze
  s.version = "1.0.10"

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.require_paths = ["lib".freeze]
  s.authors = ["Sylvester Keil".freeze]
  s.date = "2020-01-07"
  s.description = "A cite processor interface for Citation Style Language (CSL) styles.".freeze
  s.email = ["sylvester@keil.or.at".freeze]
  s.homepage = "https://github.com/inukshuk/citeproc".freeze
  s.licenses = ["AGPL-3.0".freeze]
  s.required_ruby_version = Gem::Requirement.new(">= 2.3".freeze)
  s.rubygems_version = "3.1.2".freeze
  s.summary = "A cite processor interface.".freeze

  s.installed_by_version = "3.1.2" if s.respond_to? :installed_by_version

  if s.respond_to? :specification_version then
    s.specification_version = 4
  end

  if s.respond_to? :add_runtime_dependency then
    s.add_runtime_dependency(%q<namae>.freeze, ["~> 1.0"])
  else
    s.add_dependency(%q<namae>.freeze, ["~> 1.0"])
  end
end
