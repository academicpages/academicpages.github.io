Feature: Keys containing '/' symbols
	As a hacker who works with bibliographies
	I want to parse BibTeX entries with keys starting with numbers
	Because they frequently occur in key naming schemes
	
	Scenario: Two entries with keys starting with a number
		When I parse the following file:
		"""
		@misc{2008knowledge,
			Date-Added = {2011-04-24 17:41:02 -0400},
			Date-Modified = {2011-04-27 20:13:35 -0400},
			Howpublished = {http://oro.open.ac.uk/11766/},
			Month = sep,
			Note = {Knowledge Cartography is the discipline of mapping intellectual {landscapes.The} focus of this book is on the process by which manually crafting interactive, hypertextual maps clarifies one’s own understanding, as well as communicating {it.The} authors see mapping software as a set of visual tools for reading and writing in a networked age. In an information ocean, the primary challenge is to find meaningful patterns around which we can weave plausible narratives. Maps of concepts, discussions and arguments make the connections between ideas tangible and disputable. With 17 chapters from the leading researchers and practitioners, the reader will find the current state–of-the-art in the field. Part 1 focuses on educational applications in schools and universities, before Part 2 turns to applications in professional communities},
			Shorttitle = {Knowledge Cartography},
			Title = {Knowledge Cartography: Software tools and mapping techniques},
			Type = {Edited Book},
			Url = {http://oro.open.ac.uk/11766/},
			Year = {2008},
			Bdsk-File-1 = {YnBsaXN0MDDUAQIDBAUIJidUJHRvcFgkb2JqZWN0c1gkdmVyc2lvblkkYXJjaGl2ZXLRBgdUcm9vdIABqAkKFRYXGyIjVSRudWxs0wsMDQ4RFFpOUy5vYmplY3RzV05TLmtleXNWJGNsYXNzog8QgASABqISE4ACgAOAB1lhbGlhc0RhdGFccmVsYXRpdmVQYXRo0hgNGRpXTlMuZGF0YU8RAXwAAAAAAXwAAgAABEhvbWUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMmm5vlIKwAAABLivBEyMDA4a25vd2xlZGdlLnBkZgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEtx5ydoOuQAAAAAAAAAAAAIAAwAACQAAAAAAAAAAAAAAAAAAAAAHQmliZGVzawAAEAAIAADJpx85AAAAEQAIAADJ2kb5AAAAAQAMABLivAAAAF8AAABXAAIALkhvbWU6c3RpYW46RG9jdW1lbnRzOkJpYmRlc2s6MjAwOGtub3dsZWRnZS5wZGYADgAkABEAMgAwADAAOABrAG4AbwB3AGwAZQBkAGcAZQAuAHAAZABmAA8ACgAEAEgAbwBtAGUAEgAqL3N0aWFuL0RvY3VtZW50cy9CaWJkZXNrLzIwMDhrbm93bGVkZ2UucGRmABMADS9Wb2x1bWVzL0hvbWUAABUAAgAT//8AAIAF0hwdHh9YJGNsYXNzZXNaJGNsYXNzbmFtZaMfICFdTlNNdXRhYmxlRGF0YVZOU0RhdGFYTlNPYmplY3RfECkuLi8uLi9Eb2N1bWVudHMvQmliZGVzay8yMDA4a25vd2xlZGdlLnBkZtIcHSQloiUhXE5TRGljdGlvbmFyeRIAAYagXxAPTlNLZXllZEFyY2hpdmVyAAgAEQAWAB8AKAAyADUAOgA8AEUASwBSAF0AZQBsAG8AcQBzAHYAeAB6AHwAhgCTAJgAoAIgAiICJwIwAjsCPwJNAlQCXQKJAo4CkQKeAqMAAAAAAAACAQAAAAAAAAAoAAAAAAAAAAAAAAAAAAACtQ==}}

		@misc{2007proceedings,
			Date-Added = {2011-04-24 17:34:26 -0400},
			Date-Modified = {2011-04-27 20:13:35 -0400},
			Howpublished = {http://oro.open.ac.uk/9275/},
			Month = oct,
			Note = {Proceedings {ICPW'07:} 2nd International Conference on the Pragmatic Web, 22-23 Oct. 2007, Tilburg: {NL}},
			Shorttitle = {Proceedings {ICPW'07}},
			Title = {Proceedings {ICPW'07:} 2nd International Conference on the Pragmatic Web, 22-23 Oct. 2007, Tilburg: {NL}},
			Type = {Edited Book},
			Url = {http://oro.open.ac.uk/9275/},
			Year = {2007},
			Bdsk-File-1 = {YnBsaXN0MDDUAQIDBAUIJidUJHRvcFgkb2JqZWN0c1gkdmVyc2lvblkkYXJjaGl2ZXLRBgdUcm9vdIABqAkKFRYXGyIjVSRudWxs0wsMDQ4RFFpOUy5vYmplY3RzV05TLmtleXNWJGNsYXNzog8QgASABqISE4ACgAOAB1lhbGlhc0RhdGFccmVsYXRpdmVQYXRo0hgNGRpXTlMuZGF0YU8RAYQAAAAAAYQAAgAABEhvbWUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMmm5vlIKwAAABLivBMyMDA3cHJvY2VlZGluZ3MucGRmAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEuYBydoPoVBERiAAAAAAAAIAAwAACQAAAAAAAAAAAAAAAAAAAAAHQmliZGVzawAAEAAIAADJpx85AAAAEQAIAADJ2kfhAAAAAQAMABLivAAAAF8AAABXAAIAMEhvbWU6c3RpYW46RG9jdW1lbnRzOkJpYmRlc2s6MjAwN3Byb2NlZWRpbmdzLnBkZgAOACgAEwAyADAAMAA3AHAAcgBvAGMAZQBlAGQAaQBuAGcAcwAuAHAAZABmAA8ACgAEAEgAbwBtAGUAEgAsL3N0aWFuL0RvY3VtZW50cy9CaWJkZXNrLzIwMDdwcm9jZWVkaW5ncy5wZGYAEwANL1ZvbHVtZXMvSG9tZQAAFQACABP//wAAgAXSHB0eH1gkY2xhc3Nlc1okY2xhc3NuYW1lox8gIV1OU011dGFibGVEYXRhVk5TRGF0YVhOU09iamVjdF8QKy4uLy4uL0RvY3VtZW50cy9CaWJkZXNrLzIwMDdwcm9jZWVkaW5ncy5wZGbSHB0kJaIlIVxOU0RpY3Rpb25hcnkSAAGGoF8QD05TS2V5ZWRBcmNoaXZlcgAIABEAFgAfACgAMgA1ADoAPABFAEsAUgBdAGUAbABvAHEAcwB2AHgAegB8AIYAkwCYAKACKAIqAi8COAJDAkcCVQJcAmUCkwKYApsCqAKtAAAAAAAAAgEAAAAAAAAAKAAAAAAAAAAAAAAAAAAAAr8=}}
		"""
		Then my bibliography should contain a misc with id "2008knowledge"
		And my bibliography should contain a misc with id "2007proceedings"		

	Scenario: An entry with a number-only key
		When I parse the following file:
		"""
		@book{2011,
			Title = {Test}
		}
		"""
		Then my bibliography should contain a book with id "2011"
