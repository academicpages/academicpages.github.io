# -*- coding: utf-8 -*-

#
# Robust unicode upcase/downcase
#

if RUBY_PLATFORM =~ /java/i
  require 'java'

  puts java.lang.System.getProperty('file.encoding')

  module CiteProc
    def upcase(string)
      java.lang.String.new(string).to_upper_case(java.util.Locale::ENGLISH).to_s
    end

    def downcase(string)
      java.lang.String.new(string).to_lower_case(java.util.Locale::ENGLISH).to_s
    end
  end

else

  module CiteProc
    if RUBY_VERSION >= '2.4'
      def upcase(string)
        string.upcase
      end

      def downcase(string)
        string.downcase
      end
    else
      # Ruby 2.3 and older require extra Gems
      begin
        require 'unicode_utils'
        def upcase(string)
          UnicodeUtils.upcase(string)
        end

        def downcase(string)
          UnicodeUtils.downcase(string)
        end
      rescue LoadError
        begin
          require 'unicode'
          def upcase(string)
            Unicode.upcase(string)
          end

          def downcase(string)
            Unicode.downcase(string)
          end
        rescue LoadError
          warn "CiteProc requires the `unicode_utils` or `unicode` Gem on Ruby 2.3"
        end
      end
    end
  end
end

module CiteProc
  module_function :upcase, :downcase
end
