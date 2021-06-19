Feature: Parse names with a suffix
  As a hacker who works with Namae
  I want to be able to parse names with a suffix

  @names @suffix
  Scenario: Names with a suffix BibTeX style
    When I parse the names "Griffey, Jr., Ken"
    Then the names should be:
      | given      | family  | suffix  |
      | Ken        | Griffey | Jr.     |

  @names @suffix
  Scenario: Names with a suffix in display-order
    When I parse the names "Ken Griffey, Jr."
    Then the names should be:
      | given      | family  | suffix  |
      | Ken        | Griffey | Jr.     |
  
  @names @suffix
  Scenario: Names with a suffix in sort-order chicago style
    When I parse the names "Griffey, Ken, Jr."
    Then the names should be:
      | given      | family  | suffix  |
      | Ken        | Griffey | Jr.     |
  
  @names @suffix
  Scenario: Names with a suffix in sort-order with no comma
    When I parse the names "Griffey, Ken Jr."
    Then the names should be:
      | given      | family  | suffix  |
      | Ken        | Griffey | Jr.     |

  @names @suffix
  Scenario: Names with a suffix in display-order no comma
    When I parse the names "Ken Griffey Jr."
    Then the names should be:
      | given      | family  | suffix  |
      | Ken        | Griffey | Jr.     |
  
  
  @names @suffix @list
  Scenario: Names with a suffix
    When I parse the names "Griffey, Jr., Ken and Ken Griffey, Jr. and Griffey, Ken, Jr. and Ken Griffey Jr."
    Then the names should be:
      | given      | family  | suffix  |
      | Ken        | Griffey | Jr.     |
      | Ken        | Griffey | Jr.     |
      | Ken        | Griffey | Jr.     |
      | Ken        | Griffey | Jr.     |
