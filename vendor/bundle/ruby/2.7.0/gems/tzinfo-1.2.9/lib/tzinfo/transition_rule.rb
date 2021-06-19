require 'date'

module TZInfo
  # Base class for rules definining the transition between standard and daylight
  # savings time.
  class TransitionRule #:nodoc:
    # Returns the number of seconds after midnight local time on the day
    # identified by the rule at which the transition occurs. Can be negative to
    # denote a time on the prior day. Can be greater than or equal to 86,400 to
    # denote a time of the following day.
    attr_reader :transition_at

    # Initializes a new TransitionRule.
    def initialize(transition_at)
      raise ArgumentError, 'Invalid transition_at' unless transition_at.kind_of?(Integer)
      @transition_at = transition_at
    end

    # Calculates the UTC time of the transition from a given offset on a given
    # year.
    def at(offset, year)
      day = get_day(year)
      day.add_with_convert(@transition_at - offset.utc_total_offset)
    end

    # Determines if this TransitionRule is equal to another instance.
    def ==(r)
      r.kind_of?(TransitionRule) && @transition_at == r.transition_at
    end
    alias eql? ==

    # Returns a hash based on hash_args (defaulting to transition_at).
    def hash
      hash_args.hash
    end

    protected

    # Returns an Array of parameters that will influence the output of hash.
    def hash_args
      [@transition_at]
    end

    def new_time_or_datetime(year, month = 1, day = 1)
      result = if ((year >= 2039 || (year == 2038 && (month >= 2 || (month == 1 && day >= 20)))) && !RubyCoreSupport.time_supports_64bit) ||
        (year < 1970 && !RubyCoreSupport.time_supports_negative)

        # Time handles 29 February on a non-leap year as 1 March.
        # DateTime rejects. Advance manually.
        if month == 2 && day == 29 && !Date.gregorian_leap?(year)
          month = 3
          day = 1
        end

        RubyCoreSupport.datetime_new(year, month, day)
      else
        Time.utc(year, month, day)
      end

      TimeOrDateTime.wrap(result)
    end
  end

  # A base class for transition rules that activate based on an integer day of
  # the year.
  #
  # @private
  class DayOfYearTransitionRule < TransitionRule #:nodoc:
    # Initializes a new DayOfYearTransitionRule.
    def initialize(day, transition_at)
      super(transition_at)
      raise ArgumentError, 'Invalid day' unless day.kind_of?(Integer)
      @seconds = day * 86400
    end

    # Determines if this DayOfYearTransitionRule is equal to another instance.
    def ==(r)
      super(r) && r.kind_of?(DayOfYearTransitionRule) && @seconds == r.seconds
    end
    alias eql? ==

    protected

    # @return [Integer] the day multipled by the number of seconds in a day.
    attr_reader :seconds

    # Returns an Array of parameters that will influence the output of hash.
    def hash_args
      [@seconds] + super
    end
  end

  # Defines transitions that occur on the zero-based nth day of the year.
  #
  # Day 0 is 1 January.
  #
  # Leap days are counted. Day 59 will be 29 February on a leap year and 1 March
  # on a non-leap year. Day 365 will be 31 December on a leap year and 1 January
  # the following year on a non-leap year.
  #
  # @private
  class AbsoluteDayOfYearTransitionRule < DayOfYearTransitionRule #:nodoc:
    # Initializes a new AbsoluteDayOfYearTransitionRule.
    def initialize(day, transition_at = 0)
      super(day, transition_at)
      raise ArgumentError, 'Invalid day' unless day >= 0 && day <= 365
    end

    # Returns true if the day specified by this transition is the first in the
    # year (a day number of 0), otherwise false.
    def is_always_first_day_of_year?
      seconds == 0
    end

    # @returns false.
    def is_always_last_day_of_year?
      false
    end

    # Determines if this AbsoluteDayOfYearTransitionRule is equal to another
    # instance.
    def ==(r)
      super(r) && r.kind_of?(AbsoluteDayOfYearTransitionRule)
    end
    alias eql? ==

    protected

    # Returns a TimeOrDateTime representing midnight local time on the day
    # specified by the rule for the given offset and year.
    def get_day(year)
      new_time_or_datetime(year).add_with_convert(seconds)
    end

    # Returns an Array of parameters that will influence the output of hash.
    def hash_args
      [AbsoluteDayOfYearTransitionRule] + super
    end
  end

  # Defines transitions that occur on the one-based nth Julian day of the year.
  #
  # Leap days are not counted. Day 1 is 1 January. Day 60 is always 1 March.
  # Day 365 is always 31 December.
  #
  # @private
  class JulianDayOfYearTransitionRule < DayOfYearTransitionRule #:nodoc:
    # The 60 days in seconds.
    LEAP = 60 * 86400

    # The length of a non-leap year in seconds.
    YEAR = 365 * 86400

    # Initializes a new JulianDayOfYearTransitionRule.
    def initialize(day, transition_at = 0)
      super(day, transition_at)
      raise ArgumentError, 'Invalid day' unless day >= 1 && day <= 365
    end

    # Returns true if the day specified by this transition is the first in the
    # year (a day number of 1), otherwise false.
    def is_always_first_day_of_year?
      seconds == 86400
    end

    # Returns true if the day specified by this transition is the last in the
    # year (a day number of 365), otherwise false.
    def is_always_last_day_of_year?
      seconds == YEAR
    end

    # Determines if this JulianDayOfYearTransitionRule is equal to another
    # instance.
    def ==(r)
      super(r) && r.kind_of?(JulianDayOfYearTransitionRule)
    end
    alias eql? ==

    protected

    # Returns a TimeOrDateTime representing midnight local time on the day
    # specified by the rule for the given offset and year.
    def get_day(year)
      # Returns 1 March on non-leap years.
      leap = new_time_or_datetime(year, 2, 29)
      diff = seconds - LEAP
      diff += 86400 if diff >= 0 && leap.mday == 29
      leap.add_with_convert(diff)
    end

    # Returns an Array of parameters that will influence the output of hash.
    def hash_args
      [JulianDayOfYearTransitionRule] + super
    end
  end

  # A base class for rules that transition on a particular day of week of a
  # given week (subclasses specify which week of the month).
  #
  # @private
  class DayOfWeekTransitionRule < TransitionRule #:nodoc:
    # Initializes a new DayOfWeekTransitionRule.
    def initialize(month, day_of_week, transition_at)
      super(transition_at)
      raise ArgumentError, 'Invalid month' unless month.kind_of?(Integer) && month >= 1 && month <= 12
      raise ArgumentError, 'Invalid day_of_week' unless day_of_week.kind_of?(Integer) && day_of_week >= 0 && day_of_week <= 6
      @month = month
      @day_of_week = day_of_week
    end

    # Returns false.
    def is_always_first_day_of_year?
      false
    end

    # Returns false.
    def is_always_last_day_of_year?
      false
    end

    # Determines if this DayOfWeekTransitionRule is equal to another instance.
    def ==(r)
      super(r) && r.kind_of?(DayOfWeekTransitionRule) && @month == r.month && @day_of_week == r.day_of_week
    end
    alias eql? ==

    protected

    # Returns the month of the year (1 to 12).
    attr_reader :month

    # Returns the day of the week (0 to 6 for Sunday to Monday).
    attr_reader :day_of_week

    # Returns an Array of parameters that will influence the output of hash.
    def hash_args
      [@month, @day_of_week] + super
    end
  end

  # A rule that transitions on the nth occurrence of a particular day of week
  # of a calendar month.
  #
  # @private
  class DayOfMonthTransitionRule < DayOfWeekTransitionRule #:nodoc:
    # Initializes a new DayOfMonthTransitionRule.
    def initialize(month, week, day_of_week, transition_at = 0)
      super(month, day_of_week, transition_at)
      raise ArgumentError, 'Invalid week' unless week.kind_of?(Integer) && week >= 1 && week <= 4
      @offset_start = (week - 1) * 7 + 1
    end

    # Determines if this DayOfMonthTransitionRule is equal to another instance.
    def ==(r)
      super(r) && r.kind_of?(DayOfMonthTransitionRule) && @offset_start == r.offset_start
    end
    alias eql? ==

    protected

    # Returns the day the week starts on for a month starting on a Sunday.
    attr_reader :offset_start

    # Returns a TimeOrDateTime representing midnight local time on the day
    # specified by the rule for the given offset and year.
    def get_day(year)
      candidate = new_time_or_datetime(year, month, @offset_start)
      diff = day_of_week - candidate.wday

      if diff < 0
        candidate.add_with_convert((7 + diff) * 86400)
      elsif diff > 0
        candidate.add_with_convert(diff * 86400)
      else
        candidate
      end
    end

    # Returns an Array of parameters that will influence the output of hash.
    def hash_args
      [@offset_start] + super
    end
  end

  # A rule that transitions on the last occurrence of a particular day of week
  # of a calendar month.
  #
  # @private
  class LastDayOfMonthTransitionRule < DayOfWeekTransitionRule #:nodoc:
    # Initializes a new LastDayOfMonthTransitionRule.
    def initialize(month, day_of_week, transition_at = 0)
      super(month, day_of_week, transition_at)
    end

    # Determines if this LastDayOfMonthTransitionRule is equal to another
    # instance.
    def ==(r)
      super(r) && r.kind_of?(LastDayOfMonthTransitionRule)
    end
    alias eql? ==

    protected

    # Returns a TimeOrDateTime representing midnight local time on the day
    # specified by the rule for the given offset and year.
    def get_day(year)
      next_month = month + 1
      if next_month == 13
        year += 1
        next_month = 1
      end

      candidate = new_time_or_datetime(year, next_month).add_with_convert(-86400)
      diff = candidate.wday - day_of_week

      if diff < 0
        candidate - (diff + 7) * 86400
      elsif diff > 0
        candidate - diff * 86400
      else
        candidate
      end
    end
  end
end
