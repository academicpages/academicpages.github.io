# frozen_string_literal: true

require "jekyll"
require "fileutils"
require "tempfile"
require "addressable"
require "net/http"
require "zip"

$LOAD_PATH.unshift(File.dirname(__FILE__))

module Jekyll
  module RemoteTheme
    class DownloadError < StandardError; end

    autoload :Downloader,  "jekyll-remote-theme/downloader"
    autoload :MockGemspec, "jekyll-remote-theme/mock_gemspec"
    autoload :Munger,      "jekyll-remote-theme/munger"
    autoload :Theme,       "jekyll-remote-theme/theme"
    autoload :VERSION,     "jekyll-remote-theme/version"

    CONFIG_KEY  = "remote_theme"
    LOG_KEY     = "Remote Theme:"
    TEMP_PREFIX = "jekyll-remote-theme-"

    def self.init(site)
      Munger.new(site).munge!
    end
  end
end

Jekyll::Hooks.register :site, :after_reset do |site|
  Jekyll::RemoteTheme.init(site)
end
