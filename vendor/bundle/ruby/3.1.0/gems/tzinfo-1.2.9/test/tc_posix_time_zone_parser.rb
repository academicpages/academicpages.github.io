require File.join(File.expand_path(File.dirname(__FILE__)), 'test_utils')

include TZInfo

class TCPosixTimeZoneParser < Minitest::Test
  HOUR = 3600
  MINUTE = 60

  class << self
    private

    def append_time_to_rule(day_rule, time)
      time ? "#{day_rule}/#{time}" : day_rule
    end

    def define_invalid_dst_rule_tests(type, rule)
      define_method "test_#{type}_dst_start_rule_for_invalid_#{rule}" do
        tz_string = "STD-1DST,#{rule},300"
        assert_raises(InvalidPosixTimeZone) { @parser.parse(tz_string) }
      end

      define_method "test_#{type}_dst_end_rule_for_invalid_#{rule}" do
        tz_string = "STD-1DST,60,#{rule}"
        assert_raises(InvalidPosixTimeZone) { @parser.parse(tz_string) }
      end
    end
  end

  def setup
    @parser = PosixTimeZoneParser.new
  end

  def test_empty_rule_returns_nil
    result = @parser.parse('')
    assert_nil(result)
  end

  ABBREVIATIONS_WITH_OFFSETS = [
    ['UTC0', :UTC, 0],
    ['U0', :U, 0],
    ['West1', :West, -HOUR],
    ['East-1', :East, HOUR],
    ['<-05>5', :'-05', -5 * HOUR],
    ['<+12>-12', :'+12', 12 * HOUR],
    ['HMM2:30', :HMM, -(2 * HOUR + 30 * MINUTE)],
    ['HHMM02:30', :HHMM, -(2 * HOUR + 30 * MINUTE)],
    ['HHMM+02:30', :HHMM, -(2 * HOUR + 30 * MINUTE)],
    ['HHMSS-12:5:50', :HHMSS, 12 * HOUR + 5 * MINUTE + 50],
    ['HHMMSS-12:05:50', :HHMMSS, 12 * HOUR + 5 * MINUTE + 50],
    ['HHMMS-12:05:7', :HHMMS, 12 * HOUR + 5 * MINUTE + 7]
  ]

  ABBREVIATIONS_WITH_OFFSETS.each do |(tz_string, expected_abbrev, expected_base_offset)|
    define_method "test_std_only_returns_std_offset_#{tz_string}" do
      result = @parser.parse(tz_string)
      expected = TimezoneOffset.new(expected_base_offset, 0, expected_abbrev)
      assert_equal(expected, result)
    end
  end

  ABBREVIATIONS_WITH_OFFSETS.each do |(abbrev_and_offset, expected_abbrev, expected_base_offset)|
    define_method "test_std_offset_#{abbrev_and_offset}" do
      result = @parser.parse(abbrev_and_offset + 'DST,60,300')
      expected_std_offset = TimezoneOffset.new(expected_base_offset, 0, expected_abbrev)
      assert_equal(expected_std_offset, result.std_offset)
    end
  end

  [
    ['Zero0One-1', :One, 0, HOUR],
    ['Zero0One', :One, 0, HOUR],
    ['Z0O', :O, 0, HOUR],
    ['West1WestS0', :WestS, -HOUR, HOUR],
    ['West1WestS', :WestS, -HOUR, HOUR],
    ['East-1EastS-2', :EastS, HOUR, HOUR],
    ['East-1EastS', :EastS, HOUR, HOUR],
    ['Neg2NegS3', :NegS, -2 * HOUR, -HOUR],
    ['<-05>5<-04>4', :'-04', -5 * HOUR, HOUR],
    ['STD5<-04>4', :'-04', -5 * HOUR, HOUR],
    ['<+12>-12<+13>-13', :'+13', 12 * HOUR, HOUR],
    ['STD-12<+13>-13', :'+13', 12 * HOUR, HOUR],
    ['HMM2:30SHMM1:15', :SHMM, -(2 * HOUR + 30 * MINUTE), HOUR + 15 * MINUTE],
    ['HHMM02:30SHHMM01:15', :SHHMM, -(2 * HOUR + 30 * MINUTE), HOUR + 15 * MINUTE],
    ['HHMM+02:30SHHMM+01:15', :SHHMM, -(2 * HOUR + 30 * MINUTE), HOUR + 15 * MINUTE],
    ['HHMSS-12:5:50SHHMSS-13:4:30', :SHHMSS, 12 * HOUR + 5 * MINUTE + 50, 58 * MINUTE + 40],
    ['HHMMSS-12:05:50SHHMMSS-13:04:30', :SHHMMSS, 12 * HOUR + 5 * MINUTE + 50, 58 * MINUTE + 40],
    ['HHMMS-12:05:7SHHMMSS-13:06:8', :SHHMMSS, 12 * HOUR + 5 * MINUTE + 7, HOUR + MINUTE + 1],
  ].each do |(abbrevs_and_offsets, expected_abbrev, expected_base_offset, expected_std_offset)|
    define_method "test_dst_offset_#{abbrevs_and_offsets}" do
      result = @parser.parse(abbrevs_and_offsets + ',60,300')
      expected_dst_offset = TimezoneOffset.new(expected_base_offset, expected_std_offset, expected_abbrev)
      assert_equal(expected_dst_offset, result.dst_offset)
    end
  end

  ['<M-1>01:-1', '<M60>01:60', '<S-1>01:00:-1', '<S60>01:00:60'].each do |abbrev_and_offset|
    ['', 'DST,60,300'].each do |dst_suffix|
      tz_string = abbrev_and_offset + dst_suffix
      define_method "test_std_offset_invalid_#{tz_string}" do
        assert_raises(InvalidPosixTimeZone) { @parser.parse(tz_string) }
      end
    end

    tz_string = "STD1#{abbrev_and_offset},60,300"
    define_method "test_dst_offset_invalid_#{tz_string}" do
      assert_raises(InvalidPosixTimeZone) { @parser.parse(tz_string) }
    end
  end

  [
    [nil, 2 * HOUR],
    ['2', 2 * HOUR],
    ['+2', 2 * HOUR],
    ['-2', -2 * HOUR],
    ['2:3:4', 2 * HOUR + 3 * MINUTE + 4],
    ['02:03:04', 2 * HOUR + 3 * MINUTE + 4],
    ['-2:3:4', -2 * HOUR + 3 * MINUTE + 4], # 22:03:04 on the day prior to the one specified
    ['-02:03:04', -2 * HOUR + 3 * MINUTE + 4],
    ['167', 167 * HOUR],
    ['-167', -167 * HOUR]
  ].each do |(time, expected_offset_from_midnight)|
    [
      ['J1', 1],
      ['J365', 365]
    ].each do |(julian_day_rule, expected_julian_day)|
      rule = append_time_to_rule(julian_day_rule, time)

      define_method "test_julian_day_dst_start_rule_for_#{rule}" do
        result = @parser.parse("STD-1DST,#{rule},300")
        expected_dst_start_rule = JulianDayOfYearTransitionRule.new(expected_julian_day, expected_offset_from_midnight)
        assert_equal(expected_dst_start_rule, result.dst_start_rule)
      end

      define_method "test_julian_day_dst_end_rule_for_#{rule}" do
        result = @parser.parse("STD-1DST,60,#{rule}")
        expected_dst_end_rule = JulianDayOfYearTransitionRule.new(expected_julian_day, expected_offset_from_midnight)
        assert_equal(expected_dst_end_rule, result.dst_end_rule)
      end
    end

    [
      ['0', 0],
      ['365', 365]
    ].each do |(absolute_day_rule, expected_day)|
      rule = append_time_to_rule(absolute_day_rule, time)

      define_method "test_absolute_day_dst_start_rule_for_#{rule}" do
        result = @parser.parse("STD-1DST,#{rule},J300")
        expected_dst_start_rule = AbsoluteDayOfYearTransitionRule.new(expected_day, expected_offset_from_midnight)
        assert_equal(expected_dst_start_rule, result.dst_start_rule)
      end

      define_method "test_absolute_day_dst_end_rule_for_#{rule}" do
        result = @parser.parse("STD-1DST,J60,#{rule}")
        expected_dst_end_rule = AbsoluteDayOfYearTransitionRule.new(expected_day, expected_offset_from_midnight)
        assert_equal(expected_dst_end_rule, result.dst_end_rule)
      end
    end

    [
      ['M1.1.0', 1, 1, 0],
      ['M12.4.6', 12, 4, 6]
    ].each do |(day_of_month_rule, expected_month, expected_week, expected_day_of_week)|
      rule = append_time_to_rule(day_of_month_rule, time)

      define_method "test_day_of_month_dst_start_rule_for_#{rule}" do
        result = @parser.parse("STD-1DST,#{rule},300")
        expected_dst_start_rule = DayOfMonthTransitionRule.new(expected_month, expected_week, expected_day_of_week, expected_offset_from_midnight)
        assert_equal(expected_dst_start_rule, result.dst_start_rule)
      end

      define_method "test_day_of_month_dst_end_rule_for_#{rule}" do
        result = @parser.parse("STD-1DST,60,#{rule}")
        expected_dst_end_rule = DayOfMonthTransitionRule.new(expected_month, expected_week, expected_day_of_week, expected_offset_from_midnight)
        assert_equal(expected_dst_end_rule, result.dst_end_rule)
      end
    end

    [
      ['M1.5.0', 1, 0],
      ['M12.5.6', 12, 6]
    ].each do |(last_day_of_month_rule, expected_month, expected_day_of_week)|
      rule = append_time_to_rule(last_day_of_month_rule, time)

      define_method "test_last_day_of_month_dst_start_rule_for_#{rule}" do
        result = @parser.parse("STD-1DST,#{rule},300")
        expected_dst_start_rule = LastDayOfMonthTransitionRule.new(expected_month, expected_day_of_week, expected_offset_from_midnight)
        assert_equal(expected_dst_start_rule, result.dst_start_rule)
      end

      define_method "test_last_day_of_month_dst_end_rule_for_#{rule}" do
        result = @parser.parse("STD-1DST,60,#{rule}")
        expected_dst_end_rule = LastDayOfMonthTransitionRule.new(expected_month, expected_day_of_week, expected_offset_from_midnight)
        assert_equal(expected_dst_end_rule, result.dst_end_rule)
      end
    end
  end

  ['J0', 'J366'].each do |julian_day_rule|
    define_invalid_dst_rule_tests('julian_day', julian_day_rule)
  end

  ['-1', '366'].each do |absolute_day_rule|
    define_invalid_dst_rule_tests('absolute_day', absolute_day_rule)
  end

  ['M0,1,0', 'M13,1,0', 'M6,0,0', 'M6,6,0', 'M6,1,-1', 'M6,1,7'].each do |day_of_month_rule|
    define_invalid_dst_rule_tests('day_of_month', day_of_month_rule)
  end

  ['M0,5,0', 'M13,5,0', 'M6,5,-1', 'M6,5,7'].each do |last_day_of_month_rule|
    define_invalid_dst_rule_tests('last_day_of_month', last_day_of_month_rule)
  end

  def test_invalid_dst_start_rule
    assert_raises(InvalidPosixTimeZone) { @parser.parse('STD1DST,X60,300') }
  end

  def test_invalid_dst_end_rule
    assert_raises(InvalidPosixTimeZone) { @parser.parse('STD1DST,60,X300') }
  end

  [
    ['STD5DST,0/0,J365/25', :DST, -5 * HOUR, HOUR],
    ['STD-5DST,0/0,J365/25', :DST, 5 * HOUR, HOUR],
    ['STD5DST3,0/0,J365/26', :DST, -5 * HOUR, 2 * HOUR],
    ['STD5DST6,0/0,J365/23', :DST, -5 * HOUR, -HOUR],
    ['STD5DST,J1/0,J365/25', :DST, -5 * HOUR, HOUR],
    ['Winter5Summer,0/0,J365/25', :Summer, -5 * HOUR, HOUR],
    ['<-05>5<-06>,0/0,J365/25', :'-06', -5 * HOUR, HOUR]
  ].each do |(tz_string, expected_abbrev, expected_base_offset, expected_std_offset)|
    define_method "test_dst_only_returns_continuous_offset_for_#{tz_string}" do
      result = @parser.parse(tz_string)
      expected = TimezoneOffset.new(expected_base_offset, expected_std_offset, expected_abbrev)
      assert_equal(expected, result)
    end
  end

  def test_parses_tainted_string_in_safe_mode_and_returns_untainted_abbreviations
    safe_test(:unavailable => :skip) do
      result = @parser.parse('STD1DST,60,300'.dup.taint)

      assert_equal(:STD, result.std_offset.abbreviation)
      assert_equal(:DST, result.dst_offset.abbreviation)
    end
  end

  ['STD1', 'STD1DST,60,300'].each do |tz_string|
    tz_string += "-"
    define_method "test_content_after_end_for_#{tz_string}" do
      error = assert_raises(InvalidPosixTimeZone) { @parser.parse(tz_string) }
      assert_equal("Expected the end of a POSIX-style time zone string but found '-'.", error.message)
    end
  end

  ['X', 0].each do |invalid_tz_string|
    define_method "test_invalid_tz_string_#{invalid_tz_string}" do
      assert_raises(InvalidPosixTimeZone) { @parser.parse(invalid_tz_string) }
    end
  end
end
