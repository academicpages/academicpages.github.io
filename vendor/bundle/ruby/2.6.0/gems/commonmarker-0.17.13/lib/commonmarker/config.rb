require 'ruby-enum'
module CommonMarker
  # For Ruby::Enum, these must be classes, not modules
  module Config
    class Parse
      include Ruby::Enum

      define :DEFAULT, 0
      define :VALIDATE_UTF8, (1 << 9)
      define :SMART, (1 << 10)
      define :LIBERAL_HTML_TAG, (1 << 12)
      define :FOOTNOTES, (1 << 13)
      define :STRIKETHROUGH_DOUBLE_TILDE, (1 << 14)
    end

    class Render
      include Ruby::Enum

      define :DEFAULT, 0
      define :SOURCEPOS, (1 << 1)
      define :HARDBREAKS, (1 << 2)
      define :SAFE, (1 << 3)
      define :NOBREAKS, (1 << 4)
      define :GITHUB_PRE_LANG, (1 << 11)
      define :TABLE_PREFER_STYLE_ATTRIBUTES, (1 << 15)
      define :FULL_INFO_STRING, (1 << 16)
    end

    def self.process_options(option, type)
      type = Config.const_get(type.capitalize)
      if option.is_a?(Symbol)
        check_option(option, type)
        type.to_h[option]
      elsif option.is_a?(Array)
        option = [nil] if option.empty?
        # neckbearding around. the map will both check the opts and then bitwise-OR it
        option.map { |o| check_option(o, type); type.to_h[o] }.inject(0, :|)
      else
        raise TypeError, 'option type must be a valid symbol or array of symbols'
      end
    end

    def self.check_option(option, type)
      unless type.keys.include?(option)
        raise TypeError, "option ':#{option}' does not exist for #{type}"
      end
    end
  end
end
