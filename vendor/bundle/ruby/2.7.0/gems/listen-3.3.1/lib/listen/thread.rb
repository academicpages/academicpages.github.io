# frozen_string_literal: true

require 'thread'

require_relative 'logger'

module Listen
  module Thread
    class << self
      # Creates a new thread with the given name.
      # Any exceptions raised by the thread will be logged with the thread name and complete backtrace.
      def new(name, &block)
        thread_name = "listen-#{name}"
        caller_stack = caller

        ::Thread.new do
          rescue_and_log(thread_name, caller_stack: caller_stack, &block)
        end.tap do |thread|
          thread.name = thread_name
        end
      end

      def rescue_and_log(method_name, *args, caller_stack: nil)
        yield(*args)
      rescue Exception => ex
        _log_exception(ex, method_name, caller_stack: caller_stack)
      end

      private

      def _log_exception(ex, thread_name, caller_stack: nil)
        complete_backtrace = if caller_stack
                               [*ex.backtrace, "--- Thread.new ---", *caller_stack]
                             else
                               ex.backtrace
                             end
        message = "Exception rescued in #{thread_name}:\n#{_exception_with_causes(ex)}\n#{complete_backtrace * "\n"}"
        Listen.logger.error(message)
      end

      def _exception_with_causes(ex)
        result = +"#{ex.class}: #{ex}"
        if ex.cause
          result << "\n"
          result << "--- Caused by: ---\n"
          result << _exception_with_causes(ex.cause)
        end
        result
      end
    end
  end
end
