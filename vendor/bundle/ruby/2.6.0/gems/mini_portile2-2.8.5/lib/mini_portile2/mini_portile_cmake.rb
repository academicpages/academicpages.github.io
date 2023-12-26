require 'mini_portile2/mini_portile'
require 'open3'

class MiniPortileCMake < MiniPortile
  attr_accessor :system_name

  def configure_prefix
    "-DCMAKE_INSTALL_PREFIX=#{File.expand_path(port_path)}"
  end

  def initialize(name, version, **kwargs)
    super(name, version, **kwargs)
    @cmake_command = kwargs[:cmake_command]
    @cmake_build_type = kwargs[:cmake_build_type]
  end

  def configure_defaults
    [
      generator_defaults,
      cmake_compile_flags,
    ].flatten
  end

  def configure
    return if configured?

    cache_file = File.join(tmp_path, 'configure.options_cache')
    File.open(cache_file, "w") { |f| f.write computed_options.to_s }

    execute('configure', [cmake_cmd] + computed_options + ["."])
  end

  def configured?
    configure = File.join(work_path, 'configure')
    makefile  = File.join(work_path, 'CMakefile')
    cache_file  = File.join(tmp_path, 'configure.options_cache')

    stored_options  = File.exist?(cache_file) ? File.read(cache_file) : ""
    current_options = computed_options.to_s

    (current_options == stored_options) && newer?(makefile, configure)
  end

  def make_cmd
    return "nmake" if MiniPortile.mswin?
    super
  end

  def cmake_cmd
    (ENV["CMAKE"] || @cmake_command || "cmake").dup
  end

  def cmake_build_type
    (ENV["CMAKE_BUILD_TYPE"] || @cmake_build_type || "Release").dup
  end

  private

  def generator_defaults
    if MiniPortile.mswin? && generator_available?('NMake')
      ['-G', 'NMake Makefiles']
    elsif MiniPortile.mingw? && generator_available?('MSYS')
      ['-G', 'MSYS Makefiles']
    else
      []
    end
  end

  def cmake_compile_flags
    c_compiler, cxx_compiler = find_c_and_cxx_compilers(host)

    # needed to ensure cross-compilation with CMake targets the right CPU and compilers
    [
      "-DCMAKE_SYSTEM_NAME=#{cmake_system_name}",
      "-DCMAKE_SYSTEM_PROCESSOR=#{cpu_type}",
      "-DCMAKE_C_COMPILER=#{c_compiler}",
      "-DCMAKE_CXX_COMPILER=#{cxx_compiler}",
      "-DCMAKE_BUILD_TYPE=#{cmake_build_type}",
    ]
  end

  def find_compiler(compilers)
    compilers.find { |binary| which(binary) }
  end

  # configure automatically searches for the right compiler based on the
  # `--host` parameter.  However, CMake doesn't have an equivalent feature.
  # Search for the right compiler for the target architecture using
  # some basic heruistics.
  def find_c_and_cxx_compilers(host)
    c_compiler = ENV["CC"]
    cxx_compiler = ENV["CXX"]

    if MiniPortile.darwin?
      c_compiler ||= 'clang'
      cxx_compiler ||='clang++'
    else
      c_compiler ||= 'gcc'
      cxx_compiler ||= 'g++'
    end

    c_platform_compiler = "#{host}-#{c_compiler}"
    cxx_platform_compiler = "#{host}-#{cxx_compiler}"
    c_compiler = find_compiler([c_platform_compiler, c_compiler])
    cxx_compiler = find_compiler([cxx_platform_compiler, cxx_compiler])

    [c_compiler, cxx_compiler]
  end

  # Full list: https://gitlab.kitware.com/cmake/cmake/-/blob/v3.26.4/Modules/CMakeDetermineSystem.cmake?ref_type=tags#L12-31
  def cmake_system_name
    return system_name if system_name

    if MiniPortile.linux?
      'Linux'
    elsif MiniPortile.darwin?
      'Darwin'
    elsif MiniPortile.windows?
      'Windows'
    elsif MiniPortile.freebsd?
      'FreeBSD'
    elsif MiniPortile.openbsd?
      'OpenBSD'
    elsif MiniPortile.solaris?
      'SunOS'
    else
      raise "Unable to set CMAKE_SYSTEM_NAME for #{MiniPortile.target_os}"
    end
  end

  def generator_available?(generator_type)
    stdout_str, status = Open3.capture2("#{cmake_cmd} --help")

    raise 'Unable to determine whether CMake supports #{generator_type} Makefile generator' unless status.success?

    stdout_str.include?("#{generator_type} Makefiles")
  end

  def cpu_type
    return 'x86_64' if MiniPortile.target_cpu == 'x64'

    MiniPortile.target_cpu
  end
end
