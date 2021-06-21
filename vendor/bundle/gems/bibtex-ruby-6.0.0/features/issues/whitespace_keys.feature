Feature: Whitespace in before cite keys
	As a hacker who works with bibliographies
	I want to parse BibTeX entries with whitespace before the cite key
	Because they frequently occur in the wild
	
	Scenario: An entry with spaces before the cite key
		When I parse the following file:
		"""
    @InCollection{    brown:family:1997,
      address       = {Princeton},
      title         = {Family Strategies and Religious Practice: Baptism and the
                      Lord's Supper in Early New England},
      booktitle     = {Lived Religion in America: Toward a History of Practice},
      shorttitle    = {Family Strategies},
      publisher     = {Princeton University Press},
      author        = {Brown, Anne S. and Hall, David D.},
      editor        = {Hall, David D.},
      year          = {1997},
      pages         = {41--68},
      crossref      = {hall:lived:1997}
    }
    """
		Then my bibliography should contain an incollection with id "brown:family:1997"
