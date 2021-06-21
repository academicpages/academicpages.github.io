CSL-Ruby
========
CSL-Ruby provides a Ruby parser and a comprehensive API for the
[Citation Style Language](http://citationstyles.org) (CSL), an XML-based
format to describe the formatting of citations, notes and bibliographies.

[![Build Status](https://secure.travis-ci.org/inukshuk/csl-ruby.png)](http://travis-ci.org/inukshuk/csl-ruby)
[![Coverage Status](https://coveralls.io/repos/inukshuk/csl-ruby/badge.png?branch=master)](https://coveralls.io/r/inukshuk/csl-ruby?branch=master)

Styles and Locales
------------------
You can load CSL styles and locales by passing a respective XML string, file
name, or URL. You can also load styles and locales by name if the
corresponding files are installed in your local styles and locale directories.
By default, CSL-Ruby looks for CSL styles and locale files in

    /usr/local/share/csl/styles
    /usr/local/share/csl/locales

You can change these locations by changing the value of `CSL::Style.root` and
`CSL::Locale.root` respectively.

Alternatively, you can `gem install csl-styles` to install all official CSL
styles and locales. To make the styles and locales available, simply
`require 'csl/styles`.

Usage
-----
CSL-Ruby is broadly aimed at two very different usage scenarios: on the one
hand, you can use the parser to load existing styles and locales and
manipulate, query or otherwise work with them using a dedicated API: that is
to say, you do not have to resort to XML-related methods of access, but can
make use of a large set of library methods which are specific to CSL. This
is useful, primarily, for citation processors like
[CiteProc-Ruby](https://github.com/inukshuk/citeproc).

On the other hand, CSL-Ruby makes it easy to create new styles and locales
using Ruby; this is useful, for example, if you need to change or adapt
styles on-the-fly or for writing an interactive style editor.

To get you started, here are a few usage examples; for the full set of
available features, please consult the
[API documentation](http://rubydoc.info/gems/csl/).

    require 'csl'

    # Load a style from the Zotero style repository
    jps = CSL::Style.load 'http://zotero.org/styles/american-journal-of-political-science'

    # Query style information
    jps.title #-> "American Journal of Political Science"
    jps.independent? #-> true
    jps.citation_format #-> :"author-date"

    # Validate style against the CSL schema
    jps.valid? #-> true

    # Load another style
    amc = CSL::Style.load 'http://zotero.org/styles/applied-mathematics-and-computation'

    amc.independent? #-> false

    # Load the independent parent style
    parent = amc.independent_parent
    parent.title #-> "Elsevier (numeric, with titles)"

    # Load standard CSL styles and locales from csl-styles gem
    # Requires you to gem install csl-styles
    require 'csl/styles'

    # Load a locally installed style
    apa = CSL::Style.load :apa

    # Fetch the a macro
    authors = apa.macros['authors'].children[0]
    #-> #<CSL::Style::Names variable="author" children=[2]>

    # Load a locally installed locale
    fr = CSL::Locale.load :fr

    # Translate a term
    fr.translate 'editor' #-> "éditeur"
    fr.translate 'editor', plural: true #-> "éditeurs"
    fr.translate 'editor', form: 'short' #-> "éd."

    # Ordinalize a number
    fr.ordinalize 42 #=> "42ᵉ"
    fr.ordinalize 3, form: 'long' => "troisième"

    # Create a new style
    style = CSL::Style.new

    style.id = 'http://www.zotero.org/styles/my-style'
    style.title = 'My Style'

    # Add the default license for CSL styles
    style.default_license!

    # Access the style as XML
    style.to_xml

    # Access the style as XML (pretty printed)
    style.to_s

Dependencies
------------
CSL-Ruby was written with portability in mind. For performance reasons it
will use [Nokogiri ](http://nokogiri.org) for XML parsing and validation
if available; however, CSL-Ruby will fallback to REXML from the Ruby standard
library. In order to use Nokogiri, simply `gem install nokogiri` or add it
to your Gemfile.

Development
-----------
The CSL-Ruby source code is [hosted on GitHub](https://github.com/inukshuk/csl-ruby).
You can check out a copy of the latest code using Git:

    $ git clone https://github.com/inukshuk/csl-ruby.git

To get started, install the development dependencies and run all tests:

    $ cd csl-ruby
    $ bundle install
    $ rake

If you've found a bug or have a question, please open an issue on the
[issue tracker](https://github.com/inukshuk/csl-ruby/issues).
Or, for extra credit, clone the CSL-Ruby repository, write a failing
example, fix the bug and submit a pull request.

Credits
-------
Thanks to Rintze M. Zelle, Sebastian Karcher, Frank G. Bennett, Jr.,
and Bruce D'Arcus of CSL and citeproc-js fame for their support!

Thanks to Google and the Berkman Center at Harvard University for supporting
this project as part of [Google Summer of Code](https://developers.google.com/open-source/soc/).

Copyright
---------
Copyright 2009-2020 Sylvester Keil. All rights reserved.

Copyright 2012 President and Fellows of Harvard College.

License
-------
CSL-Ruby is dual licensed under the AGPL and the FreeBSD license.
