# Faraday Net::HTTP adapter

This gem is a [Faraday][faraday] adapter for the [Net::HTTP][net-http] library. Faraday is an HTTP client library that provides a common interface over many adapters. Every adapter is defined into it's own gem. This gem defines the adapter for `Net::HTTP` the HTTP library that's included into the standard library of Ruby.

## Installation

Add this line to your application's Gemfile:

```ruby
gem 'faraday-net_http'
```

And then execute:

    $ bundle install

Or install it yourself as:

    $ gem install faraday-net_http

## Usage

Configure your Faraday connection to use this adapter like this:

```ruby
connection = Faraday.new(url, conn_options) do |conn|
  conn.adapter(:net_http)
end
```

For more information on how to setup your Faraday connection and adapters usage, please refer to the [Faraday Website][faraday-website].

## Development

After checking out the repo, run `bin/setup` to install dependencies. Then, run `bin/test` to run the tests. You can also run `bin/console` for an interactive prompt that will allow you to experiment.

To release a new version, update the version number in `version.rb`, and then run `bundle exec rake release`, which will create a git tag for the version, push git commits and tags, and push the `.gem` file to [rubygems.org](rubygems).

## Contributing

Bug reports and pull requests are welcome on [GitHub][repo].

## License

The gem is available as open source under the terms of the [license][license].

## Code of Conduct

Everyone interacting in the Faraday Net::HTTP adapter project's codebases, issue trackers, chat rooms and mailing lists is expected to follow the [code of conduct][code-of-conduct].

[faraday]: https://github.com/lostisland/faraday
[faraday-website]: https://lostisland.github.io/faraday
[net-http]: https://ruby-doc.org/stdlib-2.7.0/libdoc/net/http/rdoc/Net/HTTP.html
[rubygems]: https://rubygems.org
[repo]: https://github.com/lostisland/faraday-net_http
[license]: https://github.com/lostisland/faraday-net_http/blob/main/LICENSE.md
[code-of-conduct]: https://github.com/lostisland/faraday-net_http/blob/main/CODE_OF_CONDUCT.md