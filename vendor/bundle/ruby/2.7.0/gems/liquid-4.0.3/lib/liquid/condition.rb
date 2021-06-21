module Liquid
  # Container for liquid nodes which conveniently wraps decision making logic
  #
  # Example:
  #
  #   c = Condition.new(1, '==', 1)
  #   c.evaluate #=> true
  #
  class Condition #:nodoc:
    @@operators = {
      '=='.freeze => ->(cond, left, right) {  cond.send(:equal_variables, left, right) },
      '!='.freeze => ->(cond, left, right) { !cond.send(:equal_variables, left, right) },
      '<>'.freeze => ->(cond, left, right) { !cond.send(:equal_variables, left, right) },
      '<'.freeze  => :<,
      '>'.freeze  => :>,
      '>='.freeze => :>=,
      '<='.freeze => :<=,
      'contains'.freeze => lambda do |cond, left, right|
        if left && right && left.respond_to?(:include?)
          right = right.to_s if left.is_a?(String)
          left.include?(right)
        else
          false
        end
      end
    }

    def self.operators
      @@operators
    end

    attr_reader :attachment, :child_condition
    attr_accessor :left, :operator, :right

    def initialize(left = nil, operator = nil, right = nil)
      @left = left
      @operator = operator
      @right = right
      @child_relation  = nil
      @child_condition = nil
    end

    def evaluate(context = Context.new)
      condition = self
      result = nil
      loop do
        result = interpret_condition(condition.left, condition.right, condition.operator, context)

        case condition.child_relation
        when :or
          break if result
        when :and
          break unless result
        else
          break
        end
        condition = condition.child_condition
      end
      result
    end

    def or(condition)
      @child_relation = :or
      @child_condition = condition
    end

    def and(condition)
      @child_relation = :and
      @child_condition = condition
    end

    def attach(attachment)
      @attachment = attachment
    end

    def else?
      false
    end

    def inspect
      "#<Condition #{[@left, @operator, @right].compact.join(' '.freeze)}>"
    end

    protected

    attr_reader :child_relation

    private

    def equal_variables(left, right)
      if left.is_a?(Liquid::Expression::MethodLiteral)
        if right.respond_to?(left.method_name)
          return right.send(left.method_name)
        else
          return nil
        end
      end

      if right.is_a?(Liquid::Expression::MethodLiteral)
        if left.respond_to?(right.method_name)
          return left.send(right.method_name)
        else
          return nil
        end
      end

      left == right
    end

    def interpret_condition(left, right, op, context)
      # If the operator is empty this means that the decision statement is just
      # a single variable. We can just poll this variable from the context and
      # return this as the result.
      return context.evaluate(left) if op.nil?

      left = context.evaluate(left)
      right = context.evaluate(right)

      operation = self.class.operators[op] || raise(Liquid::ArgumentError.new("Unknown operator #{op}"))

      if operation.respond_to?(:call)
        operation.call(self, left, right)
      elsif left.respond_to?(operation) && right.respond_to?(operation) && !left.is_a?(Hash) && !right.is_a?(Hash)
        begin
          left.send(operation, right)
        rescue ::ArgumentError => e
          raise Liquid::ArgumentError.new(e.message)
        end
      end
    end

    class ParseTreeVisitor < Liquid::ParseTreeVisitor
      def children
        [
          @node.left, @node.right,
          @node.child_condition, @node.attachment
        ].compact
      end
    end
  end

  class ElseCondition < Condition
    def else?
      true
    end

    def evaluate(_context)
      true
    end
  end
end
