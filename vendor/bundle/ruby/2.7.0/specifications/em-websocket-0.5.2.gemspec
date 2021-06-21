# -*- encoding: utf-8 -*-
# stub: em-websocket 0.5.2 ruby lib

Gem::Specification.new do |s|
  s.name = "em-websocket".freeze
  s.version = "0.5.2"

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.require_paths = ["lib".freeze]
  s.authors = ["Ilya Grigorik".freeze, "Martyn Loughran".freeze]
  s.date = "2020-09-23"
  s.description = "EventMachine based WebSocket server".freeze
  s.email = ["ilya@igvita.com".freeze, "me@mloughran.com".freeze]
  s.homepage = "http://github.com/igrigorik/em-websocket".freeze
  s.licenses = ["MIT".freeze]
  s.rubygems_version = "3.1.2".freeze
  s.summary = "EventMachine based WebSocket server".freeze

  s.installed_by_version = "3.1.2" if s.respond_to? :installed_by_version

  if s.respond_to? :specification_version then
    s.specification_version = 4
  end

  if s.respond_to? :add_runtime_dependency then
    s.add_runtime_dependency(%q<eventmachine>.freeze, [">= 0.12.9"])
    s.add_runtime_dependency(%q<http_parser.rb>.freeze, ["~> 0.6.0"])
  else
    s.add_dependency(%q<eventmachine>.freeze, [">= 0.12.9"])
    s.add_dependency(%q<http_parser.rb>.freeze, ["~> 0.6.0"])
  end
end
