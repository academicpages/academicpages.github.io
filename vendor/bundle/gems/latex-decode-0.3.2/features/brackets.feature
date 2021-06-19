Feature: Decode LaTeX umlauts
  As a hacker who works with LaTeX
  I want to be able to remove brackets around single characters

  Scenario: Single character in curly brackets
    When I decode the string '{a}'
    Then the result should be 'a'

  Scenario: German umlauts in curly brackets
    When I decode the string '{\"A}{\"o}{\"u}'
    Then the result should be 'Äöü'