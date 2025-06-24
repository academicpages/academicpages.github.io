# frozen_string_literal: true

module Jekyll
  module RemoteTheme
    # Jekyll::Theme expects the theme's gemspec to tell it things like
    # the path to the theme and runtime dependencies. MockGemspec serves as a
    # stand in, since remote themes don't need Gemspecs
    class MockGemspec
      extend Forwardable
      def_delegator :theme, :root, :full_gem_path

      DEPENDENCY_PREFIX = %r!^\s*[a-z]+\.add_(?:runtime_)?dependency!.freeze
      DEPENDENCY_REGEX = %r!#{DEPENDENCY_PREFIX}\(?\s*["']([a-z_-]+)["']!.freeze

      def initialize(theme)
        @theme = theme
      end

      def runtime_dependencies
        @runtime_dependencies ||= dependency_names.map do |name|
          Gem::Dependency.new(name)
        end
      end

      private

      def contents
        @contents ||= File.read(path, :encoding => "utf-8") if path
      end

      def path
        @path ||= potential_paths.find { |path| File.exist? path }
      end

      def potential_paths
        [theme.name, "jekyll-theme-#{theme.name}"].map do |filename|
          File.expand_path "#{filename}.gemspec", theme.root
        end
      end

      def dependency_names
        @dependency_names ||= if contents
                                contents.scan(DEPENDENCY_REGEX).flatten
                              else
                                []
                              end
      end

      attr_reader :theme
    end
  end
end
