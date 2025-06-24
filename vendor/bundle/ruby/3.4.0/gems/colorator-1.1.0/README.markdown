# colorator

Colorize your text for the terminal

[![Build Status](https://travis-ci.org/octopress/colorator.png?branch=master)](https://travis-ci.org/octopress/colorator)

## Example

```ruby
"this string".red
# => \e[31mthis string\e[0m
"my string".blue
# => \e[34mmy string\e[0m
# etc...
```

## Supported Colors

- `red`
- `black`
- `green`
- `yellow`
- `magenta`
- `white`
- `blue`
- `cyan`
- `bold`

## Other supported Ansi methods

- `clear_line`
- `has_ansi?`, `has_color?`
- `strip_ansi`, `strip_color`
- `reset_ansi`, `reset_color`
- `clear_screen`
- `ansi_jump`

## Why

There are a bunch of gems that provide functionality like this, but none have
as simple an API as this. Just call `"string".color` and your text will be
colorized.

## License

MIT. Written as a single Ruby file by Brandon Mathis, converted into a gem by
Parker Moore.
