# EM-WebSocket

[![Gem Version](https://badge.fury.io/rb/em-websocket.png)](http://rubygems.org/gems/em-websocket)
[![Analytics](https://ga-beacon.appspot.com/UA-71196-10/em-websocket/readme)](https://github.com/igrigorik/ga-beacon)

EventMachine based, async, Ruby WebSocket server. Take a look at examples directory, or check out the blog post: [Ruby & Websockets: TCP for the Web](http://www.igvita.com/2009/12/22/ruby-websockets-tcp-for-the-browser/).

## Simple server example

```ruby
require 'em-websocket'

EM.run {
  EM::WebSocket.run(:host => "0.0.0.0", :port => 8080) do |ws|
    ws.onopen { |handshake|
      puts "WebSocket connection open"

      # Access properties on the EM::WebSocket::Handshake object, e.g.
      # path, query_string, origin, headers

      # Publish message to the client
      ws.send "Hello Client, you connected to #{handshake.path}"
    }

    ws.onclose { puts "Connection closed" }

    ws.onmessage { |msg|
      puts "Recieved message: #{msg}"
      ws.send "Pong: #{msg}"
    }
  end
}
```

## Protocols supported, and protocol specific functionality

Supports all WebSocket protocols in use in the wild (and a few that are not): drafts 75, 76, 1-17, rfc.

While some of the changes between protocols are unimportant from the point of view of application developers, a few drafts did introduce new functionality. It's possible to easily test for this functionality by using

### Ping & pong supported

Call `ws.pingable?` to check whether ping & pong is supported by the protocol in use.

It's possible to send a ping frame (`ws.ping(body = '')`), which the client must respond to with a pong, or the server can send an unsolicited pong frame (`ws.pong(body = '')`) which the client should not respond to. These methods can be used regardless of protocol version; they return true if the protocol supports ping&pong or false otherwise.

When receiving a ping, the server will automatically respond with a pong as the spec requires (so you should _not_ write an onping handler that replies with a pong), however it is possible to bind to ping & pong events if desired by using the `onping` and `onpong` methods.

### Close codes and reasons

A WebSocket connection can be closed cleanly, regardless of protocol, by calling `ws.close(code = nil, body = nil)`.

Early protocols just close the TCP connection, draft 3 introduced a close handshake, and draft 6 added close codes and reasons to the close handshake. Call `ws.supports_close_codes?` to check whether close codes are supported (i.e. the protocol version is 6 or above).

The `onclose` callback is passed a hash which may contain following keys (depending on the protocol version):

* `was_clean`: boolean indicating whether the connection was closed via the close handshake.
* `code`: the close code. There are two special close codes which the server may set (as defined in the WebSocket spec):
  * 1005: no code was supplied
  * 1006: abnormal closure (the same as `was_clean: false`)
* `reason`: the close reason

Acceptable close codes are defined in the WebSocket rfc (<http://tools.ietf.org/html/rfc6455#section-7.4>). The following codes can be supplies when calling `ws.close(code)`:

* 1000: a generic normal close
* range 3xxx: reserved for libraries, frameworks, and applications (and can be registered with IANA)
* range 4xxx: for private use

If unsure use a code in the 4xxx range. em-websocket may also close a connection with one of the following close codes:

* 1002: WebSocket protocol error.
* 1009: Message too big to process. By default em-websocket will accept frames up to 10MB in size. If a frame is larger than this the connection will be closed without reading the frame data. The limit can be overriden globally (`EM::WebSocket.max_frame_size = bytes`) or on a specific connection (`ws.max_frame_size = bytes`).

## Secure server

It is possible to accept secure `wss://` connections by passing `:secure => true` when opening the connection. Pass a `:tls_options` hash containing keys as described in http://www.rubydoc.info/github/eventmachine/eventmachine/EventMachine/Connection:start_tls

**Warning**: Safari 5 does not currently support prompting on untrusted SSL certificates therefore using a self signed certificate may leave you scratching your head.

```ruby
EM::WebSocket.start({
  :host => "0.0.0.0",
  :port => 443,
  :secure => true,
  :tls_options => {
    :private_key_file => "/private/key",
    :cert_chain_file => "/ssl/certificate"
  }
}) do |ws|
  # ...
end
```

It's possible to check whether an incoming connection is secure by reading `handshake.secure?` in the onopen callback.

## Running behind an SSL Proxy/Terminator, like Stunnel

The `:secure_proxy => true` option makes it possible to use em-websocket behind a secure SSL proxy/terminator like [Stunnel](http://www.stunnel.org/) which does the actual encryption & decryption.

Note that this option is only required to support drafts 75 & 76 correctly (e.g. Safari 5.1.x & earlier, and Safari on iOS 5.x & earlier).

```ruby
EM::WebSocket.start({
  :host => "0.0.0.0",
  :port => 8080,
  :secure_proxy => true
}) do |ws|
  # ...
end
```

## Handling errors

There are two kinds of errors that need to be handled -- WebSocket protocol errors and errors in application code.

WebSocket protocol errors (for example invalid data in the handshake or invalid message frames) raise errors which descend from `EM::WebSocket::WebSocketError`. Such errors are rescued internally and the WebSocket connection will be closed immediately or an error code sent to the browser in accordance to the WebSocket specification. It is possible to be notified in application code of such errors by including an `onerror` callback.

```ruby
ws.onerror { |error|
  if error.kind_of?(EM::WebSocket::WebSocketError)
    # ...
  end
}
```

Application errors are treated differently. If no `onerror` callback has been defined these errors will propagate to the EventMachine reactor, typically causing your program to terminate. If you wish to handle exceptions, simply supply an `onerror callback` and check for exceptions which are not descendant from `EM::WebSocket::WebSocketError`.

It is also possible to log all errors when developing by including the `:debug => true` option when initialising the WebSocket server.

## Emulating WebSockets in older browsers

It is possible to emulate WebSockets in older browsers using flash emulation. For example take a look at the [web-socket-js](https://github.com/gimite/web-socket-js) project.

Using flash emulation does require some minimal support from em-websocket which is enabled by default. If flash connects to the WebSocket port and requests a policy file (which it will do if it fails to receive a policy file on port 843 after a timeout), em-websocket will return one. Also see <https://github.com/igrigorik/em-websocket/issues/61> for an example policy file server which you can run on port 843.

## Examples & Projects using em-websocket

* [Pusher](http://pusher.com) - Realtime Messaging Service
* [Livereload](https://github.com/mockko/livereload) - LiveReload applies CSS/JS changes to Safari or Chrome w/o reloading
* [Twitter AMQP WebSocket Example](http://github.com/rubenfonseca/twitter-amqp-websocket-example)
* examples/multicast.rb - broadcast all ruby tweets to all subscribers
* examples/echo.rb - server <> client exchange via a websocket
