module CiteProc

  module Attributes
    extend Forwardable

    def self.included(base)
      base.extend(ClassMethods)
    end

    def attributes
      @attributes ||= {}
    end

    def_delegators :attributes, :length, :empty?, :values_at, :key?, :value?

    alias size length

    def read_attribute(key)
      attributes[filter_key(key)]
    end
    alias [] read_attribute

    def write_attribute(key, value)
      attributes[filter_key(key)] = filter_value(value, key)
    end
    alias []= write_attribute

    def attribute?(key)
      # this method is used only for conditional type access.
      # When included on an object with read observations, don't count this as an observable read
      if respond_to? :unobservable_read_attribute
        value = unobservable_read_attribute key
      else
        value = read_attribute key
      end

      return false if value.nil?
      return false if value.respond_to?(:empty?) && value.empty?

      value.to_s !~ /^(false|no|never)$/i
    end

    def filter_key(key)
      key.to_sym
    end

    def filter_value(value, key = nil)
      value.respond_to?(:deep_copy) ? value.deep_copy : value.dup
    rescue
      value
    end

    def merge(other)
      return self if other.nil?

      case
      when other.is_a?(String) && /^\s*\{/ =~ other
        other = ::JSON.parse(other, :symbolize_names => true)
      when other.respond_to?(:each_pair)
        # do nothing
      when other.respond_to?(:to_hash)
        other = other.to_hash
      else
        raise ParseError, "failed to merge attributes and #{other.inspect}"
      end

      other.each_pair do |key, value|
        attributes[filter_key(key)] = filter_value(value, key)
      end

      self
    end
    alias update merge

    def reverse_merge(other)
      fail "not implemented yet"
    end

    def to_hash
      attributes.deep_copy
    end

    # @return [Hash] a hash-based representation of the attributes
    def to_citeproc
      Hash[attributes.map { |k,v|
        [k.to_s, v.respond_to?(:to_citeproc) ? v.to_citeproc : v.to_s]
      }]
    end

    # @return [String] a JSON string representation of the attributes
    def to_json
      ::JSON.dump(to_citeproc)
    end

    # Don't expose internals to public API
    private :filter_key, :filter_value

    # initialize_copy should be able to access attributes
    protected :attributes


    # Two Attribute-based objects are equal if they are the same object,
    # or if all their attributes are equal using _#eql?_.
    #
    # @param other [Object] the other object
    # @return [Boolean] whether or not self and passed-in object are equal
    def eql?(other)
      case
      when equal?(other)
        true
      when self.class != other.class, length != other.length
        false
      else
        other.attributes.each_pair do |key, value|
          return false unless attributes[key].eql?(value)
        end

        true
      end
    end

    # @return [Fixnum] a hash value based on the object's attributes
    def hash
      digest = size
      attributes.each do |attribute|
        digest ^= attribute.hash
      end

      digest
    end

    module ClassMethods

      def create(parameters)
        create!(parameters)
      rescue
        nil
      end

      def create!(parameters)
        new.merge(parameters)
      end

      def attr_predicates(*arguments)
        arguments.flatten.each do |field|
          field, default = *(field.is_a?(Hash) ? field.to_a.flatten : [field])
          attr_field(field, default, true)
        end
      end

      def attr_fields(*arguments)
        arguments.flatten.each do |field|
          attr_field(*(field.is_a?(Hash) ? field.to_a.flatten : [field]))
        end
      end

      def attr_field(field, default = nil, predicate = false)
        method_id = field.to_s.downcase.gsub(/[-\s]+/, '_')

        unless instance_methods.include?(method_id)
          if default
            define_method(method_id) do
              read_attribute field
            end
          else
            define_method(method_id) do
              attributes[filter_key(field)] ||= default
            end
          end
        end

        writer_id = [method_id,'='].join
        unless instance_methods.include?(writer_id)
          define_method(writer_id) do |value|
            write_attribute field, value
          end
        end

        predicate_id = [method_id, '?'].join
        if predicate && !instance_methods.include?(predicate_id)
          define_method(predicate_id) do
            attribute?(field)
          end

          has_predicate = ['has_', predicate_id].join
          alias_method(has_predicate, predicate_id) unless instance_methods.include?(has_predicate)
        end
      end

    end

  end
end
