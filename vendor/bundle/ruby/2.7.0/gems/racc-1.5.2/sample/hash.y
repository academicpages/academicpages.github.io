#
#
# Converting Hash-like string into Ruby's Hash.

class HashParser
  options no_result_var
rule
  hash    : '{' contents '}'   { val[1] }
          | '{' '}'            { Hash.new }
           
                  # Racc can handle string over 2 bytes.
  contents: IDENT '=>' IDENT              { {val[0] => val[2]} }
          | contents ',' IDENT '=>' IDENT { val[0][val[2]] = val[4]; val[0] }
end

---- inner

  def parse(str)
    @str = str
    yyparse self, :scan
  end

  private

  def scan
    str = @str
    until str.empty?
      case str
      when /\A\s+/
        str = $'
      when /\A\w+/
        yield :IDENT, $&
        str = $'
      when /\A=>/
        yield '=>', '=>'
        str = $'
      else
        c = str[0,1]
        yield c, c
        str = str[1..-1]
      end
    end
    yield false, '$'   # is optional from Racc 1.3.7
  end

---- footer

if $0 == __FILE__
  src = <<EOS
{
  name => MyName,
  id => MyIdent
}
EOS
  puts 'Parsing (String):'
  print src
  puts
  puts 'Result (Ruby Object):'
  p HashParser.new.parse(src)
end
