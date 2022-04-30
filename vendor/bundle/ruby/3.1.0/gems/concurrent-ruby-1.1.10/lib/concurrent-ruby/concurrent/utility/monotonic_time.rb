require 'concurrent/synchronization'

module Concurrent

  # @!macro monotonic_get_time
  #
  #   Returns the current time a tracked by the application monotonic clock.
  #
  #   @param [Symbol] unit the time unit to be returned, can be either
  #     :float_second, :float_millisecond, :float_microsecond, :second,
  #     :millisecond, :microsecond, or :nanosecond default to :float_second.
  #
  #   @return [Float] The current monotonic time since some unspecified
  #     starting point
  #
  #   @!macro monotonic_clock_warning
  if defined?(Process::CLOCK_MONOTONIC)

    def monotonic_time(unit = :float_second)
      Process.clock_gettime(Process::CLOCK_MONOTONIC, unit)
    end

  elsif Concurrent.on_jruby?

    # @!visibility private
    TIME_UNITS = Hash.new { |_hash, key| raise ArgumentError, "unexpected unit: #{key}" }.compare_by_identity
    TIME_UNITS.merge!(
      second: 1_000_000_000,
      millisecond: 1_000_000,
      microsecond: 1_000,
      nanosecond: 1,
      float_second: 1_000_000_000.0,
      float_millisecond: 1_000_000.0,
      float_microsecond: 1_000.0,
    )
    TIME_UNITS.freeze
    private_constant :TIME_UNITS

    def monotonic_time(unit = :float_second)
      java.lang.System.nanoTime() / TIME_UNITS[unit]
    end

  else

    class_definition = Class.new(Synchronization::LockableObject) do
      def initialize
        @last_time = Time.now.to_f
        @time_units = Hash.new { |_hash, key| raise ArgumentError, "unexpected unit: #{key}" }.compare_by_identity
        @time_units.merge!(
          second: [nil, true],
          millisecond: [1_000, true],
          microsecond: [1_000_000, true],
          nanosecond: [1_000_000_000, true],
          float_second: [nil, false],
          float_millisecond: [1_000.0, false],
          float_microsecond: [1_000_000.0, false],
        )
        super()
      end

      # @!visibility private
      def get_time(unit)
        synchronize do
          now = Time.now.to_f
          if @last_time < now
            @last_time = now
          else # clock has moved back in time
            @last_time += 0.000_001
          end
          scale, to_int = @time_units[unit]
          now *= scale if scale
          now = now.to_i if to_int
          now
        end
      end
    end

    # Clock that cannot be set and represents monotonic time since
    # some unspecified starting point.
    #
    # @!visibility private
    GLOBAL_MONOTONIC_CLOCK = class_definition.new
    private_constant :GLOBAL_MONOTONIC_CLOCK
    
    def monotonic_time(unit = :float_second)
      GLOBAL_MONOTONIC_CLOCK.get_time(unit)
    end
  end
  module_function :monotonic_time
end
