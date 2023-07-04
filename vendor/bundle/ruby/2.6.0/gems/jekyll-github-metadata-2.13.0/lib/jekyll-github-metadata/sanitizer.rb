# frozen_string_literal: true

module Jekyll
  module GitHubMetadata
    module Sanitizer
      extend self
      # Sanitize an object.
      # When the resource is either `false`, `true`, `nil` or a number,
      #   it returns the resource as-is. When the resource is an array,
      #   it maps over the entire array, sanitizing each of its values.
      #   When the resource responds to the #to_hash method, it returns
      #   the value of #sanitize_resource (see below). If none of the
      #   aforementioned conditions are met, the return value of #to_s
      #   is used.
      #
      # resource - an Object
      #
      # Returns the sanitized resource.
      # rubocop:disable Metrics/CyclomaticComplexity
      def sanitize(resource)
        case resource
        when Array
          resource.map { |item| sanitize(item) }
        when Numeric, Time
          resource
        when FalseClass
          false
        when TrueClass
          true
        when NilClass
          nil
        when String
          resource
        else
          if resource.respond_to?(:to_hash)
            sanitize_resource(resource)
          else
            resource.to_s
          end
        end
      end
      # rubocop:enable Metrics/CyclomaticComplexity

      # Sanitize the Sawyer Resource or Hash
      # Note: the object must respond to :to_hash for this to work.
      # Consider using #sanitize instead of this method directly.
      #
      # resource - an Object which responds to :to_hash
      #
      # Returns the sanitized sawyer resource or hash as a hash.
      def sanitize_resource(resource)
        resource.to_hash.each_with_object({}) do |(k, v), result|
          result[k.to_s] = sanitize(v)
          result
        end
      end
    end
  end
end
