Feature: BibTeX
  As a scholar who likes to blog
  I want to publish my BibTeX bibliography on my blog
  In order to share my awesome references with my peers

  @converters
  Scenario: Simple Bibliography
    Given I have a scholar configuration with:
      | key   | value |
      | style | apa   |
     And I have a page "references.bib":
      """
      ---
      ---
      @book{ruby,
        title     = {The Ruby Programming Language},
        author    = {Flanagan, David and Matsumoto, Yukihiro},
        year      = {2008},
        publisher = {O'Reilly Media}
      }
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/references.html" file should exist
    And I should see "<i>The Ruby Programming Language</i>" in "_site/references.html"

  @converters @post
  Scenario: Simple Bibliography
    Given I have a scholar configuration with:
      | key   | value |
      | style | apa   |
     And I have a "_posts" directory
     And I have a page "_posts/2017-06-26-references.bib":
      """
      ---
      ---
      @book{ruby,
        title     = {The Ruby Programming Language},
        author    = {Flanagan, David and Matsumoto, Yukihiro},
        year      = {2008},
        publisher = {O'Reilly Media}
      }
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/2017/06/26/references.html" file should exist
    And I should see "<i>The Ruby Programming Language</i>" in "_site/2017/06/26/references.html"

  @converters
  Scenario: Markdown Formatted Bibliography
    Given I have a scholar configuration with:
      | key   | value |
      | style | apa   |
    And I have a page "references.bib":
      """
      ---
      ---
      References
      ==========

      @book{ruby,
        title     = {The Ruby Programming Language},
        author    = {Flanagan, David and Matsumoto, Yukihiro},
        year      = {2008},
        publisher = {O'Reilly Media}
      }
      """
    When I run jekyll
    Then I should see "<h1[^>]*>References</h1>" in "_site/references.html"

  @latex
  Scenario: Simple Bibliography with LaTeX directives
    Given I have a scholar configuration with:
      | key   | value |
      | style | apa   |
    And I have a page "references.bib":
      """
      ---
      ---
      @misc{umlaut,
        title     = {Look, an umlaut: \"u!},
      }
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/references.html" file should exist
    And I should see "Look, an umlaut: ü!" in "_site/references.html"

  @superscript
  Scenario: Simple Bibliography with LaTeX superscript
    Given I have a scholar configuration with:
      | key   | value |
      | style | apa   |
    And I have a page "references.bib":
      """
      ---
      ---
      @misc{umlaut,
        title     = {Look, \textsuperscript{superscript}!},
      }
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/references.html" file should exist
    And I should see "Look, <sup>superscript</sup>!" in "_site/references.html"

  @tags @bibtex
  Scenario: Embedded BibTeX
    Given I have a scholar configuration with:
      | key   | value |
      | style | apa   |
     And I have a page "references.md":
      """
      ---
      ---
      References
      ==========

      {% bibtex %}
      @book{ruby,
        title     = {The Ruby Programming Language},
        author    = {Flanagan, David and Matsumoto, Yukihiro},
        year      = {2008},
        publisher = {O'Reilly Media}
      }
      {% endbibtex %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/references.html" file should exist
    And I should see "<i>The Ruby Programming Language</i>" in "_site/references.html"

  @tags @bibtex @post
  Scenario: Embedded BibTeX
    Given I have a scholar configuration with:
      | key   | value |
      | style | apa   |
     And I have a "_posts" directory
     And I have a page "_posts/2017-06-26-references.md":
      """
      ---
      ---
      References
      ==========

      {% bibtex %}
      @book{ruby,
        title     = {The Ruby Programming Language},
        author    = {Flanagan, David and Matsumoto, Yukihiro},
        year      = {2008},
        publisher = {O'Reilly Media}
      }
      {% endbibtex %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/2017/06/26/references.html" file should exist
    And I should see "<i>The Ruby Programming Language</i>" in "_site/2017/06/26/references.html"

  @tags @bibliography
  @tags @bibliography
  Scenario: Simple Bibliography Loaded From Default Directory
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

  @tags @bibliography @post
  Scenario: Simple Bibliography in a Jekyll Post
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
      }
      """
    And I have a "_posts" directory
    And I have a page "_posts/2017-06-26-scholar.html":
      """
      ---
      ---
      {% bibliography -f references %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/2017/06/26/scholar.html" file should exist
    And I should see "<i>The Ruby Programming Language</i>" in "_site/2017/06/26/scholar.html"

  @tags @bibliography @config @template
  Scenario: Simple Bibliography With Custom Template
    Given I have a scholar configuration with:
      | key                   | value                                         |
      | source                | ./_bibliography                               |
      | bibliography_template | <abbr>{{index}} {{entry.type}} [{{key}}]</abbr>{{entry.author_1_last}} |
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
      ---
      {% bibliography -f references %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    And I should see "<abbr>1 book \[ruby\]</abbr>Matsumoto" in "_site/scholar.html"

  @tags @bibliography @config @template
  Scenario: Simple Bibliography With Custom Template
    Given I have a scholar configuration with:
      | key                   | value                                         |
      | source                | ./_bibliography                               |
      | bibliography_template | <abbr>{{index}} {{entry.type}} [{{key}}]</abbr>{{entry.author_array[1].last}} |
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
      ---
      {% bibliography -f references %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    And I should see "<abbr>1 book \[ruby\]</abbr>Matsumoto" in "_site/scholar.html"

  @tags @bibliography @config @template @names
  Scenario: Simple Bibliography With Custom Template and Name Parsing
    Given I have a scholar configuration with:
      | key                   | value                         |
      | source                | ./_bibliography               |
      | bibliography_template | <span>{{entry.author}}</span> |
    And I have the following BibTeX options:
      | key                   | value  |
      | parse_names           | false  |
    And I have a "_bibliography" directory
    And I have a file "_bibliography/references.bib":
      """
      @book{ruby,
        title     = {The Ruby Programming Language},
        author    = {David Flanagan and Matsumoto, Yukihiro},
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
    And I should see "David Flanagan and Matsumoto, Yukihiro" in "_site/scholar.html"

  @tags @filter
  Scenario: Filtered Bibliography Loaded From Default Directory
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
    And I have a page "scholar.html":
      """
      ---
      ---
      {% bibliography -f references --query @book[year <= 2000] %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    And I should not see "<i>The Ruby Programming Language</i>" in "_site/scholar.html"
    And I should see "<i>Smalltalk Best Practice Patterns</i>" in "_site/scholar.html"

  @tags @filter @variables
  Scenario: Filter using interpolated query variable
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
    And I have a page "scholar.html":
      """
      ---
      ---
      {% assign yr = 2000 %}
      {% bibliography -f references --query @book[year <= {{ yr }}] %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    And I should not see "<i>The Ruby Programming Language</i>" in "_site/scholar.html"
    And I should see "<i>Smalltalk Best Practice Patterns</i>" in "_site/scholar.html"

  @filter @regex
  Scenario: Filter using interpolated query variable
    Given I have a scholar configuration with:
      | key    | value             |
      | source | ./_bibliography   |
    And I have a "_bibliography" directory
    And I have a file "_bibliography/references.bib":
      """
      @article{testa,
        title={test1},
        author={Albert, Alex A and Booth, Brian and Cook, Cathy},
        journal={Irrelevant},
        year={2018}
      }
      @article{testb,
        title={test2},
        author={Booth, Brian and Albert, Alex and Cook, Cathy},
        journal={Irrelevant},
        year={2018}
      }
      @article{testc,
        title={test3},
        author={Cook, Cathy and Booth, Brian and Albert, Alex},
        journal={Irrelevant},
        year={2018}
      }
      @article{testd,
        title={test4},
        author={Done, Daniel},
        journal={Irrelevant},
        year={2018}
      }
      """
    And I have a page "scholar.html":
      """
      ---
      ---
      {% bibliography --query @*[author ~= \bAlbert\b] %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    And I should see "test1" in "_site/scholar.html"
    And I should see "test2" in "_site/scholar.html"
    And I should see "test3" in "_site/scholar.html"
    And I should not see "test4" in "_site/scholar.html"

  @tags @bibliography @prefix
  Scenario: A Prefixed Bibliography
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
    And I have a page "scholar.html":
      """
      ---
      ---
      {% bibliography --file references --prefix a -q @book[year <= 2000] %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    And I should not see "ruby" in "_site/scholar.html"
    And I should see "id=\"a-smalltalk\"" in "_site/scholar.html"

  @tags @bibliography @style
  Scenario: Simple Bibliography Loaded From Default Directory
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
      }
      """
    And I have a page "scholar.html":
      """
      ---
      ---
      {% bibliography  --style modern-language-association %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    And I should see "<i>The Ruby Programming Language</i>. O’Reilly Media, 2008" in "_site/scholar.html"

  @config @bibliography @style
  Scenario: A custom style with Jekyll source directory set
    Given I have a configuration file with:
      | key     | value              |
      | source  | src                |
    And I have a scholar configuration with:
      | key     | value              |
      | source  | _bibliography      |
      | style   | _styles/custom.csl |
    And I have a "src" directory
    And I have a "src/_bibliography" directory
    And I have a "src/_styles" directory
    And I have a file "src/_styles/custom.csl":
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
    And I have a file "src/_bibliography/references.bib":
      """
      @book{ruby,
        title     = {The Ruby Programming Language},
        author    = {Flanagan, David and Matsumoto, Yukihiro},
        year      = {2008},
        publisher = {O'Reilly Media}
      }
      """
    And I have a page "src/scholar.html":
      """
      ---
      ---
      {% bibliography --style _styles/custom.csl %}
      """
    When I run jekyll
    Then the _site directory should exist
    And I should see "The Ruby Programming Language" in "_site/scholar.html"

  @tags @bibliography @locale
  Scenario: Non-english reference
    Given I have a scholar configuration with:
      | key                    | value                         |
      | source                 | ./_bibliography               |
      | bibliography           | my_references                 |
      | allow_locale_overrides | true                          |
      | style                  | chicago-fullnote-bibliography |
    And I have a "_bibliography" directory
    And I have a file "_bibliography/my_references.bib":
      """
      @article{one,
        title = {Ideología y narrativa en el Ramayana de Valmiki},
        number = {22},
        language = {es},
        journal = {Estudios de Asia y Africa},
        author = {Pollock, Sheldon I.},
        year = {1987},
        pages = {336--54}
      }
      @article{two,
        title = {{Ideología y narrativa en el Ramayana de Valmiki}},
        number = {22},
        journal = {Estudios de Asia y Africa},
        author = {Pollock, Sheldon I.},
        year = {1987},
        pages = {336--54}
      }
      """
    And I have a page "scholar.html":
      """
      ---
      ---
      {% bibliography %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    And I should see "Estudios de Asia y Africa</i>, n.º 22" in "_site/scholar.html"
    And I should see "Estudios De Asia y Africa</i>, no. 22" in "_site/scholar.html"

  @latex
  Scenario: Simple Bibliography with LaTeX directives
    Given I have a "_bibliography" directory
    And I have a file "_bibliography/references.bib":
      """
      @book{rosso_image_2006,
        address = {{Paris}},
        series = {{Arch{\'e}ologie et histoire de l'art}},
        title = {{L'image de l'empereur en Gaule romaine :  portraits et inscriptions}},
        isbn = {978-2-7355-0583-8},
        lccn = {Tolbiac - Rez de Jardin - Philosophie, histoire, sciences de l'homme - Magasin - 2006-174258},
        shorttitle = {{L'image de l'empereur en Gaule romaine}},
        language = {fre},
        number = {20},
        publisher = {{{\'E}d. du Comit{\'e} des travaux historiques et scientifiques}},
        author = {Rosso, Emmanuelle},
        year = {2006},
        keywords = {Empereurs,Inscriptions latines,Sculpture de portraits romaine},
        note = {ill., couv. ill. 27 cm. Ouvrage issu des m{\'e}moires de ma{\^i}trise et de DEA. Bibliogr. p. 561-582. Notes bibliogr.}
      }
      """
    And I have a page "test.md":
      """
      ---
      ---
      {% bibliography --style apa-6th-edition %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/test.html" file should exist
    And I should see "L’image de l’empereur en Gaule romaine" in "_site/test.html"
    And I should see "Paris" in "_site/test.html"

  Scenario: Simple Bibliography With Custom Template and Double Braces
    Given I have a scholar configuration with:
      | key                   | value                    |
      | source                | ./_bibliography          |
      | bibliography_template | <h1>{{entry.title}}</h1> |
    And I have a "_bibliography" directory
    And I have a file "_bibliography/references.bib":
      """
      @misc{x,
        title = {{No Escape}},
        year  = {2019}
      }
      """
    And I have a page "scholar.html":
      """
      ---
      ---
      {% bibliography %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    And I should see "<h1>No Escape</h1>" in "_site/scholar.html"

  Scenario: Simple Bibliography With Custom Template and Raw BibTeX
    Given I have a scholar configuration with:
      | key                   | value                           |
      | source                | ./_bibliography                 |
      | bibliography_template | <pre>{{entry.bibtex}}</pre> |
    And I have a "_bibliography" directory
    And I have a file "_bibliography/references.bib":
      """
      @misc{x,
        title = {{No Escape}},
        year  = {2019}
      }
      """
    And I have a page "scholar.html":
      """
      ---
      ---
      {% bibliography %}
      """
    When I run jekyll
    Then the _site directory should exist
    And the "_site/scholar.html" file should exist
    And I should see "{{No Escape}}" in "_site/scholar.html"
    And I should not see "raw" in "_site/scholar.html"
