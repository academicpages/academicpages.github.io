# -*- encoding: utf-8 -*-
# stub: kramdown 2.3.2 ruby lib

Gem::Specification.new do |s|
  s.name = "kramdown".freeze
  s.version = "2.3.2"

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.require_paths = ["lib".freeze]
  s.authors = ["Thomas Leitner".freeze]
  s.date = "2022-03-18"
  s.description = "kramdown is yet-another-markdown-parser but fast, pure Ruby,\nusing a strict syntax definition and supporting several common extensions.\n".freeze
  s.email = "t_leitner@gmx.at".freeze
  s.executables = ["kramdown".freeze]
  s.files = ["bin/kramdown".freeze]
  s.homepage = "http://kramdown.gettalong.org".freeze
  s.licenses = ["MIT".freeze]
  s.rdoc_options = ["--main".freeze, "lib/kramdown/document.rb".freeze]
  s.required_ruby_version = Gem::Requirement.new(">= 2.3".freeze)
  s.rubygems_version = "3.0.3.1".freeze
  s.summary = "kramdown is a fast, pure-Ruby Markdown-superset converter.".freeze

  s.installed_by_version = "3.0.3.1" if s.respond_to? :installed_by_version

  if s.respond_to? :specification_version then
    s.specification_version = 4

    if Gem::Version.new(Gem::VERSION) >= Gem::Version.new('1.2.0') then
      s.add_runtime_dependency(%q<rexml>.freeze, [">= 0"])
      s.add_development_dependency(%q<minitest>.freeze, ["~> 5.0"])
      s.add_development_dependency(%q<rouge>.freeze, ["~> 3.0", ">= 3.26.0"])
      s.add_development_dependency(%q<stringex>.freeze, ["~> 1.5.1"])
    else
      s.add_dependency(%q<rexml>.freeze, [">= 0"])
      s.add_dependency(%q<minitest>.freeze, ["~> 5.0"])
      s.add_dependency(%q<rouge>.freeze, ["~> 3.0", ">= 3.26.0"])
      s.add_dependency(%q<stringex>.freeze, ["~> 1.5.1"])
    end
  else
    s.add_dependency(%q<rexml>.freeze, [">= 0"])
    s.add_dependency(%q<minitest>.freeze, ["~> 5.0"])
    s.add_dependency(%q<rouge>.freeze, ["~> 3.0", ">= 3.26.0"])
    s.add_dependency(%q<stringex>.freeze, ["~> 1.5.1"])
  end
end
