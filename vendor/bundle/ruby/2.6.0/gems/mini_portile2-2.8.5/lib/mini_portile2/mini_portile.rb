require 'rbconfig'
require 'net/http'
require 'net/https'
require 'fileutils'
require 'tempfile'
require 'digest'
require 'open-uri'
require 'cgi'
require 'rbconfig'
require 'shellwords'

# Monkey patch for Net::HTTP by ruby open-uri fix:
# https://github.com/ruby/ruby/commit/58835a9
class Net::HTTP
  private
  remove_method(:edit_path)
  def edit_path(path)
    if proxy?
      if path.start_with?("ftp://") || use_ssl?
        path
      else
        "http://#{addr_port}#{path}"
      end
    else
      path
    end
  end
end

$MINI_PORTILE_STATIC_LIBS = {}

class MiniPortile
  DEFAULT_TIMEOUT = 10

  attr_reader :name, :version, :original_host, :source_directory
  attr_writer :configure_options
  attr_accessor :host, :files, :patch_files, :target, :logger

  def self.windows?
    target_os =~ /mswin|mingw/
  end

  # GNU MinGW compiled Ruby?
  def self.mingw?
    target_os =~ /mingw/
  end

  # MS Visual-C compiled Ruby?
  def self.mswin?
    target_os =~ /mswin/
  end

  def self.darwin?
    target_os =~ /darwin/
  end

  def self.freebsd?
    target_os =~ /freebsd/
  end

  def self.openbsd?
    target_os =~ /openbsd/
  end

  def self.linux?
    target_os =~ /linux/
  end

  def self.solaris?
    target_os =~ /solaris/
  end

  def self.target_os
    RbConfig::CONFIG['target_os']
  end

  def self.target_cpu
    RbConfig::CONFIG['target_cpu']
  end

  def self.native_path(path)
    path = File.expand_path(path)
    if File::ALT_SEPARATOR
      path.tr(File::SEPARATOR, File::ALT_SEPARATOR)
    else
      path
    end
  end

  def self.posix_path(path)
    path = File.expand_path(path)
    if File::ALT_SEPARATOR
      "/" + path.tr(File::ALT_SEPARATOR, File::SEPARATOR).tr(":", File::SEPARATOR)
    else
      path
    end
  end

  def initialize(name, version, **kwargs)
    @name = name
    @version = version
    @target = 'ports'
    @files = []
    @patch_files = []
    @log_files = {}
    @logger = STDOUT
    @source_directory = nil

    @gcc_command = kwargs[:gcc_command]
    @make_command = kwargs[:make_command]
    @open_timeout = kwargs[:open_timeout] || DEFAULT_TIMEOUT
    @read_timeout = kwargs[:read_timeout] || DEFAULT_TIMEOUT

    @original_host = @host = detect_host
  end

  def source_directory=(path)
    @source_directory = posix_path(path)
  end

  def prepare_build_directory
    raise "source_directory is not set" if source_directory.nil?
    output "Building #{@name} from source at '#{source_directory}'"
    FileUtils.mkdir_p(File.join(tmp_path, [name, version].join("-")))
    FileUtils.rm_rf(port_path) # make sure we always re-install
  end

  def download
    files_hashs.each do |file|
      download_file(file[:url], file[:local_path])
      verify_file(file)
    end
  end

  def extract
    files_hashs.each do |file|
      verify_file(file)
      extract_file(file[:local_path], tmp_path)
    end
  end

  def apply_patch(patch_file)
    (
      # Not a class variable because closures will capture self.
      @apply_patch ||=
      case
      when which('git')
        lambda { |file|
          message "Running git apply with #{file}... "
          Dir.mktmpdir do |tmp_git_dir|
            execute('patch', ["git", "--git-dir=#{tmp_git_dir}", "--work-tree=.", "apply", "--whitespace=warn", file], :initial_message => false)
          end
        }
      when which('patch')
        lambda { |file|
          message "Running patch with #{file}... "
          execute('patch', ["patch", "-p1", "-i", file], :initial_message => false)
        }
      else
        raise "Failed to complete patch task; patch(1) or git(1) is required."
      end
    ).call(patch_file)
  end

  def patch
    @patch_files.each do |full_path|
      next unless File.exist?(full_path)
      apply_patch(full_path)
    end
  end

  def configure_options
    @configure_options ||= configure_defaults
  end

  def configure
    return if configured?

    FileUtils.mkdir_p(tmp_path)
    cache_file = File.join(tmp_path, 'configure.options_cache')
    File.open(cache_file, "w") { |f| f.write computed_options.to_s }

    command = Array(File.join((source_directory || "."), "configure"))
    if RUBY_PLATFORM=~/mingw|mswin/
      # Windows doesn't recognize the shebang.
      command.unshift("sh")
    end
    execute('configure', command + computed_options, altlog: "config.log")
  end

  def compile
    execute('compile', make_cmd)
  end

  def install
    return if installed?
    execute('install', %Q(#{make_cmd} install))
  end

  def downloaded?
    missing = files_hashs.detect do |file|
      !File.exist?(file[:local_path])
    end

    missing ? false : true
  end

  def configured?
    configure = File.join((source_directory || work_path), 'configure')
    makefile  = File.join(work_path, 'Makefile')
    cache_file  = File.join(tmp_path, 'configure.options_cache')

    stored_options  = File.exist?(cache_file) ? File.read(cache_file) : ""
    current_options = computed_options.to_s

    (current_options == stored_options) && newer?(makefile, configure)
  end

  def installed?
    makefile  = File.join(work_path, 'Makefile')
    target_dir = Dir.glob("#{port_path}/*").find { |d| File.directory?(d) }

    newer?(target_dir, makefile)
  end

  def cook
    if source_directory
      prepare_build_directory
    else
      download unless downloaded?
      extract
      patch
    end
    configure unless configured?
    compile
    install unless installed?

    return true
  end

  def activate
    vars = {
      'PATH'          => File.join(port_path, 'bin'),
      'CPATH'         => include_path,
      'LIBRARY_PATH'  => lib_path,
    }.reject { |env, path| !File.directory?(path) }

    output "Activating #{@name} #{@version} (from #{port_path})..."
    vars.each do |var, path|
      full_path = native_path(path)

      # save current variable value
      old_value = ENV[var] || ''

      unless old_value.include?(full_path)
        ENV[var] = "#{full_path}#{File::PATH_SEPARATOR}#{old_value}"
      end
    end

    # rely on LDFLAGS when cross-compiling
    if File.exist?(lib_path) && (@host != @original_host)
      full_path = native_path(lib_path)

      old_value = ENV.fetch("LDFLAGS", "")

      unless old_value.include?(full_path)
        ENV["LDFLAGS"] = "-L#{full_path} #{old_value}".strip
      end
    end
  end

  # pkg: the pkg-config file name (without the .pc extension)
  # dir: inject the directory path for the pkg-config file (probably only useful for tests)
  # static: the name of the static library archive (without the "lib" prefix or the file extension), or nil for dynamic linking
  #
  # we might be able to be terribly clever and infer the name of the static archive file, but
  # unfortunately projects have so much freedom in what they can report (for name, for libs, etc.)
  # that it feels unreliable to try to do so, so I'm preferring to just have the developer make it
  # explicit.
  def mkmf_config(pkg: nil, dir: nil, static: nil)
    require "mkmf"

    if pkg
      dir ||= File.join(lib_path, "pkgconfig")
      pcfile = File.join(dir, "#{pkg}.pc")
      unless File.exist?(pcfile)
        raise ArgumentError, "pkg-config file '#{pcfile}' does not exist"
      end

      output "Configuring MakeMakefile for #{File.basename(pcfile)} (in #{File.dirname(pcfile)})\n"

      # on macos, pkg-config will not return --cflags without this
      ENV["PKG_CONFIG_ALLOW_SYSTEM_CFLAGS"] = "t"

      # append to PKG_CONFIG_PATH as we go, so later pkg-config files can depend on earlier ones
      ENV["PKG_CONFIG_PATH"] = [ENV["PKG_CONFIG_PATH"], dir].compact.join(File::PATH_SEPARATOR)

      incflags = minimal_pkg_config(pcfile, "cflags-only-I")
      cflags = minimal_pkg_config(pcfile, "cflags-only-other")
      if static
        ldflags = minimal_pkg_config(pcfile, "libs-only-L", "static")
        libflags = minimal_pkg_config(pcfile, "libs-only-l", "static")
      else
        ldflags = minimal_pkg_config(pcfile, "libs-only-L")
        libflags = minimal_pkg_config(pcfile, "libs-only-l")
      end
    else
      output "Configuring MakeMakefile for #{@name} #{@version} (from #{path})\n"

      lib_name = name.sub(/\Alib/, "") # TODO: use delete_prefix when we no longer support ruby 2.4

      incflags = Dir.exist?(include_path) ? "-I#{include_path}" : ""
      cflags = ""
      ldflags = Dir.exist?(lib_path) ? "-L#{lib_path}" : ""
      libflags = Dir.exist?(lib_path) ? "-l#{lib_name}" : ""
    end

    if static
      libdir = lib_path
      if pcfile
        variables = minimal_pkg_config(pcfile, "print-variables").split("\n").map(&:strip)
        if variables.include?("libdir")
          libdir = minimal_pkg_config(pcfile, "variable=libdir")
        end
      end

      #
      # keep track of the libraries we're statically linking against, and fix up ldflags and
      # libflags to make sure we link statically against the recipe's libaries.
      #
      # this avoids the unintentionally dynamically linking against system libraries, and makes sure
      # that if multiple pkg-config files reference each other that we are able to intercept flags
      # from dependent packages that reference the static archive.
      #
      $MINI_PORTILE_STATIC_LIBS[static] = libdir
      static_ldflags = $MINI_PORTILE_STATIC_LIBS.values.map { |v| "-L#{v}" }
      static_libflags = $MINI_PORTILE_STATIC_LIBS.keys.map { |v| "-l#{v}" }

      # remove `-L#{libdir}` and `-lfoo`. we don't need them since we link against the static
      # archive using the full path.
      ldflags = ldflags.shellsplit.reject { |f| static_ldflags.include?(f) }.shelljoin
      libflags = libflags.shellsplit.reject { |f| static_libflags.include?(f) }.shelljoin

      # prepend the full path to the static archive to the linker flags
      static_archive = File.join(libdir, "lib#{static}.#{$LIBEXT}")
      libflags = [static_archive, libflags].join(" ").strip
    end

    # prefer this package by prepending to search paths and library flags
    #
    # convert the ldflags into a list of directories and append to $LIBPATH (instead of just using
    # $LDFLAGS) to ensure we get the `-Wl,-rpath` linker flag for re-finding shared libraries.
    $INCFLAGS = [incflags, $INCFLAGS].join(" ").strip
    libpaths = ldflags.shellsplit.map { |f| f.sub(/\A-L/, "") }
    $LIBPATH = libpaths | $LIBPATH
    $libs = [libflags, $libs].join(" ").strip

    # prefer this package's compiler flags by appending them to the command line
    $CFLAGS = [$CFLAGS, cflags].join(" ").strip
    $CXXFLAGS = [$CXXFLAGS, cflags].join(" ").strip
  end

  def path
    File.expand_path(port_path)
  end

  def include_path
    File.join(path, "include")
  end

  def lib_path
    File.join(path, "lib")
  end

  def gcc_cmd
    (ENV["CC"] || @gcc_command || RbConfig::CONFIG["CC"] || "gcc").dup
  end

  def make_cmd
    (ENV["MAKE"] || @make_command || ENV["make"] || "make").dup
  end

  private

  def native_path(path)
    MiniPortile.native_path(path)
  end

  def posix_path(path)
    MiniPortile.posix_path(path)
  end

  def tmp_path
    "tmp/#{@host}/ports/#{@name}/#{@version}"
  end

  def port_path
    "#{@target}/#{@host}/#{@name}/#{@version}"
  end

  def archives_path
    "#{@target}/archives"
  end

  def work_path
    Dir.glob("#{tmp_path}/*").find { |d| File.directory?(d) }
  end

  def configure_defaults
    [
      "--host=#{@host}",    # build for specific target (host)
      "--enable-static",    # build static library
      "--disable-shared"    # disable generation of shared object
    ]
  end

  def configure_prefix
    "--prefix=#{File.expand_path(port_path)}"
  end

  def computed_options
    [
      configure_options,     # customized or default options
      configure_prefix,      # installation target
    ].flatten
  end

  def files_hashs
    @files.map do |file|
      hash = case file
      when String
        { :url => file }
      when Hash
        file.dup
      else
        raise ArgumentError, "files must be an Array of Stings or Hashs"
      end

      url = hash.fetch(:url){ raise ArgumentError, "no url given" }
      filename = File.basename(url)
      hash[:local_path] = File.join(archives_path, filename)
      hash
    end
  end

  KEYRING_NAME = "mini_portile_keyring.gpg"

  def verify_file(file)
    if file.has_key?(:gpg)
      gpg = file[:gpg]

      signature_url = gpg[:signature_url] || "#{file[:url]}.asc"
      signature_file = file[:local_path] + ".asc"
      # download the signature file
      download_file(signature_url, signature_file)

      gpg_exe = which('gpg2') || which('gpg') || raise("Neither GPG nor GPG2 is installed")

      # import the key into our own keyring
      gpg_status = IO.popen([gpg_exe, "--status-fd", "1", "--no-default-keyring", "--keyring", KEYRING_NAME, "--import"], "w+") do |io|
        io.write gpg[:key]
        io.close_write
        io.read
      end
      key_ids = gpg_status.scan(/\[GNUPG:\] IMPORT_OK \d+ (?<key_id>[0-9a-f]+)/i).map(&:first)
      raise "invalid gpg key provided" if key_ids.empty?

      # verify the signature against our keyring
      gpg_status = IO.popen([gpg_exe, "--status-fd", "1", "--no-default-keyring", "--keyring", KEYRING_NAME, "--verify", signature_file, file[:local_path]], &:read)

      # remove the key from our keyring
      key_ids.each do |key_id|
        IO.popen([gpg_exe, "--batch", "--yes", "--no-default-keyring", "--keyring", KEYRING_NAME, "--delete-keys", key_id], &:read)
        raise "unable to delete the imported key" unless $?.exitstatus==0
      end

      raise "signature mismatch" unless gpg_status.match(/^\[GNUPG:\] VALIDSIG/)

    else
      digest = case
        when exp=file[:sha256] then Digest::SHA256
        when exp=file[:sha1] then Digest::SHA1
        when exp=file[:md5] then Digest::MD5
      end
      if digest
        is = digest.file(file[:local_path]).hexdigest
        unless is == exp.downcase
          raise "Downloaded file '#{file[:local_path]}' has wrong hash: expected: #{exp} is: #{is}"
        end
      end
    end
  end

  def log_file(action)
    @log_files[action] ||=
      File.expand_path("#{action}.log", tmp_path).tap { |file|
        File.unlink(file) if File.exist?(file)
      }
  end

  TAR_EXECUTABLES = %w[gtar bsdtar tar basic-bsdtar]
  def tar_exe
    @@tar_exe ||= begin
      TAR_EXECUTABLES.find { |c|
        which(c)
      } or raise("tar not found - please make sure that one of the following commands is in the PATH: #{TAR_EXECUTABLES.join(", ")}")
    end
  end

  def tar_compression_switch(filename)
    case File.extname(filename)
      when '.gz', '.tgz'
        'z'
      when '.bz2', '.tbz2'
        'j'
      when '.xz'
        'J'
      when '.Z'
        'Z'
      else
        ''
    end
  end

  # From: http://stackoverflow.com/a/5471032/7672
  # Thanks, Mislav!
  #
  # Cross-platform way of finding an executable in the $PATH.
  #
  #   which('ruby') #=> /usr/bin/ruby
  def which(cmd)
    exts = ENV['PATHEXT'] ? ENV['PATHEXT'].split(';') : ['']
    ENV['PATH'].split(File::PATH_SEPARATOR).each do |path|
      exts.each { |ext|
        exe = File.join(path, "#{cmd}#{ext}")
        return exe if File.executable? exe
      }
    end
    return nil
  end

  def detect_host
    return @detect_host if defined?(@detect_host)

    begin
      ENV["LC_ALL"], old_lc_all = "C", ENV["LC_ALL"]

      output = `#{gcc_cmd} -v 2>&1`
      if m = output.match(/^Target\: (.*)$/)
        @detect_host = m[1]
      end

      @detect_host
    ensure
      ENV["LC_ALL"] = old_lc_all
    end
  end

  def extract_file(file, target)
    filename = File.basename(file)
    FileUtils.mkdir_p target

    message "Extracting #{filename} into #{target}... "
    execute('extract', [tar_exe, "#{tar_compression_switch(filename)}xf", file, "-C", target], {:cd => Dir.pwd, :initial_message => false})
  end

  # command could be an array of args, or one string containing a command passed to the shell. See
  # Process.spawn for more information.
  def execute(action, command, command_opts={})
    opt_message = command_opts.fetch(:initial_message, true)
    opt_debug =   command_opts.fetch(:debug, false)
    opt_cd =      command_opts.fetch(:cd) { work_path }
    opt_env =     command_opts.fetch(:env) { Hash.new }
    opt_altlog =  command_opts.fetch(:altlog, nil)

    log_out = log_file(action)

    Dir.chdir(opt_cd) do
      output "DEBUG: env is #{opt_env.inspect}" if opt_debug
      output "DEBUG: command is #{command.inspect}" if opt_debug
      message "Running '#{action}' for #{@name} #{@version}... " if opt_message

      if Process.respond_to?(:spawn) && ! RbConfig.respond_to?(:java)
        options = {[:out, :err]=>[log_out, "a"]}
        output "DEBUG: options are #{options.inspect}" if opt_debug
        args = [opt_env, command, options].flatten
        pid = spawn(*args)
        Process.wait(pid)
      else
        env_args = opt_env.map { |k,v| "#{k}=#{v}".shellescape }.join(" ")
        c = if command.kind_of?(Array)
              command.map(&:shellescape).join(" ")
            else
              command
            end
        redirected = %Q{env #{env_args} #{c} > #{log_out.shellescape} 2>&1}
        output "DEBUG: final command is #{redirected.inspect}" if opt_debug
        system redirected
      end

      if $?.success?
        output "OK"
        return true
      else
        output "ERROR. Please review logs to see what happened:\n"
        [log_out, opt_altlog].compact.each do |log|
          next unless File.exist?(log)
          output("----- contents of '#{log}' -----")
          output(File.read(log))
          output("----- end of file -----")
        end
        raise "Failed to complete #{action} task"
      end
    end
  end

  def newer?(target, checkpoint)
    if (target && File.exist?(target)) && (checkpoint && File.exist?(checkpoint))
      File.mtime(target) > File.mtime(checkpoint)
    else
      false
    end
  end

  # print out a message with the logger
  def message(text)
    @logger.print text
    @logger.flush
  end

  # print out a message using the logger but return to a new line
  def output(text = "")
    @logger.puts text
    @logger.flush
  end

  # Slighly modified from RubyInstaller uri_ext, Rubinius configure
  # and adaptations of Wayne's RailsInstaller
  def download_file(url, full_path, count = 3)
    return if File.exist?(full_path)
    uri = URI.parse(url)

    case uri.scheme.downcase
    when /ftp/
      download_file_ftp(uri, full_path)
    when /http|https/
      download_file_http(url, full_path, count)
    when /file/
      download_file_file(uri, full_path)
    else
      raise ArgumentError.new("Unsupported protocol for #{url}")
    end
  rescue Exception => e
    File.unlink full_path if File.exist?(full_path)
    raise e
  end

  def download_file_http(url, full_path, count = 3)
    filename = File.basename(full_path)
    with_tempfile(filename, full_path) do |temp_file|
      total = 0
      params = {
        "Accept-Encoding" => 'identity',
        :content_length_proc => lambda{|length| total = length },
        :progress_proc => lambda{|bytes|
          if total
            new_progress = (bytes * 100) / total
            message "\rDownloading %s (%3d%%) " % [filename, new_progress]
          else
            # Content-Length is unavailable because Transfer-Encoding is chunked
            message "\rDownloading %s " % [filename]
          end
        },
        :open_timeout => @open_timeout,
        :read_timeout => @read_timeout,
      }
      proxy_uri = URI.parse(url).scheme.downcase == 'https' ?
                  ENV["https_proxy"] :
                  ENV["http_proxy"]
      if proxy_uri
        _, userinfo, _p_host, _p_port = URI.split(proxy_uri)
        if userinfo
          proxy_user, proxy_pass = userinfo.split(/:/).map{|s| CGI.unescape(s) }
          params[:proxy_http_basic_authentication] =
            [proxy_uri, proxy_user, proxy_pass]
        end
      end

      begin
        OpenURI.open_uri(url, 'rb', params) do |io|
          temp_file << io.read
        end
        output
      rescue OpenURI::HTTPRedirect => redirect
        raise "Too many redirections for the original URL, halting." if count <= 0
        count = count - 1
        return download_file(redirect.url, full_path, count-1)
      rescue => e
        count = count - 1
        puts "#{count} retrie(s) left for #{filename} (#{e.message})"
        if count > 0
          sleep 1
          return download_file_http(url, full_path, count)
        end

        output e.message
        return false
      end
    end
  end

  def download_file_file(uri, full_path)
    FileUtils.mkdir_p File.dirname(full_path)
    FileUtils.cp uri.path, full_path
  end

  def download_file_ftp(uri, full_path)
    require "net/ftp"
    filename = File.basename(uri.path)
    with_tempfile(filename, full_path) do |temp_file|
      total = 0
      params = {
        :content_length_proc => lambda{|length| total = length },
        :progress_proc => lambda{|bytes|
          new_progress = (bytes * 100) / total
          message "\rDownloading %s (%3d%%) " % [filename, new_progress]
        },
        :open_timeout => @open_timeout,
        :read_timeout => @read_timeout,
      }
      if ENV["ftp_proxy"]
        _, userinfo, _p_host, _p_port = URI.split(ENV['ftp_proxy'])
        if userinfo
          proxy_user, proxy_pass = userinfo.split(/:/).map{|s| CGI.unescape(s) }
          params[:proxy_http_basic_authentication] =
            [ENV['ftp_proxy'], proxy_user, proxy_pass]
        end
      end
      OpenURI.open_uri(uri, 'rb', params) do |io|
        temp_file << io.read
      end
      output
    end
  rescue LoadError
    raise LoadError, "Ruby #{RUBY_VERSION} does not provide the net-ftp gem, please add it as a dependency if you need to use FTP"
  rescue Net::FTPError
    return false
  end

  def with_tempfile(filename, full_path)
    temp_file = Tempfile.new("download-#{filename}")
    temp_file.binmode
    yield temp_file
    temp_file.close
    File.unlink full_path if File.exist?(full_path)
    FileUtils.mkdir_p File.dirname(full_path)
    FileUtils.mv temp_file.path, full_path, :force => true
  end

  #
  #  this minimal version of pkg_config is based on ruby 29dc9378 (2023-01-09)
  #
  #  specifically with the fix from b90e56e6 to support multiple pkg-config options, and removing
  #  code paths that aren't helpful for mini-portile's use case of parsing pc files.
  #
  def minimal_pkg_config(pkg, *pcoptions)
    if pcoptions.empty?
      raise ArgumentError, "no pkg-config options are given"
    end

    if ($PKGCONFIG ||=
        (pkgconfig = MakeMakefile.with_config("pkg-config") {MakeMakefile.config_string("PKG_CONFIG") || "pkg-config"}) &&
        MakeMakefile.find_executable0(pkgconfig) && pkgconfig)
      pkgconfig = $PKGCONFIG
    else
      raise RuntimeError, "pkg-config is not found"
    end

    pcoptions = Array(pcoptions).map { |o| "--#{o}" }
    response = IO.popen([pkgconfig, *pcoptions, pkg], err:[:child, :out], &:read)
    raise RuntimeError, response unless $?.success?
    response.strip
  end
end
