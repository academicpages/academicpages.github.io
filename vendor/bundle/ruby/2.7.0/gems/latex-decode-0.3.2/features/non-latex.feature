Feature: Keep non-LaTeX markup as it is
  As a hacker who works with LaTeX
  I want to preserve non-LaTeX text as it is

  Scenario: Standalone escape characters
    When I decode the string '\\'
    Then the result should be '\\'

  Scenario: Common markup in Regular Expressions
    When I decode the string '.*'
    Then the result should be '.*'
    When I decode the string '^x$'
    Then the result should be '^x$'
    When I decode the string '\\\\2'
    Then the result should be '\\\\2'
