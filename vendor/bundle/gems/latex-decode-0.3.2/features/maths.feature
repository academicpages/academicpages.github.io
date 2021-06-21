# Feature: Convert LaTeX maths to MathML
#   As a maths-inclined hacker who works with LaTeX
#   I want to convert LaTeX maths to MathML
#
#   Scenario: Inline maths environment
#     When I decode the string '$I_{S}A$'
#     Then the result should be '<msub><mi>I</mi><mrow><mi>S</mi></mrow></msub><mi>A</mi>'
#     When I decode the string '\underline{firstName LastName$3^g$}'
#     Then the result should be ''
