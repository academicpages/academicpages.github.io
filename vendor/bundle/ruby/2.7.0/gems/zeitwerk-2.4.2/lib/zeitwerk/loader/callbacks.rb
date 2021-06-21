module Zeitwerk::Loader::Callbacks
  include Zeitwerk::RealModName

  # Invoked from our decorated Kernel#require when a managed file is autoloaded.
  #
  # @private
  # @sig (String) -> void
  def on_file_autoloaded(file)
    cref  = autoloads.delete(file)
    cpath = cpath(*cref)

    to_unload[cpath] = [file, cref] if reloading_enabled?
    Zeitwerk::Registry.unregister_autoload(file)

    if logger && cdef?(*cref)
      log("constant #{cpath} loaded from file #{file}")
    elsif !cdef?(*cref)
      raise Zeitwerk::NameError.new("expected file #{file} to define constant #{cpath}, but didn't", cref.last)
    end

    run_on_load_callbacks(cpath)
  end

  # Invoked from our decorated Kernel#require when a managed directory is
  # autoloaded.
  #
  # @private
  # @sig (String) -> void
  def on_dir_autoloaded(dir)
    # Module#autoload does not serialize concurrent requires, and we handle
    # directories ourselves, so the callback needs to account for concurrency.
    #
    # Multi-threading would introduce a race condition here in which thread t1
    # autovivifies the module, and while autoloads for its children are being
    # set, thread t2 autoloads the same namespace.
    #
    # Without the mutex and subsequent delete call, t2 would reset the module.
    # That not only would reassign the constant (undesirable per se) but, worse,
    # the module object created by t2 wouldn't have any of the autoloads for its
    # children, since t1 would have correctly deleted its lazy_subdirs entry.
    mutex2.synchronize do
      if cref = autoloads.delete(dir)
        autovivified_module = cref[0].const_set(cref[1], Module.new)
        cpath = autovivified_module.name
        log("module #{cpath} autovivified from directory #{dir}") if logger

        to_unload[cpath] = [dir, cref] if reloading_enabled?

        # We don't unregister `dir` in the registry because concurrent threads
        # wouldn't find a loader associated to it in Kernel#require and would
        # try to require the directory. Instead, we are going to keep track of
        # these to be able to unregister later if eager loading.
        autoloaded_dirs << dir

        on_namespace_loaded(autovivified_module)

        run_on_load_callbacks(cpath)
      end
    end
  end

  # Invoked when a class or module is created or reopened, either from the
  # tracer or from module autovivification. If the namespace has matching
  # subdirectories, we descend into them now.
  #
  # @private
  # @sig (Module) -> void
  def on_namespace_loaded(namespace)
    if subdirs = lazy_subdirs.delete(real_mod_name(namespace))
      subdirs.each do |subdir|
        set_autoloads_in_dir(subdir, namespace)
      end
    end
  end

  private

  # @sig (String) -> void
  def run_on_load_callbacks(cpath)
    # Very common, do not even compute a hash code.
    return if on_load_callbacks.empty?

    callbacks = reloading_enabled? ? on_load_callbacks[cpath] : on_load_callbacks.delete(cpath)
    callbacks.each(&:call) if callbacks
  end
end
