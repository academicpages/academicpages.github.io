# frozen_string_literal: true

require_relative 'adapter/em_http'
require_relative 'em_http/version'

module Faraday
  # Main Faraday::EmHttp module
  module EmHttp
    Faraday::Adapter.register_middleware(em_http: Faraday::Adapter::EMHttp)
  end
end
