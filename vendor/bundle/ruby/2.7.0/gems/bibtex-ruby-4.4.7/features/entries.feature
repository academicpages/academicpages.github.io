Feature: Parse BibTeX preambles
	As a hacker who works with bibliographies
	I want to be able to parse BibTeX files with entries
	Because that's what BibTeX is all about

	Scenario: A BibTeX file with three books
		When I parse the following file:
		"""
		%% This BibTeX bibliography file was created using BibDesk.
		%% http://bibdesk.sourceforge.net/


		%% Created for Sylvester Keil at 2010-08-05 10:07:07 +0200 


		%% Saved with string encoding Unicode (UTF-8) 



		@book{rails,
			Address = {Raleigh, North Carolina},
			Author = {Ruby, Sam, and Thomas, Dave, and Hansson Heinemeier, David},
			Booktitle = {Agile Web Development with Rails},
			Date-Added = {2010-08-05 10:01:36 +0200},
			Date-Modified = {2010-08-05 10:06:46 +0200},
			Edition = {third},
			Isbn = {978-1-9343561-6-6},
			Keywords = {ruby, rails},
			Publisher = {The Pragmatic Bookshelf},
			Series = {The Facets of Ruby},
			Title = {Agile Web Development with Rails},
			Year = {2009}
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
		"""
		Then my bibliography should contain these books:
			| title                                                  | author                                                   | publisher               | year |
			| Agile Web Development with Rails                       | Ruby, Sam and Thomas, Dave and Hansson Heinemeier, David | The Pragmatic Bookshelf | 2009 |
			| Compilers: Principles, Techniques, and Tools           | Aho, Alfred V. and Lam, Monica S. and Ullman, Jeffrey D. | Addison Wesley          | 2007 |
			| Programming Ruby 1.9: The Pragmatic Programmer's Guide | Thomas, Dave and Fowler, Chad and Hunt, Andy             | The Pragmatic Bookshelf | 2009 |
		And my bibliography should contain 2 books published in 2009
		And my bibliography should contain a book with id "pickaxe"
		And my bibliography should contain a book with id "dragon"
