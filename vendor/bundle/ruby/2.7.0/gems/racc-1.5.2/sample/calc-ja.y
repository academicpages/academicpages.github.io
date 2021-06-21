#
#
# A simple calculator, version 2.
# This file contains Japanese characters (encoding=EUC-JP).

class Calculator2
  prechigh
    nonassoc UMINUS
    left '*' '/'
    left '+' '-'
  preclow
  options no_result_var
rule
  target  : exp
          | /* none */ { 0 }

  exp     : exp '+' exp { val[0] + val[2] }
          | exp '-' exp { val[0] - val[2] }
          | exp '*' exp { val[0] * val[2] }
          | exp '/' exp { val[0] / val[2] }
          | '(' exp ')' { val[1] }
          | '-' NUMBER  =UMINUS { -(val[1]) }
          | NUMBER
end

---- header
#
---- inner
  
  def evaluate(str)
    @tokens = []
    until str.empty?
      case str
      when /\A\s+/
        ;
      when /\A\d+/
        @tokens.push [:NUMBER, $&.to_i]
      when /\A.|\n/
        s = $&
        @tokens.push [s, s]
      end
      str = $'
    end
    @tokens.push [false, '$']
    do_parse
  end

  def next_token
    @tokens.shift
  end

---- footer

puts 'Ä¶¹ë²ÚÅÅÂî 2 ¹æµ¡'
puts 'Q ¤Ç½ªÎ»¤·¤Ş¤¹'
calc = Calculator2.new
while true
  print '>>> '; $stdout.flush
  str = $stdin.gets.strip
  break if /q/i =~ str
  begin
    p calc.evaluate(str)
  rescue ParseError
    puts 'parse error'
  end
end
