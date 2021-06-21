Feature: BibTeX String Replacement
	As a hacker who works with bibliographies
	I want to be able to parse BibTeX files with string assignments
	And replace string symbols in other values
	Because that is a cool BibTeX feature
	
	@string @replacement
	Scenario: A BibTeX file with string assignments and symbols
		When I parse the following file:
		"""
		%%
		%% A valid BibTeX file
		%% String assignment and replacement
		%%

		@string{ foo = "foo" }
		@string{ bar = "bar" }
		@string{ foobar = foo # "bar" }
		@string{ foobarfoo = foobar # foo }
		@string{ barfoobar = bar # "foo" # bar }

		@preamble { "foo" # foo # foobarfoo # "bar" }

		@manual {manual:1,
			title = "foo" # barfoobar
		}
		"""
		Then my bibliography should contain these strings:
			| value             |
			| foo               |
			| bar               |
			| foo # "bar"       |
			| foobar # foo      |
			| bar # "foo" # bar |
		And my bibliography should contain these preambles:
			| content                         |
			| "foo" # foo # foobarfoo # "bar" |
		And my bibliography should contain these manuals:
			| title             |
			| "foo" # barfoobar |
		When I replace all strings in my bibliography
		Then my bibliography should contain these strings:
			| content                           |
			| foo = "foo"                       |
			| bar = "bar"                       |
			| foobar = "foo" # "bar"            |
			| foobarfoo = "foo" # "bar" # "foo" |
			| barfoobar = "bar" # "foo" # "bar" |
		And my bibliography should contain these preambles:
			| content                                       |
			| "foo" # "foo" # "foo" # "bar" # "foo" # "bar" |
		And my bibliography should contain these manuals:
			| title                         |
			| "foo" # "bar" # "foo" # "bar" |
		When I join all strings in my bibliography
		Then my bibliography should contain these strings:
			| content                 |
			| foo = "foo"             |
			| bar = "bar"             |
			| foobar = "foobar"       |
			| foobarfoo = "foobarfoo" |
			| barfoobar = "barfoobar" |
		And my bibliography should contain these preambles:
			| content              |
			| "foofoofoobarfoobar" |
		And my bibliography should contain these manuals:
			| title        |
			| foobarfoobar |
