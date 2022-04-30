# frozen_string_literal: true

require_relative 'multipart/file_part'
require_relative 'multipart/param_part'
require_relative 'multipart/middleware'
require_relative 'multipart/version'

module Faraday
  # Main Faraday::Multipart module.
  module Multipart
    Faraday::Request.register_middleware(multipart: Faraday::Multipart::Middleware)
  end

  # Aliases for Faraday v1, these are all deprecated and will be removed in v2 of this middleware
  FilePart = Multipart::FilePart
  ParamPart = Multipart::ParamPart
  Parts = Multipart::Parts
  CompositeReadIO = Multipart::CompositeReadIO
  UploadIO = ::UploadIO
end
