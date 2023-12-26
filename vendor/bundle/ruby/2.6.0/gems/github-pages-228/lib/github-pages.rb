# frozen_string_literal: true

$LOAD_PATH.unshift(File.dirname(__FILE__))
require "jekyll"

# Top-level namespace for all GitHub Pages-related concerns.
module GitHubPages
  autoload :Plugins,       "github-pages/plugins"
  autoload :Configuration, "github-pages/configuration"
  autoload :Dependencies,  "github-pages/dependencies"
  autoload :VERSION,       "github-pages/version"

  def self.versions
    Dependencies.versions
  end
end

Jekyll::Hooks.register :site, :after_reset do |site|
  GitHubPages::Configuration.set(site)
end
