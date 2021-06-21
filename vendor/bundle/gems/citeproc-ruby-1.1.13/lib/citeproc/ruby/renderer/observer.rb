module CiteProc
  module Ruby

    class Renderer

      class ItemObserver
        attr_accessor :history, :item

        def initialize(item, history = {})
          @item, @history = item, history
        end

        def start
          item.add_observer(self)
          self
        end

        def stop
          item.delete_observer(self)
          self
        end

        def update(method, key, value)
          history[key] = value if method == :read
        end

        def skip?
          !history.empty? && history.values.all? { |v|
            v.nil? || v.respond_to?(:empty?) && v.empty?
          }
        end

        def accessed
          history.select { |key, value| !value.nil? }.keys
        end

        def clear!
          history.clear
          self
        end
      end

    end

  end
end
