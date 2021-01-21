require 'thread'
require 'concurrent/atomic/abstract_thread_local_var'

module Concurrent

  # @!visibility private
  # @!macro internal_implementation_note
  class RubyThreadLocalVar < AbstractThreadLocalVar

    # Each thread has a (lazily initialized) array of thread-local variable values
    # Each time a new thread-local var is created, we allocate an "index" for it
    # For example, if the allocated index is 1, that means slot #1 in EVERY
    #   thread's thread-local array will be used for the value of that TLV
    #
    # The good thing about using a per-THREAD structure to hold values, rather
    #   than a per-TLV structure, is that no synchronization is needed when
    #    reading and writing those values (since the structure is only ever
    #    accessed by a single thread)
    #
    # Of course, when a TLV is GC'd, 1) we need to recover its index for use
    #   by other new TLVs (otherwise the thread-local arrays could get bigger
    #   and bigger with time), and 2) we need to null out all the references
    #   held in the now-unused slots (both to avoid blocking GC of those objects,
    #   and also to prevent "stale" values from being passed on to a new TLV
    #   when the index is reused)
    # Because we need to null out freed slots, we need to keep references to
    #   ALL the thread-local arrays -- ARRAYS is for that
    # But when a Thread is GC'd, we need to drop the reference to its thread-local
    #   array, so we don't leak memory

    FREE                = []
    LOCK                = Mutex.new
    THREAD_LOCAL_ARRAYS = {} # used as a hash set

    # synchronize when not on MRI
    # on MRI using lock in finalizer leads to "can't be called from trap context" error
    # so the code is carefully written to be tread-safe on MRI relying on GIL

    if Concurrent.on_cruby?
      # @!visibility private
      def self.semi_sync(&block)
        block.call
      end
    else
      # @!visibility private
      def self.semi_sync(&block)
        LOCK.synchronize(&block)
      end
    end

    private_constant :FREE, :LOCK, :THREAD_LOCAL_ARRAYS

    # @!macro thread_local_var_method_get
    def value
      if (array = get_threadlocal_array)
        value = array[@index]
        if value.nil?
          default
        elsif value.equal?(NULL)
          nil
        else
          value
        end
      else
        default
      end
    end

    # @!macro thread_local_var_method_set
    def value=(value)
      me = Thread.current
      # We could keep the thread-local arrays in a hash, keyed by Thread
      # But why? That would require locking
      # Using Ruby's built-in thread-local storage is faster
      unless (array = get_threadlocal_array(me))
        array = set_threadlocal_array([], me)
        self.class.semi_sync { THREAD_LOCAL_ARRAYS[array.object_id] = array }
        ObjectSpace.define_finalizer(me, self.class.thread_finalizer(array.object_id))
      end
      array[@index] = (value.nil? ? NULL : value)
      value
    end

    protected

    # @!visibility private
    def allocate_storage
      @index = FREE.pop || next_index

      ObjectSpace.define_finalizer(self, self.class.thread_local_finalizer(@index))
    end

    # @!visibility private
    def self.thread_local_finalizer(index)
      proc do
        semi_sync do
          # The cost of GC'ing a TLV is linear in the number of threads using TLVs
          # But that is natural! More threads means more storage is used per TLV
          # So naturally more CPU time is required to free more storage
          THREAD_LOCAL_ARRAYS.each_value { |array| array[index] = nil }
          # free index has to be published after the arrays are cleared
          FREE.push(index)
        end
      end
    end

    # @!visibility private
    def self.thread_finalizer(id)
      proc do
        semi_sync do
          # The thread which used this thread-local array is now gone
          # So don't hold onto a reference to the array (thus blocking GC)
          THREAD_LOCAL_ARRAYS.delete(id)
        end
      end
    end

    private

    # noinspection RubyClassVariableUsageInspection
    @@next = 0
    # noinspection RubyClassVariableUsageInspection
    def next_index
      LOCK.synchronize do
        result = @@next
        @@next += 1
        result
      end
    end

    if Thread.instance_methods.include?(:thread_variable_get)

      def get_threadlocal_array(thread = Thread.current)
        thread.thread_variable_get(:__threadlocal_array__)
      end

      def set_threadlocal_array(array, thread = Thread.current)
        thread.thread_variable_set(:__threadlocal_array__, array)
      end

    else

      def get_threadlocal_array(thread = Thread.current)
        thread[:__threadlocal_array__]
      end

      def set_threadlocal_array(array, thread = Thread.current)
        thread[:__threadlocal_array__] = array
      end
    end

    # This exists only for use in testing
    # @!visibility private
    def value_for(thread)
      if (array = get_threadlocal_array(thread))
        value = array[@index]
        if value.nil?
          get_default
        elsif value.equal?(NULL)
          nil
        else
          value
        end
      else
        get_default
      end
    end

    # @!visibility private
    def get_default
      if @default_block
        raise "Cannot use default_for with default block"
      else
        @default
      end
    end
  end
end
