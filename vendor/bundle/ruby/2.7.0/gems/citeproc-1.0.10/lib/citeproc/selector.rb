
module CiteProc

  class Selector

    @types = [:all, :any, :none].freeze
    @matcher = Hash[*@types.zip([:all?, :any?, :none?]).flatten].freeze

    @rb2cp = Hash[*(@types + [:skip]).zip(%w{
      select include exclude quash
    }).flatten]

    @cp2rb = @rb2cp.invert.freeze
    @rb2cp.freeze

    class << self
      attr_reader :types, :matcher, :rb2cp, :cp2rb
    end

    attr_reader :type, :conditions, :skip_conditions, :custom_matcher

    def initialize(attributes = nil)
      @conditions, @skip_conditions = {}, {}

      if block_given?
        @type = :ruby

      else
        unless attributes.nil? || attributes.empty?
          attributes.symbolize_keys.each_pair do |key, conditions|
            conditions = convert_conditions(conditions) if conditions.is_a?(Array)

            case key
            when :all, :any, :none
              @type = key
              @conditions.merge!(conditions)

            when :select, :include, :exclude
              @type = Selector.cp2rb[key.to_s]
              @conditions.merge!(conditions)

            when :skip, :quash
              @skip_conditions.merge!(conditions)

            else
              raise TypeError, "failed to create selector from #{key.inspect}"
            end
          end
        end
      end
    end

    def initialize_copy(other)
      @type = other.type
      @conditions = other.conditions.deep_copy
      @skip_conditions = other.skip_conditions.deep_copy
      @custom_matcher = other
    end

    def type=(type)
      raise TypeError, "failed to set selector type to #{type.inspect}" unless
        type.respond_to(:to_sym) && Selector.types.include?(type.to_sym)

      @type = type.to_sym
    end

    def empty?
      type.nil? && skip_conditions.empty?
    end

    def custom_matcher?
      defined?(@custom_matcher)
    end

    alias ruby? custom_matcher?

    def matches?(item)
      if custom_matcher?
        custom_matcher.call(item)
      else
        conditions.each_pair.send(matcher) do |field, value|
          item[field].to_s == value.to_s
        end
      end
    end

    def skip?(item)
      if custom_matcher? || skip_conditions.empty?
        false # skips are ignored for custom matchers
      else
        skip_conditions.each_pair.all? do |field, value|
          item[field].to_s == value.to_s
        end
      end
    end

    def to_proc
      Proc.new { |item| matches?(item) && !skip?(item) }
    end

    def to_citeproc
      return nil if empty? || custom_matcher?

      cp = {}
      cp[Selector.rb2cp[type]] = conditions.map do |field, value|
        { 'field' => field.to_s, 'value' => value.to_s }
      end unless conditions.empty?

      cp['quash'] = skip_conditions.map do |field, value|
        { 'field' => field.to_s, 'value' => value.to_s }
      end unless skip_conditions.empty?

      cp
    end

    def to_json
      ::JSON.dump(to_citeproc)
    end

    private

    def matcher
      Selector.matcher[type] || :all?
    end

    # Converts a CiteProc-JS style conditions list into
    # a conditions Hash.
    def convert_conditions(conditions)
      Hash[conditions.map { |c| [c['field'], c['value']] }]
    end

  end

end
