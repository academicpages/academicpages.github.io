Feature: BibTeX
  As a scholar who likes to blog
  I want to publish my BibTeX bibliography on my website
  Based on multiple BibTeX files


  Scenario: Multiple bibliography files
    Given I have a scholar configuration with:
      | key    | value             |
      | source | ./_bibliography   |
    And I have a "_bibliography" directory
    And I have a file "_bibliography/references1.bib":
      """
      @book{ruby,
        title     = {The Ruby Programming Language},
        author    = {Flanagan, David and Matsumoto, Yukihiro},
        year      = {2008},
        publisher = {O'Reilly Media}
      }
      """
    And I have a file "_bibliography/references2.bib":
      """
      @book{microscope,
        title     = {Ruby Under a Microscope},
        author    = {Pat Shaughnessy},
        year      = {2013},
        publisher = {No Starch Press}
      }
      """
    And I have a page "scholar.html":
      """
      ---
      ---
      {% bibliography -f references1 -f references2 %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    And I should see "<i>The Ruby Programming Language</i>" in "_site/scholar.html"
    And I should see "<i>Ruby Under a Microscope</i>" in "_site/scholar.html"

