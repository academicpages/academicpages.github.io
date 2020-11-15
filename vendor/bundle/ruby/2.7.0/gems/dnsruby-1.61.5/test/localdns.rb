#!/usr/bin/env ruby

require_relative 'spec_helper'

require_relative "test_dnsserver"

class SimpleTCPPipeliningUDPServer < Async::DNS::Server
  PORT     = 53938
  IP   = '127.0.0.1'

  def initialize(**options)
    super(options)

    @handlers << TcpPipelineHandler.new(self, IP, PORT)
    @handlers << Async::DNS::UDPServerHandler.new(self, IP, PORT)

  end

  def process(name, resource_class, transaction)
    @logger.debug "name: #{name}"
    transaction.respond!("93.184.216.34", { resource_class: ::Resolv::DNS::Resource::IN::A })
  end

end


if __FILE__ == $0
  RubyDNS::run_server(server_class: SimpleTCPPipeliningUDPServer)
end
