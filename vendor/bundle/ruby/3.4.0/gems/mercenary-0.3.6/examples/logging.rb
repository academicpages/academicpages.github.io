#!/usr/bin/env ruby

$:.unshift File.join(File.dirname(__FILE__), *%w{ .. lib })

require "mercenary"

# This example sets the logging mode of mercenary to
# debug. Logging messages from "p.logger.debug" will
# be output to STDOUT.

Mercenary.program(:logger_output) do |p|

  p.version "5.2.6"
  p.description 'An example of turning on logging for Mercenary.'
  p.syntax 'logger_output'


  p.logger.info "The default log level is INFO. So this will output."
  p.logger.debug "Since DEBUG is below INFO, this will not output."

  p.logger(Logger::DEBUG)
  p.logger.debug "Logger level now set to DEBUG. So everything will output."
  
  p.logger.debug    "Example of DEBUG level message."
  p.logger.info     "Example of INFO level message."
  p.logger.warn     "Example of WARN level message."
  p.logger.error    "Example of ERROR level message."
  p.logger.fatal    "Example of FATAL level message."
  p.logger.unknown  "Example of UNKNOWN level message."

  p.action do |args, options|
    
    p.logger(Logger::INFO)
    p.logger.debug "Logger level back to INFO. This line will not output."
    p.logger.info "This INFO message will output."

  end

end
