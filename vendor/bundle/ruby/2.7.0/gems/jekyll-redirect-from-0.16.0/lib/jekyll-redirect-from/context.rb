# frozen_string_literal: true

module JekyllRedirectFrom
  # Stubbed LiquidContext to support relative_url and absolute_url helpers
  class Context
    attr_reader :site

    def initialize(site)
      @site = site
    end

    def registers
      { :site => site }
    end
  end
end
