module CSL
  module_function

  def silence_warnings
    original_verbosity, $VERBOSE = $VERBOSE, nil
    yield
  ensure
    $VERBOSE = original_verbosity
  end
end

class Module
  if RUBY_VERSION < '1.9'
    alias const? const_defined?
  else
    def const?(name)
      const_defined?(name, false)
    end
  end
end

class Struct
  alias_method :__class__, :class
end unless Struct.instance_methods.include?(:__class__)

module CSL
  module_function

  if RUBY_VERSION < '1.9'

    XML_ENTITY_SUBSTITUTION = Hash[*%w{
     & &amp; < &lt; > &gt; ' &apos; " &quot;
    }].freeze

    def encode_xml_text(string)
      string.gsub(/[&<>]/) { |match|
        XML_ENTITY_SUBSTITUTION[match]
      }
    end

    def encode_xml_attr(string)
      string.gsub(/[&<>'"]/) { |match|
        XML_ENTITY_SUBSTITUTION[match]
      }.inspect
    end
  else
    def encode_xml_text(string)
      string.encode(string.encoding, :xml => :text)
    end

    def encode_xml_attr(string)
      string.encode(string.encoding, :xml => :attr)
    end
  end
end
