# encoding: utf-8
require 'emoji/character'
require 'json'

module Emoji
  extend self

  def data_file
    File.expand_path('../../db/emoji.json', __FILE__)
  end

  def apple_palette_file
    File.expand_path('../../db/Category-Emoji.json', __FILE__)
  end

  def images_path
    File.expand_path("../../images", __FILE__)
  end

  def all
    return @all if defined? @all
    @all = []
    parse_data_file
    @all
  end

  def apple_palette
    return @apple_palette if defined? @apple_palette
    data = File.open(apple_palette_file, 'r:UTF-8') { |f| JSON.parse(f.read) }
    @apple_palette = data.fetch('EmojiDataArray').each_with_object({}) do |group, all|
      title = group.fetch('CVDataTitle').split('-', 2)[1]
      all[title] = group.fetch('CVCategoryData').fetch('Data').split(',').map do |raw|
        TEXT_GLYPHS.include?(raw) ? raw + VARIATION_SELECTOR_16 : raw
      end
    end
  end

  # Public: Initialize an Emoji::Character instance and yield it to the block.
  # The character is added to the `Emoji.all` set.
  def create(name)
    emoji = Emoji::Character.new(name)
    self.all << edit_emoji(emoji) { yield emoji if block_given? }
    emoji
  end

  # Public: Yield an emoji to the block and update the indices in case its
  # aliases or unicode_aliases lists changed.
  def edit_emoji(emoji)
    @names_index ||= Hash.new
    @unicodes_index ||= Hash.new

    yield emoji

    emoji.aliases.each do |name|
      @names_index[name] = emoji
    end
    emoji.unicode_aliases.each do |unicode|
      @unicodes_index[unicode] = emoji
    end

    emoji
  end

  # Public: Find an emoji by its aliased name. Return nil if missing.
  def find_by_alias(name)
    names_index[name]
  end

  # Public: Find an emoji by its unicode character. Return nil if missing.
  def find_by_unicode(unicode)
    unicodes_index[unicode]
  end

  private
    VARIATION_SELECTOR_16 = "\u{fe0f}".freeze
    ZERO_WIDTH_JOINER = "\u{200d}".freeze
    FEMALE_SYMBOL = "\u{2640}".freeze
    MALE_SYMBOL = "\u{2642}".freeze

    # Chars from Apple's palette which must have VARIATION_SELECTOR_16 to render:
    TEXT_GLYPHS = ["🈷", "🈂", "🅰", "🅱", "🅾", "©", "®", "™", "〰"].freeze

    def parse_data_file
      data = File.open(data_file, 'r:UTF-8') { |file| JSON.parse(file.read) }
      data.each do |raw_emoji|
        self.create(nil) do |emoji|
          raw_emoji.fetch('aliases').each { |name| emoji.add_alias(name) }
          if raw = raw_emoji['emoji']
            unicodes = [raw, raw.sub(VARIATION_SELECTOR_16, '') + VARIATION_SELECTOR_16].uniq
            unicodes.each { |uni| emoji.add_unicode_alias(uni) }
          end
          raw_emoji.fetch('tags').each { |tag| emoji.add_tag(tag) }

          emoji.category = raw_emoji['category']
          emoji.description = raw_emoji['description']
          emoji.unicode_version = raw_emoji['unicode_version']
          emoji.ios_version = raw_emoji['ios_version']
        end
      end

      # Add an explicit gendered variant to emoji that historically imply a gender
      data.each do |raw_emoji|
        raw = raw_emoji['emoji']
        next unless raw
        no_gender = raw.sub(/(#{VARIATION_SELECTOR_16})?#{ZERO_WIDTH_JOINER}(#{FEMALE_SYMBOL}|#{MALE_SYMBOL})/, '')
        next unless $2
        emoji = find_by_unicode(no_gender)
        next unless emoji
        edit_emoji(emoji) do
          emoji.add_unicode_alias(
            $2 == FEMALE_SYMBOL ?
              raw.sub(FEMALE_SYMBOL, MALE_SYMBOL) :
              raw.sub(MALE_SYMBOL, FEMALE_SYMBOL)
          )
        end
      end
    end

    def names_index
      all unless defined? @all
      @names_index
    end

    def unicodes_index
      all unless defined? @all
      @unicodes_index
    end
end

# Preload emoji into memory
Emoji.all
