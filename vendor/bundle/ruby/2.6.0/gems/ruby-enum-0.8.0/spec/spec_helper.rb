# frozen_string_literal: true

$LOAD_PATH.unshift(File.join(File.dirname(__FILE__), '..', 'lib'))

require 'rubygems'
require 'rspec'
require 'ruby-enum'

RSpec.configure(&:raise_errors_for_deprecations!)
