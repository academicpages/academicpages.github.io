Ruby::Enum
==========

[![Gem Version](http://img.shields.io/gem/v/ruby-enum.svg)](http://badge.fury.io/rb/ruby-enum)
[![Build Status](https://github.com/dblock/ruby-enum/workflows/test/badge.svg?branch=master)](https://github.com/dblock/ruby-enum/actions)
[![Code Climate](https://codeclimate.com/github/dblock/ruby-enum.svg)](https://codeclimate.com/github/dblock/ruby-enum)

Enum-like behavior for Ruby, heavily inspired by [this](http://www.rubyfleebie.com/enumerations-and-ruby), and improved upon [another blog post](http://code.dblock.org/how-to-define-enums-in-ruby).

## Table of Contents

- [Usage](#usage)
  - [Constants](#constants)
  - [Class Methods](#class-methods)
  - [Default Value](#default-value)
  - [Enumerating](#enumerating)
    - [Iterating](#iterating)
    - [Mapping](#mapping)
    - [Reducing](#reducing)
    - [Sorting](#sorting)
  - [Hashing](#hashing)
    - [Retrieving keys and values](#retrieving-keys-and-values)
    - [Mapping keys to values](#mapping-keys-to-values)
    - [Mapping values to keys](#mapping-values-to-keys)
  - [Duplicate enumerator keys or duplicate values](#duplicate-enumerator-keys-or-duplicate-values)
  - [Inheritance](#inheritance)
- [Contributing](#contributing)
- [Copyright and License](#copyright-and-license)
- [Related Projects](#related-projects)

## Usage

Enums can be defined and accessed either as constants, or class methods, which is a matter of preference.

### Constants

Define enums, and reference them as constants.

``` ruby
class OrderState
  include Ruby::Enum

  define :CREATED, 'created'
  define :PAID, 'paid'
end
```

``` ruby
OrderState::CREATED # 'created'
OrderState::PAID # 'paid'
OrderState::UNKNOWN # raises Ruby::Enum::Errors::UninitializedConstantError
OrderState.keys # [ :CREATED, :PAID ]
OrderState.values # [ 'created', 'paid' ]
OrderState.to_h # { :CREATED => 'created', :PAID => 'paid' }
```

### Class Methods

Define enums, and reference them as class methods.

``` ruby
class OrderState
  include Ruby::Enum

  define :created, 'created'
  define :paid, 'paid'
end
```

```ruby
OrderState.created # 'created'
OrderState.paid # 'paid'
OrderState.undefined # NoMethodError is raised
OrderState.keys # [ :created, :paid ]
OrderState.values # ['created', 'paid']
OrderState.to_h # { :created => 'created', :paid => 'paid' }
```

### Default Value

The value is optional. If unspecified, the value will default to the key.

``` ruby
class OrderState
  include Ruby::Enum

  define :UNSPECIFIED
  define :unspecified
end
```

``` ruby
OrderState::UNSPECIFIED # :UNSPECIFIED
OrderState.unspecified # :unspecified
```

### Enumerating

Enums support all `Enumerable` methods.

#### Iterating

``` ruby
OrderState.each do |key, enum|
  # key and enum.key are :CREATED, :PAID
  # enum.value is 'created', 'paid'
end
```

``` ruby
OrderState.each_key do |key|
  # :CREATED, :PAID
end
```

``` ruby
OrderState.each_value do |value|
  # 'created', 'paid'
end
```

#### Mapping

``` ruby
OrderState.map do |key, enum|
  # key and enum.key are :CREATED, :PAID
  # enum.value is 'created', 'paid'
  [enum.value, key]
end

# => [ ['created', :CREATED], ['paid', :PAID] ]
```

#### Reducing

``` ruby
OrderState.reduce([]) do |arr, (key, enum)|
  # key and enum.key are :CREATED, :PAID
  # enum.value is 'created', 'paid'
  arr << [enum.value, key]
end

# => [ ['created', :CREATED], ['paid', :PAID] ]
```

#### Sorting

``` ruby
OrderState.sort_by do |key, enum|
  # key and enum.key are :CREATED, :PAID
  # enum.value is 'created', 'paid'
  enum.value.length
end

# => [[:PAID, #<OrderState:0x0 @key=:PAID, @value="paid">], [:CREATED, #<OrderState:0x1 @key=:CREATED, @value="created">]]
```

### Hashing

Several hash-like methods are supported.

#### Retrieving keys and values

``` ruby
OrderState.keys
# => [:CREATED, :PAID]

OrderState.values
# => ['created', 'paid']
```

#### Mapping keys to values

``` ruby
OrderState.key?(:CREATED)
# => true

OrderState.value(:CREATED)
# => 'created'

OrderState.key?(:FAILED)
# => false

OrderState.value(:FAILED)
# => nil
```

#### Mapping values to keys

``` ruby
OrderState.value?('paid')
# => true

OrderState.key('paid')
# => :PAID

OrderState.value?('failed')
# => false

OrderState.key('failed')
# => nil
```

### Duplicate enumerator keys or duplicate values

Defining duplicate enums raises `Ruby::Enum::Errors::DuplicateKeyError`.

```ruby
class OrderState
  include Ruby::Enum

  define :CREATED, 'created'
  define :CREATED, 'recreated' # raises DuplicateKeyError
end
```

Defining a duplicate value raises `Ruby::Enum::Errors::DuplicateValueError`.

```ruby
class OrderState
  include Ruby::Enum

  define :CREATED, 'created'
  define :RECREATED, 'created' # raises DuplicateValueError
end
```

The `DuplicateValueError` exception is raised to be consistent with the unique key constraint. Since keys are unique, there needs to be a way to map values to keys using `OrderState.value('created')`.

### Inheritance

When inheriting from a `Ruby::Enum` class, all defined enums in the parent class will be accessible in sub classes as well. Sub classes can also provide extra enums, as usual.

``` ruby
class OrderState
  include Ruby::Enum

  define :CREATED, 'CREATED'
  define :PAID, 'PAID'
end

class ShippedOrderState < OrderState
  define :PREPARED, 'PREPARED'
  define :SHIPPED, 'SHIPPED'
end
```

``` ruby
ShippedOrderState::CREATED # 'CREATED'
ShippedOrderState::PAID # 'PAID'
ShippedOrderState::PREPARED # 'PREPARED'
ShippedOrderState::SHIPPED # 'SHIPPED'
```

The `values` class method will enumerate the values from all base classes.

``` ruby
OrderState.values # ['CREATED', 'PAID']
ShippedOrderState.values # ['CREATED', 'PAID', 'PREPARED', SHIPPED']
```

## Contributing

You're encouraged to contribute to ruby-enum. See [CONTRIBUTING](CONTRIBUTING.md) for details.

## Copyright and License

Copyright (c) 2013-2021, Daniel Doubrovkine and [Contributors](CHANGELOG.md).

This project is licensed under the [MIT License](LICENSE.md).

## Related Projects

* [typesafe_enum](https://github.com/dmolesUC3/typesafe_enum): Typesafe enums, inspired by Java.
* [renum](https://github.com/duelinmarkers/renum): A readable, but terse enum.
