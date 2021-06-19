Feature: Citations
  As a scholar who likes to blog
  I want to reference cool papers and books from my bibliography

  @tags @cite
  Scenario: A Simple Citation
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
      {% cite ruby %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    And I should see "Flanagan" in "_site/scholar.html"

  @tags @cite @post
  Scenario: A Simple Citation in a Post
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
      {% cite ruby %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/2017/06/26/scholar.html" file should exist
    And I should see "Flanagan" in "_site/2017/06/26/scholar.html"

  @tags @cite @file
  Scenario: Citing from another bibliography
    Given I have a scholar configuration with:
      | key          | value             |
      | source       | ./_bibliography   |
      | bibliography | my_references     |
    And I have a "_bibliography" directory
    And I have a file "_bibliography/other_references.bib":
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
      {% cite ruby --file other_references %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    And I should see "Flanagan" in "_site/scholar.html"

  @tags @cite @suppress-author
  Scenario: Citations With Suppressed Author
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
      {% cite ruby --suppress_author %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    And I should see "2008" in "_site/scholar.html"
    And I should not see "Flanagan" in "_site/scholar.html"

  @tags @cite
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
      {% cite java %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    And I should see "missing reference" in "_site/scholar.html"

  @tags @quote
  Scenario: A Simple Block-Quote
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
      {% quote ruby %}
      We <3 Ruby
      {% endquote %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    And I should see "<blockquote><p>We <3 Ruby</p><cite><a .*#ruby.+\(Flanagan" in "_site/scholar.html"

  @tags @quote @post
  Scenario: A Simple Block-Quote in a Post
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
      {% quote ruby %}
      We <3 Ruby
      {% endquote %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/2017/06/26/scholar.html" file should exist
    And I should see "<blockquote><p>We <3 Ruby</p><cite><a .*#ruby.+\(Flanagan" in "_site/2017/06/26/scholar.html"

  @tags @cite
  Scenario: A prefixed citation
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
      {% cite ruby --prefix a %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    And I should see "#a-ruby" in "_site/scholar.html"

  @tags @cite
  Scenario: Multiple Citations
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
      {% cite ruby microscope %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    And I should see "Flanagan &amp; Matsumoto, 2008; Shaughnessy, 2013" in "_site/scholar.html"

  @tags @cite @locator
  Scenario: Multiple Citations with locators
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
      {% cite ruby microscope -l 2-3 --locator 23 & 42 %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    And I should see "Matsumoto, 2008, pp. 2-3; Shaughnessy, 2013, pp. 23 &amp; 42" in "_site/scholar.html"

  @tags @cite @locator @label
  Scenario: Citations with locator labels
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
      {% cite ruby microscope --label chapter --locator 2-3 -L figure -l 4,5 %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    And I should see "Matsumoto, 2008, chaps. 2-3; Shaughnessy, 2013, figs. 4,5" in "_site/scholar.html"

  @tags @cite @locator @label
  Scenario: Citations with multiple locator labels
    Given I have a scholar configuration with:
      | key          | value             |
      | source       | ./_bibliography   |
      | bibliography | my_references     |
    And I have a "_bibliography" directory
    And I have a file "_bibliography/my_references.bib":
      """
      @book{ruby,
        title     = {The Ruby Programming Language},
        author    = {Matsumoto, Yukihiro},
        year      = {2008},
        publisher = {O'Reilly Media}
      }
      """
    And I have a page "scholar.html":
      """
      ---
      ---
      {% cite ruby --label chapter --locator 3 %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    And I should see "Matsumoto, 2008, chap. 3" in "_site/scholar.html"

  @tags @cite @citation_number
  Scenario: Multiple citations using citation numbers
    Given I have a scholar configuration with:
      | key          | value             |
      | source       | ./_bibliography   |
      | bibliography | my_references     |
      | style        | ieee              |
    And I have a "_bibliography" directory
    And I have a file "_bibliography/my_references.bib":
      """
      @book{ruby,
        title     = {The Ruby Programming Language},
        author    = {Flanagan, David and Matsumoto, Yukihiro},
        year      = {2008},
        publisher = {O'Reilly Media}
      }

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
      {% cite ruby microscope %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    And I should see "\[1\], \[2\]" in "_site/scholar.html"

  @tags @cite @citation_number
  Scenario: Multiple citations of the same item using citation numbers
    Given I have a scholar configuration with:
      | key          | value             |
      | source       | ./_bibliography   |
      | bibliography | my_references     |
      | style        | ieee              |
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
      {% cite ruby %}
      {% cite ruby %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    And I should see "\[1\]" in "_site/scholar.html"
    And I should not see "\[2\]" in "_site/scholar.html"

  @tags @cite @variables
  Scenario: A Simple Citation using liquid variables
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
      {% assign myVariable = 'ruby' %}
      {% cite myVariable %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    And I should see "Flanagan" in "_site/scholar.html"

  @tags @cite @variables @data
  Scenario: A Simple Citation using liquid variables
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
    And I have a "_data" directory
    And I have a file "_data/covers.yml":
      """
      - reference: "ruby"
        image: "/img/covers/cover_01.png"
      """
    And I have a page "scholar.html":
      """
      ---
      ---
      {% for cover in site.data.covers %}
        {% cite cover.reference %}
      {% endfor %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    And I should see "Flanagan" in "_site/scholar.html"

  @tags @cite @variables @data
  Scenario: Multiple Citations in a list using liquid variables
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

      @book{gof,
         Author = {Erich Gamma and Richard Helm and Ralph Johnson and John Vlissides},
         Title = {Design Patterns: Elements of Reusable Object-Oriented Software},
         Publisher = {Addison-Wesley Professional},
         Year = {1994},
      }
      """
    And I have a "_data" directory
    And I have a file "_data/covers.yml":
      """
      - reference: "ruby"
        image: "/img/covers/cover_01.png"
      - reference: "gof"
        image: "/img/covers/cover_02.png"
      """
    And I have a page "scholar.html":
      """
      ---
      ---
      {% for cover in site.data.covers %}
        {% cite cover.reference %}
      {% endfor %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    And I should see "Flanagan" in "_site/scholar.html"
    And I should see "Gamma" in "_site/scholar.html"

