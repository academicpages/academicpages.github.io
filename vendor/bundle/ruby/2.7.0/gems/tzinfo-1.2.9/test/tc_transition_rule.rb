require File.join(File.expand_path(File.dirname(__FILE__)), 'test_utils')

include TZInfo

class TCTransitionRule < Minitest::Test
  [-1, 0, 1].each do |transition_at|
    define_method "test_transition_at_#{transition_at}" do
      rule = TestTransitionRule.new(transition_at)
      assert_equal(transition_at, rule.transition_at)
    end
  end

  [
    [-1, 19, 23, 59, 59],
    [0, 20, 0, 0, 0],
    [1, 20, 0, 0, 1],
    [60, 20, 0, 1, 0],
    [86399, 20, 23, 59, 59],
    [86400, 21, 0, 0, 0]
  ].each do |(transition_at, expected_day, expected_hour, expected_minute, expected_second)|
    define_method "test_at_with_transition_at_#{transition_at}" do
      offset = TimezoneOffset.new(0, 0, 'TEST')
      rule = TestTransitionRule.new(transition_at) do |y|
        assert_equal(2020, y)
        TimeOrDateTime.wrap(Time.utc(2020, 3, 20))
      end

      result = rule.at(offset, 2020)

      assert_kind_of(TimeOrDateTime, result)
      assert_equal(Time.utc(2020, 3, expected_day, expected_hour, expected_minute, expected_second), result.to_time)
    end
  end

  [-7200, 0, 7200].each do |offset_seconds|
    define_method "test_at_with_offset_#{offset_seconds}" do
      offset = TimezoneOffset.new(offset_seconds, 0, 'TEST')
      rule = TestTransitionRule.new(3600) do |y|
        assert_equal(2020, y)
        TimeOrDateTime.wrap(Time.utc(2020, 3, 20))
      end

      result = rule.at(offset, 2020)

      assert_kind_of(TimeOrDateTime, result)
      assert_equal(Time.utc(2020, 3, 20, 1, 0, 0) - offset_seconds, result.to_time)
    end
  end

  [2020, 2021].each do |year|
    define_method "test_at_with_year_#{year}" do
      offset = TimezoneOffset.new(0, 0, 'TEST')
      rule = TestTransitionRule.new(3600) do |y|
        assert_equal(year, y)
        TimeOrDateTime.wrap(Time.utc(year, 3, 20))
      end

      result = rule.at(offset, year)

      assert_kind_of(TimeOrDateTime, result)
      assert_equal(Time.utc(year, 3, 20, 1, 0, 0), result.to_time)
    end
  end

  def test_at_crosses_64_bit_boundary
    offset = TimezoneOffset.new(0, 0, 'TEST')
    rule = TestTransitionRule.new(11648) do |y|
      assert_equal(2038, y)
      TimeOrDateTime.wrap(Time.utc(2038, 1, 19))
    end

    result = rule.at(offset, 2038)

    assert_kind_of(TimeOrDateTime, result)
    if RubyCoreSupport.time_supports_64bit
      assert_kind_of(Time, result.to_orig)
    else
      assert_kind_of(DateTime, result.to_orig)
    end
    assert_equal(DateTime.new(2038, 1, 19, 3, 14, 8), result.to_datetime)
  end

  def test_at_crosses_negative_boundary
    offset = TimezoneOffset.new(0, 0, 'TEST')
    rule = TestTransitionRule.new(-1) do |y|
      assert_equal(1970, y)
      TimeOrDateTime.wrap(Time.utc(1970, 1, 1))
    end

    result = rule.at(offset, 1970)

    assert_kind_of(TimeOrDateTime, result)
    if RubyCoreSupport.time_supports_negative
      assert_kind_of(Time, result.to_orig)
    else
      assert_kind_of(DateTime, result.to_orig)
    end
    assert_equal(DateTime.new(1969, 12, 31, 23, 59, 59), result.to_datetime)
  end

  NEGATIVE_DATES = [[1969, 12, 31]]
  B32_DATES = [[1970, 1, 1], [2038, 1, 19]]
  B64_DATES = [[2038, 1, 20], [2038, 2, 1], [2039, 1, 1]]

  B32_DATES.concat(RubyCoreSupport.time_supports_negative ? NEGATIVE_DATES : []).concat(RubyCoreSupport.time_supports_64bit ? B64_DATES : []).each do |(year, month, day)|
    define_method "test_new_time_or_datetime_returns_time_based_instance_for_#{year}_#{month}_#{day}" do
      result = TestTransitionRule.new(0).new_time_or_datetime!(year, month, day)
      assert_kind_of(TimeOrDateTime, result)
      assert_kind_of(Time, result.to_orig)
      assert_equal(Time.utc(year, month, day), result.to_orig)
    end
  end

  (RubyCoreSupport.time_supports_negative ? [] : NEGATIVE_DATES).concat(RubyCoreSupport.time_supports_64bit ? [] : B64_DATES).each do |(year, month, day)|
    define_method "test_new_time_or_datetime_returns_datetime_based_instance_for_#{year}_#{month}_#{day}" do
      result = TestTransitionRule.new(0).new_time_or_datetime!(year, month, day)
      assert_kind_of(TimeOrDateTime, result)
      assert_kind_of(DateTime, result.to_orig)
      assert_equal(DateTime.new(year, month, day), result.to_orig)
    end
  end

  [1900, 2021, 2039].each do |year|
    define_method "test_new_time_or_datetime_returns_march_1_for_feb_29_on_non_leap_year_#{year}" do
      result = TestTransitionRule.new(0).new_time_or_datetime!(year, 2, 29)
      assert_kind_of(TimeOrDateTime, result)
      assert_equal(DateTime.new(year, 3, 1), result.to_datetime)
    end
  end

  [1968, 2000, 2040].each do |year|
    define_method "test_new_time_or_datetime_returns_feb_29_on_leap_year_#{year}" do
      result = TestTransitionRule.new(0).new_time_or_datetime!(year, 2, 29)
      assert_kind_of(TimeOrDateTime, result)
      assert_equal(DateTime.new(year, 2, 29), result.to_datetime)
    end
  end

  class TestTransitionRule < TransitionRule
    def initialize(transition_at, &block)
      super(transition_at)
      @get_day = block
    end

    alias new_time_or_datetime! new_time_or_datetime
    public :new_time_or_datetime!

    protected

    def get_day(year)
      @get_day.call(year)
    end
  end
end

module BaseTransitionRuleTestHelper
  def test_invalid_transition_at
    error = assert_raises(ArgumentError) { create_with_transition_at('0') }
    assert_match(/\btransition_at(\b.*)?/, error.message)
  end

  [:==, :eql?].each do |method|
    define_method "test_not_equal_by_transition_at_with_#{method}" do
      rule1 = create_with_transition_at(0)
      rule2 = create_with_transition_at(1)
      assert_equal(false, rule1.send(method, rule2))
      assert_equal(false, rule2.send(method, rule1))
    end

    define_method "test_not_equal_to_other_with_#{method}" do
      rule = create_with_transition_at(0)
      assert_equal(false, rule.send(method, Object.new))
    end
  end
end

class TCAbsoluteDayOfYearTransitionRule < Minitest::Test
  include BaseTransitionRuleTestHelper

  [-1, 366, '0'].each do |value|
    define_method "test_invalid_day_#{value}" do
      error = assert_raises(ArgumentError) { AbsoluteDayOfYearTransitionRule.new(value) }
      assert_match(/\bday\b/, error.message)
    end
  end

  [
    [2020, 0, 1, 1],
    [2020, 58, 2, 28],
    [2020, 59, 2, 29],
    [2020, 365, 12, 31],
    [2021, 59, 3, 1],
    [2021, 365, 13, 1],
    [2100, 59, 3, 1],
    [2100, 365, 13, 1],
    [2000, 59, 2, 29],
    [2000, 365, 12, 31]
  ].each do |(year, day, expected_month, expected_day)|
    define_method "test_day_#{day}_of_year_#{year}" do
      rule = AbsoluteDayOfYearTransitionRule.new(day, 3600)
      offset = TimezoneOffset.new(0, 0, 'TEST')

      result = rule.at(offset, year)

      expected_year = year
      if expected_month == 13
        expected_year += 1
        expected_month = 1
      end

      assert_kind_of(TimeOrDateTime, result)
      assert_equal(DateTime.new(expected_year, expected_month, expected_day, 1, 0, 0), result.to_datetime)
    end
  end

  def test_crosses_64_bit_boundary
    # Internally the calculation starts with Jan 1 and adds days. Jan 20 2038
    # will require a DateTime on 32-bit only systems.

    rule = AbsoluteDayOfYearTransitionRule.new(19, 3600)
    offset = TimezoneOffset.new(0, 0, 'TEST')

    result = rule.at(offset, 2038)

    assert_kind_of(TimeOrDateTime, result)
    if RubyCoreSupport.time_supports_64bit
      assert_kind_of(Time, result.to_orig)
    else
      assert_kind_of(DateTime, result.to_orig)
    end
    assert_equal(DateTime.new(2038, 1, 20, 1, 0, 0), result.to_datetime)
  end

  def test_day_0_is_always_first_day_of_year
    rule = AbsoluteDayOfYearTransitionRule.new(0)
    assert_equal(true, rule.is_always_first_day_of_year?)
  end

  [1, 365].each do |day|
    define_method "test_day_#{day}_is_not_always_first_day_of_year" do
      rule = AbsoluteDayOfYearTransitionRule.new(day)
      assert_equal(false, rule.is_always_first_day_of_year?)
    end

    define_method "test_day_#{day}_is_not_always_last_day_of_year" do
      rule = AbsoluteDayOfYearTransitionRule.new(day)
      assert_equal(false, rule.is_always_last_day_of_year?)
    end
  end

  [:==, :eql?].each do |method|
    [
      [0, 0],
      [0, 3600],
      [365, 0]
    ].each do |(day, transition_at)|
      define_method "test_equal_for_day_#{day}_and_transition_at_#{transition_at}_with_#{method}" do
        rule1 = AbsoluteDayOfYearTransitionRule.new(day, transition_at)
        rule2 = AbsoluteDayOfYearTransitionRule.new(day, transition_at)
        assert_equal(true, rule1.send(method, rule2))
        assert_equal(true, rule2.send(method, rule1))
      end
    end

    define_method "test_not_equal_by_day_with_#{method}" do
      rule1 = AbsoluteDayOfYearTransitionRule.new(0, 3600)
      rule2 = AbsoluteDayOfYearTransitionRule.new(1, 3600)
      assert_equal(false, rule1.send(method, rule2))
      assert_equal(false, rule2.send(method, rule1))
    end

    define_method "test_not_equal_to_julian_with_#{method}" do
      rule1 = AbsoluteDayOfYearTransitionRule.new(1, 0)
      rule2 = JulianDayOfYearTransitionRule.new(1, 0)
      assert_equal(false, rule1.send(method, rule2))
      assert_equal(false, rule2.send(method, rule1))
    end
  end

  [
    [0, 0],
    [0, 3600],
    [365, 0]
  ].each do |(day, transition_at)|
    define_method "test_hash_for_day_#{day}_and_transition_at_#{transition_at}" do
      rule = AbsoluteDayOfYearTransitionRule.new(day, transition_at)
      expected = [AbsoluteDayOfYearTransitionRule, day * 86400, transition_at].hash
      assert_equal(expected, rule.hash)
    end
  end

  protected

  def create_with_transition_at(transition_at)
    AbsoluteDayOfYearTransitionRule.new(1, transition_at)
  end
end

class TCJulianDayOfYearTransitionRule < Minitest::Test
  include BaseTransitionRuleTestHelper

  [0, 366, '1'].each do |value|
    define_method "test_invalid_day_#{value}" do
      error = assert_raises(ArgumentError) { JulianDayOfYearTransitionRule.new(value) }
      assert_match(/\bday\b/, error.message)
    end
  end

  [2020, 2021, 2100, 2000].each do |year|
    [
      [1, 1, 1],
      [59, 2, 28],
      [60, 3, 1],
      [365, 12, 31]
    ].each do |(day, expected_month, expected_day)|
      define_method "test_day_#{day}_of_year_#{year}" do
        rule = JulianDayOfYearTransitionRule.new(day, 3600)
        offset = TimezoneOffset.new(0, 0, 'TEST')

        result = rule.at(offset, year)

        assert_kind_of(TimeOrDateTime, result)
        assert_equal(DateTime.new(year, expected_month, expected_day, 1, 0, 0), result.to_datetime)
      end
    end
  end

  def test_day_1_is_always_first_day_of_year
    rule = JulianDayOfYearTransitionRule.new(1)
    assert_equal(true, rule.is_always_first_day_of_year?)
  end

  [2, 365].each do |day|
    define_method "test_day_#{day}_is_not_always_first_day_of_year" do
      rule = JulianDayOfYearTransitionRule.new(day)
      assert_equal(false, rule.is_always_first_day_of_year?)
    end
  end

  def test_day_365_is_always_last_day_of_year
    rule = JulianDayOfYearTransitionRule.new(365)
    assert_equal(true, rule.is_always_last_day_of_year?)
  end

  [1, 364].each do |day|
    define_method "test_day_#{day}_is_not_always_last_day_of_year" do
      rule = JulianDayOfYearTransitionRule.new(day)
      assert_equal(false, rule.is_always_last_day_of_year?)
    end
  end

  [:==, :eql?].each do |method|
    [
      [1, 0],
      [1, 3600],
      [365, 0]
    ].each do |(day, transition_at)|
      define_method "test_equal_for_day_#{day}_and_transition_at_#{transition_at}_with_#{method}" do
        rule1 = JulianDayOfYearTransitionRule.new(day, transition_at)
        rule2 = JulianDayOfYearTransitionRule.new(day, transition_at)
        assert_equal(true, rule1.send(method, rule2))
        assert_equal(true, rule2.send(method, rule1))
      end
    end

    define_method "test_not_equal_by_day_with_#{method}" do
      rule1 = JulianDayOfYearTransitionRule.new(1, 0)
      rule2 = JulianDayOfYearTransitionRule.new(2, 0)
      assert_equal(false, rule1.send(method, rule2))
      assert_equal(false, rule2.send(method, rule1))
    end

    define_method "test_not_equal_to_absolute_with_#{method}" do
      rule1 = JulianDayOfYearTransitionRule.new(1, 0)
      rule2 = AbsoluteDayOfYearTransitionRule.new(1, 0)
      assert_equal(false, rule1.send(method, rule2))
      assert_equal(false, rule2.send(method, rule1))
    end
  end

  [
    [1, 0],
    [1, 3600],
    [365, 0]
  ].each do |(day, transition_at)|
    define_method "test_hash_for_day_#{day}_and_transition_at_#{transition_at}" do
      rule = JulianDayOfYearTransitionRule.new(day, transition_at)
      expected = [JulianDayOfYearTransitionRule, day * 86400, transition_at].hash
      assert_equal(expected, rule.hash)
    end
  end

  protected

  def create_with_transition_at(transition_at)
    JulianDayOfYearTransitionRule.new(1, transition_at)
  end
end

module DayOfWeekTransitionRuleTestHelper
  [-1, 0, 13, '1'].each do |month|
    define_method "test_invalid_month_#{month}" do
      error = assert_raises(ArgumentError) { create_with_month_and_day_of_week(month, 0) }
      assert_match(/\bmonth\b/, error.message)
    end
  end

  [-1, 7, '0'].each do |day_of_week|
    define_method "test_invalid_day_of_week_#{day_of_week}" do
      error = assert_raises(ArgumentError) { create_with_month_and_day_of_week(1, day_of_week) }
      assert_match(/\bday_of_week\b/, error.message)
    end
  end

  def test_is_not_always_first_day_of_year
    rule = create_with_month_and_day_of_week(1, 0)
    assert_equal(false, rule.is_always_first_day_of_year?)
  end

  def test_is_not_always_last_day_of_year
    rule = create_with_month_and_day_of_week(12, 6)
    assert_equal(false, rule.is_always_last_day_of_year?)
  end

  [:==, :eql?].each do |method|
    define_method "test_not_equal_by_month_with_#{method}" do
      rule1 = create_with_month_and_day_of_week(1, 0)
      rule2 = create_with_month_and_day_of_week(2, 0)
      assert_equal(false, rule1.send(method, rule2))
      assert_equal(false, rule2.send(method, rule1))
    end

    define_method "test_not_equal_by_day_of_week_with_#{method}" do
      rule1 = create_with_month_and_day_of_week(1, 0)
      rule2 = create_with_month_and_day_of_week(1, 1)
      assert_equal(false, rule1.send(method, rule2))
      assert_equal(false, rule2.send(method, rule1))
    end
  end
end

class TCDayOfMonthTransitionRule < Minitest::Test
  include BaseTransitionRuleTestHelper
  include DayOfWeekTransitionRuleTestHelper

  [-1, 0, 5, '1'].each do |week|
    define_method "test_invalid_week_#{week}" do
      error = assert_raises(ArgumentError) { DayOfMonthTransitionRule.new(1, week, 0) }
      assert_match(/\bweek\b/, error.message)
    end
  end

  [
    # All possible first week start days.
    [2020, 3, [1, 2, 3, 4, 5, 6, 7]],
    [2021, 3, [7, 1, 2, 3, 4, 5, 6]],
    [2022, 3, [6, 7, 1, 2, 3, 4, 5]],
    [2023, 3, [5, 6, 7, 1, 2, 3, 4]],
    [2018, 3, [4, 5, 6, 7, 1, 2, 3]],
    [2024, 3, [3, 4, 5, 6, 7, 1, 2]],
    [2025, 3, [2, 3, 4, 5, 6, 7, 1]],

    # All possible months.
    [2019, 1, [6]],
    [2019, 2, [3]],
    [2019, 3, [3]],
    [2019, 4, [7]],
    [2019, 5, [5]],
    [2019, 6, [2]],
    [2019, 7, [7]],
    [2019, 8, [4]],
    [2019, 9, [1]],
    [2019, 10, [6]],
    [2019, 11, [3]],
    [2019, 12, [1]]
  ].each do |(year, month, days)|
    days.each_with_index do |expected_day, day_of_week|
      (1..4).each do |week|
        define_method "test_month_#{month}_week_#{week}_and_day_of_week_#{day_of_week}_year_#{year}" do
          rule = DayOfMonthTransitionRule.new(month, week, day_of_week, 3600)
          offset = TimezoneOffset.new(0, 0, 'TEST')

          result = rule.at(offset, year)

          assert_kind_of(TimeOrDateTime, result)
          assert_equal(Time.utc(year, month, expected_day + (week - 1) * 7, 1, 0, 0), result.to_time)
        end
      end
    end
  end

  [[3, 3, 20], [4, 6, 23]].each do |(week, day_of_week, expected_day)|
    define_method "test_crosses_64_bit_boundary_for_day_of_week_#{day_of_week}" do
      rule = DayOfMonthTransitionRule.new(1, week, day_of_week, 3600)
      offset = TimezoneOffset.new(0, 0, 'TEST')

      result = rule.at(offset, 2038)

      assert_kind_of(TimeOrDateTime, result)
      if RubyCoreSupport.time_supports_64bit
        assert_kind_of(Time, result.to_orig)
      else
        assert_kind_of(DateTime, result.to_orig)
      end
      assert_equal(DateTime.new(2038, 1, expected_day, 1, 0, 0), result.to_datetime)
    end
  end

  [:==, :eql?].each do |method|
    [
      [1, 1, 0, 0],
      [1, 1, 0, 1],
      [1, 1, 1, 0],
      [1, 2, 0, 0],
      [2, 1, 0, 0]
    ].each do |(month, week, day_of_week, transition_at)|
      define_method "test_equal_for_month_#{month}_week_#{week}_day_of_week_#{day_of_week}_and_transition_at_#{transition_at}_with_#{method}" do
        rule1 = DayOfMonthTransitionRule.new(month, week, day_of_week, transition_at)
        rule2 = DayOfMonthTransitionRule.new(month, week, day_of_week, transition_at)
        assert_equal(true, rule1.send(method, rule2))
        assert_equal(true, rule2.send(method, rule1))
      end
    end

    define_method "test_not_equal_by_week_with_#{method}" do
      rule1 = DayOfMonthTransitionRule.new(1, 1, 0, 0)
      rule2 = DayOfMonthTransitionRule.new(1, 2, 0, 0)
      assert_equal(false, rule1.send(method, rule2))
      assert_equal(false, rule2.send(method, rule1))
    end

    define_method "test_not_equal_to_last_day_of_month_with_#{method}" do
      rule1 = DayOfMonthTransitionRule.new(1, 1, 0, 0)
      rule2 = LastDayOfMonthTransitionRule.new(1, 0, 0)
      assert_equal(false, rule1.send(method, rule2))
      assert_equal(false, rule2.send(method, rule1))
    end
  end

  [
    [1, 1, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 1, 0],
    [1, 2, 0, 0],
    [2, 1, 0, 0]
  ].each do |(month, week, day_of_week, transition_at)|
    define_method "test_hash_for_month_#{month}_week_#{week}_day_of_week_#{day_of_week}_and_transition_at_#{transition_at}" do
      rule = DayOfMonthTransitionRule.new(month, week, day_of_week, transition_at)
      expected = [(week - 1) * 7 + 1, month, day_of_week, transition_at].hash
      assert_equal(expected, rule.hash)
    end
  end

  protected

  def create_with_transition_at(transition_at)
    DayOfMonthTransitionRule.new(1, 1, 0, transition_at)
  end

  def create_with_month_and_day_of_week(month, day_of_week)
    DayOfMonthTransitionRule.new(month, 1, day_of_week)
  end
end

class TCLastDayOfMonthTransitionRule < Minitest::Test
  include BaseTransitionRuleTestHelper
  include DayOfWeekTransitionRuleTestHelper

  [
    # All possible last days.
    [2021, 10, [31, 25, 26, 27, 28, 29, 30]],
    [2022, 10, [30, 31, 25, 26, 27, 28, 29]],
    [2023, 10, [29, 30, 31, 25, 26, 27, 28]],
    [2018, 10, [28, 29, 30, 31, 25, 26, 27]],
    [2024, 10, [27, 28, 29, 30, 31, 25, 26]],
    [2025, 10, [26, 27, 28, 29, 30, 31, 25]],
    [2026, 10, [25, 26, 27, 28, 29, 30, 31]],

    # All possible months.
    [2020, 1, [26]],
    [2020, 2, [23]],
    [2020, 3, [29]],
    [2020, 4, [26]],
    [2020, 5, [31]],
    [2020, 6, [28]],
    [2020, 7, [26]],
    [2020, 8, [30]],
    [2020, 9, [27]],
    [2020, 10, [25]],
    [2020, 11, [29]],
    [2020, 12, [27]]
  ].each do |(year, month, days)|
    days.each_with_index do |expected_day, day_of_week|
      define_method "test_month_#{month}_day_of_week_#{day_of_week}_year_#{year}" do
        rule = LastDayOfMonthTransitionRule.new(month, day_of_week, 7200)
        offset = TimezoneOffset.new(0, 0, 'TEST')

        result = rule.at(offset, year)

        assert_kind_of(TimeOrDateTime, result)
        assert_equal(Time.utc(year, month, expected_day, 2, 0, 0), result.to_time)
      end
    end
  end

  [[2020, 6, 29], [2021, 0, 28], [2000, 2, 29], [2100, 0, 28]].each do |(year, day_of_week, expected_day)|
    define_method "test_#{expected_day == 29 ? '' : 'non_'}leap_year_#{year}" do
      rule = LastDayOfMonthTransitionRule.new(2, day_of_week, 7200)
      offset = TimezoneOffset.new(0, 0, 'TEST')

      result = rule.at(offset, year)

      assert_kind_of(TimeOrDateTime, result)
      assert_equal(DateTime.new(year, 2, expected_day, 2, 0, 0), result.to_datetime)
    end
  end

  [:==, :eql?].each do |method|
    [
      [1, 0, 0],
      [1, 0, 1],
      [1, 1, 0],
      [2, 0, 0]
    ].each do |(month, day_of_week, transition_at)|
      define_method "test_equal_for_month_#{month}_day_of_week_#{day_of_week}_and_transition_at_#{transition_at}_with_#{method}" do
        rule1 = LastDayOfMonthTransitionRule.new(month, day_of_week, transition_at)
        rule2 = LastDayOfMonthTransitionRule.new(month, day_of_week, transition_at)
        assert_equal(true, rule1.send(method, rule2))
        assert_equal(true, rule2.send(method, rule1))
      end
    end

    define_method "test_not_equal_to_day_of_month_with_#{method}" do
      rule1 = LastDayOfMonthTransitionRule.new(1, 0, 0)
      rule2 = DayOfMonthTransitionRule.new(1, 1, 0, 0)
      assert_equal(false, rule1.send(method, rule2))
      assert_equal(false, rule2.send(method, rule1))
    end
  end

  [
    [1, 0, 0],
    [1, 0, 1],
    [1, 1, 0],
    [2, 0, 0]
  ].each do |(month, day_of_week, transition_at)|
    define_method "test_hash_for_month_#{month}_day_of_week_#{day_of_week}_and_transition_at_#{transition_at}" do
      rule = LastDayOfMonthTransitionRule.new(month, day_of_week, transition_at)
      expected = [month, day_of_week, transition_at].hash
      assert_equal(expected, rule.hash)
    end
  end

  protected

  def create_with_transition_at(transition_at)
    LastDayOfMonthTransitionRule.new(1, 0, transition_at)
  end

  def create_with_month_and_day_of_week(month, day_of_week)
    LastDayOfMonthTransitionRule.new(month, day_of_week)
  end
end
