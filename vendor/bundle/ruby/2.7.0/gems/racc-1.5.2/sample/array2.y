#
#
# Converting Array-like string into Ruby's Array, version 2.
# This grammer uses no_result_var.

class ArrayParser2
  options no_result_var
rule
  array   : '[' contents ']' { val[1] }
          | '[' ']'          { [] }

  contents: ITEM              { val }
          | contents ',' ITEM { val[0].push val[2]; val[0] }
end

---- inner

  def parse(str)
    @str = str
    yyparse self, :scan
  end

  def scan
    str = @str.strip
    until str.empty?
      case str
      when /\A\s+/
        str = $'
      when /\A\w+/
        yield :ITEM, $&
        str = $'
      else
        c = str[0,1]
        yield c, c
        str = str[1..-1]
      end
    end
    yield false, '$'   # is optional from Racc 1.3.7
  end

  def next_token
    @q.shift
  end

---- footer

if $0 == __FILE__
  src = <<EOS
[
  a, b, c,
  d,
  e ]
EOS
  puts 'parsing:'
  print src
  puts
  puts 'result:'
  p ArrayParser2.new.parse(src)
end
