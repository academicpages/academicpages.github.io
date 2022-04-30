# Faraday Multipart

[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/lostisland/faraday-multipart/ci)](https://github.com/lostisland/faraday-multipart/actions?query=branch%3Amain)
[![Gem](https://img.shields.io/gem/v/faraday-multipart.svg?style=flat-square)](https://rubygems.org/gems/faraday-multipart)
[![License](https://img.shields.io/github/license/lostisland/faraday-multipart.svg?style=flat-square)](LICENSE.md)

The `Multipart` middleware converts a `Faraday::Request#body` Hash of key/value pairs into a multipart form request, but
only under these conditions:

* The request's Content-Type is "multipart/form-data"
* Content-Type is unspecified, AND one of the values in the Body responds to
  `#content_type`.

Faraday contains a couple helper classes for multipart values:

* `Faraday::Multipart::FilePart` wraps binary file data with a Content-Type. The file data can be specified with a String path to a
  local file, or an IO object.
* `Faraday::Multipart::ParamPart` wraps a String value with a Content-Type, and optionally a Content-ID.

## Installation

Add this line to your application's Gemfile:

```ruby
gem 'faraday-multipart'
```

And then execute:

```shell
bundle install
```

Or install it yourself as:

```shell
gem install faraday-multipart
```

## Usage

First of all, you'll need to add the multipart middleware to your Faraday connection:

```ruby
require 'faraday/multipart'

conn = Faraday.new(...) do |f|
  f.request :multipart
  # ...
end
```

Payload can be a mix of POST data and multipart values.

```ruby
# regular POST form value
payload = { string: 'value' }

# filename for this value is File.basename(__FILE__)
payload[:file] = Faraday::Multipart::FilePart.new(__FILE__, 'text/x-ruby')

# specify filename because IO object doesn't know it
payload[:file_with_name] = Faraday::Multipart::FilePart.new(
  File.open(__FILE__),
  'text/x-ruby',
  File.basename(__FILE__)
)

# Sets a custom Content-Disposition:
# nil filename still defaults to File.basename(__FILE__)
payload[:file_with_header] = Faraday::Multipart::FilePart.new(
  __FILE__,
  'text/x-ruby',
  nil,
  'Content-Disposition' => 'form-data; foo=1'
)

# Upload raw json with content type
payload[:raw_data] = Faraday::Multipart::ParamPart.new(
  { a: 1 }.to_json,
  'application/json'
)

# optionally sets Content-ID too
payload[:raw_with_id] = Faraday::Multipart::ParamPart.new(
  { a: 1 }.to_json,
  'application/json',
  'foo-123'
)

conn.post('/', payload)
```

## Development

After checking out the repo, run `bin/setup` to install dependencies.

Then, run `bin/test` to run the tests.

To install this gem onto your local machine, run `rake build`.

To release a new version, make a commit with a message such as "Bumped to 0.0.2" and then run `rake release`. See how it
works [here](https://bundler.io/guides/creating_gem.html#releasing-the-gem).

## Contributing

Bug reports and pull requests are welcome on [GitHub](https://github.com/lostisland/faraday-multipart).

## License

The gem is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).
