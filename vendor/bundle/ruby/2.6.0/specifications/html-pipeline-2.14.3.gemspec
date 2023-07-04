# -*- encoding: utf-8 -*-
# stub: html-pipeline 2.14.3 ruby lib

Gem::Specification.new do |s|
  s.name = "html-pipeline".freeze
  s.version = "2.14.3"

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.require_paths = ["lib".freeze]
  s.authors = ["Ryan Tomayko".freeze, "Jerry Cheung".freeze, "Garen J. Torikian".freeze]
  s.date = "2022-10-14"
  s.description = "GitHub HTML processing filters and utilities".freeze
  s.email = ["ryan@github.com".freeze, "jerry@github.com".freeze, "gjtorikian@gmail.com".freeze]
  s.homepage = "https://github.com/jch/html-pipeline".freeze
  s.licenses = ["MIT".freeze]
  s.post_install_message = "-------------------------------------------------\nThank you for installing html-pipeline!\nYou must bundle Filter gem dependencies.\nSee html-pipeline README.md for more details.\nhttps://github.com/jch/html-pipeline#dependencies\n-------------------------------------------------\n".freeze
  s.rubygems_version = "3.0.3.1".freeze
  s.summary = "Helpers for processing content through a chain of filters".freeze

  s.installed_by_version = "3.0.3.1" if s.respond_to? :installed_by_version

  if s.respond_to? :specification_version then
    s.specification_version = 4

    if Gem::Version.new(Gem::VERSION) >= Gem::Version.new('1.2.0') then
      s.add_runtime_dependency(%q<activesupport>.freeze, [">= 2"])
      s.add_runtime_dependency(%q<nokogiri>.freeze, [">= 1.4"])
    else
      s.add_dependency(%q<activesupport>.freeze, [">= 2"])
      s.add_dependency(%q<nokogiri>.freeze, [">= 1.4"])
    end
  else
    s.add_dependency(%q<activesupport>.freeze, [">= 2"])
    s.add_dependency(%q<nokogiri>.freeze, [">= 1.4"])
  end
end
