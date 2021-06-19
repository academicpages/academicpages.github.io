Feature: Decode LaTeX punctuation directives
  As a hacker who works with LaTeX
  I want to be able to decode LaTeX punctuation marks

  Scenario Outline: LaTeX to Unicode transformation
    When I decode the string '<latex>'
    Then the result should be '<unicode>'

  Scenarios: Punctuation macros
    | latex                | unicode |
    | \\textendash         | –       |
    | \\textemdash         | —       |
    | \\textquoteleft      | ‘       |
    | \\textquoteright     | ’       |
    | \\quotesinglbase     | ‚       |
    | \\textquotedblleft   | “       |
    | \\textquotedblright  | ”       |
    | \\quotedblbase       | „       |
    | \\dag                | †       |
    | \\ddag               | ‡       |
    | \\textbullet         | •       |
    | \\dots               | …       |
    | \\textperthousand    | ‰       |
    | \\textpertenthousand | ‱       |
    | \\guilsinglleft      | ‹       |
    | \\guilsinglright     | ›       |
    | \\textreferencemark  | ※       |
    | \\textinterrobang    | ‽       |
    | \\textoverline       | ‾       |
    | \\langle             | ⟨       |
    | \\rangle             | ⟩       |
    | \\textquotesingle    | ’       |


  Scenarios: Punctuation symbols
    | latex              | unicode | description |
    | -                  | -       | hyphen      |
    | --                 | –       | en-dash     |
    | ---                | —       | em-dash     |
    | \\~{}              | ~       | tilde       |
    | \\textasciitilde{} | ~       | tilde       |
    | \\textasciitilde   | ~       | tilde       |
    | X\\ X              | X X     | space       |

  Scenarios: Quotation marks
    | latex   | unicode | description         |
    | ``      | “       | left double quotes  |
    | ''      | ”       | right double quotes |
    | `       | ‘       | left single quotes  |
    | '       | ’       | right single quotes |
