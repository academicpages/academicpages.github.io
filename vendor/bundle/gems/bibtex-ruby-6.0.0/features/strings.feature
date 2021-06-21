Feature: BibTeX Strings
	As a hacker who works with bibliographies
	I want to be able to parse BibTeX files containing string assignments

	@string
	Scenario: A BibTeX file with string assignments
		When I parse the following file:
		"""
		%%
		%% This is a valid BibTeX file
		%% String assignments Test
		%%

		@string{foo="bar"}
		@ string{foo="bar"}
		@string {foo="bar"}
		@string{ foo="bar"}
		@string{foo ="bar"}
		@string{foo= "bar"}
		@string{foo="bar" }
		@ string { foo = "bar" }
		@string   { foo=   "bar"}
		@string{ foo = "bar" }

		@string{foo="bar"}
		@string{foo="'bar'"}
		@string{foo="{"}bar{"}"}

		Using some interesting symbols
		@string{foo="@bar@"}
		@string{foo="'bar'"}
		@string{foo="{"}bar{"}"}
		@string{foo="{bar}"}
		"""
		Then my bibliography should contain the following objects:
			| type     | value     |
			| string   | bar       |
			| string   | bar       |
			| string   | bar       |
			| string   | bar       |
			| string   | bar       |
			| string   | bar       |
			| string   | bar       |
			| string   | bar       |
			| string   | bar       |
			| string   | bar       |
			| string   | bar       |
			| string   | 'bar'     |
			| string   | {"}bar{"} |
			| string   | @bar@     |
			| string   | 'bar'     |
			| string   | {"}bar{"} |
			| string   | {bar}     |
