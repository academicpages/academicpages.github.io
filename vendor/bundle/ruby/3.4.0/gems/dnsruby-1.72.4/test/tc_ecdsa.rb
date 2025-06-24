require_relative 'spec_helper'

Dnsruby::TheLog.level = Logger::DEBUG

class VerifierTest < Minitest::Test

  def test_ecdsa
    inner_resolver = Dnsruby::Resolver.new
    inner_resolver.do_validation = true
    inner_resolver.dnssec = true
    resolver = Dnsruby::Recursor.new(inner_resolver)
    resolver.dnssec = true

    #    Dnsruby::TheLog.level=Logger::DEBUG

    name = 'carlgo11.com'
    type = 'A'
    klass = 'IN'

    begin
      answer = resolver.query(name, type, klass)
      print answer
    rescue Exception => e
      fatal_error("query failed: #{e}")
    end
  end
end
