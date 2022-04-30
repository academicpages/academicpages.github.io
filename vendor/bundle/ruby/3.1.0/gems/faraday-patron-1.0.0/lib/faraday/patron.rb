# frozen_string_literal: true

require_relative 'adapter/patron'
require_relative 'patron/version'

module Faraday
  # Main Faraday::Patron module
  module Patron
    Faraday::Adapter.register_middleware(patron: Faraday::Adapter::Patron)
  end
end
