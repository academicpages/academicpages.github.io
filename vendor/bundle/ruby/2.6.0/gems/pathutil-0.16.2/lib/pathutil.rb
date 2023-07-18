# Frozen-string-literal: true
# Copyright: 2015 - 2017 Jordon Bedwell - MIT License
# Encoding: utf-8

require "pathutil/helpers"
require "forwardable/extended"
require "find"

class Pathutil
  attr_writer :encoding
  extend Forwardable::Extended
  extend Helpers

  # --
  # @note A lot of this class can be compatible with Pathname.
  # Initialize a new instance.
  # @return Pathutil
  # --
  def initialize(path)
    return @path = path if path.is_a?(String)
    return @path = path.to_path if path.respond_to?(:to_path)
    return @path = path.to_s
  end

  # --
  # Make a path relative.
  # --
  def relative
    return self if relative?
    self.class.new(strip_windows_drive.gsub(
      %r!\A(\\+|/+)!, ""
    ))
  end

  # --
  # Make a path absolute
  # --
  def absolute
    return self if absolute?
    self.class.new("/").join(
      @path
    )
  end

  # --
  # @see Pathname#cleanpath.
  # @note This is a wholesale rip and cleanup of Pathname#cleanpath
  # @return Pathutil
  # --
  def cleanpath(symlink = false)
    symlink ? conservative_cleanpath : aggressive_cleanpath
  end

  # --
  # @yield Pathutil
  # @note It will return all results that it finds across all ascending paths.
  # @example Pathutil.new("~/").expand_path.search_backwards(".bashrc") => [#<Pathutil:/home/user/.bashrc>]
  # Search backwards for a file (like Rakefile, _config.yml, opts.yml).
  # @return Enum
  # --
  def search_backwards(file, backwards: Float::INFINITY)
    ary = []

    ascend.with_index(1).each do |path, index|
      if index > backwards
        break

      else
        Dir.chdir path do
          if block_given?
            file = self.class.new(file)
            if yield(file)
              ary.push(
                file
              )
            end

          elsif File.exist?(file)
            ary.push(self.class.new(
              path.join(file)
            ))
          end
        end
      end
    end

    ary
  end

  # --
  # Read the file as a YAML file turning it into an object.
  # @see self.class.load_yaml as this a direct alias of that method.
  # @return Hash
  # --
  def read_yaml(throw_missing: false, **kwd)
    self.class.load_yaml(
      read, **kwd
    )

  rescue Errno::ENOENT
    throw_missing ? raise : (
      return {}
    )
  end

  # --
  # Read the file as a JSON file turning it into an object.
  # @see self.class.read_json as this is a direct alias of that method.
  # @return Hash
  # --
  def read_json(throw_missing: false)
    JSON.parse(
      read
    )

  rescue Errno::ENOENT
    throw_missing ? raise : (
      return {}
    )
  end

  # --
  # @note The blank part is intentionally left there so that you can rejoin.
  # Splits the path into all parts so that you can do step by step comparisons
  # @example Pathutil.new("/my/path").split_path # => ["", "my", "path"]
  # @return Array<String>
  # --
  def split_path
    @path.split(
      %r!\\+|/+!
    )
  end

  # --
  # @see `String#==` for more details.
  # A stricter version of `==` that also makes sure the object matches.
  # @return true|false
  # --
  def ===(other)
    other.is_a?(self.class) && @path == other
  end

  # --
  # @example Pathutil.new("/hello") >= Pathutil.new("/") # => true
  # @example Pathutil.new("/hello") >= Pathutil.new("/hello") # => true
  # Checks to see if a path falls within a path and deeper or is the other.
  # @return true|false
  # --
  def >=(other)
    mine, other = expanded_paths(other)
    return true if other == mine
    mine.in_path?(other)
  end

  # --
  # @example Pathutil.new("/hello/world") > Pathutil.new("/hello") # => true
  # Strictly checks to see if a path is deeper but within the path of the other.
  # @return true|false
  # --
  def >(other)
    mine, other = expanded_paths(other)
    return false if other == mine
    mine.in_path?(other)
  end

  # --
  # @example Pathutil.new("/") < Pathutil.new("/hello") # => true
  # Strictly check to see if a path is behind other path but within it.
  # @return true|false
  # --
  def <(other)
    mine, other = expanded_paths(other)
    return false if other == mine
    other.in_path?(mine)
  end

  # --
  # Check to see if a path is behind the other path but within it.
  # @example Pathutil.new("/hello") < Pathutil.new("/hello") # => true
  # @example Pathutil.new("/") < Pathutil.new("/hello") # => true
  # @return true|false
  # --
  def <=(other)
    mine, other = expanded_paths(other)
    return true if other == mine
    other.in_path?(mine)
  end

  # --
  # @note "./" is considered relative.
  # Check to see if the path is absolute, as in: starts with "/"
  # @return true|false
  # --
  def absolute?
    return !!(
      @path =~ %r!\A(?:[A-Za-z]:)?(?:\\+|/+)!
    )
  end

  # --
  # @yield Pathutil
  # Break apart the path and yield each with the previous parts.
  # @example Pathutil.new("/hello/world").ascend.to_a # => ["/", "/hello", "/hello/world"]
  # @example Pathutil.new("/hello/world").ascend { |path| $stdout.puts path }
  # @return Enum
  # --
  def ascend
    unless block_given?
      return to_enum(
        __method__
      )
    end

    yield(
      path = self
    )

    while (new_path = path.dirname)
      if path == new_path || new_path == "."
        break
      else
        path = new_path
        yield  new_path
      end
    end

    nil
  end

  # --
  # @yield Pathutil
  # Break apart the path in reverse order and descend into the path.
  # @example Pathutil.new("/hello/world").descend.to_a # => ["/hello/world", "/hello", "/"]
  # @example Pathutil.new("/hello/world").descend { |path| $stdout.puts path }
  # @return Enum
  # --
  def descend
    unless block_given?
      return to_enum(
        __method__
      )
    end

    ascend.to_a.reverse_each do |val|
      yield val
    end

    nil
  end

  # --
  # @yield Pathutil
  # @example Pathutil.new("/hello/world").each_line { |line| $stdout.puts line }
  # Wraps `readlines` and allows you to yield on the result.
  # @return Enum
  # --
  def each_line
    return to_enum(__method__) unless block_given?
    readlines.each do |line|
      yield line
    end

    nil
  end

  # --
  # @example Pathutil.new("/hello").fnmatch?("/hello") # => true
  # Unlike traditional `fnmatch`, with this one `Regexp` is allowed.
  # @example Pathutil.new("/hello").fnmatch?(/h/) # => true
  # @see `File#fnmatch` for more information.
  # @return true|false
  # --
  def fnmatch?(matcher)
    matcher.is_a?(Regexp) ? !!(self =~ matcher) : \
      File.fnmatch(matcher, self)
  end

  # --
  # Allows you to quickly determine if the file is the root folder.
  # @return true|false
  # --
  def root?
    !!(self =~ %r!\A(?:[A-Za-z]:)?(?:\\+|/+)\z!)
  end

  # --
  # Allows you to check if the current path is in the path you want.
  # @return true|false
  # --
  def in_path?(path)
    path = self.class.new(path).expand_path.split_path
    mine = (symlink?? expand_path.realpath : expand_path).split_path
    path.each_with_index { |part, index| return false if mine[index] != part }
    true
  end

  # --
  def inspect
    "#<#{self.class}:#{@path}>"
  end

  # --
  # @return Array<Pathutil>
  # Grab all of the children from the current directory, including hidden.
  # @yield Pathutil
  # --
  def children
    ary = []

    Dir.foreach(@path) do |path|
      if path == "." || path == ".."
        next
      else
        path = self.class.new(File.join(@path, path))
        yield path if block_given?
        ary.push(
          path
        )
      end
    end

    ary
  end

  # --
  # @yield Pathutil
  # Allows you to glob however you wish to glob in the current `Pathutil`
  # @see `File::Constants` for a list of flags.
  # @return Enum
  # --
  def glob(pattern, flags = 0)
    unless block_given?
      return to_enum(
        __method__, pattern, flags
      )
    end

    chdir do
      Dir.glob(pattern, flags).each do |file|
        yield self.class.new(
          File.join(@path, file)
        )
      end
    end

    nil
  end

  # --
  # @yield &block
  # Move to the current directory temporarily (or for good) and do work son.
  # @note you do not need to ship a block at all.
  # @return nil
  # --
  def chdir
    if !block_given?
      Dir.chdir(
        @path
      )

    else
      Dir.chdir @path do
        yield
      end
    end
  end

  # --
  # @yield Pathutil
  # Find all files without care and yield the given block.
  # @return Enum
  # --
  def find
    return to_enum(__method__) unless block_given?
    Find.find @path do |val|
      yield self.class.new(val)
    end
  end

  # --
  # @yield Pathutil
  # Splits the path returning each part (filename) back to you.
  # @return Enum
  # --
  def each_filename
    return to_enum(__method__) unless block_given?
    @path.split(File::SEPARATOR).delete_if(&:empty?).each do |file|
      yield file
    end
  end

  # --
  # Get the parent of the current path.
  # @note This will simply return self if "/".
  # @return Pathutil
  # --
  def parent
    return self if @path == "/"
    self.class.new(absolute?? File.dirname(@path) : File.join(
      @path, ".."
    ))
  end

  # --
  # @yield Pathutil
  # Split the file into its dirname and basename, so you can do stuff.
  # @return nil
  # --
  def split
    File.split(@path).collect! do |path|
      self.class.new(path)
    end
  end

  # --
  # @note Your extension should start with "."
  # Replace a files extension with your given extension.
  # @return Pathutil
  # --
  def sub_ext(ext)
    self.class.new(@path.chomp(File.extname(@path)) + ext)
  end

  # --
  # A less complex version of `relative_path_from` that simply uses a
  # `Regexp` and returns the full path if it cannot be determined.
  # @return Pathutil
  # --
  def relative_path_from(from)
    from = self.class.new(from).expand_path.gsub(%r!/$!, "")
    self.class.new(expand_path.gsub(%r!^#{
      from.regexp_escape
    }/!, ""))
  end

  # --
  # Expands the path and left joins the root to the path.
  # @return Pathutil
  # --
  def enforce_root(root)
    return self if !relative? && in_path?(root)
    self.class.new(root).join(
      self
    )
  end

  # --
  # Copy a directory, allowing symlinks if the link falls inside of the root.
  # This is indented for people who wish some safety to their copies.
  # @note Ignore is ignored on safe_copy file because it's explicit.
  # @return nil
  # --
  def safe_copy(to, root: nil, ignore: [])
    raise ArgumentError, "must give a root" unless root
    root = self.class.new(root)
    to   = self.class.new(to)

    if directory?
      safe_copy_directory(to, {
        :root => root, :ignore => ignore
      })

    else
      safe_copy_file(to, {
        :root => root
      })
    end
  end

  # --
  # @see `self.class.normalize` as this is an alias.
  # --
  def normalize
    return @normalize ||= begin
      self.class.normalize
    end
  end

  # --
  # @see `self.class.encoding` as this is an alias.
  # --
  def encoding
    return @encoding ||= begin
      self.class.encoding
    end
  end

  # --
  # @note You can set the default encodings via the class.
  # Read took two steroid shots: it can normalize your string, and encode.
  # @return String
  # --
  def read(*args, **kwd)
    kwd[:encoding] ||= encoding

    if normalize[:read]
      File.read(self, *args, kwd).encode({
        :universal_newline => true
      })

    else
      File.read(
        self, *args, kwd
      )
    end
  end

  # --
  # @note You can set the default encodings via the class.
  # Binread took two steroid shots: it can normalize your string, and encode.
  # @return String
  # --
  def binread(*args, **kwd)
    kwd[:encoding] ||= encoding

    if normalize[:read]
      File.binread(self, *args, kwd).encode({
        :universal_newline => true
      })

    else
      File.read(
        self, *args, kwd
      )
    end
  end

  # --
  # @note You can set the default encodings via the class.
  # Readlines took two steroid shots: it can normalize your string, and encode.
  # @return Array<String>
  # --
  def readlines(*args, **kwd)
    kwd[:encoding] ||= encoding

    if normalize[:read]
      File.readlines(self, *args, kwd).encode({
        :universal_newline => true
      })

    else
      File.readlines(
        self, *args, kwd
      )
    end
  end

  # --
  # @note You can set the default encodings via the class.
  # Write took two steroid shots: it can normalize your string, and encode.
  # @return Fixnum<Bytes>
  # --
  def write(data, *args, **kwd)
    kwd[:encoding] ||= encoding

    if normalize[:write]
      File.write(self, data.encode(
        :crlf_newline => true
      ), *args, kwd)

    else
      File.write(
        self, data, *args, kwd
      )
    end
  end

  # --
  # @note You can set the default encodings via the class.
  # Binwrite took two steroid shots: it can normalize your string, and encode.
  # @return Fixnum<Bytes>
  # --
  def binwrite(data, *args, **kwd)
    kwd[:encoding] ||= encoding

    if normalize[:write]
      File.binwrite(self, data.encode(
        :crlf_newline => true
      ), *args, kwd)

    else
      File.binwrite(
        self, data, *args, kwd
      )
    end
  end

  # --
  def to_regexp(guard: true)
    Regexp.new((guard ? "\\A" : "") + Regexp.escape(
      self
    ))
  end

  # --
  # Strips the windows drive from the path.
  # --
  def strip_windows_drive(path = @path)
    self.class.new(path.gsub(
      %r!\A[A-Za-z]:(?:\\+|/+)!, ""
    ))
  end

  # --
  # rubocop:disable Metrics/AbcSize
  # rubocop:disable Metrics/CyclomaticComplexity
  # rubocop:disable Metrics/PerceivedComplexity
  # --

  def aggressive_cleanpath
    return self.class.new("/") if root?

    _out = split_path.each_with_object([]) do |part, out|
      next if part == "." || (part == ".." && out.last == "")
      if part == ".." && out.last && out.last != ".."
        out.pop

      else
        out.push(
          part
        )
      end
    end

    # --

    return self.class.new("/") if _out == [""].freeze
    return self.class.new(".") if _out.empty? && (end_with?(".") || relative?)
    self.class.new(_out.join("/"))
  end

  # --
  def conservative_cleanpath
    _out = split_path.each_with_object([]) do |part, out|
      next if part == "." || (part == ".." && out.last == "")
      out.push(
        part
      )
    end

    # --

    if !_out.empty? && basename == "." && _out.last != "" && _out.last != ".."
      _out << "."
    end

    # --

    return self.class.new("/") if _out == [""].freeze
    return self.class.new(".") if _out.empty? && (end_with?(".") || relative?)
    return self.class.new(_out.join("/")).join("") if @path =~ %r!/\z! \
      && _out.last != "." && _out.last != ".."
    self.class.new(_out.join("/"))
  end

  # --
  # rubocop:enable Metrics/AbcSize
  # rubocop:enable Metrics/CyclomaticComplexity
  # rubocop:enable Metrics/PerceivedComplexity
  # Expand the paths and return.
  # --
  private
  def expanded_paths(path)
    return expand_path, self.class.new(path).expand_path
  end

  # --
  # Safely copy a file.
  # --
  private
  def safe_copy_file(to, root: nil)
    raise Errno::EPERM, "#{self} not in #{root}" unless in_path?(root)
    FileUtils.cp(self, to, {
      :preserve => true
    })
  end

  # --
  # Safely copy a directory and it's sub-files.
  # --
  private
  def safe_copy_directory(to, root: nil, ignore: [])
    ignore = [ignore].flatten.uniq

    if !in_path?(root)
      raise Errno::EPERM, "#{self} not in #{
        root
      }"

    else
      to.mkdir_p unless to.exist?
      children do |file|
        unless ignore.any? { |path| file.in_path?(path) }
          if !file.in_path?(root)
            raise Errno::EPERM, "#{file} not in #{
              root
            }"

          elsif file.file?
            FileUtils.cp(file, to, {
              :preserve => true
            })

          else
            path = file.realpath
            path.safe_copy(to.join(file.basename), {
              :root => root, :ignore => ignore
            })
          end
        end
      end
    end
  end

  class << self
    attr_writer :encoding

    # --
    # @note We do nothing special here.
    # Get the current directory that Ruby knows about.
    # @return Pathutil
    # --
    def pwd
      new(
        Dir.pwd
      )
    end

    alias gcwd pwd
    alias cwd  pwd

    # --
    # @note you are encouraged to override this if you need to.
    # Aliases the default system encoding to us so that we can do most read
    # and write operations with that encoding, instead of being crazy.
    # --
    def encoding
      return @encoding ||= begin
        Encoding.default_external
      end
    end

    # --
    # Normalize CRLF -> LF   on Windows reads, to ease  your troubles.
    # Normalize LF   -> CLRF on Windows write, to ease  your troubles.
    # --
    def normalize
      return @normalize ||= {
        :read  => Gem.win_platform?,
        :write => Gem.win_platform?
      }
    end

    # --
    # Make a temporary directory.
    # @note if you adruptly exit it will not remove the dir.
    # @note this directory is removed on exit.
    # @return Pathutil
    # --
    def tmpdir(*args)
      rtn = new(make_tmpname(*args)).tap(&:mkdir)
      ObjectSpace.define_finalizer(rtn, proc do
        rtn.rm_rf
      end)

      rtn
    end

    # --
    # Make a temporary file.
    # @note if you adruptly exit it will not remove the dir.
    # @note this file is removed on exit.
    # @return Pathutil
    # --
    def tmpfile(*args)
      rtn = new(make_tmpname(*args)).tap(&:touch)
      ObjectSpace.define_finalizer(rtn, proc do
        rtn.rm_rf
      end)

      rtn
    end
  end

  # --

  rb_delegate :gcwd, :to => :"self.class"
  rb_delegate :pwd,  :to => :"self.class"

  # --

  rb_delegate :sub,         :to => :@path, :wrap => true
  rb_delegate :chomp,       :to => :@path, :wrap => true
  rb_delegate :gsub,        :to => :@path, :wrap => true
  rb_delegate :[],          :to => :@path
  rb_delegate :=~,          :to => :@path
  rb_delegate :==,          :to => :@path
  rb_delegate :to_s,        :to => :@path
  rb_delegate :freeze,      :to => :@path
  rb_delegate :end_with?,   :to => :@path
  rb_delegate :start_with?, :to => :@path
  rb_delegate :frozen?,     :to => :@path
  rb_delegate :to_str,      :to => :@path
  rb_delegate :"!~",        :to => :@path
  rb_delegate :<=>,         :to => :@path

  # --

  rb_delegate :chmod,        :to => :File, :args => { :after => :@path }
  rb_delegate :lchown,       :to => :File, :args => { :after => :@path }
  rb_delegate :lchmod,       :to => :File, :args => { :after => :@path }
  rb_delegate :chown,        :to => :File, :args => { :after => :@path }
  rb_delegate :basename,     :to => :File, :args => :@path, :wrap => true
  rb_delegate :dirname,      :to => :File, :args => :@path, :wrap => true
  rb_delegate :readlink,     :to => :File, :args => :@path, :wrap => true
  rb_delegate :expand_path,  :to => :File, :args => :@path, :wrap => true
  rb_delegate :realdirpath,  :to => :File, :args => :@path, :wrap => true
  rb_delegate :realpath,     :to => :File, :args => :@path, :wrap => true
  rb_delegate :rename,       :to => :File, :args => :@path, :wrap => true
  rb_delegate :join,         :to => :File, :args => :@path, :wrap => true
  rb_delegate :empty?,       :to => :file, :args => :@path
  rb_delegate :size,         :to => :File, :args => :@path
  rb_delegate :link,         :to => :File, :args => :@path
  rb_delegate :atime,        :to => :File, :args => :@path
  rb_delegate :ctime,        :to => :File, :args => :@path
  rb_delegate :lstat,        :to => :File, :args => :@path
  rb_delegate :utime,        :to => :File, :args => :@path
  rb_delegate :sysopen,      :to => :File, :args => :@path
  rb_delegate :birthtime,    :to => :File, :args => :@path
  rb_delegate :mountpoint?,  :to => :File, :args => :@path
  rb_delegate :truncate,     :to => :File, :args => :@path
  rb_delegate :symlink,      :to => :File, :args => :@path
  rb_delegate :extname,      :to => :File, :args => :@path
  rb_delegate :zero?,        :to => :File, :args => :@path
  rb_delegate :ftype,        :to => :File, :args => :@path
  rb_delegate :mtime,        :to => :File, :args => :@path
  rb_delegate :open,         :to => :File, :args => :@path
  rb_delegate :stat,         :to => :File, :args => :@path

  # --

  rb_delegate :pipe?,            :to => :FileTest, :args => :@path
  rb_delegate :file?,            :to => :FileTest, :args => :@path
  rb_delegate :owned?,           :to => :FileTest, :args => :@path
  rb_delegate :setgid?,          :to => :FileTest, :args => :@path
  rb_delegate :socket?,          :to => :FileTest, :args => :@path
  rb_delegate :readable?,        :to => :FileTest, :args => :@path
  rb_delegate :blockdev?,        :to => :FileTest, :args => :@path
  rb_delegate :directory?,       :to => :FileTest, :args => :@path
  rb_delegate :readable_real?,   :to => :FileTest, :args => :@path
  rb_delegate :world_readable?,  :to => :FileTest, :args => :@path
  rb_delegate :executable_real?, :to => :FileTest, :args => :@path
  rb_delegate :world_writable?,  :to => :FileTest, :args => :@path
  rb_delegate :writable_real?,   :to => :FileTest, :args => :@path
  rb_delegate :executable?,      :to => :FileTest, :args => :@path
  rb_delegate :writable?,        :to => :FileTest, :args => :@path
  rb_delegate :grpowned?,        :to => :FileTest, :args => :@path
  rb_delegate :chardev?,         :to => :FileTest, :args => :@path
  rb_delegate :symlink?,         :to => :FileTest, :args => :@path
  rb_delegate :sticky?,          :to => :FileTest, :args => :@path
  rb_delegate :setuid?,          :to => :FileTest, :args => :@path
  rb_delegate :exist?,           :to => :FileTest, :args => :@path
  rb_delegate :size?,            :to => :FileTest, :args => :@path

  # --

  rb_delegate :rm_rf,   :to => :FileUtils, :args => :@path
  rb_delegate :rm_r,    :to => :FileUtils, :args => :@path
  rb_delegate :rm_f,    :to => :FileUtils, :args => :@path
  rb_delegate :rm,      :to => :FileUtils, :args => :@path
  rb_delegate :cp_r,    :to => :FileUtils, :args => :@path
  rb_delegate :touch,   :to => :FileUtils, :args => :@path
  rb_delegate :mkdir_p, :to => :FileUtils, :args => :@path
  rb_delegate :mkpath,  :to => :FileUtils, :args => :@path
  rb_delegate :cp,      :to => :FileUtils, :args => :@path

  # --

  rb_delegate :each_child, :to => :children
  rb_delegate :each_entry, :to => :children
  rb_delegate :to_a,       :to => :children

  # --

  rb_delegate :opendir, :to => :Dir, :alias_of => :open
  rb_delegate :relative?, :to => :self, :alias_of => :absolute?, :bool => :reverse
  rb_delegate :regexp_escape, :to => :Regexp, :args => :@path, :alias_of => :escape
  rb_delegate :shellescape, :to => :Shellwords, :args => :@path
  rb_delegate :mkdir, :to => :Dir, :args => :@path

  # --

  alias + join
  alias delete rm
  alias rmtree rm_r
  alias to_path to_s
  alias last basename
  alias entries children
  alias make_symlink symlink
  alias cleanpath_conservative conservative_cleanpath
  alias cleanpath_aggressive aggressive_cleanpath
  alias prepend enforce_root
  alias fnmatch fnmatch?
  alias make_link link
  alias first dirname
  alias rmdir rm_r
  alias unlink rm
  alias / join
end
