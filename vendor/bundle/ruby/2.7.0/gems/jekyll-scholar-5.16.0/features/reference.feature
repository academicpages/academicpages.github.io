Feature: Formatted References
  As a scholar who likes to blog
  I want to reference cool papers and books from my bibliography

  @tags @reference
  Scenario: A Simple Reference
    Given I have a scholar configuration with:
      | key          | value             |
      | source       | ./_bibliography   |
      | bibliography | my_references     |
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
      {% reference ruby %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    And I should see "Matsumoto, Y. \(2008\). <i>The Ruby" in "_site/scholar.html"

  @tags @reference @post
  Scenario: A Simple Reference in a Post
    Given I have a scholar configuration with:
      | key          | value             |
      | source       | ./_bibliography   |
      | bibliography | my_references     |
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
    And I have a "_posts" directory
    And I have a page "_posts/2017-06-26-scholar.html":
      """
      ---
      ---
      {% reference ruby %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/2017/06/26/scholar.html" file should exist
    And I should see "Matsumoto, Y. \(2008\). <i>The Ruby" in "_site/2017/06/26/scholar.html"

  @tags @reference @missing
  Scenario: Missing references
    Given I have a scholar configuration with:
      | key          | value             |
      | source       | ./_bibliography   |
      | bibliography | my_references     |
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
      {% reference java %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    And I should see "(missing reference)" in "_site/scholar.html"

  @tags @reference @missing
  Scenario: Missing references with a custom text
    Given I have a scholar configuration with:
      | key                | value             |
      | source             | ./_bibliography   |
      | bibliography       | my_references     |
      | missing_reference  | not found!        |
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
      {% reference java %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    And I should see "not found!" in "_site/scholar.html"
    And I should not see "(missing reference)" in "_site/scholar.html"
