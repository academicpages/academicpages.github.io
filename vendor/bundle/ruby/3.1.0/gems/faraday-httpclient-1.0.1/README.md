# Faraday HTTPClient adapter

This gem is a [Faraday][faraday] adapter for the [HTTPClient][httpclient] library.
Faraday is an HTTP client library that provides a common interface over many adapters.
Every adapter is defined into its own gem. This gem defines the adapter for HTTPClient.

## Installation

Add these lines to your application's Gemfile:

```ruby
gem 'httpclient', '>= 2.2'
gem 'faraday'
gem 'faraday-httpclient'
```

And then execute:

    $ bundle install

Or install them yourself as:

    $ gem install httpclient -v '>= 2.2'
    $ gem install faraday faraday-httpclient

## Usage

Configure your Faraday connection to use this adapter like this:

```ruby
connection = Faraday.new(url, conn_options) do |conn|
  conn.adapter(:httpclient)
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

Everyone interacting in the Faraday HTTPClient adapter project's codebase, issue trackers, chat rooms and mailing lists is expected to follow the [code of conduct][code-of-conduct].

[faraday]: https://github.com/lostisland/faraday
[faraday-website]: https://lostisland.github.io/faraday
[httpclient]: https://github.com/nahi/httpclient
[rubygems]: https://rubygems.org
[repo]: https://github.com/lostisland/faraday-httpclient
[license]: https://github.com/lostisland/faraday-httpclient/blob/main/LICENSE.md
[code-of-conduct]: https://github.com/lostisland/faraday-httpclient/blob/main/CODE_OF_CONDUCT.md
