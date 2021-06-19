Feature: Interpolations ...
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
    And I have a file "custom.csl":
      """
      <style>
        <citation>
          <layout>
            <text variable="title"/>
          </layout>
        </citation>
        <bibliography>
          <layout>
            <text variable="title"/>
          </layout>
        </bibliography>
      </style>
      """
    And I have a page "scholar.html":
      """
      ---
      ---
      {% assign style_file = 'custom.csl' %}
      {% bibliography --style {{style_file}} %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    And I should see "The Ruby Programming Language" in "_site/scholar.html"


  @tags @grouping
  Scenario: Local grouping override - grouping by year with interpolation
    Given I have a scholar configuration with:
      | key         | value             |
      | group_by    | none              |
      | group_order | ascending         |
    And I have a "_bibliography" directory
    And I have a file "_bibliography/references.bib":
      """
      @book{ruby1,
        title     = {The Ruby Programming Language},
        author    = {Flanagan, David and Matsumoto, Yukihiro},
        year      = {2008},
        publisher = {O'Reilly Media}
      }
      @book{ruby2,
        title     = {The Ruby Programming Language},
        author    = {Flanagan, David and Matsumoto, Yukihiro},
        year      = {2007},
        publisher = {O'Reilly Media}
      }
      """
    And I have a page "scholar.html":
      """
      ---
      ---
      {% assign group_year = 'year' %}
      {% bibliography -f references --group_by {{group_year}} --group_order descending %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    Then I should see "<h2 class=\"bibliography\">2007</h2>" in "_site/scholar.html"
    And I should see "<h2 class=\"bibliography\">2008</h2>" in "_site/scholar.html"
    And "2008" should come before "2007" in "_site/scholar.html"

  @tags @reference @liquid @interpolate
  Scenario: Interpolate liquid variables in queries
    Given I have a scholar configuration with:
      | key                | value             |
      | source             | ./_bibliography   |
      | bibliography       | my_references     |
    And I have a "_bibliography" directory
    And I have a file "_bibliography/my_references.bib":
      """
      @book{a,
        title     = {Book A},
        year      = {2008}
      }
      @book{b,
        title     = {Book B},
        year      = {2018}
      }
      """
    And I have a page "scholar.html":
      """
      ---
      ---
      {% assign from = 2000 %}
      {% assign to = 2010 %}
      {% bibliography --query @book[year >= {{from}} && year <= {{to}}] %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    And I should see "Book A" in "_site/scholar.html"
    And I should not see "Book B" in "_site/scholar.html"

  @tags @bibliography @liquid @interpolate
  Scenario: Interpolate page variables in queries
    Given I have a scholar configuration with:
      | key                | value             |
      | source             | ./_bibliography   |
    And I have a "_bibliography" directory
    And I have a file "_bibliography/references.bib":
      """
      @book{a,
        title     = {Book A},
        year      = {2008}
      }
      @book{b,
        title     = {Book B},
        year      = {2018}
      }
      """
    And I have a page "scholar.html":
      """
      ---
      bibquery: year >= 2000 && year <= 2010
      ---
      {% bibliography --query @*[{{page.bibquery}}] %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    And I should see "Book A" in "_site/scholar.html"
    And I should not see "Book B" in "_site/scholar.html"

  @tags @bibliography @liquid @interpolate
  Scenario: Interpolate page variables in queries
    Given I have a scholar configuration with:
      | key                | value             |
      | source             | ./_bibliography   |
    And I have a "_bibliography" directory
    And I have a file "_bibliography/references.bib":
      """
      @book{a,
        title     = {Book A},
        year      = {2008}
      }
      @book{b,
        title     = {Book B},
        year      = {2018}
      }
      """
    And I have a page "scholar.html":
      """
      ---
      bibquery: "@book[year >= 2000 && year <= 2010]"
      ---
      {% bibliography --query {{page.bibquery}} %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    And I should see "Book A" in "_site/scholar.html"
    And I should not see "Book B" in "_site/scholar.html"
