Feature: Keys containing '/' symbols
	As a hacker who works with bibliographies
	I want to parse BibTeX entries with keys containing slashes
	Because they frequently occur in key naming schemes
	
	Scenario: An entry taken from the DBLP
		When I parse the following file:
		"""
		@article{DBLP:journals/dq/RossinK99,
		  author    = {Donald F. Rossin and
		               Barbara D. Klein},
		  title     = {Data Errors in Neural Network and Linear Regression Models:
		               An Experimental Comparison},
		  journal   = {Data Quality Journal},
		  volume    = {5},
		  year      = {1999},
		  ee        = {http://www.dataquality.com/999KR.htm},
		  bibsource = {DBLP, http://dblp.uni-trier.de}
		}
		"""
		Then my bibliography should contain an article with id "DBLP:journals/dq/RossinK99"