Feature: Parse BibTeX-style names
	As a hacker who works with bibliographies
	I want to be able to parse BibTeX-style names

  Scenario Outline: Name splitting
    When I parse the name "<name>"
    Then the BibTeX parts should be:
      |  first  |  von  |  last  |  jr  |
      | <first> | <von> | <last> | <jr> |

  @names @display
  Scenarios: Decoret test suite (display order)
    | name            | first      | von        | last    | jr |
    | AA BB           | AA         |            | BB      |    |
    | AA BB CC        | AA BB      |            | CC      |    |
#   | AA              |            |            | AA      |    |
    | AA bb           | AA         |            | bb      |    |
#   | aa              |            |            | aa      |    |
    | aa bb           |            | aa         | bb      |    |
    | aa BB           |            | aa         | BB      |    |
    | AA bb CC        | AA         | bb         | CC      |    |
    | AA bb CC dd EE  | AA         | bb CC dd   | EE      |    |
#    | AA 1B cc dd     | AA 1B      | cc         | dd      |    |
#    | AA 1b cc dd     | AA         | 1b cc      | dd      |    |
    | AA {b}B cc dd   | AA {b}B    | cc         | dd      |    |
    | AA {b}b cc dd   | AA         | {b}b cc    | dd      |    |
    | AA {B}b cc dd   | AA         | {B}b cc    | dd      |    |
    | AA {B}B cc dd   | AA {B}B    | cc         | dd      |    |
    | AA \BB{b} cc dd | AA \\BB{b} | cc         | dd      |    |
    | AA \bb{b} cc dd | AA \\bb{b} | cc         | dd      |    |
    | AA {bb} cc DD   | AA {bb}    | cc         | DD      |    |
    | AA bb {cc} DD   | AA         | bb         | {cc} DD |    |
    | AA {bb} CC      | AA {bb}    |            | CC      |    |

  @names @sort
  Scenarios: Decoret test suite (sort order)
    | name            | first      | von        | last    | jr |
    | bb CC, AA       | AA         | bb         | CC      |    |
    | bb CC, aa       | aa         | bb         | CC      |    |
    | bb CC dd EE, AA | AA         | bb CC dd   | EE      |    |
    | bb, AA          | AA         |            | bb      |    |
    | BB,             |            |            | BB      |    |
    | bb CC,II, AA    | AA         | bb         | CC      | II |
    | bb CC,jr, AA    | AA         | bb         | CC      | jr |
#    | BB,, AA         | AA         |            | BB      |    |
    | CC dd BB, AA    | AA         | CC dd      | BB      |    |
    | BB, AA          | AA         |            | BB      |    |

  @names @sort
  Scenarios: Long von parts
    | name            | first      | von        | last    | jr |
    | bb cc dd CC, AA | AA         | bb cc dd   | CC      |    |
    | bb CC dd CC, AA | AA         | bb CC dd   | CC      |    |
    | BB cc dd CC, AA | AA         | BB cc dd   | CC      |    |
    | BB CC dd CC, AA | AA         | BB CC dd   | CC      |    |

  @names 
  Scenarios: Decoret further remarks
    | name                               | first                | von            | last                    | jr |
    | Dominique Galouzeau de Villepin    | Dominique Galouzeau  | de             | Villepin                |    |
    | Dominique {G}alouzeau de Villepin  | Dominique            | {G}alouzeau de | Villepin                |    |
    | Galouzeau {de} Villepin, Dominique | Dominique            |                | Galouzeau {de} Villepin |    |

  @names 
  Scenarios: Some actual names
    | name                              | first                   | von            | last                           | jr  |
    | John Paul Jones                   | John Paul               |                | Jones                          |     |
    | Ludwig von Beethoven              | Ludwig                  | von            | Beethoven                      |     |
    | von Beethoven, Ludwig             | Ludwig                  | von            | Beethoven                      |     |
    | {von Beethoven}, Ludwig           | Ludwig                  |                | {von Beethoven}                |     |
    | {{von} Beethoven}, Ludwig         | Ludwig                  |                | {{von} Beethoven}              |     |
    | John {}Paul Jones                 | John {}Paul             |                | Jones                          |     |
    | Ford, Jr., Henry                  | Henry                   |                | Ford                           | Jr. |
    | Brinch Hansen, Per                | Per                     |                | Brinch Hansen                  |     |
#    | {Barnes and Noble, Inc.}          |                         |                | {Barnes and Noble, Inc.}       |     |
    | {Barnes and} {Noble, Inc.}        | {Barnes and}            |                | {Noble, Inc.}                  |     |
    | {Barnes} {and} {Noble,} {Inc.}    | {Barnes} {and} {Noble,} |                | {Inc.}                         |     |
    | Charles Louis Xavier Joseph de la Vallee Poussin | Charles Louis Xavier Joseph | de la | Vallee Poussin       |     |
