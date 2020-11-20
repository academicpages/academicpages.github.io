require 'em-websocket'
# requires the twitter-stream gem
require 'twitter/json_stream'
require 'json'

#
# broadcast all ruby related tweets to all connected users!
#

username = ARGV.shift
password = ARGV.shift
raise "need username and password" if !username or !password

EventMachine.run {
  @channel = EM::Channel.new

  @twitter = Twitter::JSONStream.connect(
    :path => '/1/statuses/filter.json?track=ruby',
    :auth => "#{username}:#{password}",
    :ssl => true
  )

  @twitter.each_item do |status|
    status = JSON.parse(status)
    @channel.push "#{status['user']['screen_name']}: #{status['text']}"
  end


  EventMachine::WebSocket.start(:host => "0.0.0.0", :port => 8080, :debug => true) do |ws|

    ws.onopen {
      sid = @channel.subscribe { |msg| ws.send msg }
      @channel.push "#{sid} connected!"

      ws.onmessage { |msg|
        @channel.push "<#{sid}>: #{msg}"
      }

      ws.onclose {
        @channel.unsubscribe(sid)
      }
    }

  end

  puts "Server started"
}
