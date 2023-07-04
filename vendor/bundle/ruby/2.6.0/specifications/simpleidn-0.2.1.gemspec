# -*- encoding: utf-8 -*-
# stub: simpleidn 0.2.1 ruby lib

Gem::Specification.new do |s|
  s.name = "simpleidn".freeze
  s.version = "0.2.1"

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.require_paths = ["lib".freeze]
  s.authors = ["Morten M\u00F8ller Riis".freeze]
  s.date = "2021-01-14"
  s.description = "This gem allows easy conversion from punycode ACE strings to unicode UTF-8 strings and vice-versa.".freeze
  s.email = ["mortenmoellerriis _AT_ gmail.com".freeze]
  s.homepage = "https://github.com/mmriis/simpleidn".freeze
  s.licenses = ["MIT".freeze]
  s.required_ruby_version = Gem::Requirement.new(">= 2.2".freeze)
  s.rubygems_version = "3.0.3.1".freeze
  s.summary = "Punycode ACE to unicode UTF-8 (and vice-versa) string conversion.".freeze

  s.installed_by_version = "3.0.3.1" if s.respond_to? :installed_by_version

  if s.respond_to? :specification_version then
    s.specification_version = 4

    if Gem::Version.new(Gem::VERSION) >= Gem::Version.new('1.2.0') then
      s.add_runtime_dependency(%q<unf>.freeze, ["~> 0.1.4"])
      s.add_development_dependency(%q<bundler>.freeze, ["~> 1.11"])
      s.add_development_dependency(%q<rake>.freeze, ["~> 10.0"])
      s.add_development_dependency(%q<rspec>.freeze, ["~> 3.0"])
    else
      s.add_dependency(%q<unf>.freeze, ["~> 0.1.4"])
      s.add_dependency(%q<bundler>.freeze, ["~> 1.11"])
      s.add_dependency(%q<rake>.freeze, ["~> 10.0"])
      s.add_dependency(%q<rspec>.freeze, ["~> 3.0"])
    end
  else
    s.add_dependency(%q<unf>.freeze, ["~> 0.1.4"])
    s.add_dependency(%q<bundler>.freeze, ["~> 1.11"])
    s.add_dependency(%q<rake>.freeze, ["~> 10.0"])
    s.add_dependency(%q<rspec>.freeze, ["~> 3.0"])
  end
end
