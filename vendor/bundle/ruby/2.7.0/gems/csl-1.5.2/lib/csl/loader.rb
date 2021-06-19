module CSL
  #
  # Mixin used by Locale and Style to load assets either from disk or from
  # the network. Classes including the Loader module are expected to provide
  # appropriate root, prefix and extension values and a parse method that
  # will be passed the contents of the asset data.
  #
  # @note
  #   Base classes are exepcted to define a #parse method.
  module Loader

    attr_accessor :root, :prefix, :extension

    # @example
    #   Style.load(:apa)                         -> style
    #   Style.load('chicago-author.csl')         -> style
    #   Locale.load('en')                        -> locale
    #   Locale.load('http://example.com/de.xml') -> locale
    #
    # Resolves the passed-in path/name or string and loads the asset data.
    # The data will be passed on to the #parse! method of the base class.
    # Typically, this will return a new instance of the class.
    #
    # @note
    #   The base class is expected to define a #parse! method.
    #
    # @raise ParseError
    #
    # @return [Style, Locale] the parsed CSL resource
    def load(input)
      parse! extract_data_from(input)
    end

    def list
      Dir["#{root}/#{prefix}*#{extension}"].map do |path|
        File.basename(path, extension).sub(/^#{prefix}/, '')
      end
    end
    alias ls list

    # Extends the passed-in string to a full path.
    def extend_path(string)
      File.join(root.to_s, extend_name(string))
    end

    # Extends the passed-in string to a style/locale name, by prefixing and
    # appending the default name prefix and extension.
    def extend_name(string)
      if File.extname(string.to_s).empty?
        name = [string, extension].compact.join
      else
        name = string.to_s.dup
      end

      unless name.start_with?(prefix.to_s)
        name = [prefix, name].join
      end

      name
    end

    private

    def extract_data_from(input)
      case
      when input.respond_to?(:read)
        input.read
      when input.to_s =~ /^\s*</
        input.to_s
      else

        input = input.to_s

        case
        when File.exist?(input)
          location = input
        when File.exist?(extend_name(input))
          location = extend_name(input)
        when File.exist?(extend_path(input))
          location = extend_path(input)
        else
          location = input
        end

        Kernel.open(location, 'r:UTF-8') do |io|
          io.read
        end
      end
    rescue => e
      raise ParseError, "failed to extract CSL data from #{input.inspect}: #{e.message}"
    end
  end

end
