Feature: Keys containing non-ASCII characters
	As a hacker who works with bibliographies
	I want to parse BibTeX entries with keys containing non-ASCII characters
	Because they can occur in many languages other than English
	
	Scenario: An entry whose key contains a German umlaut
		When I parse the following file:
		"""
		@article{müller.2011,
		  author    = {Christian Müller},
		  title     = {Important article},
		  journal   = {Not so important journal},
		  volume    = {5},
		  year      = {2011}
		}
		"""
		Then my bibliography should contain an article with id "müller.2011"
