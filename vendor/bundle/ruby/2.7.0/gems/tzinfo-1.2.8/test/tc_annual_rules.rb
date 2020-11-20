require File.join(File.expand_path(File.dirname(__FILE__)), 'test_utils')

include TZInfo

class TCAnnualRules < Minitest::Test

  def test_initialize
    std_offset = TimezoneOffset.new(0, 0, 'GMT')
    dst_offset = TimezoneOffset.new(0, 3600, 'BST')
    dst_start_rule = FakeAlwaysDateAdjustmentRule.new(3, 1)
    dst_end_rule = FakeAlwaysDateAdjustmentRule.new(10, 1)

    rules = AnnualRules.new(std_offset, dst_offset, dst_start_rule, dst_end_rule)
    assert_same(std_offset, rules.std_offset)
    assert_same(dst_offset, rules.dst_offset)
    assert_same(dst_start_rule, rules.dst_start_rule)
    assert_same(dst_end_rule, rules.dst_end_rule)
  end

  [2020, 2021].each do |year|
    define_method "test_transitions_for_dst_mid_year_#{year}" do
      std_offset = TimezoneOffset.new(3600, 0, 'TEST')
      dst_offset = TimezoneOffset.new(3600, 3600, 'TESTS')

      rules = AnnualRules.new(
        std_offset,
        dst_offset,
        FakeAlwaysDateAdjustmentRule.new(3, 21),
        FakeAlwaysDateAdjustmentRule.new(10, 22)
      )

      result = rules.transitions(year)

      expected = [
        AnnualRules::Transition.new(dst_offset, std_offset, TimeOrDateTime.wrap(Time.utc(year,  3, 21, 0, 0, 0) - 3600)),
        AnnualRules::Transition.new(std_offset, dst_offset, TimeOrDateTime.wrap(Time.utc(year, 10, 22, 0, 0, 0) - 7200))
      ]

      assert_equal(expected, result)
    end

    define_method "test_transitions_for_dst_start_and_end_of_year_#{year}" do
      std_offset = TimezoneOffset.new(3600, 0, 'TEST')
      dst_offset = TimezoneOffset.new(3600, 3600, 'TESTS')

      rules = AnnualRules.new(
        std_offset,
        dst_offset,
        FakeAlwaysDateAdjustmentRule.new(10, 22),
        FakeAlwaysDateAdjustmentRule.new(3, 21)
      )

      result = rules.transitions(year)

      expected = [
        AnnualRules::Transition.new(std_offset, dst_offset, TimeOrDateTime.wrap(Time.utc(year,  3, 21, 0, 0, 0) - 7200)),
        AnnualRules::Transition.new(dst_offset, std_offset, TimeOrDateTime.wrap(Time.utc(year, 10, 22, 0, 0, 0) - 3600))
      ]

      assert_equal(expected, result)
    end

    define_method "test_transitions_for_negative_dst_start_and_end_of_year_#{year}" do
      std_offset = TimezoneOffset.new(7200, 0, 'TEST')
      dst_offset = TimezoneOffset.new(7200, -3600, 'TESTW')

      rules = AnnualRules.new(
        std_offset,
        dst_offset,
        FakeAlwaysDateAdjustmentRule.new(10, 22),
        FakeAlwaysDateAdjustmentRule.new(3, 21)
      )

      result = rules.transitions(year)

      expected = [
        AnnualRules::Transition.new(std_offset, dst_offset, TimeOrDateTime.wrap(Time.utc(year,  3, 21, 0, 0, 0) - 3600)),
        AnnualRules::Transition.new(dst_offset, std_offset, TimeOrDateTime.wrap(Time.utc(year, 10, 22, 0, 0, 0) - 7200))
      ]

      assert_equal(expected, result)
    end
  end

  class FakeAlwaysDateAdjustmentRule
    def initialize(month, day)
      @month = month
      @day = day
    end

    def at(offset, year)
      TimeOrDateTime.wrap(Time.utc(year, @month, @day, 0, 0, 0) - offset.utc_total_offset)
    end
  end
end
