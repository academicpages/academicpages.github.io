Feature: Parse BibTeX files and convert LaTeX to Unicode
	As a hacker who works with bibliographies
	I want to be able to parse BibTeX files containing LaTeX strings and
	convert them to Unicode

	@latex
  Scenario: A BibTeX file containing a LaTeX umlaut
     When I parse the following file:
     """
     @misc{issue16,
       author = {rbq},
       title  = {An umlaut: \"u!},
       year   = 2011,
     }
     """
     Then my bibliography should contain an entry with key "issue16"
     When I convert all entries using the filter "latex"
     Then the entry with key "issue16" should have a field "title" with the value "An umlaut: ü!"

	@latex
  Scenario: A BibTeX file containing a variety of LaTeX strings
    When I parse the following file:
    """
    @book{proust_1996,
      address = {Paris},
      author = {Proust, Jo\"{e}lle},
      booktitle = {Perception et Intermodalit\'{e}: Approches Actuelles De La Question De Molyneux},
      editor = {Proust, Jo\"{e}lle},
      keywords = {Perception; Molyneux's Problem},
      publisher = {Presses Universitaires de France},
      title = {Perception et Intermodalit\'{e}: Approches Actuelles De La Question De Molyneux},
      year = {1996}
    }
    @incollection{bach-y-rita_1996,
      author = {{Bach-y-Rita}, Paul},
      crossref = {proust_1996},
      keywords = {Perception; Molyneux's Problem; Vision},
      note = {Reprinted in translation in \textcite[pp. 497--514]{noe_2002}.},
      pages = {81--100},
      title = {Substitution Sensorielle et Qualia}
    }
    @article{noe_2008,
      author = {No\"{e}, Alva},
      journal = {Philosophy and Phenomenological Research},
      keywords = {Perception; Enactivism; Vision},
      month = {may},
      number = {3},
      pages = {660--665},
      title = {Pr\'{e}cis of \emph{Action in Perception}},
      url = {http://dx.doi.org/10.1111/j.1933-1592.2008.00161.x},
      volume = {76},
      year = {2008}
    }
    @article{bermudez_2007,
      author = {Berm\'{u}dez, Jos\'{e} Luis},
      date-added = {2011-10-02 12:43:54 -0400},
      date-modified = {2011-10-02 12:43:54 -0400},
      journal = {Philosophical Perspectives},
      keywords = {Nonconceptual Content; Mind; Perception},
      month = {dec},
      number = {1},
      pages = {55--72},
      title = {What is at Stake in the Debate on Nonconceptual Content?},
      url = {http://dx.doi.org/10.1111/j.1520-8583.2007.00120.x},
      volume = {21},
      year = {2007}
    }
    @book{ellegard_1958,
      address = {G\"{o}teborg},
      author = {Elleg{\aa}rd, Alvar},
      booktitle = {Darwin and the General Reader: The Reception of Darwin's Theory of Evolution in the British Periodical Press, 1859---1972},
      keywords = {Darwin; History of Biology; History of Science; Sociology of Science},
      note = {Reprinted by University of Chicago Press.},
      publisher = {G\"{o}teborg Universitets {\AA}rsskrift},
      title = {Darwin and the General Reader: The Reception of Darwin's Theory of Evolution in the British Periodical Press, 1859--1972},
      volume = {64},
      year = {1958}
    }
    @article{haggqvist_2007,
      author = {H\"{a}ggqvist, S\"{o}ren and {\AA}sa Maria Wikforss},
      journal = {Erkenntnis},
      keywords = {Externalism; Content; Mind},
      month = {nov},
      number = {3},
      pages = {373--386},
      title = {Externalism and A Posteriori Semantics},
      url = {http://dx.doi.org/10.1007/s10670-007-9051-4},
      volume = {67},
      year = {2007}
    }
    @article{hajek_1996,
      abstract = {According to finite frequentism, the probability of an attribute A in a finite reference class B is the relative frequency of actual occurrences of A within B. I present fifteen arguments against this position.},
      author = {H\'{a}jek, Alan},
      journal = {Erkenntnis},
      keywords = {Probability},
      month = {nov},
      number = {2-3},
      pages = {209-227},
      title = {``Mises redux''---Redux: Fifteen Arguments against Finite Frequentism},
      volume = {45},
      year = {1996}
    }
    @article{bergstrom_1970a,
      author = {Bergstr\"{o}m, Ingvar},
      journal = {Oud Holland},
      keywords = {Holland; 17C; History of Art},
      number = {1-4},
      pages = {143-157},
      title = {De Gheyn as a \emph{Vanitas} Painter},
      url = {http://dx.doi.org/10.1163/187501770X00112},
      volume = {85},
      year = {1970}
    }
    @incollection{bricmont_2001,
      address = {Heidelberg},
      author = {Bricmont, Jean and D\"{u}rr, Detlef and Galavotti, Maria C. and Ghirardi, Giancarlo and Petruccione, Francesco and Zangh\`{i}, Nino},
      booktitle = {Chance in Physics: Foundations and Perspectives},
      editor = {Bricmont, Jean and D\"{u}rr, Detlef and Galavotti, Maria C. and Ghirardi, Giancarlo and Petruccione, Francesco and Zangh\`{i}, Nino},
      keywords = {Philosophy of Science; Physics; Probability; Quantum Mechanics; Thermodynamics},
      publisher = {Springer},
      series = {Lecture Notes in Physics},
      title = {Chance in Physics: Foundations and Perspectives},
      year = {2001}
    }
    @article{bowler_1975,
      author = {Bowler, Peter J.},
      journal = {Journal of the History of Ideas},
      keywords = {History of Biology; History of Science},
      month = {mar},
      number = {1},
      pages = {95--114},
      title = {The Changing Meaning of ``Evolution''\,},
      url = {http://dx.doi.org/10.2307/2709013},
      volume = {36},
      year = {1975}
    }
    @article{wood_1995,
      author = {Wood, Christopher S.},
      issue = {October-December},
      journal = {Word and Image},
      keywords = {History of Art; Holland; 17C; Curiosity},
      number = {4},
      pages = {332-352},
      title = {\,`Curious Pictures' and the Art of Description},
      volume = {11},
      year = {1995}
    }
    @article{worrall_2000a,
      author = {Worrall, John},
      journal = {British Journal for the Philosophy of Science},
      keywords = {Newton; Underdetermination; Confirmation; Induction; Scientific Method; Philosophy of Science},
      month = {mar},
      number = {1},
      pages = {45--80},
      title = {The Scope, Limits, and Distinctiveness of the Method of `Deduction from the Phenomena': Some Lessons from Newton's `Demonstrations' in Optics},
      url = {http://dx.doi.org/10.1093/bjps/51.1.45},
      volume = {51},
      year = {2000}
    }
    """
		When I convert all entries using the filter "latex"
		Then the entry with key "proust_1996" should have a field "author" with the value "Proust, Joëlle"
		And the entry with key "proust_1996" should have a field "booktitle" with the value "Perception et Intermodalité: Approches Actuelles De La Question De Molyneux"
		And the entry with key "bermudez_2007" should have a field "author" with the value "Bermúdez, José Luis"
		And the entry with key "ellegard_1958" should have a field "address" with the value "Göteborg"
		And the entry with key "ellegard_1958" should have a field "publisher" with the value "Göteborg Universitets Årsskrift"
		And the entry with key "haggqvist_2007" should have a field "author" with the value "Häggqvist, Sören and Åsa Maria Wikforss"
		And the entry with key "hajek_1996" should have a field "author" with the value "Hájek, Alan"
		And the entry with key "hajek_1996" should have a field "title" with the value "“Mises redux”—Redux: Fifteen Arguments against Finite Frequentism"
    And the entry with key "bergstrom_1970a" should have a field "author" with the value "Bergström, Ingvar"
		And the entry with key "worrall_2000a" should have a field "title" with the value "The Scope, Limits, and Distinctiveness of the Method of ‘Deduction from the Phenomena’: Some Lessons from Newton’s ‘Demonstrations’ in Optics"