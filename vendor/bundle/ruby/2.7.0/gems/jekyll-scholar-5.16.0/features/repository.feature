Feature: PDF Repository
  As a scholar who likes to blog
  I want to publish my BibTeX bibliography on my blog
  And I want Jekyll to generate links to PDFs of my references automatically

  @repository
  Scenario: A bibliography with a single entry and a repository
    Given I have a scholar configuration with:
      | key                   | value             |
      | source                | ./_bibliography   |
      | repository            | papers            |
      | bibliography_template | bibliography      |
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
    And I have a "papers" directory
    And I have a file "papers/ruby.pdf":
      """
      The PDF
      """
    And I have a file "papers/ruby.ppt":
      """
      The PPT
      """
    And I have a "_layouts" directory
    And I have a file "_layouts/bibliography.html":
      """
      ---
      ---
      {{ reference }} Link: {{ link }} Slides: {{ links.ppt }}
      """
    And I have a page "scholar.html":
      """
      ---
      ---
      {% bibliography %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/papers/ruby.pdf" file should exist
    And I should see "The Ruby Programming Language" in "_site/scholar.html"
    And I should see "Link: /papers/ruby.pdf" in "_site/scholar.html"
    And I should see "Slides: /papers/ruby.ppt" in "_site/scholar.html"

  @repository
  Scenario: A bibliography with a single entry and a repository, with source directory set
    Given I have a configuration file with:
      | key                   | value             |
      | source                | src               |
    And I have a scholar configuration with:
      | key                   | value             |
      | source                | _bibliography     |
      | repository            | papers            |
      | bibliography_template | bibliography      |
    And I have a "src" directory
    And I have a "src/_bibliography" directory
    And I have a file "src/_bibliography/references.bib":
      """
      @book{ruby,
        title     = {The Ruby Programming Language},
        author    = {Flanagan, David and Matsumoto, Yukihiro},
        year      = {2008},
        publisher = {O'Reilly Media}
      }
      """
    And I have a "src/papers" directory
    And I have a file "src/papers/ruby.pdf":
      """
      The PDF
      """
    And I have a file "src/papers/ruby.ppt":
      """
      The PPT
      """
    And I have a "src/_layouts" directory
    And I have a file "src/_layouts/bibliography.html":
      """
      ---
      ---
      {{ reference }} Link: {{ link }} Slides: {{ links.ppt }}
      """
    And I have a page "src/scholar.html":
      """
      ---
      ---
      {% bibliography %}
      """
    When I run jekyll
    Then the _site directory should exist
    And I should see "The Ruby Programming Language" in "_site/scholar.html"
    And the "_site/papers/ruby.pdf" file should exist
    And I should see "Link: /papers/ruby.pdf" in "_site/scholar.html"
    And I should see "Slides: /papers/ruby.ppt" in "_site/scholar.html"

  @repository
  Scenario: A bibliography with a single entry and a repository with slides pdf
    Given I have a scholar configuration with:
      | key                   | value             |
      | source                | ./_bibliography   |
      | repository            | papers            |
      | bibliography_template | bibliography      |

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
    And I have a "papers" directory
    And I have a file "papers/ruby.pdf":
      """
      The PDF
      """
    And I have a file "papers/ruby.slides.pdf":
      """
      The Slides PDF
      """
    And I have a "_layouts" directory
    And I have a file "_layouts/bibliography.html":
      """
      ---
      ---
      {{ reference }} Link: {{ link }} Slides: {{ links['slides.pdf'] }}
      """
    And I have a page "scholar.html":
      """
      ---
      ---
      {% bibliography %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/papers/ruby.pdf" file should exist
    And the "_site/papers/ruby.slides.pdf" file should exist
    And I should see "The Ruby Programming Language" in "_site/scholar.html"
    And I should see "Link: /papers/ruby.pdf" in "_site/scholar.html"
    And I should see "Slides: /papers/ruby.slides.pdf" in "_site/scholar.html"

  @repository
  Scenario: A bibliography with a single entry and a repository with slides pdf
    using a custom delimiter
    Given I have a scholar configuration with:
      | key                       | value             |
      | source                    | ./_bibliography   |
      | repository                | papers            |
      | bibliography_template     | bibliography      |
      | repository_file_delimiter | ':'               |

    And I have a "_bibliography" directory
    And I have a file "_bibliography/references.bib":
      """
      @book{ruby.ref,
        title     = {The Ruby Programming Language},
        author    = {Flanagan, David and Matsumoto, Yukihiro},
        year      = {2008},
        publisher = {O'Reilly Media}
      }
      """
    And I have a "papers" directory
    And I have a file "papers/ruby.ref:pdf":
      """
      The PDF
      """
    And I have a file "papers/ruby.ref:slides.pdf":
      """
      The Slides PDF
      """
    And I have a "_layouts" directory
    And I have a file "_layouts/bibliography.html":
      """
      ---
      ---
      {{ reference }} Link: {{ link }} Slides: {{ links['slides.pdf'] }}
      """
    And I have a page "scholar.html":
      """
      ---
      ---
      {% bibliography %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/papers/ruby.ref:pdf" file should exist
    And the "_site/papers/ruby.ref:slides.pdf" file should exist
    And I should see "The Ruby Programming Language" in "_site/scholar.html"
    And I should see "Link: /papers/ruby.ref:pdf" in "_site/scholar.html"
    And I should see "Slides: /papers/ruby.ref:slides.pdf" in "_site/scholar.html"

  @repository
  Scenario: A bibliography with a single entry and a repository with a directory
    named using the delimiter with slides pdf
    Given I have a scholar configuration with:
      | key                       | value             |
      | source                    | ./_bibliography   |
      | repository                | papers.dir        |
      | bibliography_template     | bibliography      |
      | repository_file_delimiter | '.'               |

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
    And I have a "papers.dir" directory
    And I have a file "papers.dir/ruby.pdf":
      """
      The PDF
      """
    And I have a file "papers.dir/ruby.slides.pdf":
      """
      The Slides PDF
      """
    And I have a "_layouts" directory
    And I have a file "_layouts/bibliography.html":
      """
      ---
      ---
      {{ reference }} Link: {{ link }} Slides: {{ links['slides.pdf'] }}
      """
    And I have a page "scholar.html":
      """
      ---
      ---
      {% bibliography %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/papers.dir/ruby.pdf" file should exist
    And the "_site/papers.dir/ruby.slides.pdf" file should exist
    And I should see "The Ruby Programming Language" in "_site/scholar.html"
    And I should see "Link: /papers.dir/ruby.pdf" in "_site/scholar.html"
    And I should see "Slides: /papers.dir/ruby.slides.pdf" in "_site/scholar.html"

  @repository
  Scenario: A bibliography with a single entry with a complex name
    Given I have a scholar configuration with:
      | key                   | value             |
      | source                | ./_bibliography   |
      | repository            | papers            |
      | bibliography_template | bibliography      |
    And I have a "_bibliography" directory
    And I have a file "_bibliography/references.bib":
      """
      @book{test:book/ruby/Flanagan08,
        title     = {The Ruby Programming Language},
        author    = {Flanagan, David and Matsumoto, Yukihiro},
        year      = {2008},
        publisher = {O'Reilly Media}
      }
      """
    And I have a "papers" directory
    And I have a "papers/test_book" directory
    And I have a "papers/test_book/ruby" directory
    And I have a file "papers/test_book/ruby/Flanagan08.pdf":
      """
      The PDF
      """
    And I have a "_layouts" directory
    And I have a file "_layouts/bibliography.html":
      """
      ---
      ---
      {{ reference }} Link: {{ link }}
      """
    And I have a page "scholar.html":
      """
      ---
      ---
      {% bibliography %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/papers/test_book/ruby/Flanagan08.pdf" file should exist
    And I should see "The Ruby Programming Language" in "_site/scholar.html"
    And I should see "Link: /papers/test_book/ruby/Flanagan08.pdf" in "_site/scholar.html"
