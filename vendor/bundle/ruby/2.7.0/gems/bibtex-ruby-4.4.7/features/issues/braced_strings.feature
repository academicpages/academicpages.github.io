Feature: BibTeX Braced Strings
	As a hacker who works with bibliographies
	I want to be able to parse BibTeX files containing string definitions using braced expressions
	Because applications such as BibDesk produce that format

	@string
	Scenario: A simple string assignment
		When I parse the following file:
		"""
		@string{ foo = {foo} }
		"""
		Then my bibliography should contain 1 string
		
	@string @replacement
	Scenario: A BibTeX file with string assignments
		When I parse the following file:
		"""
		Simple strings:
		@string{ foo1 = {foo} }
		@string{ foo2 = {foo}}
		@string{ foo3 ={foo}}
		@string{foo4={foo}}
		@string{ foo5 = {"foo" bar} }
		@string{ foo6 = {"foo" bar{"}} }
		
		Compound strings:
		@string{ foo7 = foo1 }
		@string{ foo8 = foo1 # {bar} }
		@string{ foo9 = {foo } # {bar} }
		
		"""
		Then my bibliography should contain 9 strings
		And my bibliography should contain these strings:
			| value            |
			| foo              |
			| foo              |
			| foo              |
			| foo              |
			| "foo" bar        |
			| "foo" bar{"}     |
			| foo1             |
			| foo1 # "bar"     |
			| "foo " # "bar"   |
		When I replace and join all strings in my bibliography
		Then the string "foo7" should be "foo"
		And the string "foo8" should be "foobar"
		And the string "foo9" should be "foo bar"
		
