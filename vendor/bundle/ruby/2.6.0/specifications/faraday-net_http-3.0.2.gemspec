# -*- encoding: utf-8 -*-
# stub: faraday-net_http 3.0.2 ruby lib

Gem::Specification.new do |s|
  s.name = "faraday-net_http".freeze
  s.version = "3.0.2"

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.metadata = { "changelog_uri" => "https://github.com/lostisland/faraday-net_http/releases/tag/v3.0.2", "homepage_uri" => "https://github.com/lostisland/faraday-net_http", "source_code_uri" => "https://github.com/lostisland/faraday-net_http" } if s.respond_to? :metadata=
  s.require_paths = ["lib".freeze]
  s.authors = ["Jan van der Pas".freeze]
  s.date = "2022-11-11"
  s.description = "Faraday adapter for Net::HTTP".freeze
  s.email = ["janvanderpas@gmail.com".freeze]
  s.homepage = "https://github.com/lostisland/faraday-net_http".freeze
  s.licenses = ["MIT".freeze]
  s.required_ruby_version = Gem::Requirement.new(">= 2.6.0".freeze)
  s.rubygems_version = "3.0.3.1".freeze
  s.summary = "Faraday adapter for Net::HTTP".freeze

  s.installed_by_version = "3.0.3.1" if s.respond_to? :installed_by_version

  if s.respond_to? :specification_version then
    s.specification_version = 4

    if Gem::Version.new(Gem::VERSION) >= Gem::Version.new('1.2.0') then
      s.add_development_dependency(%q<faraday>.freeze, [">= 2.5"])
    else
      s.add_dependency(%q<faraday>.freeze, [">= 2.5"])
    end
  else
    s.add_dependency(%q<faraday>.freeze, [">= 2.5"])
  end
end
