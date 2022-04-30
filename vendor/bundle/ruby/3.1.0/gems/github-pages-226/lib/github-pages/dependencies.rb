# frozen_string_literal: true

module GitHubPages
  # Dependencies is where all the public dependencies for GitHub Pages are defined,
  # and versions locked. Any plugin for Pages must be specified here with a
  # corresponding version to which it shall be locked in the runtime dependencies.
  class Dependencies
    VERSIONS = {
      # Jekyll
      "jekyll" => "3.9.2",
      "jekyll-sass-converter" => "1.5.2",

      # Converters
      "kramdown" => "2.3.2",
      "kramdown-parser-gfm" => "1.1.0",
      "jekyll-commonmark-ghpages" => "0.2.0",

      # Misc
      "liquid" => "4.0.3",
      "rouge" => "3.26.0",
      "github-pages-health-check" => "1.17.9",

      # Plugins
      "jekyll-redirect-from" => "0.16.0",
      "jekyll-sitemap" => "1.4.0",
      "jekyll-feed" => "0.15.1",
      "jekyll-gist" => "1.5.0",
      "jekyll-paginate" => "1.1.0",
      "jekyll-coffeescript" => "1.1.1",
      "jekyll-seo-tag" => "2.8.0",
      "jekyll-github-metadata" => "2.13.0",
      "jekyll-avatar" => "0.7.0",
      "jekyll-remote-theme" => "0.4.3",
      "jekyll-include-cache" => "0.2.1",

      # Plugins to match GitHub.com Markdown
      "jemoji" => "0.12.0",
      "jekyll-mentions" => "1.6.0",
      "jekyll-relative-links" => "0.6.1",
      "jekyll-optional-front-matter" => "0.3.2",
      "jekyll-readme-index" => "0.3.0",
      "jekyll-default-layout" => "0.1.4",
      "jekyll-titles-from-headings" => "0.5.3",
    }.freeze

    # Jekyll and related dependency versions as used by GitHub Pages.
    # For more information see:
    # https://help.github.com/articles/using-jekyll-with-pages
    def self.gems
      VERSIONS.merge(GitHubPages::Plugins::THEMES)
    end

    # Versions used by GitHub Pages, including github-pages gem and ruby version
    # Useful for programmatically querying for the current-running version
    def self.versions
      gems.merge version_report
    end

    def self.version_report
      require "html/pipeline/version"
      require "sass/version"
      require "safe_yaml/version"
      require "nokogiri"

      {
        "ruby" => RUBY_VERSION,

        # Gem versions we're curious about
        "github-pages" => VERSION.to_s,
        "html-pipeline" => HTML::Pipeline::VERSION,
        "sass" => Sass.version[:number],
        "safe_yaml" => SafeYAML::VERSION,
        "nokogiri" => Nokogiri::VERSION,
      }
    end
  end
end
