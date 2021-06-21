
if RUBY_VERSION < "1.9"
  $KCODE = 'U'

  module LaTeX
    def self.to_unicode(string)
      string.gsub(/\\?u([\da-f]{4})/i) { |m| [$1.to_i(16)].pack('U') }
    end
  end

  def ruby_18; yield; end
  def ruby_19; false; end
else

  module LaTeX
    def self.to_unicode(string)
      string
    end
  end

  def ruby_18; false; end
  def ruby_19; yield; end
end

if RUBY_PLATFORM == 'java'
  require 'java'

  # Use the Java native Unicode normalizer
  module LaTeX
    def self.normalize_C(string)
      java.text.Normalizer.normalize(string, java.text.Normalizer::Form::NFC).to_s
    end
  end

else
  if RUBY_VERSION >= '2.3'
    module LaTeX
      def self.normalize_C(string)
        string.unicode_normalize(:nfc)
      end
    end
  else
    begin
      require 'unicode'

      # Use the Unicode gem
      module LaTeX
        def self.normalize_C(string)
          Unicode::normalize_C(string)
        end
      end
    rescue LoadError
      begin
        require 'active_support/multibyte/chars'

        # Use ActiveSupport's normalizer
        module LaTeX
          def self.normalize_C(string)
            ActiveSupport::Multibyte::Chars.new(string).normalize(:c).to_s
          end
        end
      rescue LoadError
        fail "Failed to load unicode normalizer: please gem install unicode (or active_support)"
      end
    end
  end
end

module LaTeX
  begin
    require 'ritex'

    def self.ritex
      Ritex::Parser.new(:mathml)
    end

    def self.to_math_ml(string)
      ritex.parse string, :nowrap => true, :display => false
    end

  rescue LoadError
    begin
      require 'math_ml'

      def self.to_math_ml(string)
        MathML::String.mathml_latex_parser.parse(string, false)
      end

    rescue LoadError
      # No MathML conversion

      def self.to_math_ml(string)
        string
      end
    end
  end
end
