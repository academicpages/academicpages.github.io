# frozen_string_literal: true

require 'faraday/adapter/rack'
require 'faraday/rack/version'

module Faraday
  # Main Faraday::Rack module
  module Rack
    Faraday::Adapter.register_middleware(rack: Faraday::Adapter::Rack)
  end
end
