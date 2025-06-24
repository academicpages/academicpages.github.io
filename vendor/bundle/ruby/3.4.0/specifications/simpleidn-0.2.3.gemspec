# -*- encoding: utf-8 -*-
# stub: simpleidn 0.2.3 ruby lib

Gem::Specification.new do |s|
  s.name = "simpleidn".freeze
  s.version = "0.2.3".freeze

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.require_paths = ["lib".freeze]
  s.authors = ["Morten M\u00F8ller Riis".freeze]
  s.date = "2024-05-22"
  s.description = "This gem allows easy conversion from punycode ACE strings to unicode UTF-8 strings and vice-versa.".freeze
  s.email = ["mortenmoellerriis _AT_ gmail.com".freeze]
  s.homepage = "https://github.com/mmriis/simpleidn".freeze
  s.licenses = ["MIT".freeze]
  s.required_ruby_version = Gem::Requirement.new(">= 2.2".freeze)
  s.rubygems_version = "3.4.19".freeze
  s.summary = "Punycode ACE to unicode UTF-8 (and vice-versa) string conversion.".freeze

  s.installed_by_version = "3.6.9".freeze

  s.specification_version = 4

  s.add_development_dependency(%q<rake>.freeze, ["~> 13.0.3".freeze])
  s.add_development_dependency(%q<rspec>.freeze, ["~> 3.10".freeze])
end
