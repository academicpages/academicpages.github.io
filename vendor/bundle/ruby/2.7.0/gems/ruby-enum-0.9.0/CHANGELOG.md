### 0.9.0 (2021/01/21)

* [#34](https://github.com/dblock/ruby-enum/pull/34): Added support for Ruby 3.0 - [@dblock](https://github.com/dblock).
* [#29](https://github.com/dblock/ruby-enum/pull/29): Added superclass values when enumerating with `Ruby::Enum#values` - [@gi](https://github.com/gi).
* [#30](https://github.com/dblock/ruby-enum/pull/30): Default value to key - [@gi](https://github.com/gi).
* [#34](https://github.com/dblock/ruby-enum/pull/34): Replaced Travis-CI with Github Actions, added Danger PR linter - [@dblock](https://github.com/dblock).
* [#37](https://github.com/dblock/ruby-enum/pull/37): Added code coverage - [@dblock](https://github.com/dblock).

### 0.8.0 (2020/03/27)

* [#22](https://github.com/dblock/ruby-enum/pull/22): Added `Ruby::Enum#each_key` and `Ruby::Enum#each_value` - [@dblock](https://github.com/dblock).
* [#22](https://github.com/dblock/ruby-enum/pull/22): Dropped support for Ruby 2.2 - [@dblock](https://github.com/dblock).
* [#22](https://github.com/dblock/ruby-enum/pull/22): Upgraded RuboCop to 0.80.1 - [@dblock](https://github.com/dblock).

### 0.7.2 (2017/03/15)

* [#18](https://github.com/dblock/ruby-enum/pull/18): Added support for non constant definition - [@laertispappas](https://github.com/laertispappas).

### 0.7.1 (2017/02/23)

* [#16](https://github.com/dblock/ruby-enum/pull/16): Replaced `const_missing` with `const_set` - [@laertispappas](https://github.com/laertispappas).

### 0.7.0 (2017/02/21)

* [#3](https://github.com/dblock/ruby-enum/pull/13): Added support for subclassing an Enum - [@laertispappas](https://github.com/laertispappas).

### 0.6.0 (2016/05/12)

* [#12](https://github.com/dblock/ruby-enum/pull/12): A `Ruby::Enum::Errors::DuplicateKeyError` or a `Ruby::Enum::Errors::DuplciateKeyValyeError` will now be raised when duplicate keys / values are defined - [@laertispappas](https://github.com/laertispappas).

### 0.5.0 (2015/11/20)

* [#8](https://github.com/dblock/ruby-enum/pull/8): Added `Ruby::Enum#key`, `Ruby::Enum#value`, `Ruby::Enum#key?`, and `Ruby::Enum#value?` - [@dmolesUC3](https://github.com/dmolesUC3).

### 0.4.0 (2014/06/29)

* [#5](https://github.com/dblock/ruby-enum/pull/5): Mixed in `Enumerable` - [@kgann](https://github.com/kgann).

### 0.3.0 (2014/05/19)

* [#4](https://github.com/dblock/ruby-enum/pull/4): Added `Ruby::Enum#map` - [@ArnaudRinquin](https://github.com/ArnaudRinquin).

### 0.2.1 (2013/05/15)

* Added `Ruby::Enum#values`, `Ruby::Enum#keys` and `Ruby::Enum#to_h` - [@dblock](https://github.com/dblock).
* A `Ruby::Enum::Errors::UninitializedConstantError` will now be raised when referencing an undefined enum - [@dblock](https://github.com/dblock).

### 0.1.0 (2013/05/14)

* Initial public release, live-coded during [May 2013 NYC.rb](http://code.dblock.org/your-first-ruby-gem) - [@dblock](https://github.com/dblock).
