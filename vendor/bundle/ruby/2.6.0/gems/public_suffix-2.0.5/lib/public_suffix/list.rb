# = Public Suffix
#
# Domain name parser based on the Public Suffix List.
#
# Copyright (c) 2009-2017 Simone Carletti <weppos@weppos.net>

module PublicSuffix

  # A {PublicSuffix::List} is a collection of one
  # or more {PublicSuffix::Rule}.
  #
  # Given a {PublicSuffix::List},
  # you can add or remove {PublicSuffix::Rule},
  # iterate all items in the list or search for the first rule
  # which matches a specific domain name.
  #
  #   # Create a new list
  #   list =  PublicSuffix::List.new
  #
  #   # Push two rules to the list
  #   list << PublicSuffix::Rule.factory("it")
  #   list << PublicSuffix::Rule.factory("com")
  #
  #   # Get the size of the list
  #   list.size
  #   # => 2
  #
  #   # Search for the rule matching given domain
  #   list.find("example.com")
  #   # => #<PublicSuffix::Rule::Normal>
  #   list.find("example.org")
  #   # => nil
  #
  # You can create as many {PublicSuffix::List} you want.
  # The {PublicSuffix::List.default} rule list is used
  # to tokenize and validate a domain.
  #
  # {PublicSuffix::List} implements +Enumerable+ module.
  #
  class List
    include Enumerable

    DEFAULT_LIST_PATH = File.join(File.dirname(__FILE__), "..", "..", "data", "list.txt")

    # Gets the default rule list.
    #
    # Initializes a new {PublicSuffix::List} parsing the content
    # of {PublicSuffix::List.default_list_content}, if required.
    #
    # @return [PublicSuffix::List]
    def self.default(**options)
      @default ||= parse(File.read(DEFAULT_LIST_PATH), options)
    end

    # Sets the default rule list to +value+.
    #
    # @param [PublicSuffix::List] value
    #   The new rule list.
    #
    # @return [PublicSuffix::List]
    def self.default=(value)
      @default = value
    end

    # Sets the default rule list to +nil+.
    #
    # @return [self]
    def self.clear
      self.default = nil
      self
    end

    # rubocop:disable Metrics/MethodLength

    # Parse given +input+ treating the content as Public Suffix List.
    #
    # See http://publicsuffix.org/format/ for more details about input format.
    #
    # @param  string [#each_line] The list to parse.
    # @param  private_domain [Boolean] whether to ignore the private domains section.
    # @return [Array<PublicSuffix::Rule::*>]
    def self.parse(input, private_domains: true)
      comment_token = "//".freeze
      private_token = "===BEGIN PRIVATE DOMAINS===".freeze
      section = nil # 1 == ICANN, 2 == PRIVATE

      new do |list|
        input.each_line do |line|
          line.strip!
          case # rubocop:disable Style/EmptyCaseCondition

          # skip blank lines
          when line.empty?
            next

          # include private domains or stop scanner
          when line.include?(private_token)
            break if !private_domains
            section = 2

          # skip comments
          when line.start_with?(comment_token)
            next

          else
            list.add(Rule.factory(line, private: section == 2), reindex: false)

          end
        end
      end
    end
    # rubocop:enable Metrics/MethodLength


    # Gets the array of rules.
    #
    # @return [Array<PublicSuffix::Rule::*>]
    attr_reader :rules


    # Initializes an empty {PublicSuffix::List}.
    #
    # @yield [self] Yields on self.
    # @yieldparam [PublicSuffix::List] self The newly created instance.
    #
    def initialize
      @rules = []
      yield(self) if block_given?
      reindex!
    end


    # Creates a naive index for +@rules+. Just a hash that will tell
    # us where the elements of +@rules+ are relative to its first
    # {PublicSuffix::Rule::Base#labels} element.
    #
    # For instance if @rules[5] and @rules[4] are the only elements of the list
    # where Rule#labels.first is 'us' @indexes['us'] #=> [5,4], that way in
    # select we can avoid mapping every single rule against the candidate domain.
    def reindex!
      @indexes = {}
      @rules.each_with_index do |rule, index|
        tld = Domain.name_to_labels(rule.value).last
        @indexes[tld] ||= []
        @indexes[tld] << index
      end
    end

    # Gets the naive index, a hash that with the keys being the first label of
    # every rule pointing to an array of integers (indexes of the rules in @rules).
    def indexes
      @indexes.dup
    end


    # Checks whether two lists are equal.
    #
    # List <tt>one</tt> is equal to <tt>two</tt>, if <tt>two</tt> is an instance of
    # {PublicSuffix::List} and each +PublicSuffix::Rule::*+
    # in list <tt>one</tt> is available in list <tt>two</tt>, in the same order.
    #
    # @param [PublicSuffix::List] other
    #   The List to compare.
    #
    # @return [Boolean]
    def ==(other)
      return false unless other.is_a?(List)
      equal?(other) || rules == other.rules
    end
    alias eql? ==

    # Iterates each rule in the list.
    def each(*args, &block)
      @rules.each(*args, &block)
    end


    # Adds the given object to the list and optionally refreshes the rule index.
    #
    # @param [PublicSuffix::Rule::*] rule
    #   The rule to add to the list.
    # @param [Boolean] reindex
    #   Set to true to recreate the rule index
    #   after the rule has been added to the list.
    #
    # @return [self]
    #
    # @see #reindex!
    #
    def add(rule, reindex: true)
      @rules << rule
      reindex! if reindex
      self
    end
    alias << add

    # Gets the number of elements in the list.
    #
    # @return [Integer]
    def size
      @rules.size
    end

    # Checks whether the list is empty.
    #
    # @return [Boolean]
    def empty?
      @rules.empty?
    end

    # Removes all elements.
    #
    # @return [self]
    def clear
      @rules.clear
      reindex!
      self
    end

    # Finds and returns the most appropriate rule for the domain name.
    #
    # From the Public Suffix List documentation:
    #
    # - If a hostname matches more than one rule in the file,
    #   the longest matching rule (the one with the most levels) will be used.
    # - An exclamation mark (!) at the start of a rule marks an exception to a previous wildcard rule.
    #   An exception rule takes priority over any other matching rule.
    #
    # ## Algorithm description
    #
    # 1. Match domain against all rules and take note of the matching ones.
    # 2. If no rules match, the prevailing rule is "*".
    # 3. If more than one rule matches, the prevailing rule is the one which is an exception rule.
    # 4. If there is no matching exception rule, the prevailing rule is the one with the most labels.
    # 5. If the prevailing rule is a exception rule, modify it by removing the leftmost label.
    # 6. The public suffix is the set of labels from the domain
    #    which directly match the labels of the prevailing rule (joined by dots).
    # 7. The registered domain is the public suffix plus one additional label.
    #
    # @param  name [String, #to_s] The domain name.
    # @param  [PublicSuffix::Rule::*] default The default rule to return in case no rule matches.
    # @return [PublicSuffix::Rule::*]
    def find(name, default: default_rule, **options)
      rule = select(name, **options).inject do |l, r|
        return r if r.class == Rule::Exception
        l.length > r.length ? l : r
      end
      rule || default
    end

    # Selects all the rules matching given domain.
    #
    # Internally, the lookup heavily rely on the `@indexes`. The input is split into labels,
    # and we retriever from the index only the rules that end with the input label. After that,
    # a sequential scan is performed. In most cases, where the number of rules for the same label
    # is limited, this algorithm is efficient enough.
    #
    # If `ignore_private` is set to true, the algorithm will skip the rules that are flagged as private domain.
    # Note that the rules will still be part of the loop. If you frequently need to access lists
    # ignoring the private domains, you should create a list that doesn't include these domains setting the
    # `private_domains: false` option when calling {.parse}.
    #
    # @param  [String, #to_s] name The domain name.
    # @param  [Boolean] ignore_private
    # @return [Array<PublicSuffix::Rule::*>]
    def select(name, ignore_private: false)
      name = name.to_s
      indices = (@indexes[Domain.name_to_labels(name).last] || [])

      finder = @rules.values_at(*indices).lazy
      finder = finder.select { |rule| rule.match?(name) }
      finder = finder.select { |rule| !rule.private } if ignore_private
      finder.to_a
    end

    # Gets the default rule.
    #
    # @see PublicSuffix::Rule.default_rule
    #
    # @return [PublicSuffix::Rule::*]
    def default_rule
      PublicSuffix::Rule.default
    end

  end
end
