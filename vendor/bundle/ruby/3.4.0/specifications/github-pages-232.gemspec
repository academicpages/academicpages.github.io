# -*- encoding: utf-8 -*-
# stub: github-pages 232 ruby lib

Gem::Specification.new do |s|
  s.name = "github-pages".freeze
  s.version = "232".freeze

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.require_paths = ["lib".freeze]
  s.authors = ["GitHub, Inc.".freeze]
  s.date = "2024-08-06"
  s.description = "Bootstrap the GitHub Pages Jekyll environment locally.".freeze
  s.email = "support@github.com".freeze
  s.executables = ["github-pages".freeze]
  s.files = ["bin/github-pages".freeze]
  s.homepage = "https://github.com/github/pages-gem".freeze
  s.licenses = ["MIT".freeze]
  s.required_ruby_version = Gem::Requirement.new(">= 2.3.0".freeze)
  s.rubygems_version = "3.5.11".freeze
  s.summary = "Track GitHub Pages dependencies.".freeze

  s.installed_by_version = "3.6.9".freeze

  s.specification_version = 4

  s.add_runtime_dependency(%q<jekyll>.freeze, ["= 3.10.0".freeze])
  s.add_runtime_dependency(%q<jekyll-sass-converter>.freeze, ["= 1.5.2".freeze])
  s.add_runtime_dependency(%q<kramdown>.freeze, ["= 2.4.0".freeze])
  s.add_runtime_dependency(%q<kramdown-parser-gfm>.freeze, ["= 1.1.0".freeze])
  s.add_runtime_dependency(%q<jekyll-commonmark-ghpages>.freeze, ["= 0.5.1".freeze])
  s.add_runtime_dependency(%q<liquid>.freeze, ["= 4.0.4".freeze])
  s.add_runtime_dependency(%q<rouge>.freeze, ["= 3.30.0".freeze])
  s.add_runtime_dependency(%q<github-pages-health-check>.freeze, ["= 1.18.2".freeze])
  s.add_runtime_dependency(%q<jekyll-redirect-from>.freeze, ["= 0.16.0".freeze])
  s.add_runtime_dependency(%q<jekyll-sitemap>.freeze, ["= 1.4.0".freeze])
  s.add_runtime_dependency(%q<jekyll-feed>.freeze, ["= 0.17.0".freeze])
  s.add_runtime_dependency(%q<jekyll-gist>.freeze, ["= 1.5.0".freeze])
  s.add_runtime_dependency(%q<jekyll-paginate>.freeze, ["= 1.1.0".freeze])
  s.add_runtime_dependency(%q<jekyll-coffeescript>.freeze, ["= 1.2.2".freeze])
  s.add_runtime_dependency(%q<jekyll-seo-tag>.freeze, ["= 2.8.0".freeze])
  s.add_runtime_dependency(%q<jekyll-github-metadata>.freeze, ["= 2.16.1".freeze])
  s.add_runtime_dependency(%q<jekyll-avatar>.freeze, ["= 0.8.0".freeze])
  s.add_runtime_dependency(%q<jekyll-remote-theme>.freeze, ["= 0.4.3".freeze])
  s.add_runtime_dependency(%q<jekyll-include-cache>.freeze, ["= 0.2.1".freeze])
  s.add_runtime_dependency(%q<jemoji>.freeze, ["= 0.13.0".freeze])
  s.add_runtime_dependency(%q<jekyll-mentions>.freeze, ["= 1.6.0".freeze])
  s.add_runtime_dependency(%q<jekyll-relative-links>.freeze, ["= 0.6.1".freeze])
  s.add_runtime_dependency(%q<jekyll-optional-front-matter>.freeze, ["= 0.3.2".freeze])
  s.add_runtime_dependency(%q<jekyll-readme-index>.freeze, ["= 0.3.0".freeze])
  s.add_runtime_dependency(%q<jekyll-default-layout>.freeze, ["= 0.1.5".freeze])
  s.add_runtime_dependency(%q<jekyll-titles-from-headings>.freeze, ["= 0.5.3".freeze])
  s.add_runtime_dependency(%q<minima>.freeze, ["= 2.5.1".freeze])
  s.add_runtime_dependency(%q<jekyll-swiss>.freeze, ["= 1.0.0".freeze])
  s.add_runtime_dependency(%q<jekyll-theme-primer>.freeze, ["= 0.6.0".freeze])
  s.add_runtime_dependency(%q<jekyll-theme-architect>.freeze, ["= 0.2.0".freeze])
  s.add_runtime_dependency(%q<jekyll-theme-cayman>.freeze, ["= 0.2.0".freeze])
  s.add_runtime_dependency(%q<jekyll-theme-dinky>.freeze, ["= 0.2.0".freeze])
  s.add_runtime_dependency(%q<jekyll-theme-hacker>.freeze, ["= 0.2.0".freeze])
  s.add_runtime_dependency(%q<jekyll-theme-leap-day>.freeze, ["= 0.2.0".freeze])
  s.add_runtime_dependency(%q<jekyll-theme-merlot>.freeze, ["= 0.2.0".freeze])
  s.add_runtime_dependency(%q<jekyll-theme-midnight>.freeze, ["= 0.2.0".freeze])
  s.add_runtime_dependency(%q<jekyll-theme-minimal>.freeze, ["= 0.2.0".freeze])
  s.add_runtime_dependency(%q<jekyll-theme-modernist>.freeze, ["= 0.2.0".freeze])
  s.add_runtime_dependency(%q<jekyll-theme-slate>.freeze, ["= 0.2.0".freeze])
  s.add_runtime_dependency(%q<jekyll-theme-tactile>.freeze, ["= 0.2.0".freeze])
  s.add_runtime_dependency(%q<jekyll-theme-time-machine>.freeze, ["= 0.2.0".freeze])
  s.add_runtime_dependency(%q<mercenary>.freeze, ["~> 0.3".freeze])
  s.add_runtime_dependency(%q<nokogiri>.freeze, [">= 1.16.2".freeze, "< 2.0".freeze])
  s.add_runtime_dependency(%q<terminal-table>.freeze, ["~> 1.4".freeze])
  s.add_runtime_dependency(%q<webrick>.freeze, ["~> 1.8".freeze])
  s.add_development_dependency(%q<jekyll_test_plugin_malicious>.freeze, ["~> 0.2".freeze])
  s.add_development_dependency(%q<pry>.freeze, ["~> 0.10".freeze])
  s.add_development_dependency(%q<rspec>.freeze, ["~> 3.3".freeze])
  s.add_development_dependency(%q<rubocop-github>.freeze, ["= 0.20.0".freeze])
end
