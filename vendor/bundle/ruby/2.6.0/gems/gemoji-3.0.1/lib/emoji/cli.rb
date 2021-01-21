require 'emoji/extractor'
require 'fileutils'
require 'optparse'

module Emoji
  module CLI
    extend self

    InvalidUsage = Class.new(RuntimeError)

    def dispatch(argv)
      cmd = argv[0]
      argv = argv[1..-1]

      case cmd
      when "extract"
        public_send(cmd, argv)
      when "help", "--help", "-h"
        help
      else
        raise InvalidUsage
      end

      return 0
    rescue InvalidUsage, OptionParser::InvalidArgument, OptionParser::InvalidOption => err
      unless err.message == err.class.to_s
        $stderr.puts err.message
        $stderr.puts
      end
      $stderr.puts usage_text
      return 1
    end

    def help
      puts usage_text
    end

    VALID_SIZES = [ 20, 32, 40, 48, 64, 96, 160 ]

    def extract(argv)
      size = 64

      OptionParser.new do |opts|
        opts.on("--size=#{size}", Integer) do |val|
          if VALID_SIZES.include?(val)
            size = val
          else
            raise InvalidUsage, "size should be one of: #{VALID_SIZES.join(', ')}"
          end
        end
      end.parse!(argv)

      raise InvalidUsage unless argv.size == 1
      path = argv[0]

      Emoji::Extractor.new(size, path).extract!
      Dir["#{Emoji.images_path}/*.png"].each do |png|
        FileUtils.cp(png, File.join(path, File.basename(png)))
      end
    end

    def usage_text
      <<EOF
Usage: gemoji extract <path> [--size=64]
EOF
    end
  end
end
