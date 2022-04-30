# frozen_string_literal: true

require "securerandom"

module GitHubPages
  # Sets and manages Jekyll configuration defaults and overrides
  class Configuration
    # Backward compatability of constants
    DEFAULT_PLUGINS     = GitHubPages::Plugins::DEFAULT_PLUGINS
    PLUGIN_WHITELIST    = GitHubPages::Plugins::PLUGIN_WHITELIST
    DEVELOPMENT_PLUGINS = GitHubPages::Plugins::DEVELOPMENT_PLUGINS
    THEMES              = GitHubPages::Plugins::THEMES

    # Default, user overwritable options
    DEFAULTS = {
      "jailed" => false,
      "plugins" => GitHubPages::Plugins::DEFAULT_PLUGINS,
      "future" => true,
      "theme" => "jekyll-theme-primer",
      "markdown" => "kramdown",
      "kramdown" => {
        "input" => "GFM",
        "hard_wrap" => false,
        "gfm_quirks" => "paragraph_end",
        "syntax_highlighter_opts" => {
          "default_lang" => "plaintext",
        },
      },
      "exclude" => ["CNAME"],
    }.freeze

    # User-overwritable defaults used only in production for practical reasons
    PRODUCTION_DEFAULTS = Jekyll::Utils.deep_merge_hashes DEFAULTS, {
      "sass" => {
        "style" => "compressed",
      },
    }.freeze

    # Options which GitHub Pages sets, regardless of the user-specified value
    #
    # The following values are also overridden by GitHub Pages, but are not
    # overridden locally, for practical purposes:
    # * source
    # * destination
    # * jailed
    # * verbose
    # * incremental
    # * GH_ENV
    OVERRIDES = {
      "lsi" => false,
      "safe" => true,
      "plugins_dir" => SecureRandom.hex,
      "whitelist" => GitHubPages::Plugins::PLUGIN_WHITELIST,
      "highlighter" => "rouge",
      "kramdown" => {
        "template" => "",
        "math_engine" => "mathjax",
        "syntax_highlighter" => "rouge",
      },
      "gist" => {
        "noscript" => false,
      },
    }.freeze

    # These configuration settings have corresponding instance variables on
    # Jekyll::Site and need to be set properly when the config is updated.
    CONFIGS_WITH_METHODS = %w(
      safe lsi highlighter baseurl exclude include future unpublished
      show_drafts limit_posts keep_files
    ).freeze

    class << self
      def processed?(site)
        site.instance_variable_get(:@_github_pages_processed) == true
      end

      def processed(site)
        site.instance_variable_set :@_github_pages_processed, true
      end

      def disable_whitelist?
        development? && !ENV["DISABLE_WHITELIST"].to_s.empty?
      end

      def development?
        Jekyll.env == "development"
      end

      def defaults_for_env
        defaults = development? ? DEFAULTS : PRODUCTION_DEFAULTS
        Jekyll::Utils.deep_merge_hashes Jekyll::Configuration::DEFAULTS, defaults
      end

      # Given a user's config, determines the effective configuration by building a user
      # configuration sandwhich with our overrides overriding the user's specified
      # values which themselves override our defaults.
      #
      # Returns the effective Configuration
      #
      # Note: this is a highly modified version of Jekyll#configuration
      def effective_config(user_config)
        # Merge user config into defaults
        config = Jekyll::Utils.deep_merge_hashes(defaults_for_env, user_config)
          .fix_common_issues
          .add_default_collections

        # Allow theme to be explicitly disabled via "theme: null"
        config["theme"] = user_config["theme"] if user_config.key?("theme")

        migrate_theme_to_remote_theme(config)
        exclude_cname(config)

        # Merge overwrites into user config
        config = Jekyll::Utils.deep_merge_hashes config, OVERRIDES

        restrict_and_config_markdown_processor(config)

        configure_plugins(config)

        config
      end

      # Set the site's configuration. Implemented as an `after_reset` hook.
      # Equivalent #set! function contains the code of interest. This function
      # guards against double-processing via the value in #processed.
      def set(site)
        return if processed? site

        debug_print_versions
        set!(site)
        processed(site)
      end

      # Set the site's configuration with all the proper defaults and overrides.
      # Should be called by #set to protect against multiple processings.
      def set!(site)
        site.config = effective_config(site.config)
      end

      private

      # Ensure we're using Kramdown or GFM.  Force to Kramdown if
      # neither of these.
      #
      # This can get called multiply on the same config, so try to
      # be idempotentish.
      def restrict_and_config_markdown_processor(config)
        config["markdown"] = "kramdown" unless \
          %w(kramdown gfm commonmarkghpages).include?(config["markdown"].to_s.downcase)

        return unless config["markdown"].to_s.casecmp("gfm").zero?

        config["markdown"] = "CommonMarkGhPages"
        config["commonmark"] = {
          "extensions" => %w(table strikethrough autolink tagfilter),
          "options" => %w(unsafe footnotes),
        }
      end

      # If the user has set a 'theme', then see if we can automatically use remote theme instead.
      def migrate_theme_to_remote_theme(config)
        # This functionality has been rolled back due to complications with jekyll-remote-theme.
      end

      # If the user's 'exclude' config is the default, also exclude the CNAME
      def exclude_cname(config)
        return unless config["exclude"].eql? Jekyll::Configuration::DEFAULTS["exclude"]

        config["exclude"].concat(DEFAULTS["exclude"])
      end

      # Requires default plugins and configures whitelist in development
      def configure_plugins(config)
        # Ensure we have those gems we want.
        config["plugins"] = Array(config["plugins"]) | DEFAULT_PLUGINS

        # To minimize errors, lazy-require jekyll-remote-theme if requested by the user
        config["plugins"].push("jekyll-remote-theme") if config.key? "remote_theme"

        return unless development?

        if disable_whitelist?
          config["whitelist"] = config["whitelist"] | config["plugins"]
        end

        config["whitelist"] = config["whitelist"] | DEVELOPMENT_PLUGINS
      end

      # Print the versions for github-pages and jekyll to the debug
      # stream for debugging purposes. See by running Jekyll with '--verbose'
      def debug_print_versions
        Jekyll.logger.debug "GitHub Pages:", "github-pages v#{GitHubPages::VERSION}"
        Jekyll.logger.debug "GitHub Pages:", "jekyll v#{Jekyll::VERSION}"
      end
    end
  end
end
