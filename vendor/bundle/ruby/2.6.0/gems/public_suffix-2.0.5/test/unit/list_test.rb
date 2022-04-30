require "test_helper"

class PublicSuffix::ListTest < Minitest::Test

  def setup
    @list = PublicSuffix::List.new
  end

  def teardown
    PublicSuffix::List.clear
  end


  def test_initialize
    assert_instance_of PublicSuffix::List, @list
    assert_equal 0, @list.size
  end

  def test_initialize_indexes
    assert_equal({}, @list.indexes)
  end


  def test_equality_with_self
    list = PublicSuffix::List.new
    assert_equal list, list
  end

  def test_equality_with_internals
    rule = PublicSuffix::Rule.factory("com")
    assert_equal PublicSuffix::List.new.add(rule), PublicSuffix::List.new.add(rule)
  end

  def test_add
    assert_equal @list, @list.add(PublicSuffix::Rule.factory(""))
    assert_equal @list, @list <<  PublicSuffix::Rule.factory("")
    assert_equal 2, @list.size
  end

  def test_add_should_recreate_index
    @list = PublicSuffix::List.parse("com")
    assert_equal PublicSuffix::Rule.factory("com"), @list.find("google.com")
    assert_equal @list.default_rule, @list.find("google.net")

    @list << PublicSuffix::Rule.factory("net")
    assert_equal PublicSuffix::Rule.factory("com"), @list.find("google.com")
    assert_equal PublicSuffix::Rule.factory("net"), @list.find("google.net")
  end

  def test_add_should_not_duplicate_indices
    @list = PublicSuffix::List.parse("com")
    @list.add(PublicSuffix::Rule.factory("net"))

    assert_equal @list.indexes["com"], [0]
  end

  def test_empty?
    assert @list.empty?
    @list.add(PublicSuffix::Rule.factory(""))
    assert !@list.empty?
  end

  def test_size
    assert_equal 0, @list.size
    assert_equal @list, @list.add(PublicSuffix::Rule.factory(""))
    assert_equal 1, @list.size
  end

  def test_clear
    assert_equal 0, @list.size
    assert_equal @list, @list.add(PublicSuffix::Rule.factory(""))
    assert_equal 1, @list.size
    assert_equal @list, @list.clear
    assert_equal 0, @list.size
  end


  def test_find
    list = PublicSuffix::List.parse(<<EOS)
// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

// ===BEGIN ICANN DOMAINS===

// com
com

// uk
*.uk
*.sch.uk
!bl.uk
!british-library.uk

// io
io

// ===END ICANN DOMAINS===
// ===BEGIN PRIVATE DOMAINS===

// Google, Inc.
blogspot.com

// ===END PRIVATE DOMAINS===
EOS

    # match IANA
    assert_equal PublicSuffix::Rule.factory("com"), list.find("example.com")
    assert_equal PublicSuffix::Rule.factory("com"), list.find("foo.example.com")

    # match wildcard
    assert_equal PublicSuffix::Rule.factory("*.uk"), list.find("example.uk")
    assert_equal PublicSuffix::Rule.factory("*.uk"), list.find("example.co.uk")
    assert_equal PublicSuffix::Rule.factory("*.uk"), list.find("foo.example.co.uk")

    # match exception
    assert_equal PublicSuffix::Rule.factory("!british-library.uk"), list.find("british-library.uk")
    assert_equal PublicSuffix::Rule.factory("!british-library.uk"), list.find("foo.british-library.uk")

    # match default rule
    assert_equal PublicSuffix::Rule.factory("*"), list.find("test")
    assert_equal PublicSuffix::Rule.factory("*"), list.find("example.test")
    assert_equal PublicSuffix::Rule.factory("*"), list.find("foo.example.test")

    # match private
    assert_equal PublicSuffix::Rule.factory("blogspot.com", private: true), list.find("blogspot.com")
    assert_equal PublicSuffix::Rule.factory("blogspot.com", private: true), list.find("foo.blogspot.com")
  end


  def test_select
    assert_equal 2, list.select("british-library.uk").size
  end

  def test_select_name_blank
    assert_equal [], list.select(nil)
    assert_equal [], list.select("")
    assert_equal [], list.select(" ")
  end

  def test_select_ignore_private
    list = PublicSuffix::List.new
    list.add r1 = PublicSuffix::Rule.factory("io")
    list.add r2 = PublicSuffix::Rule.factory("example.io", private: true)

    assert_equal list.select("foo.io"), [r1]
    assert_equal list.select("example.io"), [r1, r2]
    assert_equal list.select("foo.example.io"), [r1, r2]

    assert_equal list.select("foo.io", ignore_private: false), [r1]
    assert_equal list.select("example.io", ignore_private: false), [r1, r2]
    assert_equal list.select("foo.example.io", ignore_private: false), [r1, r2]

    assert_equal list.select("foo.io", ignore_private: true), [r1]
    assert_equal list.select("example.io", ignore_private: true), [r1]
    assert_equal list.select("foo.example.io", ignore_private: true), [r1]
  end


  def test_self_default_getter
    PublicSuffix::List.default = nil
    assert_nil PublicSuffix::List.class_eval { @default }
    PublicSuffix::List.default
    assert_not_equal nil, PublicSuffix::List.class_eval { @default }
  end

  def test_self_default_setter
    PublicSuffix::List.default
    assert_not_equal nil, PublicSuffix::List.class_eval { @default }
    PublicSuffix::List.default = nil
    assert_equal nil, PublicSuffix::List.class_eval { @default }
  end

  def test_self_clear
    PublicSuffix::List.default
    assert_not_equal nil, PublicSuffix::List.class_eval { @default }
    PublicSuffix::List.clear
    assert_equal nil, PublicSuffix::List.class_eval { @default }
  end

  def test_self_parse
    list = PublicSuffix::List.parse(<<EOS)
// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

// ===BEGIN ICANN DOMAINS===

// com
com

// uk
*.uk
!british-library.uk

// ===END ICANN DOMAINS===
// ===BEGIN PRIVATE DOMAINS===

// Google, Inc.
blogspot.com

// ===END PRIVATE DOMAINS===
EOS

    assert_instance_of PublicSuffix::List, list
    assert_equal 4, list.size

    rules = %w( com *.uk !british-library.uk blogspot.com ).map { |name| PublicSuffix::Rule.factory(name) }
    assert_equal rules, list.to_a

    # private domains
    assert_equal false, list.find("com").private
    assert_equal true,  list.find("blogspot.com").private
  end

  def test_self_parse_indexes
    list = PublicSuffix::List.parse(<<EOS)
// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

// ===BEGIN ICANN DOMAINS===

// com
com

// uk
*.uk
!british-library.uk

// ===END ICANN DOMAINS===
// ===BEGIN PRIVATE DOMAINS===

// Google, Inc.
blogspot.com

// ===END PRIVATE DOMAINS===
EOS

    assert_equal({ "com" => [0, 3], "uk" => [1, 2] }, list.indexes)
  end


  private

  def list
    @_list ||= PublicSuffix::List.parse(<<EOS)
// com : http://en.wikipedia.org/wiki/.com
com

// uk : http://en.wikipedia.org/wiki/.uk
*.uk
*.sch.uk
!bl.uk
!british-library.uk
EOS
  end

end
