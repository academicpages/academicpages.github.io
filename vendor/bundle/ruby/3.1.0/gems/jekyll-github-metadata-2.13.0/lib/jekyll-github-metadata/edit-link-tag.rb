# frozen_string_literal: true

module Jekyll
  module GitHubMetadata
    class EditLinkTag < Liquid::Tag
      attr_reader :context

      # Defines an instance method that delegates to a hash's key
      #
      # hash_method -  a symbol representing the instance method to delegate to. The
      #                instance method should return a hash or respond to #[]
      # key         - the key to call within the hash
      # method      - (optional) the instance method the key should be aliased to.
      #               If not specified, defaults to the hash key
      # default     - (optional) value to return if value is nil (defaults to nil)
      #
      # Returns a symbol representing the instance method
      def self.def_hash_delegator(hash_method, key, method, default = nil)
        define_method(method) do
          hash = send(hash_method)
          if hash.respond_to? :[]
            hash[key.to_s] || default
          else
            default
          end
        end
      end

      MISSING_DATA_MSG = "Cannot generate edit URLs due to missing site.github data"
      LINK_TEXT_REGEX = %r!(?:\"(.*)\"|'(.*)')!.freeze

      extend Forwardable
      private def_hash_delegator :site,        :github,         :site_github, {}
      private def_hash_delegator :site_github, :repository_url, :repository_url
      private def_hash_delegator :site_github, :source,         :source, {}
      private def_hash_delegator :source,      :branch,         :branch
      private def_hash_delegator :source,      :path,           :source_path
      private def_hash_delegator :page,        :path,           :page_path

      def render(context)
        @context = context
        if link_text
          link
        else
          uri.to_s
        end
      end

      private

      def link_text
        @link_text ||= begin
          matches = @markup.match LINK_TEXT_REGEX
          matches[1] || matches[2] if matches
        end
      end

      def link
        "<a href=\"#{uri}\">#{link_text}</a>"
      end

      def uri
        if parts.any?(&:nil?)
          Jekyll.logger.warn "JekyllEditLink: ", MISSING_DATA_MSG
          ""
        else
          Addressable::URI.join(*parts_normalized).normalize
        end
      end

      def parts
        memoize_conditionally { [repository_url, "edit/", branch, source_path, page_path] }
      end

      def parts_normalized
        memoize_conditionally do
          parts.map.with_index do |part, index|
            part = remove_leading_slash(part.to_s)
            part = ensure_trailing_slash(part) unless index == parts.length - 1
            ensure_not_just_a_slash(part)
          end
        end
      end

      def page
        memoize_conditionally { context.registers[:page] }
      end

      # Utility function for compatibility with Jekyll 4.0
      def memoize_conditionally
        if renderer_cached?
          yield
        else
          dispatcher = "@#{caller_locations(1..1).first.label}".to_sym
          if instance_variable_defined?(dispatcher)
            instance_variable_get(dispatcher)
          else
            instance_variable_set(dispatcher, yield)
          end
        end
      end

      # Utility function to detect Jekyll 4.0
      def renderer_cached?
        @renderer_cached ||= context.registers[:site].liquid_renderer.respond_to?(:cache)
      end

      def site
        @site ||= context.registers[:site].site_payload["site"]
      end

      def remove_leading_slash(part)
        part.start_with?("/") ? part[1..-1] : part
      end

      def ensure_trailing_slash(part)
        part.end_with?("/") ? part : "#{part}/"
      end

      def ensure_not_just_a_slash(part)
        part == "/" ? "" : part
      end
    end
  end
end
