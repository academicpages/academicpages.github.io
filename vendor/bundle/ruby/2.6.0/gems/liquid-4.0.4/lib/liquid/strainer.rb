require 'set'

module Liquid
  # Strainer is the parent class for the filters system.
  # New filters are mixed into the strainer class which is then instantiated for each liquid template render run.
  #
  # The Strainer only allows method calls defined in filters given to it via Strainer.global_filter,
  # Context#add_filters or Template.register_filter
  class Strainer #:nodoc:
    @@global_strainer = Class.new(Strainer) do
      @filter_methods = Set.new
    end
    @@strainer_class_cache = Hash.new do |hash, filters|
      hash[filters] = Class.new(@@global_strainer) do
        @filter_methods = @@global_strainer.filter_methods.dup
        filters.each { |f| add_filter(f) }
      end
    end

    def initialize(context)
      @context = context
    end

    class << self
      attr_reader :filter_methods
    end

    def self.add_filter(filter)
      raise ArgumentError, "Expected module but got: #{filter.class}" unless filter.is_a?(Module)
      unless self.include?(filter)
        invokable_non_public_methods = (filter.private_instance_methods + filter.protected_instance_methods).select { |m| invokable?(m) }
        if invokable_non_public_methods.any?
          raise MethodOverrideError, "Filter overrides registered public methods as non public: #{invokable_non_public_methods.join(', ')}"
        else
          send(:include, filter)
          @filter_methods.merge(filter.public_instance_methods.map(&:to_s))
        end
      end
    end

    def self.global_filter(filter)
      @@strainer_class_cache.clear
      @@global_strainer.add_filter(filter)
    end

    def self.invokable?(method)
      @filter_methods.include?(method.to_s)
    end

    def self.create(context, filters = [])
      @@strainer_class_cache[filters].new(context)
    end

    def invoke(method, *args)
      if self.class.invokable?(method)
        send(method, *args)
      elsif @context && @context.strict_filters
        raise Liquid::UndefinedFilter, "undefined filter #{method}"
      else
        args.first
      end
    rescue ::ArgumentError => e
      raise Liquid::ArgumentError, e.message, e.backtrace
    end
  end
end
