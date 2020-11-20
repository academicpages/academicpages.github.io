class Module
  unless respond_to?(:ruby2_keywords, true)
    private
    def ruby2_keywords(name, *)
      # nil
    end
  end
end

main = TOPLEVEL_BINDING.receiver
unless main.respond_to?(:ruby2_keywords, true)
  def main.ruby2_keywords(name, *)
    # nil
  end
end

class Proc
  unless method_defined?(:ruby2_keywords)
    def ruby2_keywords
      self
    end
  end
end
