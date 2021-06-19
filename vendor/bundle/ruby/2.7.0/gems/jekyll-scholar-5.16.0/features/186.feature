Feature: BibTeX
  As a scholar who likes to blog
  I want to reference cool papers and books from my bibliography

  @tags @bibliography
  Scenario: Simple bibliography count
    Given I have a scholar configuration with:
      | key    | value             |
      | source | ./_bibliography   |
    And I have a "_bibliography" directory
    And I have a file "_bibliography/references.bib":
      """
      @book{smalltalk,
        title     = {Smalltalk Best Practice Patterns},
        author    = {Kent Beck},
        year      = {1996},
        publisher = {Prentice Hall}
      }
      @book{ruby,
        title     = {The Ruby Programming Language},
        author    = {Flanagan, David and Matsumoto, Yukihiro},
        year      = {2008},
        publisher = {O'Reilly Media}
      }
      """
    And I have a page "scholar.html":
      """
      ---
      ---
      {% bibliography_count -f references %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    And I should not see "<i>The Ruby Programming Language</i>" in "_site/scholar.html"
    And I should not see "<i>Smalltalk Best Practice Patterns</i>" in "_site/scholar.html"
    And I should see "2" in "_site/scholar.html"

  @tags @bibliography
  Scenario: Simple bibliography count with query
    Given I have a scholar configuration with:
      | key    | value             |
      | source | ./_bibliography   |
    And I have a "_bibliography" directory
    And I have a file "_bibliography/references.bib":
      """
      @book{smalltalk,
        title     = {Smalltalk Best Practice Patterns},
        author    = {Kent Beck},
        year      = {1996},
        publisher = {Prentice Hall}
      }
      @book{ruby,
        title     = {The Ruby Programming Language v1},
        author    = {Flanagan, David and Matsumoto, Yukihiro},
        year      = {1998},
        publisher = {O'Reilly Media}
      }
      @book{ruby2,
        title     = {The Ruby Programming Language v2},
        author    = {Flanagan, David and Matsumoto, Yukihiro},
        year      = {2008},
        publisher = {O'Reilly Media}
      }
      """
    And I have a page "scholar.html":
      """
      ---
      ---
      {% bibliography_count -f references --query @book[year <= 2000] %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    And I should not see "<i>The Ruby Programming Language v1</i>" in "_site/scholar.html"
    And I should not see "<i>The Ruby Programming Language v2/i>" in "_site/scholar.html"
    And I should not see "<i>Smalltalk Best Practice Patterns</i>" in "_site/scholar.html"
    And I should see "2" in "_site/scholar.html"

  @tags @bibliography
  Scenario: Simple bibliography count with query with cited
    Given I have a scholar configuration with:
      | key    | value             |
      | source | ./_bibliography   |
    And I have a "_bibliography" directory
    And I have a file "_bibliography/references.bib":
      """
      @book{smalltalk,
        title     = {Smalltalk Best Practice Patterns},
        author    = {Kent Beck},
        year      = {1996},
        publisher = {Prentice Hall}
      }
      @book{ruby,
        title     = {The Ruby Programming Language v1},
        author    = {Flanagan, David and Matsumoto, Yukihiro},
        year      = {1998},
        publisher = {O'Reilly Media}
      }
      @book{ruby2,
        title     = {The Ruby Programming Language v2},
        author    = {Flanagan, David and Matsumoto, Yukihiro},
        year      = {2008},
        publisher = {O'Reilly Media}
      }
      """
    And I have a page "scholar.html":
      """
      ---
      ---
      {% cite smalltalk %}
      {% bibliography_count -f references --query @book[year <= 2000] --cited %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    And I should not see "<i>The Ruby Programming Language v1</i>" in "_site/scholar.html"
    And I should not see "<i>The Ruby Programming Language v2/i>" in "_site/scholar.html"
    And I should not see "<i>Smalltalk Best Practice Patterns</i>" in "_site/scholar.html"
    And I should see "1" in "_site/scholar.html"
