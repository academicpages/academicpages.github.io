# frozen_string_literal: true

require 'cgi'
HTML::Pipeline.require_dependency('gemoji', 'EmojiFilter')

module HTML
  class Pipeline
    # HTML filter that replaces :emoji: with images.
    #
    # Context:
    #   :asset_root (required) - base url to link to emoji sprite
    #   :asset_path (optional) - url path to link to emoji sprite. :file_name can be used as a placeholder for the sprite file name. If no asset_path is set "emoji/:file_name" is used.
    #   :ignored_ancestor_tags (optional) - Tags to stop the emojification. Node has matched ancestor HTML tags will not be emojified. Default to pre, code, and tt tags. Extra tags please pass in the form of array, e.g., %w(blockquote summary).
    #   :img_attrs (optional) - Attributes for generated img tag. E.g. Pass { "draggble" => true, "height" => nil } to set draggable attribute to "true" and clear height attribute of generated img tag.
    class EmojiFilter < Filter
      DEFAULT_IGNORED_ANCESTOR_TAGS = %w[pre code tt].freeze

      def call
        doc.search('.//text()').each do |node|
          content = node.text
          next unless content.include?(':')
          next if has_ancestor?(node, ignored_ancestor_tags)
          html = emoji_image_filter(content)
          next if html == content
          node.replace(html)
        end
        doc
      end

      # Implementation of validate hook.
      # Errors should raise exceptions or use an existing validator.
      def validate
        needs :asset_root
      end

      # Replace :emoji: with corresponding images.
      #
      # text - String text to replace :emoji: in.
      #
      # Returns a String with :emoji: replaced with images.
      def emoji_image_filter(text)
        text.gsub(emoji_pattern) do |_match|
          emoji_image_tag(Regexp.last_match(1))
        end
      end

      # The base url to link emoji sprites
      #
      # Raises ArgumentError if context option has not been provided.
      # Returns the context's asset_root.
      def asset_root
        context[:asset_root]
      end

      # The url path to link emoji sprites
      #
      # :file_name can be used in the asset_path as a placeholder for the sprite file name. If no asset_path is set in the context "emoji/:file_name" is used.
      # Returns the context's asset_path or the default path if no context asset_path is given.
      def asset_path(name)
        if context[:asset_path]
          context[:asset_path].gsub(':file_name', emoji_filename(name))
        else
          File.join('emoji', emoji_filename(name))
        end
      end

      private

      # Build an emoji image tag
      def emoji_image_tag(name)
        require 'active_support/core_ext/hash/indifferent_access'
        html_attrs =
          default_img_attrs(name)
          .merge!((context[:img_attrs] || {}).with_indifferent_access)
          .map { |attr, value| !value.nil? && %(#{attr}="#{value.respond_to?(:call) && value.call(name) || value}") }
          .reject(&:blank?).join(' '.freeze)

        "<img #{html_attrs}>"
      end

      # Default attributes for img tag
      def default_img_attrs(name)
        {
          'class' => 'emoji'.freeze,
          'title' => ":#{name}:",
          'alt' => ":#{name}:",
          'src' => emoji_url(name).to_s,
          'height' => '20'.freeze,
          'width' => '20'.freeze,
          'align' => 'absmiddle'.freeze
        }
      end

      def emoji_url(name)
        File.join(asset_root, asset_path(name))
      end

      # Build a regexp that matches all valid :emoji: names.
      def self.emoji_pattern
        @emoji_pattern ||= /:(#{emoji_names.map { |name| Regexp.escape(name) }.join('|')}):/
      end

      def emoji_pattern
        self.class.emoji_pattern
      end

      def self.emoji_names
        Emoji.all.map(&:aliases).flatten.sort
      end

      def emoji_filename(name)
        Emoji.find_by_alias(name).image_filename
      end

      # Return ancestor tags to stop the emojification.
      #
      # @return [Array<String>] Ancestor tags.
      def ignored_ancestor_tags
        if context[:ignored_ancestor_tags]
          DEFAULT_IGNORED_ANCESTOR_TAGS | context[:ignored_ancestor_tags]
        else
          DEFAULT_IGNORED_ANCESTOR_TAGS
        end
      end
    end
  end
end
