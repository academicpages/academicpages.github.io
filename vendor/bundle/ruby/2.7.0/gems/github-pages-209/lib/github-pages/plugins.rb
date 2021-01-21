# frozen_string_literal: true

module GitHubPages
  # Manages the constants that govern which plugins are allowed on GitHub Pages
  class Plugins
    # Plugins which are activated by default
    DEFAULT_PLUGINS = %w(
      jekyll-coffeescript
      jekyll-commonmark-ghpages
      jekyll-gist
      jekyll-github-metadata
      jekyll-paginate
      jekyll-relative-links
      jekyll-optional-front-matter
      jekyll-readme-index
      jekyll-default-layout
      jekyll-titles-from-headings
    ).freeze

    # Plugins allowed by GitHub Pages
    PLUGIN_WHITELIST = %w(
      jekyll-coffeescript
      jekyll-commonmark-ghpages
      jekyll-feed
      jekyll-gist
      jekyll-github-metadata
      jekyll-paginate
      jekyll-redirect-from
      jekyll-seo-tag
      jekyll-sitemap
      jekyll-avatar
      jemoji
      jekyll-mentions
      jekyll-relative-links
      jekyll-optional-front-matter
      jekyll-readme-index
      jekyll-default-layout
      jekyll-titles-from-headings
      jekyll-include-cache
      jekyll-octicons
      jekyll-remote-theme
    ).freeze

    # Plugins only allowed locally
    DEVELOPMENT_PLUGINS = %w(
      jekyll-admin
    ).freeze

    # Themes
    THEMES = {
      "jekyll-swiss" => "1.0.0",
      "minima" => "2.5.1",
      "jekyll-theme-primer" => "0.5.4",
      "jekyll-theme-architect" => "0.1.1",
      "jekyll-theme-cayman" => "0.1.1",
      "jekyll-theme-dinky" => "0.1.1",
      "jekyll-theme-hacker" => "0.1.2",
      "jekyll-theme-leap-day" => "0.1.1",
      "jekyll-theme-merlot" => "0.1.1",
      "jekyll-theme-midnight" => "0.1.1",
      "jekyll-theme-minimal" => "0.1.1",
      "jekyll-theme-modernist" => "0.1.1",
      "jekyll-theme-slate" => "0.1.1",
      "jekyll-theme-tactile" => "0.1.1",
      "jekyll-theme-time-machine" => "0.1.1",
    }.freeze
  end
end
