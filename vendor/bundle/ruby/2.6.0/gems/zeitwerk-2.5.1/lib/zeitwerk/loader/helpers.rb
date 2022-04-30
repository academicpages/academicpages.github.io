# frozen_string_literal: true

module Zeitwerk::Loader::Helpers
  private

  # --- Logging -----------------------------------------------------------------------------------

  # @sig (String) -> void
  def log(message)
    method_name = logger.respond_to?(:debug) ? :debug : :call
    logger.send(method_name, "Zeitwerk@#{tag}: #{message}")
  end

  # --- Files and directories ---------------------------------------------------------------------

  # @sig (String) { (String, String) -> void } -> void
  def ls(dir)
    Dir.each_child(dir) do |basename|
      next if hidden?(basename)

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

  # @sig String -> bool
  def hidden?(basename)
    basename.start_with?(".")
  end

  # --- Constants ---------------------------------------------------------------------------------

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

  # @sig (Module, Symbol) -> String
  if Symbol.method_defined?(:name)
    # Symbol#name was introduced in Ruby 3.0. It returns always the same
    # frozen object, so we may save a few string allocations.
    def cpath(parent, cname)
      Object == parent ? cname.name : "#{real_mod_name(parent)}::#{cname.name}"
    end
  else
    def cpath(parent, cname)
      Object == parent ? cname.to_s : "#{real_mod_name(parent)}::#{cname}"
    end
  end

  # @sig (Module, Symbol) -> bool
  def cdef?(parent, cname)
    parent.const_defined?(cname, false)
  end

  # @raise [NameError]
  # @sig (Module, Symbol) -> Object
  def cget(parent, cname)
    parent.const_get(cname, false)
  end
end
