module Liquid
  class TablerowloopDrop < Drop
    def initialize(length, cols)
      @length = length
      @row = 1
      @col = 1
      @cols = cols
      @index = 0
    end

    attr_reader :length, :col, :row

    def index
      @index + 1
    end

    def index0
      @index
    end

    def col0
      @col - 1
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

    def col_first
      @col == 1
    end

    def col_last
      @col == @cols
    end

    protected

    def increment!
      @index += 1

      if @col == @cols
        @col = 1
        @row += 1
      else
        @col += 1
      end
    end
  end
end
