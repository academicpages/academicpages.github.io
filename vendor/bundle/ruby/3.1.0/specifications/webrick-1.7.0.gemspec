# -*- encoding: utf-8 -*-
# stub: webrick 1.7.0 ruby lib

Gem::Specification.new do |s|
  s.name = "webrick".freeze
  s.version = "1.7.0"

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.metadata = { "bug_tracker_uri" => "https://github.com/ruby/webrick/issues" } if s.respond_to? :metadata=
  s.require_paths = ["lib".freeze]
  s.authors = ["TAKAHASHI Masayoshi".freeze, "GOTOU YUUZOU".freeze, "Eric Wong".freeze]
  s.date = "2020-12-11"
  s.description = "WEBrick is an HTTP server toolkit that can be configured as an HTTPS server, a proxy server, and a virtual-host server.".freeze
  s.email = [nil, nil, "normal@ruby-lang.org".freeze]
  s.homepage = "https://github.com/ruby/webrick".freeze
  s.licenses = ["Ruby".freeze, "BSD-2-Clause".freeze]
  s.required_ruby_version = Gem::Requirement.new(">= 2.3.0".freeze)
  s.rubygems_version = "3.3.11".freeze
  s.summary = "HTTP server toolkit".freeze

  s.installed_by_version = "3.3.11" if s.respond_to? :installed_by_version

  if s.respond_to? :specification_version then
    s.specification_version = 4
  end

  if s.respond_to? :add_runtime_dependency then
    s.add_development_dependency(%q<rake>.freeze, [">= 0"])
  else
    s.add_dependency(%q<rake>.freeze, [">= 0"])
  end
end
