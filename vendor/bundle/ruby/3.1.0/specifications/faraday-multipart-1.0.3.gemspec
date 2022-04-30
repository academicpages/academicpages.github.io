# -*- encoding: utf-8 -*-
# stub: faraday-multipart 1.0.3 ruby lib

Gem::Specification.new do |s|
  s.name = "faraday-multipart".freeze
  s.version = "1.0.3"

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.metadata = { "bug_tracker_uri" => "https://github.com/lostisland/faraday-multipart/issues", "changelog_uri" => "https://github.com/lostisland/faraday-multipart/blob/v1.0.3/CHANGELOG.md", "documentation_uri" => "http://www.rubydoc.info/gems/faraday-multipart/1.0.3", "homepage_uri" => "https://github.com/lostisland/faraday-multipart", "source_code_uri" => "https://github.com/lostisland/faraday-multipart", "wiki_uri" => "https://github.com/lostisland/faraday-multipart/wiki" } if s.respond_to? :metadata=
  s.require_paths = ["lib".freeze]
  s.authors = ["Mattia Giuffrida".freeze]
  s.date = "2022-01-08"
  s.description = "Perform multipart-post requests using Faraday.\n".freeze
  s.email = ["giuffrida.mattia@gmail.com".freeze]
  s.homepage = "https://github.com/lostisland/faraday-multipart".freeze
  s.licenses = ["MIT".freeze]
  s.required_ruby_version = Gem::Requirement.new([">= 2.4".freeze, "< 4".freeze])
  s.rubygems_version = "3.3.11".freeze
  s.summary = "Perform multipart-post requests using Faraday.".freeze

  s.installed_by_version = "3.3.11" if s.respond_to? :installed_by_version

  if s.respond_to? :specification_version then
    s.specification_version = 4
  end

  if s.respond_to? :add_runtime_dependency then
    s.add_runtime_dependency(%q<multipart-post>.freeze, [">= 1.2", "< 3"])
  else
    s.add_dependency(%q<multipart-post>.freeze, [">= 1.2", "< 3"])
  end
end
