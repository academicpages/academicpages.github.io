# frozen_string_literal: true

require "set"

module Zeitwerk
  class Loader
    require_relative "loader/helpers"
    require_relative "loader/callbacks"
    require_relative "loader/config"

    include RealModName
    include Callbacks
    include Helpers
    include Config

    # Maps absolute paths for which an autoload has been set ---and not
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
    # The cpath as key helps implementing unloadable_cpath? The file name is
    # stored in order to be able to delete it from $LOADED_FEATURES, and the
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

    # @private
    # @sig Mutex
    attr_reader :mutex

    # @private
    # @sig Mutex
    attr_reader :mutex2

    def initialize
      super

      @autoloads       = {}
      @autoloaded_dirs = []
      @to_unload       = {}
      @lazy_subdirs    = Hash.new { |h, cpath| h[cpath] = [] }
      @mutex           = Mutex.new
      @mutex2          = Mutex.new
      @setup           = false
      @eager_loaded    = false

      Registry.register_loader(self)
    end

    # Sets autoloads in the root namespace.
    #
    # @sig () -> void
    def setup
      mutex.synchronize do
        break if @setup

        actual_root_dirs.each do |root_dir, namespace|
          set_autoloads_in_dir(root_dir, namespace)
        end

        on_setup_callbacks.each(&:call)

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
    # This method is public but undocumented. Main interface is `reload`, which
    # means `unload` + `setup`. This one is avaiable to be used together with
    # `unregister`, which is undocumented too.
    #
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

        autoloads.each do |abspath, (parent, cname)|
          if parent.autoload?(cname)
            unload_autoload(parent, cname)
          else
            # Could happen if loaded with require_relative. That is unsupported,
            # and the constant path would escape unloadable_cpath? This is just
            # defensive code to clean things up as much as we are able to.
            unload_cref(parent, cname)
            unloaded_files.add(abspath) if ruby?(abspath)
          end
        end

        to_unload.each do |cpath, (abspath, (parent, cname))|
          # We have to check cdef? in this condition. Reason is, constants whose
          # file does not define them have to be kept in to_unload as explained
          # in the implementation of on_file_autoloaded.
          #
          # If the constant is not defined, on_unload should not be triggered
          # for it.
          if !on_unload_callbacks.empty? && cdef?(parent, cname)
            value = parent.const_get(cname)
            run_on_unload_callbacks(cpath, value, abspath)
          end

          unload_cref(parent, cname)
          unloaded_files.add(abspath) if ruby?(abspath)
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
        ExplicitNamespace.unregister_loader(self)

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
    # directories with `do_not_eager_load`, and that can be overridden passing
    # `force: true`.
    #
    # @sig (true | false) -> void
    def eager_load(force: false)
      mutex.synchronize do
        break if @eager_loaded

        log("eager load start") if logger

        honour_exclusions = !force

        queue = []
        actual_root_dirs.each do |root_dir, namespace|
          queue << [namespace, root_dir] unless honour_exclusions && excluded_from_eager_load?(root_dir)
        end

        while to_eager_load = queue.shift
          namespace, dir = to_eager_load

          ls(dir) do |basename, abspath|
            next if honour_exclusions && excluded_from_eager_load?(abspath)

            if ruby?(abspath)
              if cref = autoloads[abspath]
                cget(*cref)
              end
            elsif dir?(abspath) && !root_dirs.key?(abspath)
              if collapse?(abspath)
                queue << [namespace, abspath]
              else
                cname = inflector.camelize(basename, abspath)
                queue << [cget(namespace, cname), abspath]
              end
            end
          end
        end

        autoloaded_dirs.each do |autoloaded_dir|
          Registry.unregister_autoload(autoloaded_dir)
        end
        autoloaded_dirs.clear

        @eager_loaded = true

        log("eager load end") if logger
      end
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

    # This is a dangerous method.
    #
    # @experimental
    # @sig () -> void
    def unregister
      Registry.unregister_loader(self)
      ExplicitNamespace.unregister_loader(self)
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

    # @sig (String, Module) -> void
    def set_autoloads_in_dir(dir, parent)
      ls(dir) do |basename, abspath|
        begin
          if ruby?(basename)
            basename.delete_suffix!(".rb")
            cname = inflector.camelize(basename, abspath).to_sym
            autoload_file(parent, cname, abspath)
          elsif dir?(abspath)
            # In a Rails application, `app/models/concerns` is a subdirectory of
            # `app/models`, but both of them are root directories.
            #
            # To resolve the ambiguity file name -> constant path this introduces,
            # the `app/models/concerns` directory is totally ignored as a namespace,
            # it counts only as root. The guard checks that.
            unless root_dir?(abspath)
              cname = inflector.camelize(basename, abspath).to_sym
              if collapse?(abspath)
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
      if autoload_path = autoload_path_set_by_me_for?(parent, cname)
        cpath = cpath(parent, cname)
        register_explicit_namespace(cpath) if ruby?(autoload_path)
        # We do not need to issue another autoload, the existing one is enough
        # no matter if it is for a file or a directory. Just remember the
        # subdirectory has to be visited if the namespace is used.
        lazy_subdirs[cpath] << subdir
      elsif !cdef?(parent, cname)
        # First time we find this namespace, set an autoload for it.
        lazy_subdirs[cpath(parent, cname)] << subdir
        set_autoload(parent, cname, subdir)
      else
        # For whatever reason the constant that corresponds to this namespace has
        # already been defined, we have to recurse.
        log("the namespace #{cpath(parent, cname)} already exists, descending into #{subdir}") if logger
        set_autoloads_in_dir(subdir, cget(parent, cname))
      end
    end

    # @sig (Module, Symbol, String) -> void
    def autoload_file(parent, cname, file)
      if autoload_path = strict_autoload_path(parent, cname) || Registry.inception?(cpath(parent, cname))
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

      log("earlier autoload for #{cpath(parent, cname)} discarded, it is actually an explicit namespace defined in #{file}") if logger

      set_autoload(parent, cname, file)
      register_explicit_namespace(cpath(parent, cname))
    end

    # @sig (Module, Symbol, String) -> void
    def set_autoload(parent, cname, abspath)
      parent.autoload(cname, abspath)

      if logger
        if ruby?(abspath)
          log("autoload set for #{cpath(parent, cname)}, to be loaded from #{abspath}")
        else
          log("autoload set for #{cpath(parent, cname)}, to be autovivified from #{abspath}")
        end
      end

      autoloads[abspath] = [parent, cname]
      Registry.register_autoload(self, abspath)

      # See why in the documentation of Zeitwerk::Registry.inceptions.
      unless parent.autoload?(cname)
        Registry.register_inception(cpath(parent, cname), abspath, self)
      end
    end

    # @sig (Module, Symbol) -> String?
    def autoload_path_set_by_me_for?(parent, cname)
      if autoload_path = strict_autoload_path(parent, cname)
        autoload_path if autoloads.key?(autoload_path)
      else
        Registry.inception?(cpath(parent, cname))
      end
    end

    # @sig (String) -> void
    def register_explicit_namespace(cpath)
      ExplicitNamespace.register(cpath, self)
    end

    # @sig (String) -> void
    def raise_if_conflicting_directory(dir)
      self.class.mutex.synchronize do
        Registry.loaders.each do |loader|
          next if loader == self
          next if loader.ignores?(dir)

          dir = dir + "/"
          loader.root_dirs.each do |root_dir, _namespace|
            next if ignores?(root_dir)

            root_dir = root_dir + "/"
            if dir.start_with?(root_dir) || root_dir.start_with?(dir)
              require "pp" # Needed for pretty_inspect, even in Ruby 2.5.
              raise Error,
                "loader\n\n#{pretty_inspect}\n\nwants to manage directory #{dir.chop}," \
                " which is already managed by\n\n#{loader.pretty_inspect}\n"
              EOS
            end
          end
        end
      end
    end

    # @sig (String, Object, String) -> void
    def run_on_unload_callbacks(cpath, value, abspath)
      # Order matters. If present, run the most specific one.
      on_unload_callbacks[cpath]&.each { |c| c.call(value, abspath) }
      on_unload_callbacks[:ANY]&.each { |c| c.call(cpath, value, abspath) }
    end

    # @sig (Module, Symbol) -> void
    def unload_autoload(parent, cname)
      parent.__send__(:remove_const, cname)
      log("autoload for #{cpath(parent, cname)} removed") if logger
    end

    # @sig (Module, Symbol) -> void
    def unload_cref(parent, cname)
      # Let's optimistically remove_const. The way we use it, this is going to
      # succeed always if all is good.
      parent.__send__(:remove_const, cname)
    rescue ::NameError
      # There are a few edge scenarios in which this may happen. If the constant
      # is gone, that is OK, anyway.
    else
      log("#{cpath(parent, cname)} unloaded") if logger
    end
  end
end
