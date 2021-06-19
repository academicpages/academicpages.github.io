Feature: Multiline values on single lines
  As a hacker who works with bibliographies
  I would find it practical to have multiline values turned to single lines by default
  Because this is what most BibTeX files will assume.

  Scenario: Multiline value
    When I parse the following file:
    """
    @article{stuff,
      title = "This very long title must be wrapped and continues
               on the next line."
    }
    """
    Then the entry with key "stuff" should have a field "title" with the value "This very long title must be wrapped and continues on the next line."
