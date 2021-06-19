# Upgrading Ruby::Enum

## Upgrading to >= 0.9.0

### Inheritance & `Ruby::Enum.values`

This only applies to classes that inherit from another which is a `Ruby::Enum`.

Prior to version `0.9.0`, the `values` class method would enumerate only the
values defined in the class.

As of version `0.9.0`, the `values` class method enumerates values defined in
the entire class heirarchy, ancestors first.

``` ruby
class PrimaryColors
  include Ruby::Enum

  define :RED, 'RED'
  define :GREEN, 'GREEN'
  define :BLUE, 'BLUE'
end

class RainbowColors < PrimaryColors
  define :ORANGE, 'ORANGE'
  define :YELLOW, 'YELLOW'
  define :INIDGO, 'INIDGO'
  define :VIOLET, 'VIOLET'
end
```

`gem 'ruby-enum', '< 0.9.0'`

``` ruby
RainbowColors.values # ['ORANGE', 'YELLOW', 'INIDGO', 'VIOLET']
```

`gem 'ruby-enum', '>= 0.9.0'`

``` ruby
RainbowColors.values # ['RED', 'ORANGE', 'YELLOW', 'GREEN', 'BLUE', 'INIDGO', 'VIOLET']
```

See [#29](https://github.com/dblock/ruby-enum/pull/29) for more information.
