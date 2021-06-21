#!/usr/bin/env ruby
require 'commonmarker/commonmarker'
require 'commonmarker/config'
require 'commonmarker/node'
require 'commonmarker/renderer'
require 'commonmarker/renderer/html_renderer'
require 'commonmarker/version'

begin
  require 'awesome_print'
rescue LoadError; end

module CommonMarker
  # Public:  Parses a Markdown string into an HTML string.
  #
  # text - A {String} of text
  # option - Either a {Symbol} or {Array of Symbol}s indicating the render options
  # extensions - An {Array of Symbol}s indicating the extensions to use
  #
  # Returns a {String} of converted HTML.
  def self.render_html(text, options = :DEFAULT, extensions = [])
    fail TypeError, "text must be a String; got a #{text.class}!" unless text.is_a?(String)
    opts = Config.process_options(options, :render)
    text = text.encode('UTF-8')
    html = Node.markdown_to_html(text, opts, extensions)
    html.force_encoding('UTF-8')
  end

  # Public: Parses a Markdown string into a `document` node.
  #
  # string - {String} to be parsed
  # option - A {Symbol} or {Array of Symbol}s indicating the parse options
  # extensions - An {Array of Symbol}s indicating the extensions to use
  #
  # Returns the `document` node.
  def self.render_doc(text, options = :DEFAULT, extensions = [])
    fail TypeError, "text must be a String; got a #{text.class}!" unless text.is_a?(String)
    opts = Config.process_options(options, :parse)
    text = text.encode('UTF-8')
    Node.parse_document(text, text.bytesize, opts, extensions)
  end
end
