module CiteProc

  module Utilities

    # call-seq:
    # process(mode = :bibliography, items, options = {})
    def process(*arguments)
    end

    def cite(items, options = {})
      process(:citation, items, options)
    end

    def bibliography(items, options = {})
      process(:bibliography, items, options)
    end

  end

end
