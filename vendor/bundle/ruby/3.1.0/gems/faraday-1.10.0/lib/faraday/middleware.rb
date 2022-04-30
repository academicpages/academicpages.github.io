# frozen_string_literal: true

module Faraday
  # Middleware is the basic base class of any Faraday middleware.
  class Middleware
    extend MiddlewareRegistry
    extend DependencyLoader

    attr_reader :app, :options

    def initialize(app = nil, options = {})
      @app = app
      @options = options
    end

    def call(env)
      on_request(env) if respond_to?(:on_request)
      app.call(env).on_complete do |environment|
        on_complete(environment) if respond_to?(:on_complete)
      end
    end

    def close
      if app.respond_to?(:close)
        app.close
      else
        warn "#{app} does not implement \#close!"
      end
    end
  end
end
