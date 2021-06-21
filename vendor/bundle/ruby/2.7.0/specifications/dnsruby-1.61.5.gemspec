# -*- encoding: utf-8 -*-
# stub: dnsruby 1.61.5 ruby lib

Gem::Specification.new do |s|
  s.name = "dnsruby".freeze
  s.version = "1.61.5"

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.metadata = { "bug_tracker_uri" => "https://github.com/alexdalitz/dnsruby/issues", "changelog_uri" => "https://github.com/alexdalitz/dnsruby/blob/master/RELEASE_NOTES.md", "documentation_uri" => "https://www.rubydoc.info/gems/dnsruby/", "homepage_uri" => "https://github.com/alexdalitz/dnsruby", "source_code_uri" => "https://github.com/alexdalitz/dnsruby", "yard.run" => "yard" } if s.respond_to? :metadata=
  s.require_paths = ["lib".freeze]
  s.authors = ["Alex Dalitz".freeze]
  s.date = "2020-10-29"
  s.description = "Dnsruby is a pure Ruby DNS client library which implements a\nstub resolver. It aims to comply with all DNS RFCs, including\nDNSSEC NSEC3 support.".freeze
  s.email = "alex@caerkettontech.com".freeze
  s.extra_rdoc_files = ["DNSSEC".freeze, "EXAMPLES".freeze, "README.md".freeze, "EVENTMACHINE".freeze]
  s.files = ["DNSSEC".freeze, "EVENTMACHINE".freeze, "EXAMPLES".freeze, "README.md".freeze]
  s.homepage = "https://github.com/alexdalitz/dnsruby".freeze
  s.licenses = ["Apache License, Version 2.0".freeze]
  s.post_install_message = "Installing dnsruby...\n  For issues and source code: https://github.com/alexdalitz/dnsruby\n  For general discussion (please tell us how you use dnsruby): https://groups.google.com/forum/#!forum/dnsruby".freeze
  s.rubygems_version = "3.1.2".freeze
  s.summary = "Ruby DNS(SEC) implementation".freeze

  s.installed_by_version = "3.1.2" if s.respond_to? :installed_by_version

  if s.respond_to? :specification_version then
    s.specification_version = 4
  end

  if s.respond_to? :add_runtime_dependency then
    s.add_development_dependency(%q<rake>.freeze, [">= 12.3.3"])
    s.add_development_dependency(%q<minitest>.freeze, ["~> 5.4"])
    s.add_development_dependency(%q<rubydns>.freeze, ["~> 2.0.1"])
    s.add_development_dependency(%q<nio4r>.freeze, ["~> 2.0"])
    s.add_development_dependency(%q<minitest-display>.freeze, [">= 0.3.0"])
    s.add_development_dependency(%q<yard>.freeze, ["~> 0.9"])
    s.add_development_dependency(%q<coveralls>.freeze, ["~> 0.7"])
    s.add_runtime_dependency(%q<simpleidn>.freeze, ["~> 0.1"])
  else
    s.add_dependency(%q<rake>.freeze, [">= 12.3.3"])
    s.add_dependency(%q<minitest>.freeze, ["~> 5.4"])
    s.add_dependency(%q<rubydns>.freeze, ["~> 2.0.1"])
    s.add_dependency(%q<nio4r>.freeze, ["~> 2.0"])
    s.add_dependency(%q<minitest-display>.freeze, [">= 0.3.0"])
    s.add_dependency(%q<yard>.freeze, ["~> 0.9"])
    s.add_dependency(%q<coveralls>.freeze, ["~> 0.7"])
    s.add_dependency(%q<simpleidn>.freeze, ["~> 0.1"])
  end
end
