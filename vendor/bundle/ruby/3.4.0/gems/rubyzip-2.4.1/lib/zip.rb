require 'English'
require 'delegate'
require 'singleton'
require 'tempfile'
require 'fileutils'
require 'stringio'
require 'zlib'
require 'zip/constants'
require 'zip/dos_time'
require 'zip/ioextras'
require 'rbconfig'
require 'zip/entry'
require 'zip/extra_field'
require 'zip/entry_set'
require 'zip/central_directory'
require 'zip/file'
require 'zip/input_stream'
require 'zip/output_stream'
require 'zip/decompressor'
require 'zip/compressor'
require 'zip/null_decompressor'
require 'zip/null_compressor'
require 'zip/null_input_stream'
require 'zip/pass_thru_compressor'
require 'zip/pass_thru_decompressor'
require 'zip/crypto/decrypted_io'
require 'zip/crypto/encryption'
require 'zip/crypto/null_encryption'
require 'zip/crypto/traditional_encryption'
require 'zip/inflater'
require 'zip/deflater'
require 'zip/streamable_stream'
require 'zip/streamable_directory'
require 'zip/errors'

module Zip
  V3_API_WARNING_MSG = <<~END_MSG
    You have called '%s' (from %s).
    This method is changing or deprecated in version 3.0.0. Please see
      https://github.com/rubyzip/rubyzip/wiki/Updating-to-version-3.x
    for more information.
  END_MSG

  def self.warn_about_v3_api(method)
    return unless ENV['RUBYZIP_V3_API_WARN']

    loc = caller_locations(2, 1)[0]
    from = "#{loc.path.split('/').last}:#{loc.lineno}"
    warn format(V3_API_WARNING_MSG, method, from)
  end

  if ENV['RUBYZIP_V3_API_WARN'] && RUBY_VERSION < '3.0'
    warn 'RubyZip 3.0 will require Ruby 3.0 or later.'
  end

  extend self
  attr_accessor :unicode_names,
                :on_exists_proc,
                :continue_on_exists_proc,
                :sort_entries,
                :default_compression,
                :write_zip64_support,
                :warn_invalid_date,
                :case_insensitive_match,
                :force_entry_names_encoding,
                :validate_entry_sizes

  def reset!
    @_ran_once = false
    @unicode_names = false
    @on_exists_proc = false
    @continue_on_exists_proc = false
    @sort_entries = false
    @default_compression = ::Zlib::DEFAULT_COMPRESSION
    @write_zip64_support = false
    @warn_invalid_date = true
    @case_insensitive_match = false
    @validate_entry_sizes = true
  end

  def setup
    yield self unless @_ran_once
    @_ran_once = true
  end

  reset!
end

# Copyright (C) 2002, 2003 Thomas Sondergaard
# rubyzip is free software; you can redistribute it and/or
# modify it under the terms of the ruby license.
