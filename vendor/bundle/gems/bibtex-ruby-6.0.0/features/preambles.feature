Feature: Parse BibTeX preambles
	As a hacker who works with bibliographies
	I want to be able to parse BibTeX files with preambles
	Because they are part of the BibTeX format

	Scenario: A BibTeX file with preambles and strings
		When I parse the following file:
		"""
		%%
		%% This is a valid BibTeX File
		%%

		% Testing preamble statements

		@preamble{"This bibliography was created \today"}
		@preamble {  "Bib\TeX"  }

		@string{ maintainer = "Myself"}

		@preamble { "Maintained by " # maintainer }
		"""
		Then my bibliography should contain the following objects:
			| type     | value                                 |
			| preamble | This bibliography was created \\today |
			| preamble | Bib\\TeX                              |
			| string   | Myself                                |
			| preamble | "Maintained by " # maintainer         |