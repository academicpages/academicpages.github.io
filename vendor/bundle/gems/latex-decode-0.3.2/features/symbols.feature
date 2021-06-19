Feature: Decode LaTeX symbol directives
  As a hacker who works with LaTeX
  I want to be able to decode LaTeX symbol directives

  Scenario Outline: LaTeX to Unicode transformation
    When I decode the string '<latex>'
    Then the result should be '<unicode>'

  Scenarios: Arrows
    | latex                | unicode |
    | \\leftarrow          | ←       |
    | \\uparrow            | ↑       |
    | \\downarrow          | ↓       |
    | \\rightarrow         | →       |

  Scenarios: Whitespace
    | latex | unicode | description        |
    | x\\,x | x x     | small space        |
    | x~x   | x x     | non-breaking space |
    | ~x    |  x      | non-breaking space |

