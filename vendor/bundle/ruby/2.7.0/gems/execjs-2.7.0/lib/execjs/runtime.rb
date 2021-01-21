require "execjs/encoding"

module ExecJS
  # Abstract base class for runtimes
  class Runtime
    class Context
      include Encoding

      def initialize(runtime, source = "", options = {})
      end

      def exec(source, options = {})
        raise NotImplementedError
      end

      def eval(source, options = {})
        raise NotImplementedError
      end

      def call(properties, *args)
        raise NotImplementedError
      end
    end

    def name
      raise NotImplementedError
    end

    def context_class
      self.class::Context
    end

    def exec(source, options = {})
      context = compile("", options)

      if context.method(:exec).arity == 1
        context.exec(source)
      else
        context.exec(source, options)
      end
    end

    def eval(source, options = {})
      context = compile("", options)

      if context.method(:eval).arity == 1
        context.eval(source)
      else
        context.eval(source, options)
      end
    end

    def compile(source, options = {})
      if context_class.instance_method(:initialize).arity == 2
        context_class.new(self, source)
      else
        context_class.new(self, source, options)
      end
    end

    def deprecated?
      false
    end

    def available?
      raise NotImplementedError
    end
  end
end
