Feature: Decode LaTeX special characters
  As a hacker who works with LaTeX
  I want to be able to decode a few special characters which are escaped by LaTeX

  Scenario Outline: LaTeX to Unicode transformation
    When I decode the string '<latex>'
    Then the result should be '<unicode>'

  Scenarios: Special characters
    | latex                | unicode |
    | \\\&                 | &       |
    | \\#                  | #       |
    | \\$                  | $       |
    | \\;                  | ;       |
    | \\%                  | %       |
    | \\{                  | {       |
    | \\}                  | }       |
    | \\_                  | _       |
    | \\textasciitilde{}   | ~       |
    | \\textbackslash{}    | \\      |
    | \\textasciicircum{}  | ^       |
