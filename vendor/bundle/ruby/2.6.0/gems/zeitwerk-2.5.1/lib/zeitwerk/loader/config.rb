# frozen_string_literal: true

require "set"
require "securerandom"

module Zeitwerk::Loader::Config
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

  # @sig #camelize
  attr_accessor :inflector

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

  # Absolute paths of files or directories not to be eager loaded.
  #
  # @private
  # @sig Set[String]
  attr_reader :eager_load_exclusions

  # User-oriented callbacks to be fired on setup and on reload.
  #
  # @private
  # @sig Array[{ () -> void }]
  attr_reader :on_setup_callbacks

  # User-oriented callbacks to be fired when a constant is loaded.
  #
  # @private
  # @sig Hash[String, Array[{ (Object, String) -> void }]]
  #      Hash[Symbol, Array[{ (String, Object, String) -> void }]]
  attr_reader :on_load_callbacks

  # User-oriented callbacks to be fired before constants are removed.
  #
  # @private
  # @sig Hash[String, Array[{ (Object, String) -> void }]]
  #      Hash[Symbol, Array[{ (String, Object, String) -> void }]]
  attr_reader :on_unload_callbacks

  # @sig #call | #debug | nil
  attr_accessor :logger

  def initialize
    @initialized_at         = Time.now
    @root_dirs              = {}
    @inflector              = Zeitwerk::Inflector.new
    @ignored_glob_patterns  = Set.new
    @ignored_paths          = Set.new
    @collapse_glob_patterns = Set.new
    @collapse_dirs          = Set.new
    @eager_load_exclusions  = Set.new
    @reloading_enabled      = false
    @on_setup_callbacks     = []
    @on_load_callbacks      = {}
    @on_unload_callbacks    = {}
    @logger                 = self.class.default_logger
    @tag                    = SecureRandom.hex(3)
  end

  # Pushes `path` to the list of root directories.
  #
  # Raises `Zeitwerk::Error` if `path` does not exist, or if another loader in
  # the same process already manages that directory or one of its ascendants or
  # descendants.
  #
  # @raise [Zeitwerk::Error]
  # @sig (String | Pathname, Module) -> void
  def push_dir(path, namespace: Object)
    # Note that Class < Module.
    unless namespace.is_a?(Module)
      raise Zeitwerk::Error, "#{namespace.inspect} is not a class or module object, should be"
    end

    abspath = File.expand_path(path)
    if dir?(abspath)
      raise_if_conflicting_directory(abspath)
      root_dirs[abspath] = namespace
    else
      raise Zeitwerk::Error, "the root directory #{abspath} does not exist"
    end
  end

  # Returns the loader's tag.
  #
  # Implemented as a method instead of via attr_reader for symmetry with the
  # writer below.
  #
  # @sig () -> String
  def tag
    @tag
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

  # You need to call this method before setup in order to be able to reload.
  # There is no way to undo this, either you want to reload or you don't.
  #
  # @raise [Zeitwerk::Error]
  # @sig () -> void
  def enable_reloading
    mutex.synchronize do
      break if @reloading_enabled

      if @setup
        raise Zeitwerk::Error, "cannot enable reloading after setup"
      else
        @reloading_enabled = true
      end
    end
  end

  # @sig () -> bool
  def reloading_enabled?
    @reloading_enabled
  end

  # Let eager load ignore the given files or directories. The constants defined
  # in those files are still autoloadable.
  #
  # @sig (*(String | Pathname | Array[String | Pathname])) -> void
  def do_not_eager_load(*paths)
    mutex.synchronize { eager_load_exclusions.merge(expand_paths(paths)) }
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

  # Configure a block to be called after setup and on each reload.
  # If setup was already done, the block runs immediately.
  #
  # @sig () { () -> void } -> void
  def on_setup(&block)
    mutex.synchronize do
      on_setup_callbacks << block
      block.call if @setup
    end
  end

  # Configure a block to be invoked once a certain constant path is loaded.
  # Supports multiple callbacks, and if there are many, they are executed in
  # the order in which they were defined.
  #
  #   loader.on_load("SomeApiClient") do |klass, _abspath|
  #     klass.endpoint = "https://api.dev"
  #   end
  #
  # Can also be configured for any constant loaded:
  #
  #   loader.on_load do |cpath, value, abspath|
  #     # ...
  #   end
  #
  # @raise [TypeError]
  # @sig (String) { (Object, String) -> void } -> void
  #      (:ANY) { (String, Object, String) -> void } -> void
  def on_load(cpath = :ANY, &block)
    raise TypeError, "on_load only accepts strings" unless cpath.is_a?(String) || cpath == :ANY

    mutex.synchronize do
      (on_load_callbacks[cpath] ||= []) << block
    end
  end

  # Configure a block to be invoked right before a certain constant is removed.
  # Supports multiple callbacks, and if there are many, they are executed in the
  # order in which they were defined.
  #
  #   loader.on_unload("Country") do |klass, _abspath|
  #     klass.clear_cache
  #   end
  #
  # Can also be configured for any removed constant:
  #
  #   loader.on_unload do |cpath, value, abspath|
  #     # ...
  #   end
  #
  # @raise [TypeError]
  # @sig (String) { (Object) -> void } -> void
  #      (:ANY) { (String, Object) -> void } -> void
  def on_unload(cpath = :ANY, &block)
    raise TypeError, "on_unload only accepts strings" unless cpath.is_a?(String) || cpath == :ANY

    mutex.synchronize do
      (on_unload_callbacks[cpath] ||= []) << block
    end
  end

  # Logs to `$stdout`, handy shortcut for debugging.
  #
  # @sig () -> void
  def log!
    @logger = ->(msg) { puts msg }
  end

  # @private
  # @sig (String) -> bool
  def ignores?(abspath)
    ignored_paths.any? do |ignored_path|
      ignored_path == abspath || (dir?(ignored_path) && abspath.start_with?(ignored_path + "/"))
    end
  end

  private

  # @sig () -> Array[String]
  def actual_root_dirs
    root_dirs.reject do |root_dir, _namespace|
      !dir?(root_dir) || ignored_paths.member?(root_dir)
    end
  end

  # @sig (String) -> bool
  def root_dir?(dir)
    root_dirs.key?(dir)
  end

  # @sig (String) -> bool
  def excluded_from_eager_load?(abspath)
    eager_load_exclusions.member?(abspath)
  end

  # @sig (String) -> bool
  def collapse?(dir)
    collapse_dirs.member?(dir)
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
end
