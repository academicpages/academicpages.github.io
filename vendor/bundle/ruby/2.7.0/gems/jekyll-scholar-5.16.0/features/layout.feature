Feature: Bibliographies in Layouts
  As a scholar who likes to blog
  I want to cite references on my website
  And generate bibliographies as part of a common layout

  Scenario: I want every page to have cited-only references from a single bibliography
    Given I have a scholar configuration with:
      | key    | value             |
      | source | ./_bibliography   |
    And I have a "_bibliography" directory
    And I have a file "_bibliography/references.bib":
      """
      @book{ruby,
        title     = {The Ruby Programming Language},
        author    = {Flanagan, David and Matsumoto, Yukihiro},
        year      = {2008},
        publisher = {O'Reilly Media}
      },
      @book{smalltalk,
        title     = {Smalltalk Best Practice Patterns},
        author    = {Kent Beck},
        year      = {1996},
        publisher = {Prentice Hall}
      }
      """
    And I have a "_layouts" directory
    And I have a file "_layouts/page.html":
      """
      ---
      ---
      <div>
        {{ content }}
      </div>
      <div>
        {% bibliography --cited %}
      </div>
      """
    And I have a page "scholar.html":
      """
      ---
      layout: page
      ---
      {% cite smalltalk %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    And I should not see "<i>The Ruby Programming Language</i>" in "_site/scholar.html"
    And I should see "<i>Smalltalk Best Practice Patterns</i>" in "_site/scholar.html"


