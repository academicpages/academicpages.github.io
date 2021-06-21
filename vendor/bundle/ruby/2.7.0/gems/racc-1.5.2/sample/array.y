#
#
# convert Array-like string into Ruby's Array.

class ArrayParser

rule

array   : '[' contents ']'
            {
              result = val[1]
            }
        | '[' ']'
            {
              result = []
            }

contents: ITEM
            {
              result = val
            }
        | contents ',' ITEM
            {
              result.push val[2]
            }

---- inner

  def parse(str)
    str = str.strip
    @q = []
    until str.empty?
      case str
      when /\A\s+/
        str = $'
      when /\A\w+/
        @q.push [:ITEM, $&]
        str = $'
      else
        c = str[0,1]
        @q.push [c, c]
        str = str[1..-1]
      end
    end
    @q.push [false, '$']   # is optional from Racc 1.3.7
    do_parse
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
  p ArrayParser.new.parse(src)
end
