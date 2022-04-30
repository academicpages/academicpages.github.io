module TZInfo
  # A set of rules that define when transitions occur in time zones with
  # annually occurring daylight savings time.
  #
  # @private
  class AnnualRules #:nodoc:
    # Returned by #transitions. #offset is the TimezoneOffset that applies
    # from the UTC TimeOrDateTime #at. #previous_offset is the prior
    # TimezoneOffset.
    Transition = Struct.new(:offset, :previous_offset, :at)

    # The standard offset that applies when daylight savings time is not in
    # force.
    attr_reader :std_offset

    # The offset that applies when daylight savings time is in force.
    attr_reader :dst_offset

    # The rule that determines when daylight savings time starts.
    attr_reader :dst_start_rule

    # The rule that determines when daylight savings time ends.
    attr_reader :dst_end_rule

    # Initializes a new {AnnualRules} instance.
    def initialize(std_offset, dst_offset, dst_start_rule, dst_end_rule)
      @std_offset = std_offset
      @dst_offset = dst_offset
      @dst_start_rule = dst_start_rule
      @dst_end_rule = dst_end_rule
    end

    # Returns the transitions between standard and daylight savings time for a
    # given year. The results are ordered by time of occurrence (earliest to
    # latest).
    def transitions(year)
      start_dst = apply_rule(@dst_start_rule, @std_offset, @dst_offset, year)
      end_dst = apply_rule(@dst_end_rule, @dst_offset, @std_offset, year)

      end_dst.at < start_dst.at ? [end_dst, start_dst] : [start_dst, end_dst]
    end

    private

    # Applies a given rule between offsets on a year.
    def apply_rule(rule, from_offset, to_offset, year)
      at = rule.at(from_offset, year)
      Transition.new(to_offset, from_offset, at)
    end
  end
end
