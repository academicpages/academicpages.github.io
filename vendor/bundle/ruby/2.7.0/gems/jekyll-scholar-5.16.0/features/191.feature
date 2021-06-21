Feature: Interpolation in references?
  As a scholar who likes to blog
  I want to reference cool papers and books from my bibliography

  @tags @reference @liquid @interpolate
  Scenario: Interpolate liquid variables
    Given I have a scholar configuration with:
      | key                | value             |
      | source             | ./_bibliography   |
      | bibliography       | my_references     |
    And I have a "_bibliography" directory
    And I have a file "_bibliography/my_references.bib":
      """
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
      {% assign key = 'ruby' %}
      {% reference {{key}} %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    And I should see "Matsumoto, Y. \(2008\). <i>The Ruby" in "_site/scholar.html"

  @tags @reference @liquid @interpolate
  Scenario: Interpolate liquid variables
    Given I have a scholar configuration with:
      | key                | value             |
      | source             | ./_bibliography   |
    And I have a "_bibliography" directory
    And I have a file "_bibliography/my_references.bib":
      """
      @book{smalltalk,
        title     = {Smalltalk Best Practice Patterns},
        author    = {Kent Beck},
        year      = {1996},
        publisher = {Prentice Hall}
      }
      """
    And I have a file "_bibliography/references.bib":
      """
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
      {% assign key = 'ruby' %}
      {% reference {{key}} --file my_references %}
      {% reference {{key}} --file references %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    And I should not see "id=\"a-smalltalk\"" in "_site/scholar.html"
    And I should see "Matsumoto, Y. \(2008\). <i>The Ruby" in "_site/scholar.html"

  @tags @reference @liquid @interpolate
  Scenario: Interpolate liquid variables
    Given I have a scholar configuration with:
      | key                | value             |
      | source             | ./_bibliography   |
    And I have a "_bibliography" directory
    And I have a file "_bibliography/my_references.bib":
      """
      @book{smalltalk,
        title     = {Smalltalk Best Practice Patterns},
        author    = {Kent Beck},
        year      = {1996},
        publisher = {Prentice Hall}
      }
      """
    And I have a file "_bibliography/references.bib":
      """
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
      {% assign key = 'smalltalk' %}
      {% assign myfile = 'my_references' %}
      {% reference {{key}} --file {{myfile}} %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    And I should see "Smalltalk Best Practice Patterns" in "_site/scholar.html"
    And I should not see "The Ruby Programming Language" in "_site/scholar.html"

