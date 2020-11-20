# frozen_string_literal: true

module Ruby
  module Enum
    module Errors
      class Base < StandardError
        # Problem occurred.
        attr_reader :problem

        # Summary of the problem.
        attr_reader :summary

        # Suggested problem resolution.
        attr_reader :resolution

        # Compose the message.
        # === Parameters
        # [key] Lookup key in the translation table.
        # [attributes] The objects to pass to create the message.
        def compose_message(key, attributes = {})
          @problem = create_problem(key, attributes)
          @summary = create_summary(key, attributes)
          @resolution = create_resolution(key, attributes)

          "\nProblem:\n  #{@problem}"\
          "\nSummary:\n  #{@summary}" + "\nResolution:\n  #{@resolution}"
        end

        private

        BASE_KEY = 'ruby.enum.errors.messages' #:nodoc:

        # Given the key of the specific error and the options hash, translate the
        # message.
        #
        # === Parameters
        # [key] The key of the error in the locales.
        # [options] The objects to pass to create the message.
        #
        # Returns a localized error message string.
        def translate(key, options)
          ::I18n.translate("#{BASE_KEY}.#{key}", { locale: :en }.merge(options)).strip
        end

        # Create the problem.
        #
        # === Parameters
        # [key] The error key.
        # [attributes] The attributes to interpolate.
        #
        # Returns the problem.
        def create_problem(key, attributes)
          translate("#{key}.message", attributes)
        end

        # Create the summary.
        #
        # === Parameters
        # [key] The error key.
        # [attributes] The attributes to interpolate.
        #
        # Returns the summary.
        def create_summary(key, attributes)
          translate("#{key}.summary", attributes)
        end

        # Create the resolution.
        #
        # === Parameters
        # [key] The error key.
        # [attributes] The attributes to interpolate.
        #
        # Returns the resolution.
        def create_resolution(key, attributes)
          translate("#{key}.resolution", attributes)
        end
      end
    end
  end
end
