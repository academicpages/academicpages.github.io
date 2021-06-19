
require 'enumerator'
require 'forwardable'
require 'open-uri'
require 'singleton'
require 'set'
require 'time'

require 'namae'

require 'csl/version'

require 'csl/compatibility'
require 'csl/extensions'
require 'csl/errors'

require 'csl/schema'

require 'csl/pretty_printer'
require 'csl/loader'
require 'csl/parser'
require 'csl/treelike'
require 'csl/node'

require 'csl/info'
require 'csl/date_part'

require 'csl/locale'
require 'csl/locale/date'
require 'csl/locale/term'
require 'csl/locale/style_options'

require 'csl/name_options'

require 'csl/style'
require 'csl/style/bibliography'
require 'csl/style/citation'
require 'csl/style/sort'
require 'csl/style/choose'
require 'csl/style/date'
require 'csl/style/group'
require 'csl/style/label'
require 'csl/style/layout'
require 'csl/style/macro'
require 'csl/style/names'
require 'csl/style/number'
require 'csl/style/text'

module CSL

  module_function

  def parse(*arguments)
    Parser.instance.parse(*arguments)
  end

  def parse!(*arguments)
    Parser.instance.parse!(*arguments)
  end

  def validate(node)
    Schema.validate(node)
  end

  def valid?(node)
    Schema.valid?(node)
  end

end
