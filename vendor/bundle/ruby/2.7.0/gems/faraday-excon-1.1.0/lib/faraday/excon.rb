# frozen_string_literal: true

require_relative 'adapter/excon'
require_relative 'excon/version'

module Faraday
  # Main Faraday::Excon module
  module Excon
    Faraday::Adapter.register_middleware(excon: Faraday::Adapter::Excon)
  end
end
