require 'concurrent/thread_safe/util'
require 'concurrent/thread_safe/util/volatile'
require 'concurrent/utility/engine'

module Concurrent

  # @!visibility private
  module ThreadSafe

    # @!visibility private
    module Util

      # Provides a cheapest possible (mainly in terms of memory usage) +Mutex+
      # with the +ConditionVariable+ bundled in.
      #
      # Usage:
      #   class A
      #     include CheapLockable
      #
      #     def do_exlusively
      #       cheap_synchronize { yield }
      #     end
      #
      #     def wait_for_something
      #       cheap_synchronize do
      #         cheap_wait until resource_available?
      #         do_something
      #         cheap_broadcast # wake up others
      #       end
      #     end
      #   end
      # 
      # @!visibility private
      module CheapLockable
        private
        if Concurrent.on_jruby?
          # Use Java's native synchronized (this) { wait(); notifyAll(); } to avoid the overhead of the extra Mutex objects
          require 'jruby'

          def cheap_synchronize
            JRuby.reference0(self).synchronized { yield }
          end

          def cheap_wait
            JRuby.reference0(self).wait
          end

          def cheap_broadcast
            JRuby.reference0(self).notify_all
          end
        else
          require 'thread'

          extend Volatile
          attr_volatile :mutex

          # Non-reentrant Mutex#syncrhonize
          def cheap_synchronize
            true until (my_mutex = mutex) || cas_mutex(nil, my_mutex = Mutex.new)
            my_mutex.synchronize { yield }
          end

          # Releases this object's +cheap_synchronize+ lock and goes to sleep waiting for other threads to +cheap_broadcast+, reacquires the lock on wakeup.
          # Must only be called in +cheap_broadcast+'s block.
          def cheap_wait
            conditional_variable = @conditional_variable ||= ConditionVariable.new
            conditional_variable.wait(mutex)
          end

          # Wakes up all threads waiting for this object's +cheap_synchronize+ lock.
          # Must only be called in +cheap_broadcast+'s block.
          def cheap_broadcast
            if conditional_variable = @conditional_variable
              conditional_variable.broadcast
            end
          end
        end
      end
    end
  end
end
