### 0.8.0 (2020/3/27)

* [#22](https://github.com/dblock/ruby-enum/pull/22): Added `Ruby::Enum#each_key` and `Ruby::Enum#each_value` - [@dblock](https://github.com/dblock).
* [#22](https://github.com/dblock/ruby-enum/pull/22): Dropped support for Ruby 2.2 - [@dblock](https://github.com/dblock).
* [#22](https://github.com/dblock/ruby-enum/pull/22): Upgraded RuboCop to 0.80.1 - [@dblock](https://github.com/dblock).

### 0.7.2 (2017/3/15)

* [#18](https://github.com/dblock/ruby-enum/pull/18): Added support for non constant definition - [@laertispappas](https://github.com/laertispappas).

### 0.7.1 (2017/2/23)

* [#16](https://github.com/dblock/ruby-enum/pull/16): Replaced `const_missing` with `const_set` - [@laertispappas](https://github.com/laertispappas).

### 0.7.0 (2017/2/21)

* [#3](https://github.com/dblock/ruby-enum/pull/13): Added support for subclassing an Enum - [@laertispappas](https://github.com/laertispappas).

### 0.6.0 (2016/5/12)

* [#12](https://github.com/dblock/ruby-enum/pull/12): A `Ruby::Enum::Errors::DuplicateKeyError` or a `Ruby::Enum::Errors::DuplciateKeyValyeError` will now be raised when duplicate keys / values are defined - [@laertispappas](https://github.com/laertispappas).

### 0.5.0 (2015/20/11)

* [#8](https://github.com/dblock/ruby-enum/pull/8): Added `Ruby::Enum#key`, `Ruby::Enum#value`, `Ruby::Enum#key?`, and `Ruby::Enum#value?` - [@dmolesUC3](https://github.com/dmolesUC3).

### 0.4.0 (2014/29/6)

* [#5](https://github.com/dblock/ruby-enum/pull/5): Mixed in `Enumerable` - [@kgann](https://github.com/kgann).

### 0.3.0 (2014/19/5)

* [#4](https://github.com/dblock/ruby-enum/pull/4): Added `Ruby::Enum#map` - [@ArnaudRinquin](https://github.com/ArnaudRinquin).

### 0.2.1 (2013/15/5)

* Added `Ruby::Enum#values`, `Ruby::Enum#keys` and `Ruby::Enum#to_h` - [@dblock](https://github.com/dblock).
* A `Ruby::Enum::Errors::UninitializedConstantError` will now be raised when referencing an undefined enum - [@dblock](https://github.com/dblock).

### 0.1.0 (2013/14/5)

* Initial public release, live-coded during [May 2013 NYC.rb](http://code.dblock.org/your-first-ruby-gem) - [@dblock](https://github.com/dblock).
