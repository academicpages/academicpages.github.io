Feature: Parse BibTeX cross-references
  As a hacker who works with bibliographies
  I want to be able to parse BibTeX files with cross-referenced entries

	@wip
	Scenario: A BibTeX file with six entries and three cross-references
		When I parse the following file:
		"""
		@book{zimmerman_2004,
			Address = {Oxford},
			Author = {Dean W. Zimmerman},
			Editor = {Dean W. Zimmerman},
			Keywords = {Metaphysics},
			Publisher = {Oxford University Press},
			Title = {Oxford Studies in Metaphysics},
			Volume = {1},
			Year = {2004}
		}

		@incollection{hall_2004b,
			Author = {Ned Hall},
			Crossref = {zimmerman_2004},
			Keywords = {Causation},
			Pages = {255-299},
			Title = {The Intrinsic Character of Causation}
		}

		@proceedings{weingartner_1989,
			Address = {Vienna},
			Editor = {Paul Weingartner and Gerhard Schurz},
			Keywords = {Anthology},
			Publisher = {Verlag H{\"o}lder-Pichter Tempsky},
			Title = {Philosophy of the Natural Sciences: Proceedings of the 13th International Wittgenstein Symposium},
			Year = {1989}}

		@inproceedings{cartwright_1989a,
			Author = {Nancy Cartwright},
			Crossref = {weingartner_1989},
			Keywords = {Causation; Quantum Mechanics},
			Pages = {120-127},
			Title = {Quantum Causes: The Lesson of the Bell Inequalities}}

		@inbook{fraassen_1989b,
			Crossref = {fraassen_1989},
			Pages = {40-64},
			Title = {Ideal Science: David Lewis's Account of Laws},
			Url = {http://dx.doi.org/10.1093/0198248601.003.0003}
		}

		@book{fraassen_1989,
			Address = {Oxford},
			Author = {Bas C. van Fraassen},
			Keywords = {Laws; Lewis},
			Publisher = {Oxford University Press},
			Title = {Laws and Symmetry},
			Url = {http://dx.doi.org/10.1093/0198248601.001.0001},
			Year = 1989
		}
	  """
	  Then the entry with key "fraassen_1989b" should have a field "Booktitle" with the value "Laws and Symmetry"
	  And the entry with key "hall_2004b" should have a field "Editor" with the value "Zimmerman, Dean W."
	  And the entry with key "cartwright_1989a" should have a field "Year" with the value "1989"