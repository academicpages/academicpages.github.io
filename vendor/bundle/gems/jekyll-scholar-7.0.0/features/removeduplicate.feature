Feature: BibTeX
  As a scholar who likes to blog
  I want to publish my BibTeX bibliography on my blog
  In order to share my awesome references with my peers

  @tags @bibliography
   Scenario: Duplicates should not be removed by default
    Given I have a scholar configuration with:
      | key    | value             |
      | source | ./_bibliography   |
      | bibliography_list_tag | ol |
    And I have a "_bibliography" directory
    And I have a file "_bibliography/references.bib":
      """
      @book{ruby,
        title     = {The Ruby Programming Language},
        author    = {Flanagan, David and Matsumoto, Yukihiro},
        year      = {2008},
        publisher = {O'Reilly Media}
      }

      @book{ruby,
        title     = {The Ruby Programming Language},
        author    = {Flanagan, David and Matsumoto, Yukihiro},
        year      = {2008},
        publisher = {O'Reilly Media}
      }

      @book{ruby,
        title     = {Smalltalk Best Practice Patterns},
        author    = {Kent Beck},
        year      = {1996},
        publisher = {Prentice Hall}
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
    And I should see "3" in "_site/scholar.html"

  @tags @bibliography
   Scenario: Duplicates should be removed
    Given I have a scholar configuration with:
      | key                   | value           |
      | source                | ./_bibliography |
      | remove_duplicates     | true            |
      | bibliography_list_tag | ol              |
    And I have a "_bibliography" directory
    And I have a file "_bibliography/references.bib":
      """
      @book{ruby,
        title     = {The Ruby Programming Language},
        author    = {Flanagan, David and Matsumoto, Yukihiro},
        year      = {2008},
        publisher = {O'Reilly Media}
      }

      @book{ruby,
        title     = {The Ruby Programming Language},
        author    = {Flanagan, David and Matsumoto, Yukihiro},
        year      = {2008},
        publisher = {O'Reilly Media}
      }

      @book{ruby,
        title     = {Smalltalk Best Practice Patterns},
        author    = {Kent Beck},
        year      = {1996},
        publisher = {Prentice Hall}
        }
      """
    And I have a page "scholar.html":
      """
      ---
      ---
      {% bibliography_count -f references --remove_duplicates %}

      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    And I should see "2" in "_site/scholar.html"

  @tags @bibliography
   Scenario: Remove duplicates by year
    Given I have a scholar configuration with:
      | key                   | value           |
      | source                | ./_bibliography |
      | remove_duplicates     | true            |
      | bibliography_list_tag | ol              |
    And I have a "_bibliography" directory
    And I have a file "_bibliography/references.bib":
      """
      @book{ruby,
        title     = {The Ruby Programming Language},
        author    = {Flanagan, David and Matsumoto, Yukihiro},
        year      = {1996},
        publisher = {O'Reilly Media}
      }

      @book{ruby,
        title     = {The Ruby Programming Language},
        author    = {Flanagan, David and Matsumoto, Yukihiro},
        year      = {2008},
        publisher = {O'Reilly Media}
      }

      @book{ruby,
        title     = {Smalltalk Best Practice Patterns},
        author    = {Kent Beck},
        year      = {1996},
        publisher = {Prentice Hall}
        }
      """
    And I have a page "scholar.html":
      """
      ---
      ---
      {% bibliography_count -f references -r year %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    And I should see "2" in "_site/scholar.html"
