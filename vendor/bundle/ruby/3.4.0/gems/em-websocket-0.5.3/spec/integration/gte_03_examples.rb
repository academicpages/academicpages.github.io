shared_examples_for "a WebSocket server drafts 3 and above" do
  it "should force close connections after a timeout if close handshake is not sent by the client" do
    em {
      server_onerror_fired = false
      server_onclose_fired = false
      client_got_close_handshake = false
      
      start_server(:close_timeout => 0.1) { |ws|
        ws.onopen {
          # 1: Send close handshake to client
          EM.next_tick { ws.close(4999, "Close message") }
        }
        
        ws.onerror { |e|
          # 3: Client should receive onerror
          e.class.should == EM::WebSocket::WSProtocolError
          e.message.should == "Close handshake un-acked after 0.1s, closing tcp connection"
          server_onerror_fired = true
        }
        
        ws.onclose {
          server_onclose_fired = true
        }
      }
      start_client { |client|
        client.onmessage { |msg|
          # 2: Client does not respond to close handshake (the fake client 
          # doesn't understand them at all hence this is in onmessage)
          msg.should =~ /Close message/ if version >= 6
          client_got_close_handshake = true
        }
        
        client.onclose {
          server_onerror_fired.should == true
          server_onclose_fired.should == true
          client_got_close_handshake.should == true
          done
        }
      }
    }
  end
end
