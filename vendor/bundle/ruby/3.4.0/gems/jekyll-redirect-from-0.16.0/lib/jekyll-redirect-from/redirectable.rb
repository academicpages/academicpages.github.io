# frozen_string_literal: true

module JekyllRedirectFrom
  # Module which can be mixed in to documents (and pages) to provide
  # redirect_to and redirect_from helpers
  module Redirectable
    # Returns a string representing the relative path or URL
    # to which the document should be redirected
    def redirect_to
      if to_liquid["redirect_to"].is_a?(Array)
        to_liquid["redirect_to"].compact.first
      else
        to_liquid["redirect_to"]
      end
    end

    # Returns an array representing the relative paths to other
    # documents which should be redirected to this document
    def redirect_from
      if to_liquid["redirect_from"].is_a?(Array)
        to_liquid["redirect_from"].compact
      else
        [to_liquid["redirect_from"]].compact
      end
    end
  end
end
