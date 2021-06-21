# frozen_string_literal: true
# The line below caused a problem on non-GAE rack environment.
# unless defined?(JRuby::Rack::VERSION) || defined?(AppEngine::ApiProxy)
#
# However, simply cutting defined?(JRuby::Rack::VERSION) off resulted in
# an unable-to-load-nokogiri problem. Thus, now, Nokogiri checks the presense
# of appengine-rack.jar in $LOAD_PATH. If Nokogiri is on GAE, Nokogiri
# should skip loading xml jars. This is because those are in WEB-INF/lib and
# already set in the classpath.
unless $LOAD_PATH.to_s.include?("appengine-rack")
  require 'stringio'
  require 'isorelax.jar'
  require 'jing.jar'
  require 'nekohtml.jar'
  require 'nekodtd.jar'
  require 'xercesImpl.jar'
  require 'serializer.jar'
  require 'xalan.jar'
  require 'xml-apis.jar'
end
