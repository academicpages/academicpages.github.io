Feature: Decode LaTeX Greek Letters
  As a hacker who works with LaTeX
  I want to be able to decode Greek letters

  Scenario Outline: LaTeX to Unicode transformation
    When I decode the string '<latex>'
    Then the result should be '<unicode>'

  Scenarios: Greek
    | latex                | unicode |
    | \\alpha              | α       |
    | \\lambda             | λ       |
    | \\Lambda             | Λ       |
