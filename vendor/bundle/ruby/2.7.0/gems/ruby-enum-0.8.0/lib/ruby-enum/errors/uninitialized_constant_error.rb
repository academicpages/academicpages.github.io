# frozen_string_literal: true

module Ruby
  module Enum
    module Errors
      class UninitializedConstantError < Base
        def initialize(attrs)
          super(compose_message('uninitialized_constant', attrs))
        end
      end
    end
  end
end
