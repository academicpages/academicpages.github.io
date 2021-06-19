Feature: Grouping BibTeX Bibliographies
  As a scholar who likes to blog
  I want to group my bibliographies according to configurable parameters

  @tags @grouping
  Scenario: Group By Year
    Given I have a scholar configuration with:
      | key      | value             |
      | group_by | year              |
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
      {% bibliography -f references %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    Then I should see "<h2 class=\"bibliography\">2007</h2>" in "_site/scholar.html"
    And I should see "<h2 class=\"bibliography\">2008</h2>" in "_site/scholar.html"

  @tags @grouping
  Scenario: Group Order
    Given I have a scholar configuration with:
      | key         | value             |
      | group_by    | year              |
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
      {% bibliography -f references %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    Then "<h2 class=\"bibliography\">2007</h2>" should come before "<h2 class=\"bibliography\">2008</h2>" in "_site/scholar.html"

  @tags @grouping
  Scenario: Reverse Group Order
    Given I have a scholar configuration with:
      | key         | value             |
      | group_by    | year              |
      | group_order | descending        |
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
      {% bibliography -f references %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    Then "<h2 class=\"bibliography\">2008</h2>" should come before "<h2 class=\"bibliography\">2007</h2>" in "_site/scholar.html"

  @tags @grouping
  Scenario: Multi-level Group Order
    Given I have a scholar configuration with:
      | key         | value                |
      | group_by    | year,month           |
      | group_order | descending,ascending |
    And I have a "_bibliography" directory
    And I have a file "_bibliography/references.bib":
      """
      @book{ruby1,
        title     = {November 08},
        year      = {2008},
        month     = {nov}
      }
      @book{ruby2,
        title     = {March 08},
        year      = {2008},
        month     = {mar}
      }
      @book{ruby3,
        title     = {June 07},
        year      = {2007},
        month     = {jun}
      }
      """
    And I have a page "scholar.html":
      """
      ---
      ---
      {% bibliography -f references %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    Then "March" should come before "November" in "_site/scholar.html"
    And "November" should come before "June" in "_site/scholar.html"

  @tags @grouping
  Scenario: Group by Type
    Given I have a scholar configuration with:
      | key         | value                |
      | group_by    | type                 |
    And I have a "_bibliography" directory
    And I have a file "_bibliography/references.bib":
      """
      @book{ruby1,
        title     = {Book 1},
      }
      @article{ruby2,
        title     = {Article 1},
      }
      @book{ruby3,
        title     = {Book 2},
      }
      @article{ruby4,
        title     = {Article 2},
      }
      """
    And I have a page "scholar.html":
      """
      ---
      ---
      {% bibliography -f references %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    Then "Journal Articles" should come before "Article 1" in "_site/scholar.html"
    And "Journal Articles" should come before "Article 2" in "_site/scholar.html"
    Then "Books" should come before "Book 1" in "_site/scholar.html"
    And "Books" should come before "Book 2" in "_site/scholar.html"

  @tags @grouping
  Scenario: Type Order
    Given I have a scholar configuration with:
      | key         | value                |
      | group_by    | type                 |
      | type_order  | [article,book]       |
    And I have a "_bibliography" directory
    And I have a file "_bibliography/references.bib":
      """
      @book{ruby1,
        title     = {Book 1},
      }
      @article{ruby2,
        title     = {Article 1},
      }
      @book{ruby3,
        title     = {Book 2},
      }
      @techreport{ruby4,
        title     = {Book 2},
      }
      @article{ruby5,
        title     = {Article 2},
      }
      """
    And I have a page "scholar.html":
      """
      ---
      ---
      {% bibliography -f references %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    Then "Journal Articles" should come before "Books" in "_site/scholar.html"
    And "Books" should come before "Technical Reports" in "_site/scholar.html"

  @tags @grouping
  Scenario: Type Names
    Given I have a scholar configuration with:
      | key         | value                      |
      | group_by    | type                       |
      | type_names  | { article: 'Long Papers' } |
    And I have a "_bibliography" directory
    And I have a file "_bibliography/references.bib":
      """
      @article{ruby1,
        title     = {Article},
      }
      @book{ruby2,
        title     = {Book},
      }
      """
    And I have a page "scholar.html":
      """
      ---
      ---
      {% bibliography -f references %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    Then I should see "Long Papers" in "_site/scholar.html"
    And I should not see "Journal Articles" in "_site/scholar.html"
    And I should see "Books" in "_site/scholar.html"

  @tags @grouping
  Scenario: Type Aliases
    Given I have a scholar configuration with:
      | key          | value                    |
      | group_by     | type                     |
      | type_aliases | { phdthesis: phdthesis } |
    And I have a "_bibliography" directory
    And I have a file "_bibliography/references.bib":
      """
      @mastersthesis{ruby1,
        title     = {MSc Thesis},
      }
      @phdthesis{ruby2,
        title     = {PhD Thesis},
      }
      """
    And I have a page "scholar.html":
      """
      ---
      ---
      {% bibliography -f references %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    Then I should see "PhD Theses" in "_site/scholar.html"
    And I should not see "Master's Theses" in "_site/scholar.html"

  @tags @grouping
  Scenario: Month Names
    Given I have a scholar configuration with:
      | key         | value                                                                                |
      | group_by    | month                                                                                |
      | month_names | [Januar,Februar,März,April,Mai,Juni,Juli,August,September,Oktober,November,Dezember] |
    And I have a "_bibliography" directory
    And I have a file "_bibliography/references.bib":
      """
      @book{ruby1,
        title     = {The Ruby Programming Language},
        author    = {Flanagan, David and Matsumoto, Yukihiro},
        year      = {2008},
        month     = jan
      }
      @book{ruby2,
        title     = {The Ruby Programming Language},
        author    = {Flanagan, David and Matsumoto, Yukihiro},
        year      = {2008},
        month     = dec
      }
      """
    And I have a page "scholar.html":
      """
      ---
      ---
      {% bibliography -f references %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    Then I should see "Januar" in "_site/scholar.html"
    And I should not see "January" in "_site/scholar.html"
    And I should see "Dezember" in "_site/scholar.html"
    And I should not see "December" in "_site/scholar.html"

  @tags @grouping
  Scenario: Local grouping override - no grouping
    Given I have a scholar configuration with:
      | group_by    | year |
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
      {% bibliography -f references --group_by none %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    Then I should not see "<h2 class=\"bibliography\">2007</h2>" in "_site/scholar.html"
    And I should not see "<h2 class=\"bibliography\">2008</h2>" in "_site/scholar.html"

  @tags @grouping
  Scenario: Local grouping override - grouping by year
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
      {% bibliography -f references --group_by year --group_order descending %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    Then I should see "<h2 class=\"bibliography\">2007</h2>" in "_site/scholar.html"
    And I should see "<h2 class=\"bibliography\">2008</h2>" in "_site/scholar.html"
    And "2008" should come before "2007" in "_site/scholar.html"
