# frozen_string_literal: true

require_relative 'adapter/httpclient'
require_relative 'httpclient/version'

module Faraday
  # Main Faraday::HTTPClient module
  module HTTPClient
    Faraday::Adapter.register_middleware(httpclient: Faraday::Adapter::HTTPClient)
  end
end
