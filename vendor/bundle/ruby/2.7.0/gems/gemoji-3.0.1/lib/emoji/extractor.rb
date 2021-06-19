require 'emoji'
require 'fileutils'

module Emoji
  class Extractor
    EMOJI_TTF = "/System/Library/Fonts/Apple Color Emoji.ttc"

    attr_reader :size, :images_path

    def initialize(size, images_path)
      @size = size
      @images_path = images_path
    end

    def each(&block)
      return to_enum(__method__) unless block_given?

      File.open(EMOJI_TTF, 'rb') do |file|
        font_offsets = parse_ttc(file)
        file.pos = font_offsets[0]

        tables = parse_tables(file)
        glyph_index = extract_glyph_index(file, tables)

        each_glyph_bitmap(file, tables, glyph_index, &block)
      end
    end

    def extract!
      each do |glyph_name, type, binread|
        if emoji = glyph_name_to_emoji(glyph_name)
          image_filename = "#{images_path}/#{emoji.image_filename}"
          FileUtils.mkdir_p(File.dirname(image_filename))
          File.open(image_filename, 'wb') { |f| f.write binread.call }
        end
      end
    end

  private

    GENDER_MAP = {
      "M" => "\u{2642}",
      "W" => "\u{2640}",
    }

    FAMILY_MAP = {
      "B" => "\u{1f466}",
      "G" => "\u{1f467}",
      "M" => "\u{1f468}",
      "W" => "\u{1f469}",
    }.freeze

    FAMILY = "1F46A"
    COUPLE = "1F491"
    KISS = "1F48F"

    def glyph_name_to_emoji(glyph_name)
      return if glyph_name =~ /\.[1-5]($|\.)/
      zwj = Emoji::ZERO_WIDTH_JOINER
      v16 = Emoji::VARIATION_SELECTOR_16

      if glyph_name =~ /^u(#{FAMILY}|#{COUPLE}|#{KISS})\.([#{FAMILY_MAP.keys.join('')}]+)$/
        if $1 == FAMILY ? $2 == "MWB" : $2 == "WM"
          raw = [$1.hex].pack('U')
        else
          if $1 == COUPLE
            middle = "#{zwj}\u{2764}#{v16}#{zwj}" # heavy black heart
          elsif $1 == KISS
            middle = "#{zwj}\u{2764}#{v16}#{zwj}\u{1F48B}#{zwj}" # heart + kiss mark
          else
            middle = zwj
          end
          raw = $2.split('').map { |c| FAMILY_MAP.fetch(c) }.join(middle)
        end
        candidates = [raw]
      else
        raw = glyph_name.gsub(/(^|_)u([0-9A-F]+)/) { ($1.empty?? $1 : zwj) + [$2.hex].pack('U') }
        raw.sub!(/\.0\b/, '')
        raw.sub!(/\.(#{GENDER_MAP.keys.join('|')})$/) { v16 + zwj + GENDER_MAP.fetch($1) }
        candidates = [raw]
        candidates << raw.sub(v16, '') if raw.include?(v16)
        candidates << raw.gsub(zwj, '') if raw.include?(zwj)
        candidates.dup.each { |c| candidates << (c + v16) }
      end

      candidates.map { |c| Emoji.find_by_unicode(c) }.compact.first
    end

    # https://www.microsoft.com/typography/otspec/otff.htm
    def parse_ttc(io)
      header_name = io.read(4).unpack('a*')[0]
      raise unless "ttcf" == header_name
      header_version, num_fonts = io.read(4*2).unpack('l>N')
      # parse_version(header_version) #=> 2.0
      io.read(4 * num_fonts).unpack('N*')
    end

    def parse_tables(io)
      sfnt_version, num_tables = io.read(4 + 2*4).unpack('Nn')
      # sfnt_version #=> 0x00010000
      num_tables.times.each_with_object({}) do |_, tables|
        tag, checksum, offset, length = io.read(4 + 4*3).unpack('a4N*')
        tables[tag] = {
          checksum: checksum,
          offset: offset,
          length: length,
        }
      end
    end

    GlyphIndex = Struct.new(:length, :name_index, :names) do
      def name_for(glyph_id)
        index = name_index[glyph_id]
        names[index - 257]
      end

      def each(&block)
        length.times(&block)
      end

      def each_with_name
        each do |glyph_id|
          yield glyph_id, name_for(glyph_id)
        end
      end
    end

    def extract_glyph_index(io, tables)
      postscript_table = tables.fetch('post')
      io.pos = postscript_table[:offset]
      end_pos = io.pos + postscript_table[:length]

      parse_version(io.read(32).unpack('l>')[0]) #=> 2.0
      num_glyphs = io.read(2).unpack('n')[0]
      glyph_name_index = io.read(2*num_glyphs).unpack('n*')

      glyph_names = []
      while io.pos < end_pos
        length = io.read(1).unpack('C')[0]
        glyph_names << io.read(length)
      end

      GlyphIndex.new(num_glyphs, glyph_name_index, glyph_names)
    end

    # https://developer.apple.com/fonts/TrueType-Reference-Manual/RM06/Chap6sbix.html
    def each_glyph_bitmap(io, tables, glyph_index)
      io.pos = sbix_offset = tables.fetch('sbix')[:offset]
      strike = extract_sbix_strike(io, glyph_index.length, size)

      glyph_index.each_with_name do |glyph_id, glyph_name|
        glyph_offset = strike[:glyph_data_offset][glyph_id]
        next_glyph_offset = strike[:glyph_data_offset][glyph_id + 1]

        if glyph_offset && next_glyph_offset && glyph_offset < next_glyph_offset
          io.pos = sbix_offset + strike[:offset] + glyph_offset
          x, y, type = io.read(2*2 + 4).unpack('s2A4')
          yield glyph_name, type, -> { io.read(next_glyph_offset - glyph_offset - 8) }
        end
      end
    end

    def extract_sbix_strike(io, num_glyphs, image_size)
      sbix_offset = io.pos
      version, flags, num_strikes = io.read(2*2 + 4).unpack('n2N')
      strike_offsets = num_strikes.times.map { io.read(4).unpack('N')[0] }

      strike_offsets.each do |strike_offset|
        io.pos = sbix_offset + strike_offset
        ppem, resolution = io.read(4*2).unpack('n2')
        next unless ppem == size

        data_offsets = io.read(4 * (num_glyphs+1)).unpack('N*')
        return {
          ppem: ppem,
          resolution: resolution,
          offset: strike_offset,
          glyph_data_offset: data_offsets,
        }
      end
      return nil
    end

    def parse_version(num)
      major = num >> 16
      minor = num & 0xFFFF
      "#{major}.#{minor}"
    end
  end
end
