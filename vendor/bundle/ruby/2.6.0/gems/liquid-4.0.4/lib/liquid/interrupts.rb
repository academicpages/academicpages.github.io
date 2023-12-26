module Liquid
  # An interrupt is any command that breaks processing of a block (ex: a for loop).
  class Interrupt
    attr_reader :message

    def initialize(message = nil)
      @message = message || "interrupt".freeze
    end
  end

  # Interrupt that is thrown whenever a {% break %} is called.
  class BreakInterrupt < Interrupt; end

  # Interrupt that is thrown whenever a {% continue %} is called.
  class ContinueInterrupt < Interrupt; end
end
