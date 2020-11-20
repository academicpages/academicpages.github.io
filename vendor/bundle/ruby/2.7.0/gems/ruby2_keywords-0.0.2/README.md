# ruby2_keywords

Provides empty `Module#ruby2_keywords` method, for the forward
source-level compatibility against ruby2.7 and ruby3.

## Installation

Add this line to your application's Gemfile:

```ruby
gem 'ruby2_keywords'
```

And then execute:

    $ bundle

Or install it yourself as:

    $ gem install ruby2_keywords

## Usage

For class/module instance methods:

```ruby
require 'ruby2_keywords'

module YourModule
  ruby2_keywords def delegating_method(*args)
    other_method(*args)
  end
end
```

For global methods:

```ruby
require 'ruby2_keywords'

ruby2_keywords def oldstyle_keywords(options = {})
end
```

## Contributing

Bug reports and pull requests are welcome on GitHub at https://bugs.ruby-lang.org.

## License

The gem is available as open source under the terms of the [2-Clause BSD License](https://opensource.org/licenses/BSD-2-Clause).
