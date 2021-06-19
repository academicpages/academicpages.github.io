Feature: BibTeX Names
  As a hacker who works with bibliographies
  I want to be able to access individual parts of names in a BibTeX file
  
  Scenario Outline: Name Parsing
    When I parse the name "<name>"
    Then the parts should be:
      |  first  |  von  |  last  |  jr  |
      | <first> | <von> | <last> | <jr> |
      
  @names @issue-46
  Scenarios: Names with LaTeX commands
    | name               | first      | von        | last           | jr |
    | G{\\"u}rkan, G.    | G.         |            | G{\\"u}rkan    |    |
    | {\"O}zge, A.       | A.         |            | {\"O}zge       |    |
    | Yonca Ozge, A.     | A.         |            | Yonca Ozge     |    |
    | Yonca \"Ozge, A.   | A.         |            | Yonca \"Ozge   |    |
    | Yonca Özge, A.     | A.         |            | Yonca Özge     |    |
    | Yonca {\"O}Zge, A. | A.         |            | Yonca {\"O}Zge |    |
