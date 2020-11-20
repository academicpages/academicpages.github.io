# frozen_string_literal: true

module Jekyll
  module RemoteTheme
    class Theme < Jekyll::Theme
      OWNER_REGEX = %r!(?<owner>[a-z0-9\-]+)!i.freeze
      NAME_REGEX  = %r!(?<name>[a-z0-9\._\-]+)!i.freeze
      REF_REGEX   = %r!@(?<ref>[a-z0-9\._\-]+)!i.freeze # May be a branch, tag, or commit
      THEME_REGEX = %r!\A#{OWNER_REGEX}/#{NAME_REGEX}(?:#{REF_REGEX})?\z!i.freeze

      # Initializes a new Jekyll::RemoteTheme::Theme
      #
      # raw_theme can be in the form of:
      #
      # 1. owner/theme-name - a GitHub owner + theme-name string
      # 2. owner/theme-name@git_ref - a GitHub owner + theme-name + Git ref string
      # 3. http[s]://github.<yourEnterprise>.com/owner/theme-name
      # - An enterprise GitHub instance + a GitHub owner + a theme-name string
      # 4. http[s]://github.<yourEnterprise>.com/owner/theme-name@git_ref
      # - An enterprise GitHub instance + a GitHub owner + a theme-name + Git ref string
      def initialize(raw_theme)
        @raw_theme = raw_theme.to_s.downcase.strip
        super(@raw_theme)
      end

      def name
        theme_parts[:name]
      end

      def owner
        theme_parts[:owner]
      end

      def host
        uri&.host
      end

      def scheme
        uri&.scheme
      end

      def name_with_owner
        [owner, name].join("/")
      end
      alias_method :nwo, :name_with_owner

      def valid?
        return false unless uri && theme_parts && name && owner

        host && valid_hosts.include?(host)
      end

      def git_ref
        theme_parts[:ref] || "master"
      end

      def root
        @root ||= File.realpath Dir.mktmpdir(TEMP_PREFIX)
      end

      def inspect
        "#<Jekyll::RemoteTheme::Theme host=\"#{host}\" owner=\"#{owner}\" name=\"#{name}\"" \
        " ref=\"#{git_ref}\" root=\"#{root}\">"
      end

      private

      def uri
        return @uri if defined? @uri

        @uri = if @raw_theme =~ THEME_REGEX
                 Addressable::URI.new(
                   :scheme => "https",
                   :host   => "github.com",
                   :path   => @raw_theme
                 )
               else
                 Addressable::URI.parse @raw_theme
               end
      rescue Addressable::URI::InvalidURIError
        @uri = nil
      end

      def theme_parts
        @theme_parts ||= uri.path[1..-1].match(THEME_REGEX) if uri
      end

      def gemspec
        @gemspec ||= MockGemspec.new(self)
      end

      def valid_hosts
        @valid_hosts ||= [
          "github.com",
          ENV["PAGES_GITHUB_HOSTNAME"],
          ENV["GITHUB_HOSTNAME"],
        ].compact.to_set
      end
    end
  end
end
