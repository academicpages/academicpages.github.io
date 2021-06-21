require 'csl'
require 'csl/styles/version'

CSL::Style.root  = File.expand_path('../../../vendor/styles',  __FILE__)
CSL::Locale.root = File.expand_path('../../../vendor/locales', __FILE__)
