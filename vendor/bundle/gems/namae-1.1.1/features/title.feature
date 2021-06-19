Feature: Parse names with a title
  As a hacker who works with Namae
  I want to be able to parse names with a title

  Scenario Outline: Names with titles

    When I parse the name "<name>"
    Then the parts should be:
      |  given  |  particle  |  family  |  suffix  |  title  |  appellation  |  nick  |
      | <given> | <particle> | <family> | <suffix> | <title> | <appellation> | <nick> |

  @names @title
  Scenarios: Names with titles
    | name                         | given        | particle | family       | suffix | title     |
#    | Bernado Franecki, PhD        | Bernado      |          | Franecki     |        | PhD       |
#    | Dr. John Smith, Ph.D.        | John         |          | Smith        |        | Dr. Ph.D. |

