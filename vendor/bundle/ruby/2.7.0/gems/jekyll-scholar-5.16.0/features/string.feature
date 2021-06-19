Feature: String replacement
  As a scholar who likes to blog
  I want to publish my BibTeX bibliography on my blog
  And make sure that strings are correctly substituted

  @tags @string
  Scenario: String replacement
    Given I have a scholar configuration with:
      | key    | value             |
      | source | ./_bibliography   |
    And I have a "_bibliography" directory
    And I have a file "_bibliography/references.bib":
      """
      @string{ rubypl = "The Ruby Programming Language" }
      @book{ruby,
        title     = rubypl,
        author    = {Flanagan, David and Matsumoto, Yukihiro},
        year      = {2008},
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
    And I should see "<i>The Ruby Programming Language</i>" in "_site/scholar.html"

  @tags @string
  Scenario: String replacement disabled
    Given I have a scholar configuration with:
      | key             | value             |
      | source          | ./_bibliography   |
      | replace_strings | false             |
    And I have a "_bibliography" directory
    And I have a file "_bibliography/references.bib":
      """
      @string{ rubypl = "The Ruby Programming Language" }
      @book{ruby,
        title     = rubypl,
        author    = {Flanagan, David and Matsumoto, Yukihiro},
        year      = {2008},
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
    And I should see "<i>rubypl</i>" in "_site/scholar.html"

  @tags @string
  Scenario: Join strings
    Given I have a scholar configuration with:
      | key    | value             |
      | source | ./_bibliography   |
    And I have a "_bibliography" directory
    And I have a file "_bibliography/references.bib":
      """
      @string{ ruby = "Ruby" }
      @book{ruby,
        title     = "The " # ruby # " Programming Language",
        author    = {Flanagan, David and Matsumoto, Yukihiro},
        year      = {2008},
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
    And I should see "<i>The Ruby Programming Language</i>" in "_site/scholar.html"

  @tags @string
  Scenario: Join strings disabled
    Given I have a scholar configuration with:
      | key          | value             |
      | source       | ./_bibliography   |
      | join_strings | false             |
    And I have a "_bibliography" directory
    And I have a file "_bibliography/references.bib":
      """
      @string{ ruby = "Ruby" }
      @book{ruby,
        title     = "The " # ruby # " Programming Language",
        author    = {Flanagan, David and Matsumoto, Yukihiro},
        year      = {2008},
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
    And I should see "<i>\"The \" # \"Ruby\" # \" Programming Language\"</i>" in "_site/scholar.html"

    @tags @string
    Scenario: String replacement with queries involving negative conditions
      Given I have a scholar configuration with:
        | key    | value             |
        | source | ./_bibliography   |
      And I have a "_bibliography" directory
      And I have a file "_bibliography/references.bib":
        """
        @string{ rubypl = "The Ruby Programming Language" }
        @book{ruby,
          title     = rubypl,
          author    = {Flanagan, David and Matsumoto, Yukihiro},
          year      = {2008},
          publisher = {O'Reilly Media}
        }
        """
      And I have a page "scholar.html":
        """
        ---
        ---
        {% bibliography -f references --query !@article %}
        """
      When I run jekyll
      Then the _site directory should exist
      And the "_site/scholar.html" file should exist
      And I should see "<i>The Ruby Programming Language</i>" in "_site/scholar.html"
