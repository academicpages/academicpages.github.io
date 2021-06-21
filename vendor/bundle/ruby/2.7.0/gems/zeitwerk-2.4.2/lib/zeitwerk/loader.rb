# frozen_string_literal: true

require "set"
require "securerandom"

module Zeitwerk
  class Loader
    require_relative "loader/callbacks"
    include Callbacks
    include RealModName

    # @sig String
    attr_reader :tag

    # @sig #camelize
    attr_accessor :inflector

    # @sig #call | #debug | nil
    attr_accessor :logger

    # Absolute paths of the root directories. Stored in a hash to preserve
    # order, easily handle duplicates, and also be able to have a fast lookup,
    # needed for detecting nested paths.
    #
    #   "/Users/fxn/blog/app/assets"   => true,
    #   "/Users/fxn/blog/app/channels" => true,
    #   ...
    #
    # This is a private collection maintained by the loader. The public
    # interface for it is `push_dir` and `dirs`.
    #
    # @private
    # @sig Hash[String, true]
    attr_reader :root_dirs

    # Absolute paths of files or directories that have to be preloaded.
    #
    # @private
    # @sig Array[String]
    attr_reader :preloads

    # Absolute paths of files, directories, or glob patterns to be totally
    # ignored.
    #
    # @private
    # @sig Set[String]
    attr_reader :ignored_glob_patterns

    # The actual collection of absolute file and directory names at the time the
    # ignored glob patterns were expanded. Computed on setup, and recomputed on
    # reload.
    #
    # @private
    # @sig Set[String]
    attr_reader :ignored_paths

    # Absolute paths of directories or glob patterns to be collapsed.
    #
    # @private
    # @sig Set[String]
    attr_reader :collapse_glob_patterns

    # The actual collection of absolute directory names at the time the collapse
    # glob patterns were expanded. Computed on setup, and recomputed on reload.
    #
    # @private
    # @sig Set[String]
    attr_reader :collapse_dirs

    # Maps real absolute paths for which an autoload has been set ---and not
    # executed--- to their corresponding parent class or module and constant
    # name.
    #
    #   "/Users/fxn/blog/app/models/user.rb"          => [Object, :User],
    #   "/Users/fxn/blog/app/models/hotel/pricing.rb" => [Hotel, :Pricing]
    #   ...
    #
    # @private
    # @sig Hash[String, [Module, Symbol]]
    attr_reader :autoloads

    # We keep track of autoloaded directories to remove them from the registry
    # at the end of eager loading.
    #
    # Files are removed as they are autoloaded, but directories need to wait due
    # to concurrency (see why in Zeitwerk::Loader::Callbacks#on_dir_autoloaded).
    #
    # @private
    # @sig Array[String]
    attr_reader :autoloaded_dirs

    # Stores metadata needed for unloading. Its entries look like this:
    #
    #   "Admin::Role" => [".../admin/role.rb", [Admin, :Role]]
    #
    # The cpath as key helps implementing unloadable_cpath? The real file name
    # is stored in order to be able to delete it from $LOADED_FEATURES, and the
    # pair [Module, Symbol] is used to remove_const the constant from the class
    # or module object.
    #
    # If reloading is enabled, this hash is filled as constants are autoloaded
    # or eager loaded. Otherwise, the collection remains empty.
    #
    # @private
    # @sig Hash[String, [String, [Module, Symbol]]]
    attr_reader :to_unload

    # Maps constant paths of namespaces to arrays of corresponding directories.
    #
    # For example, given this mapping:
    #
    #   "Admin" => [
    #     "/Users/fxn/blog/app/controllers/admin",
    #     "/Users/fxn/blog/app/models/admin",
    #     ...
    #   ]
    #
    # when `Admin` gets defined we know that it plays the role of a namespace and
    # that its children are spread over those directories. We'll visit them to set
    # up the corresponding autoloads.
    #
    # @private
    # @sig Hash[String, Array[String]]
    attr_reader :lazy_subdirs

    # Absolute paths of files or directories not to be eager loaded.
    #
    # @private
    # @sig Set[String]
    attr_reader :eager_load_exclusions

    # User-oriented callbacks to be fired when a constant is loaded.
    attr_reader :on_load_callbacks

    # @private
    # @sig Mutex
    attr_reader :mutex

    # @private
    # @sig Mutex
    attr_reader :mutex2

    def initialize
      @initialized_at = Time.now

      @tag       = SecureRandom.hex(3)
      @inflector = Inflector.new
      @logger    = self.class.default_logger

      @root_dirs              = {}
      @preloads               = []
      @ignored_glob_patterns  = Set.new
      @ignored_paths          = Set.new
      @collapse_glob_patterns = Set.new
      @collapse_dirs          = Set.new
      @autoloads              = {}
      @autoloaded_dirs        = []
      @to_unload              = {}
      @lazy_subdirs           = {}
      @eager_load_exclusions  = Set.new
      @on_load_callbacks      = {}

      # TODO: find a better name for these mutexes.
      @mutex        = Mutex.new
      @mutex2       = Mutex.new
      @setup        = false
      @eager_loaded = false

      @reloading_enabled = false

      Registry.register_loader(self)
    end

    # Sets a tag for the loader, useful for logging.
    #
    # @param tag [#to_s]
    # @sig (#to_s) -> void
    def tag=(tag)
      @tag = tag.to_s
    end

    # Absolute paths of the root directories. This is a read-only collection,
    # please push here via `push_dir`.
    #
    # @sig () -> Array[String]
    def dirs
      root_dirs.keys.freeze
    end

    # Pushes `path` to the list of root directories.
    #
    # Raises `Zeitwerk::Error` if `path` does not exist, or if another loader in
    # the same process already manages that directory or one of its ascendants
    # or descendants.
    #
    # @raise [Zeitwerk::Error]
    # @sig (String | Pathname, Module) -> void
    def push_dir(path, namespace: Object)
      # Note that Class < Module.
      unless namespace.is_a?(Module)
        raise Error, "#{namespace.inspect} is not a class or module object, should be"
      end

      abspath = File.expand_path(path)
      if dir?(abspath)
        raise_if_conflicting_directory(abspath)
        root_dirs[abspath] = namespace
      else
        raise Error, "the root directory #{abspath} does not exist"
      end
    end

    # You need to call this method before setup in order to be able to reload.
    # There is no way to undo this, either you want to reload or you don't.
    #
    # @raise [Zeitwerk::Error]
    # @sig () -> void
    def enable_reloading
      mutex.synchronize do
        break if @reloading_enabled

        if @setup
          raise Error, "cannot enable reloading after setup"
        else
          @reloading_enabled = true
        end
      end
    end

    # @sig () -> bool
    def reloading_enabled?
      @reloading_enabled
    end

    # Files or directories to be preloaded instead of lazy loaded.
    #
    # @sig (*(String | Pathname | Array[String | Pathname])) -> void
    def preload(*paths)
      mutex.synchronize do
        expand_paths(paths).each do |abspath|
          preloads << abspath
          do_preload_abspath(abspath) if @setup
        end
      end
    end

    # Configure files, directories, or glob patterns to be totally ignored.
    #
    # @sig (*(String | Pathname | Array[String | Pathname])) -> void
    def ignore(*glob_patterns)
      glob_patterns = expand_paths(glob_patterns)
      mutex.synchronize do
        ignored_glob_patterns.merge(glob_patterns)
        ignored_paths.merge(expand_glob_patterns(glob_patterns))
      end
    end

    # Configure directories or glob patterns to be collapsed.
    #
    # @sig (*(String | Pathname | Array[String | Pathname])) -> void
    def collapse(*glob_patterns)
      glob_patterns = expand_paths(glob_patterns)
      mutex.synchronize do
        collapse_glob_patterns.merge(glob_patterns)
        collapse_dirs.merge(expand_glob_patterns(glob_patterns))
      end
    end

    # Configure a block to be invoked once a certain constant path is loaded.
    # Supports multiple callbacks, and if there are many, they are executed in
    # the order in which they were defined.
    #
    #   loader.on_load("SomeApiClient") do
    #     SomeApiClient.endpoint = "https://api.dev"
    #   end
    #
    # @raise [TypeError]
    # @sig (String) { () -> void } -> void
    def on_load(cpath, &block)
      raise TypeError, "on_load only accepts strings" unless cpath.is_a?(String)

      mutex.synchronize do
        (on_load_callbacks[cpath] ||= []) << block
      end
    end

    # Sets autoloads in the root namespace and preloads files, if any.
    #
    # @sig () -> void
    def setup
      mutex.synchronize do
        break if @setup

        actual_root_dirs.each do |root_dir, namespace|
          set_autoloads_in_dir(root_dir, namespace)
        end
        do_preload

        @setup = true
      end
    end

    # Removes loaded constants and configured autoloads.
    #
    # The objects the constants stored are no longer reachable through them. In
    # addition, since said objects are normally not referenced from anywhere
    # else, they are eligible for garbage collection, which would effectively
    # unload them.
    #
    # @private
    # @sig () -> void
    def unload
      mutex.synchronize do
        # We are going to keep track of the files that were required by our
        # autoloads to later remove them from $LOADED_FEATURES, thus making them
        # loadable by Kernel#require again.
        #
        # Directories are not stored in $LOADED_FEATURES, keeping track of files
        # is enough.
        unloaded_files = Set.new

        autoloads.each do |realpath, (parent, cname)|
          if parent.autoload?(cname)
            unload_autoload(parent, cname)
          else
            # Could happen if loaded with require_relative. That is unsupported,
            # and the constant path would escape unloadable_cpath? This is just
            # defensive code to clean things up as much as we are able to.
            unload_cref(parent, cname)   if cdef?(parent, cname)
            unloaded_files.add(realpath) if ruby?(realpath)
          end
        end

        to_unload.each_value do |(realpath, (parent, cname))|
          unload_cref(parent, cname)   if cdef?(parent, cname)
          unloaded_files.add(realpath) if ruby?(realpath)
        end

        unless unloaded_files.empty?
          # Bootsnap decorates Kernel#require to speed it up using a cache and
          # this optimization does not check if $LOADED_FEATURES has the file.
          #
          # To make it aware of changes, the gem defines singleton methods in
          # $LOADED_FEATURES:
          #
          #   https://github.com/Shopify/bootsnap/blob/master/lib/bootsnap/load_path_cache/core_ext/loaded_features.rb
          #
          # Rails applications may depend on bootsnap, so for unloading to work
          # in that setting it is preferable that we restrict our API choice to
          # one of those methods.
          $LOADED_FEATURES.reject! { |file| unloaded_files.member?(file) }
        end

        autoloads.clear
        autoloaded_dirs.clear
        to_unload.clear
        lazy_subdirs.clear

        Registry.on_unload(self)
        ExplicitNamespace.unregister(self)

        @setup        = false
        @eager_loaded = false
      end
    end

    # Unloads all loaded code, and calls setup again so that the loader is able
    # to pick any changes in the file system.
    #
    # This method is not thread-safe, please see how this can be achieved by
    # client code in the README of the project.
    #
    # @raise [Zeitwerk::Error]
    # @sig () -> void
    def reload
      if reloading_enabled?
        unload
        recompute_ignored_paths
        recompute_collapse_dirs
        setup
      else
        raise ReloadingDisabledError, "can't reload, please call loader.enable_reloading before setup"
      end
    end

    # Eager loads all files in the root directories, recursively. Files do not
    # need to be in `$LOAD_PATH`, absolute file names are used. Ignored files
    # are not eager loaded. You can opt-out specifically in specific files and
    # directories with `do_not_eager_load`.
    #
    # @sig () -> void
    def eager_load
      mutex.synchronize do
        break if @eager_loaded

        queue = []
        actual_root_dirs.each do |root_dir, namespace|
          queue << [namespace, root_dir] unless eager_load_exclusions.member?(root_dir)
        end

        while to_eager_load = queue.shift
          namespace, dir = to_eager_load

          ls(dir) do |basename, abspath|
            next if eager_load_exclusions.member?(abspath)

            if ruby?(abspath)
              if cref = autoloads[File.realpath(abspath)]
                cref[0].const_get(cref[1], false)
              end
            elsif dir?(abspath) && !root_dirs.key?(abspath)
              if collapse_dirs.member?(abspath)
                queue << [namespace, abspath]
              else
                cname = inflector.camelize(basename, abspath)
                queue << [namespace.const_get(cname, false), abspath]
              end
            end
          end
        end

        autoloaded_dirs.each do |autoloaded_dir|
          Registry.unregister_autoload(autoloaded_dir)
        end
        autoloaded_dirs.clear

        @eager_loaded = true
      end
    end

    # Let eager load ignore the given files or directories. The constants
    # defined in those files are still autoloadable.
    #
    # @sig (*(String | Pathname | Array[String | Pathname])) -> void
    def do_not_eager_load(*paths)
      mutex.synchronize { eager_load_exclusions.merge(expand_paths(paths)) }
    end

    # Says if the given constant path would be unloaded on reload. This
    # predicate returns `false` if reloading is disabled.
    #
    # @sig (String) -> bool
    def unloadable_cpath?(cpath)
      to_unload.key?(cpath)
    end

    # Returns an array with the constant paths that would be unloaded on reload.
    # This predicate returns an empty array if reloading is disabled.
    #
    # @sig () -> Array[String]
    def unloadable_cpaths
      to_unload.keys.freeze
    end

    # Logs to `$stdout`, handy shortcut for debugging.
    #
    # @sig () -> void
    def log!
      @logger = ->(msg) { puts msg }
    end

    # @private
    # @sig (String) -> bool
    def manages?(dir)
      dir = dir + "/"
      ignored_paths.each do |ignored_path|
        return false if dir.start_with?(ignored_path + "/")
      end

      root_dirs.each_key do |root_dir|
        return true if root_dir.start_with?(dir) || dir.start_with?(root_dir + "/")
      end

      false
    end

    # --- Class methods ---------------------------------------------------------------------------

    class << self
      # @sig #call | #debug | nil
      attr_accessor :default_logger

      # @private
      # @sig Mutex
      attr_accessor :mutex

      # This is a shortcut for
      #
      #   require "zeitwerk"
      #   loader = Zeitwerk::Loader.new
      #   loader.tag = File.basename(__FILE__, ".rb")
      #   loader.inflector = Zeitwerk::GemInflector.new(__FILE__)
      #   loader.push_dir(__dir__)
      #
      # except that this method returns the same object in subsequent calls from
      # the same file, in the unlikely case the gem wants to be able to reload.
      #
      # @sig () -> Zeitwerk::Loader
      def for_gem
        called_from = caller_locations(1, 1).first.path
        Registry.loader_for_gem(called_from)
      end

      # Broadcasts `eager_load` to all loaders.
      #
      # @sig () -> void
      def eager_load_all
        Registry.loaders.each(&:eager_load)
      end

      # Returns an array with the absolute paths of the root directories of all
      # registered loaders. This is a read-only collection.
      #
      # @sig () -> Array[String]
      def all_dirs
        Registry.loaders.flat_map(&:dirs).freeze
      end
    end

    self.mutex = Mutex.new

    private # -------------------------------------------------------------------------------------

    # @sig () -> Array[String]
    def actual_root_dirs
      root_dirs.reject do |root_dir, _namespace|
        !dir?(root_dir) || ignored_paths.member?(root_dir)
      end
    end

    # @sig (String, Module) -> void
    def set_autoloads_in_dir(dir, parent)
      ls(dir) do |basename, abspath|
        begin
          if ruby?(basename)
            basename[-3..-1] = ''
            cname = inflector.camelize(basename, abspath).to_sym
            autoload_file(parent, cname, abspath)
          elsif dir?(abspath)
            # In a Rails application, `app/models/concerns` is a subdirectory of
            # `app/models`, but both of them are root directories.
            #
            # To resolve the ambiguity file name -> constant path this introduces,
            # the `app/models/concerns` directory is totally ignored as a namespace,
            # it counts only as root. The guard checks that.
            unless root_dirs.key?(abspath)
              cname = inflector.camelize(basename, abspath).to_sym
              if collapse_dirs.member?(abspath)
                set_autoloads_in_dir(abspath, parent)
              else
                autoload_subdir(parent, cname, abspath)
              end
            end
          end
        rescue ::NameError => error
          path_type = ruby?(abspath) ? "file" : "directory"

          raise NameError.new(<<~MESSAGE, error.name)
            #{error.message} inferred by #{inflector.class} from #{path_type}

              #{abspath}

            Possible ways to address this:

              * Tell Zeitwerk to ignore this particular #{path_type}.
              * Tell Zeitwerk to ignore one of its parent directories.
              * Rename the #{path_type} to comply with the naming conventions.
              * Modify the inflector to handle this case.
          MESSAGE
        end
      end
    end

    # @sig (Module, Symbol, String) -> void
    def autoload_subdir(parent, cname, subdir)
      if autoload_path = autoload_for?(parent, cname)
        cpath = cpath(parent, cname)
        register_explicit_namespace(cpath) if ruby?(autoload_path)
        # We do not need to issue another autoload, the existing one is enough
        # no matter if it is for a file or a directory. Just remember the
        # subdirectory has to be visited if the namespace is used.
        (lazy_subdirs[cpath] ||= []) << subdir
      elsif !cdef?(parent, cname)
        # First time we find this namespace, set an autoload for it.
        (lazy_subdirs[cpath(parent, cname)] ||= []) << subdir
        set_autoload(parent, cname, subdir)
      else
        # For whatever reason the constant that corresponds to this namespace has
        # already been defined, we have to recurse.
        set_autoloads_in_dir(subdir, parent.const_get(cname))
      end
    end

    # @sig (Module, Symbol, String) -> void
    def autoload_file(parent, cname, file)
      if autoload_path = autoload_for?(parent, cname)
        # First autoload for a Ruby file wins, just ignore subsequent ones.
        if ruby?(autoload_path)
          log("file #{file} is ignored because #{autoload_path} has precedence") if logger
        else
          promote_namespace_from_implicit_to_explicit(
            dir:    autoload_path,
            file:   file,
            parent: parent,
            cname:  cname
          )
        end
      elsif cdef?(parent, cname)
        log("file #{file} is ignored because #{cpath(parent, cname)} is already defined") if logger
      else
        set_autoload(parent, cname, file)
      end
    end

    # `dir` is the directory that would have autovivified a namespace. `file` is
    # the file where we've found the namespace is explicitly defined.
    #
    # @sig (dir: String, file: String, parent: Module, cname: Symbol) -> void
    def promote_namespace_from_implicit_to_explicit(dir:, file:, parent:, cname:)
      autoloads.delete(dir)
      Registry.unregister_autoload(dir)

      set_autoload(parent, cname, file)
      register_explicit_namespace(cpath(parent, cname))
    end

    # @sig (Module, Symbol, String) -> void
    def set_autoload(parent, cname, abspath)
      # $LOADED_FEATURES stores real paths since Ruby 2.4.4. We set and save the
      # real path to be able to delete it from $LOADED_FEATURES on unload, and to
      # be able to do a lookup later in Kernel#require for manual require calls.
      #
      # We freeze realpath because that saves allocations in Module#autoload.
      # See #125.
      realpath = File.realpath(abspath).freeze
      parent.autoload(cname, realpath)
      if logger
        if ruby?(realpath)
          log("autoload set for #{cpath(parent, cname)}, to be loaded from #{realpath}")
        else
          log("autoload set for #{cpath(parent, cname)}, to be autovivified from #{realpath}")
        end
      end

      autoloads[realpath] = [parent, cname]
      Registry.register_autoload(self, realpath)

      # See why in the documentation of Zeitwerk::Registry.inceptions.
      unless parent.autoload?(cname)
        Registry.register_inception(cpath(parent, cname), realpath, self)
      end
    end

    # @sig (Module, Symbol) -> String?
    def autoload_for?(parent, cname)
      strict_autoload_path(parent, cname) || Registry.inception?(cpath(parent, cname))
    end

    # The autoload? predicate takes into account the ancestor chain of the
    # receiver, like const_defined? and other methods in the constants API do.
    #
    # For example, given
    #
    #   class A
    #     autoload :X, "x.rb"
    #   end
    #
    #   class B < A
    #   end
    #
    # B.autoload?(:X) returns "x.rb".
    #
    # We need a way to strictly check in parent ignoring ancestors.
    #
    # @sig (Module, Symbol) -> String?
    if method(:autoload?).arity == 1
      def strict_autoload_path(parent, cname)
        parent.autoload?(cname) if cdef?(parent, cname)
      end
    else
      def strict_autoload_path(parent, cname)
        parent.autoload?(cname, false)
      end
    end

    # This method is called this way because I prefer `preload` to be the method
    # name to configure preloads in the public interface.
    #
    # @sig () -> void
    def do_preload
      preloads.each do |abspath|
        do_preload_abspath(abspath)
      end
    end

    # @sig (String) -> void
    def do_preload_abspath(abspath)
      if ruby?(abspath)
        do_preload_file(abspath)
      elsif dir?(abspath)
        do_preload_dir(abspath)
      end
    end

    # @sig (String) -> void
    def do_preload_dir(dir)
      ls(dir) do |_basename, abspath|
        do_preload_abspath(abspath)
      end
    end

    # @sig (String) -> bool
    def do_preload_file(file)
      log("preloading #{file}") if logger
      require file
    end

    # @sig (Module, Symbol) -> String
    def cpath(parent, cname)
      parent.equal?(Object) ? cname.to_s : "#{real_mod_name(parent)}::#{cname}"
    end

    # @sig (String) { (String, String) -> void } -> void
    def ls(dir)
      Dir.foreach(dir) do |basename|
        next if basename.start_with?(".")

        abspath = File.join(dir, basename)
        next if ignored_paths.member?(abspath)

        # We freeze abspath because that saves allocations when passed later to
        # File methods. See #125.
        yield basename, abspath.freeze
      end
    end

    # @sig (String) -> bool
    def ruby?(path)
      path.end_with?(".rb")
    end

    # @sig (String) -> bool
    def dir?(path)
      File.directory?(path)
    end

    # @sig (String | Pathname | Array[String | Pathname]) -> Array[String]
    def expand_paths(paths)
      paths.flatten.map! { |path| File.expand_path(path) }
    end

    # @sig (Array[String]) -> Array[String]
    def expand_glob_patterns(glob_patterns)
      # Note that Dir.glob works with regular file names just fine. That is,
      # glob patterns technically need no wildcards.
      glob_patterns.flat_map { |glob_pattern| Dir.glob(glob_pattern) }
    end

    # @sig () -> void
    def recompute_ignored_paths
      ignored_paths.replace(expand_glob_patterns(ignored_glob_patterns))
    end

    # @sig () -> void
    def recompute_collapse_dirs
      collapse_dirs.replace(expand_glob_patterns(collapse_glob_patterns))
    end

    # @sig (String) -> void
    def log(message)
      method_name = logger.respond_to?(:debug) ? :debug : :call
      logger.send(method_name, "Zeitwerk@#{tag}: #{message}")
    end

    # @sig (Module, Symbol) -> bool
    def cdef?(parent, cname)
      parent.const_defined?(cname, false)
    end

    # @sig (String) -> void
    def register_explicit_namespace(cpath)
      ExplicitNamespace.register(cpath, self)
    end

    # @sig (String) -> void
    def raise_if_conflicting_directory(dir)
      self.class.mutex.synchronize do
        Registry.loaders.each do |loader|
          if loader != self && loader.manages?(dir)
            require "pp"
            raise Error,
              "loader\n\n#{pretty_inspect}\n\nwants to manage directory #{dir}," \
              " which is already managed by\n\n#{loader.pretty_inspect}\n"
            EOS
          end
        end
      end
    end

    # @sig (Module, Symbol) -> void
    def unload_autoload(parent, cname)
      parent.__send__(:remove_const, cname)
      log("autoload for #{cpath(parent, cname)} removed") if logger
    end

    # @sig (Module, Symbol) -> void
    def unload_cref(parent, cname)
      parent.__send__(:remove_const, cname)
      log("#{cpath(parent, cname)} unloaded") if logger
    end
  end
end
