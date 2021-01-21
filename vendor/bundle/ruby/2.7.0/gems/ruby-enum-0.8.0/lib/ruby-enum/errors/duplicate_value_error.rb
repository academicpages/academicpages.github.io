# frozen_string_literal: true

module Ruby
  module Enum
    module Errors
      # Error raised when a duplicate enum value is found
      class DuplicateValueError < Base
        def initialize(attrs)
          super(compose_message('duplicate_value', attrs))
        end
      end
    end
  end
end
