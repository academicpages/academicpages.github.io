# -*- encoding: utf-8 -*-
# stub: colorator 1.1.0 ruby lib

Gem::Specification.new do |s|
  s.name = "colorator".freeze
  s.version = "1.1.0"

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.require_paths = ["lib".freeze]
  s.authors = ["Parker Moore".freeze, "Brandon Mathis".freeze]
  s.date = "2016-06-29"
  s.email = ["parkrmoore@gmail.com".freeze, "brandon@imathis.com".freeze]
  s.extra_rdoc_files = ["README.markdown".freeze, "LICENSE".freeze]
  s.files = ["LICENSE".freeze, "README.markdown".freeze]
  s.homepage = "https://github.com/octopress/colorator".freeze
  s.licenses = ["MIT".freeze]
  s.rdoc_options = ["--charset=UTF-8".freeze]
  s.rubygems_version = "3.1.2".freeze
  s.summary = "Colorize your text in the terminal.".freeze

  s.installed_by_version = "3.1.2" if s.respond_to? :installed_by_version

  if s.respond_to? :specification_version then
    s.specification_version = 4
  end

  if s.respond_to? :add_runtime_dependency then
    s.add_development_dependency(%q<rspec>.freeze, ["~> 3.1"])
  else
    s.add_dependency(%q<rspec>.freeze, ["~> 3.1"])
  end
end
