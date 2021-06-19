Feature: Searching in BibTeX bibliographies
	As a hacker who writes academic papers
	I want to be able to search my bibliographies
	In order to find the references I need
	
	Scenario: Find entries in a simple bibliography
		Given the bibliography:
		"""
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
		@article{a1,
			Keywords = {@book}
		}
		@book{dragon,
			Address = {Boston},
			Author = {Aho, Alfred V., and Lam, Monica S., and Ullman, Jeffrey D.},
			Booktitle = {Compilers: Principles, Techniques, and Tools},
			Date-Added = {2010-08-05 09:57:15 +0200},
			Date-Modified = {2010-08-05 10:06:32 +0200},
			Edition = {second},
			Keywords = {compiler, lex, yacc},
			Publisher = {Addison Wesley},
			Title = {Compilers: Principles, Techniques, and Tools},
			Year = {2007}
		}
		"""
		When I search for "pickaxe"
		Then there should be exactly 1 match
		When I search for :pickaxe
		Then there should be exactly 1 match
		When I search for "camel"
		Then there should be exactly 0 matches
		When I search for "@book"
		Then there should be exactly 2 matches
		When I search for /@book/
		Then there should be exactly 3 matches
		When I search for "@book[]"
		Then there should be exactly 2 matches
		When I search for "@book[year=2007]"
		Then there should be exactly 1 match
		When I search for "@book[year=2009, keywords=ruby]"
		Then there should be exactly 1 match
		When I search for "@book[year=2009, keywords=yacc]"
		Then there should be exactly 0 matches
		When I search for "@book, @article"
		Then there should be exactly 3 matches
		When I search for "@entry"
		Then there should be exactly 3 matches
		When I search for "@*"
		Then there should be exactly 3 matches
		When I search for "@*[year=2007]"
		Then there should be exactly 1 match
		When I search for "@*[keywords!~lex]"
		Then there should be exactly 2 matches
		
	@query
	Scenario: Find entries using compound queries
		Given the bibliography:
		"""
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
		@article{a1,
		  Title = {An Article},
			Keywords = {@book}
		}
		@book{dragon,
			Address = {Boston},
			Author = {Aho, Alfred V., and Lam, Monica S., and Ullman, Jeffrey D.},
			Booktitle = {Compilers: Principles, Techniques, and Tools},
			Date-Added = {2010-08-05 09:57:15 +0200},
			Date-Modified = {2010-08-05 10:06:32 +0200},
			Edition = {second},
			Keywords = {compiler, lex, yacc},
			Publisher = {Addison Wesley},
			Title = {Compilers: Principles, Techniques, and Tools},
			Year = {2007}
		}
		"""
		When I search for "@*[keywords = @book || edition = second]"
		Then there should be exactly 2 matches
		When I search for "@*[keywords = @book && edition = second]"
		Then there should be exactly 0 matches
		When I search for "@*[keywords = @book && title ~= Article]"
		Then there should be exactly 1 match
