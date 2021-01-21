# frozen_string_literal: true

require "sass"
require "jekyll/utils"

module Jekyll
  module Converters
    class Scss < Converter
      BYTE_ORDER_MARK = %r!^\xEF\xBB\xBF!
      SyntaxError = Class.new(ArgumentError)

      safe true
      priority :low

      ALLOWED_STYLES = %w(nested expanded compact compressed).freeze

      def matches(ext)
        ext =~ %r!^\.scss$!i
      end

      def output_ext(_ext)
        ".css"
      end

      def safe?
        !!@config["safe"]
      end

      def jekyll_sass_configuration
        options = @config["sass"] || {}
        unless options["style"].nil?
          options["style"] = options["style"].to_s.gsub(%r!\A:!, "").to_sym
        end
        options
      end

      def sass_build_configuration_options(overrides)
        if safe?
          {
            :load_paths => sass_load_paths,
            :syntax     => syntax,
            :style      => sass_style,
            :cache      => false,
          }
        else
          Jekyll::Utils.symbolize_hash_keys(
            Jekyll::Utils.deep_merge_hashes(
              jekyll_sass_configuration,
              overrides
            )
          )
        end
      end

      def syntax
        :scss
      end

      def sass_dir
        return "_sass" if jekyll_sass_configuration["sass_dir"].to_s.empty?
        jekyll_sass_configuration["sass_dir"]
      end

      def sass_style
        style = jekyll_sass_configuration.fetch("style", :compact)
        ALLOWED_STYLES.include?(style.to_s) ? style.to_sym : :compact
      end

      def user_sass_load_paths
        Array(jekyll_sass_configuration["load_paths"])
      end

      def sass_dir_relative_to_site_source
        Jekyll.sanitized_path(site_source, sass_dir)
      end

      def sass_load_paths
        paths = user_sass_load_paths + [sass_dir_relative_to_site_source]

        if safe?
          # Sanitize paths to prevent any attack vectors (.e.g. `/**/*`)
          paths.map! { |path| Jekyll.sanitized_path(site_source, path) }
        end

        # Expand file globs (e.g. `node_modules/*/node_modules` )
        Dir.chdir(site_source) do
          paths = paths.map { |path| Dir.glob(path) }.flatten.uniq

          paths.map! do |path|
            if safe?
              # Sanitize again in case globbing was able to do something crazy.
              Jekyll.sanitized_path(site_source, path)
            else
              File.expand_path(path)
            end
          end
        end

        paths.select { |path| File.directory?(path) }
      end

      def allow_caching?
        !safe?
      end

      def add_charset?
        !!jekyll_sass_configuration["add_charset"]
      end

      def sass_configs
        sass_build_configuration_options({
          "syntax"     => syntax,
          "cache"      => allow_caching?,
          "load_paths" => sass_load_paths,
        })
      end

      def convert(content)
        output = ::Sass.compile(content, sass_configs)
        replacement = add_charset? ? '@charset "UTF-8";' : ""
        output.sub(BYTE_ORDER_MARK, replacement)
      rescue ::Sass::SyntaxError => e
        raise SyntaxError, "#{e} on line #{e.sass_line}"
      end

      private
      def site_source
        @site_source ||= File.expand_path(@config["source"]).freeze
      end
    end
  end
end
