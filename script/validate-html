#!/usr/bin/env ruby
# frozen_string_literal: true

require "w3c_validators"

def validator(file)
  extension = File.extname(file)
  if extension == ".html"
    W3CValidators::NuValidator.new
  elsif extension == ".css"
    W3CValidators::CSSValidator.new
  end
end

def validate(file)
  puts "Checking #{file}..."

  path = File.expand_path "../_site/#{file}", __dir__
  results = validator(file).validate_file(path)

  return puts "Valid!" if results.errors.empty?

  results.errors.each { |err| puts err }
  exit 1
end

validate "index.html"
validate File.join "assets", "css", "style.css"
