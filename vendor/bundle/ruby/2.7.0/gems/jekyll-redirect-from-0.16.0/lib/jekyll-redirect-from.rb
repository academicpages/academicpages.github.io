# frozen_string_literal: true

require "jekyll"
require "jekyll-redirect-from/version"
require "jekyll-redirect-from/generator"

module JekyllRedirectFrom
  # Jekyll classes which should be redirectable
  CLASSES = [Jekyll::Page, Jekyll::Document].freeze

  autoload :Context,          "jekyll-redirect-from/context"
  autoload :RedirectPage,     "jekyll-redirect-from/redirect_page"
  autoload :Redirectable,     "jekyll-redirect-from/redirectable"
  autoload :Layout,           "jekyll-redirect-from/layout"
  autoload :PageWithoutAFile, "jekyll-redirect-from/page_without_a_file"
end

JekyllRedirectFrom::CLASSES.each do |klass|
  klass.send :include, JekyllRedirectFrom::Redirectable
end
