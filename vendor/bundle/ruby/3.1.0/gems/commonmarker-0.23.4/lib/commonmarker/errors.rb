# frozen_string_literal: true

require 'commonmarker/node/inspect'

module CommonMarker
  class RenderError < StandardError
    PREAMBLE = 'There was an error rendering'
    def initialize(error)
      super("#{PREAMBLE}: #{error.class} #{error.message}")
    end
  end
end
