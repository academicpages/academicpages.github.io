Feature: Page Configuration
  As a scholar who likes to blog
  I want to set local jekyll-scholar options per page
  In order to override the global config

  @tags @filters
  Scenario: Filter by Year
    Given I have a scholar configuration with:
      | key    | value             |
      | source | ./_bibliography   |
      | query  | "@*[year=2009]"   |
    And I have a "_bibliography" directory
    And I have a file "_bibliography/references.bib":
      """
      @book{ruby,
        title     = {The Ruby Programming Language},
        author    = {Flanagan, David and Matsumoto, Yukihiro},
        year      = {2008},
        publisher = {O'Reilly Media}
      }
      @book{pickaxe,
        title     = {Programming Ruby 1.9: The Pragmatic Programmer's Guide},
        author    = {Thomas, Dave and Fowler, Chad and Hunt, Andy},
        year      = {2009},
        edition   = 3,
        publisher = {Pragmatic Bookshelf}
      }
      """
    And I have a page "scholar.html":
      """
      ---
      scholar:
        query: "@*[year=2008]"
      ---
      {% bibliography %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    And I should see "The Ruby Programming Language" in "_site/scholar.html"
    And I should not see "Programming Ruby" in "_site/scholar.html"


  @tags
  Scenario: Template access to page config
    Given I have a scholar configuration with:
      | key                   | value                     |
      | source                | ./_bibliography           |
      | bibliography_template | <p>{{page.scholar.x}}</p> |
    And I have a "_bibliography" directory
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
      scholar:
        x: Asa-Nisi-Masa
      ---
      {% bibliography %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    And I should see "<p>Asa-Nisi-Masa</p>" in "_site/scholar.html"

