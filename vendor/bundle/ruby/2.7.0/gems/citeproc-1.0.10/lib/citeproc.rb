
require 'date'
require 'forwardable'
require 'observer'
require 'open-uri'

require 'json'
require 'namae'

require 'citeproc/version'

#
# CiteProc processes bibliographic data and formats it according to a style
# defined in CSL (Citation Style Language).
#
# @author Sylvester Keil
#
# Copyright 2009-2014 Sylvester Keil. All rights reserved.
#
# Copyright 2012 President and Fellows of Harvard College.
#
module CiteProc

  module Converters
  end

  module Utilities
  end

end

require 'citeproc/compatibility'
require 'citeproc/extensions'

require 'citeproc/errors'

require 'citeproc/abbreviate'
require 'citeproc/attributes'

require 'citeproc/variable'
require 'citeproc/number'
require 'citeproc/date'
require 'citeproc/names'

CiteProc::Variable.class_eval do
  @factories = Hash.new { |h,k| h.fetch(k.to_s.intern, CiteProc::Variable) }.merge(
    Hash[*@types.map { |n,k|
      [n, CiteProc.const_get(k.to_s.capitalize)]
    }.flatten]
  ).freeze
end

require 'citeproc/item'
require 'citeproc/citation_data'
require 'citeproc/selector'
require 'citeproc/bibliography'
require 'citeproc/assets'

require 'citeproc/engine'
require 'citeproc/processor'
require 'citeproc/utilities'

CiteProc.extend CiteProc::Utilities


CiteProc::Converters.class_eval do

  # Define all converters (all classes have been loaded at this point)
  CiteProc.constants.each do |name|
    klass = CiteProc.const_get(name)

    if klass.instance_of?(Class) && klass.respond_to?(:create)

      define_method(name) do |obj|
        obj.instance_of?(klass) ? obj : klass.create(obj)
      end

    end
  end

end
