require 'test_helper'

class StrainerUnitTest < Minitest::Test
  include Liquid

  module AccessScopeFilters
    def public_filter
      "public"
    end

    def private_filter
      "private"
    end
    private :private_filter
  end

  Strainer.global_filter(AccessScopeFilters)

  def test_strainer
    strainer = Strainer.create(nil)
    assert_equal 5, strainer.invoke('size', 'input')
    assert_equal "public", strainer.invoke("public_filter")
  end

  def test_stainer_raises_argument_error
    strainer = Strainer.create(nil)
    assert_raises(Liquid::ArgumentError) do
      strainer.invoke("public_filter", 1)
    end
  end

  def test_stainer_argument_error_contains_backtrace
    strainer = Strainer.create(nil)
    begin
      strainer.invoke("public_filter", 1)
    rescue Liquid::ArgumentError => e
      assert_match(
        /\ALiquid error: wrong number of arguments \((1 for 0|given 1, expected 0)\)\z/,
        e.message)
      assert_equal e.backtrace[0].split(':')[0], __FILE__
    end
  end

  def test_strainer_only_invokes_public_filter_methods
    strainer = Strainer.create(nil)
    assert_equal false, strainer.class.invokable?('__test__')
    assert_equal false, strainer.class.invokable?('test')
    assert_equal false, strainer.class.invokable?('instance_eval')
    assert_equal false, strainer.class.invokable?('__send__')
    assert_equal true, strainer.class.invokable?('size') # from the standard lib
  end

  def test_strainer_returns_nil_if_no_filter_method_found
    strainer = Strainer.create(nil)
    assert_nil strainer.invoke("private_filter")
    assert_nil strainer.invoke("undef_the_filter")
  end

  def test_strainer_returns_first_argument_if_no_method_and_arguments_given
    strainer = Strainer.create(nil)
    assert_equal "password", strainer.invoke("undef_the_method", "password")
  end

  def test_strainer_only_allows_methods_defined_in_filters
    strainer = Strainer.create(nil)
    assert_equal "1 + 1", strainer.invoke("instance_eval", "1 + 1")
    assert_equal "puts",  strainer.invoke("__send__", "puts", "Hi Mom")
    assert_equal "has_method?", strainer.invoke("invoke", "has_method?", "invoke")
  end

  def test_strainer_uses_a_class_cache_to_avoid_method_cache_invalidation
    a = Module.new
    b = Module.new
    strainer = Strainer.create(nil, [a, b])
    assert_kind_of Strainer, strainer
    assert_kind_of a, strainer
    assert_kind_of b, strainer
    assert_kind_of Liquid::StandardFilters, strainer
  end

  def test_add_filter_when_wrong_filter_class
    c = Context.new
    s = c.strainer
    wrong_filter = ->(v) { v.reverse }

    assert_raises ArgumentError do
      s.class.add_filter(wrong_filter)
    end
  end

  module PrivateMethodOverrideFilter
    private

    def public_filter
      "overriden as private"
    end
  end

  def test_add_filter_raises_when_module_privately_overrides_registered_public_methods
    strainer = Context.new.strainer

    error = assert_raises(Liquid::MethodOverrideError) do
      strainer.class.add_filter(PrivateMethodOverrideFilter)
    end
    assert_equal 'Liquid error: Filter overrides registered public methods as non public: public_filter', error.message
  end

  module ProtectedMethodOverrideFilter
    protected

    def public_filter
      "overriden as protected"
    end
  end

  def test_add_filter_raises_when_module_overrides_registered_public_method_as_protected
    strainer = Context.new.strainer

    error = assert_raises(Liquid::MethodOverrideError) do
      strainer.class.add_filter(ProtectedMethodOverrideFilter)
    end
    assert_equal 'Liquid error: Filter overrides registered public methods as non public: public_filter', error.message
  end

  module PublicMethodOverrideFilter
    def public_filter
      "public"
    end
  end

  def test_add_filter_does_not_raise_when_module_overrides_previously_registered_method
    strainer = Context.new.strainer
    strainer.class.add_filter(PublicMethodOverrideFilter)
    assert strainer.class.filter_methods.include?('public_filter')
  end

  module LateAddedFilter
    def late_added_filter(input)
      "filtered"
    end
  end

  def test_global_filter_clears_cache
    assert_equal 'input', Strainer.create(nil).invoke('late_added_filter', 'input')
    Strainer.global_filter(LateAddedFilter)
    assert_equal 'filtered', Strainer.create(nil).invoke('late_added_filter', 'input')
  end

  def test_add_filter_does_not_include_already_included_module
    mod = Module.new do
      class << self
        attr_accessor :include_count
        def included(mod)
          self.include_count += 1
        end
      end
      self.include_count = 0
    end
    strainer = Context.new.strainer
    strainer.class.add_filter(mod)
    strainer.class.add_filter(mod)
    assert_equal 1, mod.include_count
  end
end # StrainerTest
