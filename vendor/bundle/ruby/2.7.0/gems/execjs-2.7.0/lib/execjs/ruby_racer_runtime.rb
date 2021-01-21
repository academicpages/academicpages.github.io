require "execjs/runtime"

module ExecJS
  class RubyRacerRuntime < Runtime
    class Context < Runtime::Context
      def initialize(runtime, source = "", options = {})
        source = encode(source)

        lock do
          @v8_context = ::V8::Context.new

          begin
            @v8_context.eval(source)
          rescue ::V8::JSError => e
            raise wrap_error(e)
          end
        end
      end

      def exec(source, options = {})
        source = encode(source)

        if /\S/ =~ source
          eval "(function(){#{source}})()", options
        end
      end

      def eval(source, options = {})
        source = encode(source)

        if /\S/ =~ source
          lock do
            begin
              unbox @v8_context.eval("(#{source})")
            rescue ::V8::JSError => e
              raise wrap_error(e)
            end
          end
        end
      end

      def call(properties, *args)
        lock do
          begin
            unbox @v8_context.eval(properties).call(*args)
          rescue ::V8::JSError => e
            raise wrap_error(e)
          end
        end
      end

      def unbox(value)
        case value
        when ::V8::Function
          nil
        when ::V8::Array
          value.map { |v| unbox(v) }
        when ::V8::Object
          value.inject({}) do |vs, (k, v)|
            vs[k] = unbox(v) unless v.is_a?(::V8::Function)
            vs
          end
        when String
          value.force_encoding('UTF-8')
        else
          value
        end
      end

      private
        def lock
          result, exception = nil, nil
          V8::C::Locker() do
            begin
              result = yield
            rescue Exception => e
              exception = e
            end
          end

          if exception
            raise exception
          else
            result
          end
        end

        def wrap_error(e)
          error_class = e.value["name"] == "SyntaxError" ? RuntimeError : ProgramError

          stack = e.value["stack"] || ""
          stack = stack.split("\n")
          stack.shift
          stack = [e.message[/<eval>:\d+:\d+/, 0]].compact if stack.empty?
          stack = stack.map { |line| line.sub(" at ", "").sub("<eval>", "(execjs)").strip }

          error = error_class.new(e.value.to_s)
          error.set_backtrace(stack + caller)
          error
        end
    end

    def name
      "therubyracer (V8)"
    end

    def available?
      require "v8"
      true
    rescue LoadError
      false
    end
  end
end
