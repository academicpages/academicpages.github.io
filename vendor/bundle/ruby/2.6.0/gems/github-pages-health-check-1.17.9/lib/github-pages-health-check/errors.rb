# frozen_string_literal: true

Dir[File.expand_path("errors/*_error.rb", __dir__)].sort.each do |f|
  require f
end

module GitHubPages
  module HealthCheck
    module Errors
      def self.all
        Error.subclasses
      end
    end
  end
end
