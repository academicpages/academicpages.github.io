module BibTeX
  begin
    original_verbosity = $VERBOSE
    $VERBOSE = nil

    require 'iconv'

    @iconv = Iconv.new('ascii//translit//ignore', 'utf-8')

    def self.transliterate(str)
      @iconv.iconv(str)
    end
  rescue LoadError
    @iconv_replacements = Hash['ä', 'ae', 'ö', 'oe', 'ü', 'ue', 'Ä', 'Ae', 'Ö', 'Oe', 'Ü', 'Ue', 'ß', 'ss']

    # Returns +str+ transliterated containing only ASCII characters.
    def self.transliterate(str)
      str.gsub(/[äöüÄÖÜß]/, @iconv_replacements)
    end
  ensure
    $VERBOSE = original_verbosity
  end
end
