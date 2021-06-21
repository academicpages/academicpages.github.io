
# sudo dtrace -qs test/macruby.d -c "macruby -Ilib -rrubygems test/macruby.rb"

require 'bibtex'

input = <<-END
@book{pickaxe,
	Address = {Raleigh, North Carolina},
	Author = {Thomas, Dave, and Fowler, Chad, and Hunt, Andy},
	Date-Added = {2010-08-05 09:54:07 +0200},
	Date-Modified = {2010-08-05 10:07:01 +0200},
	Keywords = {ruby},
	Publisher = {The Pragmatic Bookshelf},
	Series = {The Facets of Ruby},
	Title = {Programming Ruby 1.9: The Pragmatic Programmer's Guide},
	Year = {2009}
}
END

lexer = BibTeX::Lexer.new
lexer.data = input * 100
lexer.analyse
