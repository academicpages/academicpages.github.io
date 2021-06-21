Feature: Parse BibTeX files with trailing commas
	As a hacker who works with bibliographies
	I want to be able to parse BibTeX files with a trailing comma

	Scenario: A BibTeX file with lots of objects and comments
		When I parse the following file:
		"""
		@article{rb2011,
		  author = {Keil, Sylvester},
		  title  = "BibTeX-Ruby",
		  year   = 2011,
		},

		@article{key03,
				year = 2000,
		    title = "A {bunch {of} braces {in}} title",
		},
		"""
		Then my bibliography should contain an entry with key "rb2011"
		And my bibliography should contain 1 articles published in 2011
		And my bibliography should contain an entry with key "key03"
