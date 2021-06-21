module CSL
  module PrettyPrinter
    
    def tags
      raise 'not implemened by base class'
    end
    
    def to_xml
      tags.flatten.join
    end

    def pretty_print
      preamble << tags.map { |t| pp t }.join("\n")
    end

    private
    
    def tabwidth
      2
    end
    
    def preamble
      ''
    end
    
    def pp(tag, level = 0)
      if tag.is_a?(Array)
        tag.map { |t| pp t, level + 1 }.join("\n")
      else
        (' ' * (level * tabwidth)) << tag.to_s
      end
    end
    
  end
end