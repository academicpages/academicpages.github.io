
module CiteProc
  module Extensions

    module Underscore
      def underscore(word)
        word = word.to_s.dup
        word.gsub!(/::/, '/')
        word.gsub!(/([A-Z]+)([A-Z][a-z])/,'\1_\2')
        word.gsub!(/([a-z\d])([A-Z])/,'\1_\2')
        word.tr!('-', '_')
        word.downcase!
        word
      end
    end

    module DeepCopy
      # See Matz, Flanagan: 'The Ruby Programming Language', p.83
      def deep_copy
        Marshal.load(Marshal.dump(self))
      end
    end

    module DeepFetch
      def deep_fetch(*arguments)
        arguments.reduce(self) { |s,a| s[a] } rescue nil
      end

      def [](*arguments)
        return super if arguments.length == 1
        deep_fetch(*arguments)
      end

    end

    # shamelessly copied from active_support
    module SymbolizeKeys
      def symbolize_keys
        inject({}) do |options, (key, value)|
          options[(key.to_sym rescue key) || key] = value
          options
        end
      end

      def symbolize_keys!
        replace(symbolize_keys)
      end

    end

    module StringifyKeys
      def stringify_keys
        inject({}) do |options, (key, value)|
          options[(key.to_s rescue key) || key] = value
          options
        end
      end

      def stringify_keys!
        replace(symbolize_keys)
      end
    end

    module CompactJoin
      def compact_join(delimiter = ' ')
        reject { |t| t.nil? || (t.respond_to?(:empty?) && t.empty?) }.join(delimiter)
      end
    end

    # based and compatible to the active support version
    # module ToSentence
    #   def to_sentence(options = {})
    #     options = {
    #       :words_connector => ", ",
    #       :two_words_connector => " and ",
    #       :last_word_connector => ", and "
    #     }.merge!(options)
    #
    #     case length
    #     when 0
    #       ""
    #     when 1
    #       self[0].to_s.dup
    #     when 2
    #       "#{self[0]}#{options[:two_words_connector]}#{self[1]}"
    #     else
    #       "#{self[0...-1].join(options[:words_connector])}#{options[:last_word_connector]}#{self[-1]}"
    #     end
    #   end
    # end

    module AliasMethods
      private
      def alias_methods(*arguments)
        raise ArgumentError, "wrong number of arguments (#{arguments.length} for 2 or more)" if arguments.length < 2
        method_id = arguments.shift
        arguments.each { |a| alias_method method_id, a }
      end
    end
  end
end

class Hash
  warn "citeproc: re-defining Hash#deep_copy, this may cause conflicts with other libraries" if method_defined?(:deep_copy)
  include CiteProc::Extensions::DeepCopy

  warn "citeproc: re-defining Hash#deep_fetch, this may cause conflicts with other libraries" if method_defined?(:deep_fetch)
  include CiteProc::Extensions::DeepFetch

  include CiteProc::Extensions::SymbolizeKeys unless method_defined?(:symbolize_keys)
  include CiteProc::Extensions::StringifyKeys unless method_defined?(:stringify_keys)
end

class Array
  include CiteProc::Extensions::CompactJoin
  # include CiteProc::Extensions::ToSentence unless method_defined?(:to_sentence)

  warn "citeproc: re-defining Array#deep_copy, this may cause conflicts with other libraries" if method_defined?(:deep_copy)
  include CiteProc::Extensions::DeepCopy
end

class String
  include CiteProc::Extensions::Underscore unless method_defined?(:underscore)
end

# module Kernel
#   include CiteProc::Extensions::AliasMethods
# end
