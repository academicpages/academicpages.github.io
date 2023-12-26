module Liquid
  class ForloopDrop < Drop
    def initialize(name, length, parentloop)
      @name = name
      @length = length
      @parentloop = parentloop
      @index = 0
    end

    attr_reader :name, :length, :parentloop

    def index
      @index + 1
    end

    def index0
      @index
    end

    def rindex
      @length - @index
    end

    def rindex0
      @length - @index - 1
    end

    def first
      @index == 0
    end

    def last
      @index == @length - 1
    end

    protected

    def increment!
      @index += 1
    end
  end
end
