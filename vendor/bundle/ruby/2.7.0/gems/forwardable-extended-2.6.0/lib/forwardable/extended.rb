# ----------------------------------------------------------------------------
# Frozen-string-literal: true
# Copyright: 2015-2016 Jordon Bedwell - MIT License
# Encoding: utf-8
# ----------------------------------------------------------------------------

require "forwardable/extended/version"
require "forwardable"

module Forwardable
  module Extended

    # ------------------------------------------------------------------------
    # Make our methods private on the class, there is no reason for public.
    # ------------------------------------------------------------------------

    def self.extended(klass)
      instance_methods.each do |method|
        klass.private_class_method(
          method
        )
      end
    end

    # ------------------------------------------------------------------------
    # Delegate using a Rails-like interface.
    # ------------------------------------------------------------------------

    def rb_delegate(method, to: nil, alias_of: method, **kwd)
      raise ArgumentError, "to must be provided" unless to
      def_delegator(
        to, alias_of, method, **kwd
      )
    end

    # ------------------------------------------------------------------------
    # Delegate a method to a hash and key.
    # ------------------------------------------------------------------------

    def def_hash_delegator(hash, method, key: method, **kwd)
      prefix, suffix, wrap = prepare_delegate(**kwd)

      if suffix
        method = method.to_s.gsub(
          /\?$/, ""
        )
      end

      class_eval delegate_debug(<<-STR), __FILE__, __LINE__ - 9
        def #{method}#{suffix}(*args)
          #{wrap}(
            #{prefix}#{hash}[#{key.inspect}]
          )

        rescue Exception
          if !Forwardable.debug && $@ && $@.respond_to?(:delete_if)
            $@.delete_if do |source|
              source =~ %r"#{Regexp.escape(__FILE__)}"o
            end
          end

          raise
        end
      STR
    end

    # ------------------------------------------------------------------------
    # Delegate a method to an instance variable.
    # ------------------------------------------------------------------------

    def def_ivar_delegator(ivar, alias_ = ivar, **kwd)
      prefix, suffix, wrap = prepare_delegate(**kwd)

      if suffix
        alias_ = alias_.to_s.gsub(
          /\?$/, ""
        )
      end

      class_eval delegate_debug(<<-STR), __FILE__, __LINE__ - 9
        def #{alias_.to_s.gsub(/\A@/, "")}#{suffix}
          #{wrap}(
            #{prefix}#{ivar}
          )

        rescue Exception
          if !Forwardable.debug && $@ && $@.respond_to?(:delete_if)
            $@.delete_if do |source|
              source =~ %r"#{Regexp.escape(__FILE__)}"o
            end
          end

          raise
        end
      STR
    end

    # ------------------------------------------------------------------------
    # Like def_delegator but allows you to send args and do other stuff.
    # ------------------------------------------------------------------------

    def def_modern_delegator(accessor, method, alias_ = method, args: \
        { :before => [], :after => [] }, **kwd)

      prefix, suffix, wrap = prepare_delegate(**kwd)
      args = { :before => args } unless args.is_a?(Hash)
      b = [args[:before]].flatten.compact.map(&:to_s).join(", ")
      a = [args[ :after]].flatten.compact.map(&:to_s).join(", ")
      b = b + ", " unless args[:before].nil? || args[:before].empty?
      a = ", " + a unless args[ :after].nil? || args[ :after].empty?
      alias_ = alias_.to_s.gsub(/\?$/, "") if suffix

      class_eval delegate_debug(<<-STR), __FILE__, __LINE__ - 10
        def #{alias_}#{suffix}(*args, &block)
          #{wrap}(#{prefix}#{accessor}.send(
            #{method.inspect}, #{b}*args#{a}, &block
          ))

        rescue Exception
          if !Forwardable.debug && $@ && $@.respond_to?(:delete_if)
            $@.delete_if do |source|
              source =~ %r"#{Regexp.escape(__FILE__)}"o
            end
          end

          raise
        end
      STR
    end

    # ------------------------------------------------------------------------
    # Wraps around traditional delegation and modern delegation.
    # ------------------------------------------------------------------------

    def def_delegator(accessor, method, alias_ = method, **kwd)
      kwd, alias_ = alias_, method if alias_.is_a?(Hash) && !kwd.any?

      if alias_.is_a?(Hash) || !kwd.any?
        Forwardable.instance_method(:def_delegator).bind(self) \
          .call(accessor, method, alias_)

      elsif !kwd[:type]
        def_modern_delegator(
          accessor, method, alias_, **kwd
        )

      else
        raise ArgumentError, "Alias not supported." if alias_ != method
        send("def_#{kwd[:type]}_delegator", accessor, method, **kwd.tap do |obj|
          obj.delete(:type)
        end)
      end
    end

    # ------------------------------------------------------------------------
    # Create multiple delegates at once.
    # ------------------------------------------------------------------------

    def def_delegators(accessor, *methods)
      kwd = methods.shift if methods.first.is_a?(Hash)
      kwd = methods.pop   if methods. last.is_a?(Hash)
      kwd = {} unless kwd

      methods.each do |method|
        def_delegator accessor, method, **kwd
      end
    end

    # ------------------------------------------------------------------------
    # Prepares a delegate and it's few arguments.
    # ------------------------------------------------------------------------

    private
    def prepare_delegate(wrap: nil, bool: false)
      prefix = (bool == :reverse ? "!!!" : "!!") if bool
      wrap   = "self.class.new" if wrap.is_a?(TrueClass)
      suffix = "?" if bool

      return [
        prefix, suffix, wrap
      ]
    end

    # ------------------------------------------------------------------------

    private
    def delegate_debug(str)
      if Forwardable.debug && !Forwardable.debug.is_a?(TrueClass)
        then Forwardable.debug.debug(
          str
        )

      elsif Forwardable.debug
        $stdout.puts(
          "\n# ------\n\n", str
        )
      end

      str
    end
  end
end
