module Liquid
  class Parser
    def initialize(input)
      l = Lexer.new(input)
      @tokens = l.tokenize
      @p = 0 # pointer to current location
    end

    def jump(point)
      @p = point
    end

    def consume(type = nil)
      token = @tokens[@p]
      if type && token[0] != type
        raise SyntaxError, "Expected #{type} but found #{@tokens[@p].first}"
      end
      @p += 1
      token[1]
    end

    # Only consumes the token if it matches the type
    # Returns the token's contents if it was consumed
    # or false otherwise.
    def consume?(type)
      token = @tokens[@p]
      return false unless token && token[0] == type
      @p += 1
      token[1]
    end

    # Like consume? Except for an :id token of a certain name
    def id?(str)
      token = @tokens[@p]
      return false unless token && token[0] == :id
      return false unless token[1] == str
      @p += 1
      token[1]
    end

    def look(type, ahead = 0)
      tok = @tokens[@p + ahead]
      return false unless tok
      tok[0] == type
    end

    def expression
      token = @tokens[@p]
      if token[0] == :id
        variable_signature
      elsif [:string, :number].include? token[0]
        consume
      elsif token.first == :open_round
        consume
        first = expression
        consume(:dotdot)
        last = expression
        consume(:close_round)
        "(#{first}..#{last})"
      else
        raise SyntaxError, "#{token} is not a valid expression"
      end
    end

    def argument
      str = ""
      # might be a keyword argument (identifier: expression)
      if look(:id) && look(:colon, 1)
        str << consume << consume << ' '.freeze
      end

      str << expression
      str
    end

    def variable_signature
      str = consume(:id)
      while look(:open_square)
        str << consume
        str << expression
        str << consume(:close_square)
      end
      if look(:dot)
        str << consume
        str << variable_signature
      end
      str
    end
  end
end
