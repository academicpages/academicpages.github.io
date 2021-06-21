Feature: Keys containing '/' symbols
	As a hacker who works with bibliographies
	I want to export BibTeX entries to the CiteProc format
	
	Scenario: Numeric months
		When I parse the following file:
		"""
		@article{DBLP:journals/dq/RossinK99,
		  author    = {Donald F. Rossin and
		               Barbara D. Klein},
		  title     = {Data Errors in Neural Network and Linear Regression Models:
		               An Experimental Comparison},
		  journal   = {Data Quality Journal},
		  volume    = {5},
			month     = {9},
		  year      = {1999},
		  ee        = {http://www.dataquality.com/999KR.htm},
		  bibsource = {DBLP, http://dblp.uni-trier.de}
		}
		"""
		Then my bibliography should contain these articles:
			| year | month |
			| 1999 | sep   |

	Scenario: Full month names
		When I parse the following file:
		"""
		@article{DBLP:journals/dq/RossinK99,
		  author    = {Donald F. Rossin and
		               Barbara D. Klein},
		  title     = {Data Errors in Neural Network and Linear Regression Models:
		               An Experimental Comparison},
		  journal   = {Data Quality Journal},
		  volume    = {5},
			month     = {September},
		  year      = {1999},
		  ee        = {http://www.dataquality.com/999KR.htm},
		  bibsource = {DBLP, http://dblp.uni-trier.de}
		}
		"""
		Then my bibliography should contain these articles:
			| year | month |
			| 1999 | sep   |
