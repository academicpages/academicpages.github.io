module CiteProc

  module Asset

    def self.included(base)
      base.extend(ClassMethods)
    end

    attr_reader :asset, :location

    def open?
      !asset.nil?
    end

    def open(input)
      case
      when input.respond_to?(:read)
        @location = nil
        @asset = input.read
      when input.to_s =~ /^\s*</
        @location = nil
        @asset = input.to_s.dup
      else
        case
        when File.exists?(input)
          @location = input
        when File.exists?(self.class.extend_name(input))
          @location = self.class.extend_name(input)
        when File.exists?(self.class.extend_path(input))
          @location = self.class.extend_path(input)
        else
          @location = input
        end

        Kernel.open(@location, 'r:UTF-8') do |io|
          @asset = io.read
        end
      end

      self
    rescue => e
      raise ArgumentError, "failed to open asset #@location (#{input.inspect}): #{e.message}"
    end

    def name
      File.basename(location, self.class.extension).sub(Regexp.new("^#{self.class.prefix}"), '')
    end

    alias to_s asset

    def inspect
      "#<CiteProc::#{self.class.name} #{name}>"
    end

    module ClassMethods

      attr_accessor :root, :extension, :prefix

      def open(path_or_name)
        new.open(path_or_name)
      end

      def extend_path(input)
        File.join(root.to_s, extend_name(input))
      end

      def extend_name(input)
        if File.extname(input) != extension
          name = [input, extension].compact.join
        else
          name = input.to_s.dup
        end

        unless name.start_with?(prefix.to_s)
          name = [prefix, name].join
        end

        name
      end

    end

  end

  class Style

    include Asset

    @root = '/usr/local/share/citation-style-language/styles'.freeze
    @extension = '.csl'.freeze

  end

  class Locale

    include Asset

    @root = '/usr/local/share/citation-style-language/locales'.freeze
    @extension = '.xml'.freeze
    @prefix = 'locales-'.freeze


    def language
      name.split('-')[0]
    end

    def region
      name.split('-')[1]
    end

  end

end
