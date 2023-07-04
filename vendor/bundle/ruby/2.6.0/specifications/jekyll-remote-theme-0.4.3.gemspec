# -*- encoding: utf-8 -*-
# stub: jekyll-remote-theme 0.4.3 ruby lib

Gem::Specification.new do |s|
  s.name = "jekyll-remote-theme".freeze
  s.version = "0.4.3"

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.require_paths = ["lib".freeze]
  s.authors = ["Ben Balter".freeze]
  s.date = "2021-03-10"
  s.email = ["ben.balter@github.com".freeze]
  s.homepage = "https://github.com/benbalter/jekyll-remote-theme".freeze
  s.licenses = ["MIT".freeze]
  s.required_ruby_version = Gem::Requirement.new(">= 2.3.0".freeze)
  s.rubygems_version = "3.0.3.1".freeze
  s.summary = "Jekyll plugin for building Jekyll sites with any GitHub-hosted theme".freeze

  s.installed_by_version = "3.0.3.1" if s.respond_to? :installed_by_version

  if s.respond_to? :specification_version then
    s.specification_version = 4

    if Gem::Version.new(Gem::VERSION) >= Gem::Version.new('1.2.0') then
      s.add_runtime_dependency(%q<addressable>.freeze, ["~> 2.0"])
      s.add_runtime_dependency(%q<jekyll>.freeze, [">= 3.5", "< 5.0"])
      s.add_runtime_dependency(%q<jekyll-sass-converter>.freeze, [">= 1.0", "<= 3.0.0", "!= 2.0.0"])
      s.add_runtime_dependency(%q<rubyzip>.freeze, [">= 1.3.0", "< 3.0"])
      s.add_development_dependency(%q<jekyll-theme-primer>.freeze, ["~> 0.5"])
      s.add_development_dependency(%q<jekyll_test_plugin_malicious>.freeze, ["~> 0.2"])
      s.add_development_dependency(%q<kramdown-parser-gfm>.freeze, ["~> 1.0"])
      s.add_development_dependency(%q<pry>.freeze, ["~> 0.11"])
      s.add_development_dependency(%q<rspec>.freeze, ["~> 3.0"])
      s.add_development_dependency(%q<rubocop>.freeze, ["~> 0.71"])
      s.add_development_dependency(%q<rubocop-jekyll>.freeze, ["~> 0.10"])
      s.add_development_dependency(%q<webmock>.freeze, ["~> 3.0"])
    else
      s.add_dependency(%q<addressable>.freeze, ["~> 2.0"])
      s.add_dependency(%q<jekyll>.freeze, [">= 3.5", "< 5.0"])
      s.add_dependency(%q<jekyll-sass-converter>.freeze, [">= 1.0", "<= 3.0.0", "!= 2.0.0"])
      s.add_dependency(%q<rubyzip>.freeze, [">= 1.3.0", "< 3.0"])
      s.add_dependency(%q<jekyll-theme-primer>.freeze, ["~> 0.5"])
      s.add_dependency(%q<jekyll_test_plugin_malicious>.freeze, ["~> 0.2"])
      s.add_dependency(%q<kramdown-parser-gfm>.freeze, ["~> 1.0"])
      s.add_dependency(%q<pry>.freeze, ["~> 0.11"])
      s.add_dependency(%q<rspec>.freeze, ["~> 3.0"])
      s.add_dependency(%q<rubocop>.freeze, ["~> 0.71"])
      s.add_dependency(%q<rubocop-jekyll>.freeze, ["~> 0.10"])
      s.add_dependency(%q<webmock>.freeze, ["~> 3.0"])
    end
  else
    s.add_dependency(%q<addressable>.freeze, ["~> 2.0"])
    s.add_dependency(%q<jekyll>.freeze, [">= 3.5", "< 5.0"])
    s.add_dependency(%q<jekyll-sass-converter>.freeze, [">= 1.0", "<= 3.0.0", "!= 2.0.0"])
    s.add_dependency(%q<rubyzip>.freeze, [">= 1.3.0", "< 3.0"])
    s.add_dependency(%q<jekyll-theme-primer>.freeze, ["~> 0.5"])
    s.add_dependency(%q<jekyll_test_plugin_malicious>.freeze, ["~> 0.2"])
    s.add_dependency(%q<kramdown-parser-gfm>.freeze, ["~> 1.0"])
    s.add_dependency(%q<pry>.freeze, ["~> 0.11"])
    s.add_dependency(%q<rspec>.freeze, ["~> 3.0"])
    s.add_dependency(%q<rubocop>.freeze, ["~> 0.71"])
    s.add_dependency(%q<rubocop-jekyll>.freeze, ["~> 0.10"])
    s.add_dependency(%q<webmock>.freeze, ["~> 3.0"])
  end
end
