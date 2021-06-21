# frozen_string_literal: true

require 'faraday/em_http'
require_relative 'adapter/em_synchrony'
require_relative 'em_synchrony/version'

module Faraday
  # Main Faraday::EmSynchrony module
  module EmSynchrony
    Faraday::Adapter.register_middleware(em_synchrony: Faraday::Adapter::EMSynchrony)
  end
end
