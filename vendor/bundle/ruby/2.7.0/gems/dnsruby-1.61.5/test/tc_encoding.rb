require_relative 'spec_helper'

require 'socket'

# @TODO@ We also need a test server so we can control behaviour of server to test
# different aspects of retry strategy.
# Of course, with Ruby's limit of 256 open sockets per process, we'd need to run
# the server in a different Ruby process.

class TestEncoding < Minitest::Test

  include Dnsruby

  Thread::abort_on_exception = true

  Dnsruby::TheLog.level = Logger::DEBUG


  def test_cdnskey
    rrString = "tjeb.nl.\t3600\tIN\tCDNSKEY\t256 3 RSASHA1-NSEC3-SHA1 ( AwEAAcglEOS7bECRK5fqTuGTMJycmDhTzmUu/EQbAhKJOYJxDb5SG/RYqsJgzG7wgtGy0W1aP7I4k6SPtHmwcqjLaZLVUwRNWCGr2adjb9JTFyBR7F99Ngi11lEGM6Uiw/eDRk66lhoSGzohjj/rmhRTV6gN2+0ADPnafv3MBkPgryA3 ) ; key_tag=53177"
    rr = RR.create(rrString)
    puts rr
    puts rrString
    assert(rrString.to_s == rr.to_s)
    m = Dnsruby::Message.new
    m.add_additional(rr)
    m2 = Message.decode(m.encode)
    rr2 = m2.additional()[0]
    assert(rr.to_s == rr2.to_s)
  end
end
