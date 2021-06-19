CiteProc
========
CiteProc is a cite processor interface and citation data API based on the
Citation Style Language (CSL) specifications. To actually process citations
a dedicated processor engine is required; a pure Ruby engine is available
in the [citeproc-ruby](https://rubygems/gems/citeproc-ruby) gem.


[![Build Status](https://secure.travis-ci.org/inukshuk/citeproc.svg)](http://travis-ci.org/inukshuk/citeproc)
[![Coverage Status](https://coveralls.io/repos/inukshuk/citeproc/badge.svg?branch=master)](https://coveralls.io/r/inukshuk/citeproc?branch=master)

[![Build Status](https://secure.travis-ci.org/inukshuk/citeproc-ruby.svg)](http://travis-ci.org/inukshuk/citeproc-ruby)
[![Coverage Status](https://coveralls.io/repos/inukshuk/citeproc-ruby/badge.svg?branch=master)](https://coveralls.io/r/inukshuk/citeproc-ruby?branch=master)

[![Build Status](https://secure.travis-ci.org/inukshuk/csl-ruby.svg)](http://travis-ci.org/inukshuk/csl-ruby)
[![Coverage Status](https://coveralls.io/repos/inukshuk/csl-ruby/badge.svg?branch=master)](https://coveralls.io/r/inukshuk/csl-ruby?branch=master)

Quickstart
----------
Install CiteProc-Ruby and all official CSL styles (optional).

    $ [sudo] gem install citeproc-ruby
    $ [sudo] gem install csl-styles

Start rendering you references with any CSL style!

    require 'citeproc'
    require 'csl/styles'

    # Create a new processor with the desired style,
    # format, and locale.
    cp = CiteProc::Processor.new style: 'apa', format: 'text'

    # To see what styles are available in your current
    # environment, run `CSL::Style.ls'; this also works for
    # locales as `CSL::Locale.ls'.

    # Tell the processor where to find your references. In this
    # example we load them from a BibTeX bibliography using the
    # bibtex-ruby gem.
    cp.import BibTeX.open('./references.bib').to_citeproc

    # Now you are ready for rendering; the processor API
    # provides three main rendering methods: `process',
    # `append', or `bibliography'.

    # For simple one-off renditions, you can also call
    # `render' in bibliography or citation mode:
    cp.render :bibliography, id: 'knuth'

    # This will return a rendered reference, like:
    #-> Knuth, D. (1968). The art of computer programming. Boston: Addison-Wesley.

    # CiteProc-Ruby exposes a full CSL API to you; this
    # makes it possible to just alter CSL styles on the
    # fly. For example, what if we want names not to be
    # initialized even though APA style is configured to
    # do so? We could change the CSL style itself, but
    # we can also make a quick adjustment at runtime:
    name = cp.engine.style.macros['author'] > 'names' > 'name'

    # What just happened? We selected the current style's
    # 'author' macro and then descended to the CSL name
    # node via its parent names node. Now we can change
    # this name node and the cite processor output will
    # pick-up the changes right away:
    name[:initialize] = 'false'

    cp.render :bibliography, id: 'knuth'
    #-> Knuth, Donald. (1968). The art of computer programming (Vol. 1). Boston: Addison-Wesley.

    # Note that we have picked 'text' as the output format;
    # if we want to make us of richer output formats we
    # can switch to HTML instead:
    cp.engine.format = 'html'

    cp.render :bibliography, id: 'knuth'
    #-> Knuth, Donald. (1968). <i>The art of computer programming</i> (Vol. 1). Boston: Addison-Wesley.

    # You can also render citations on the fly.
    cp.render :citation, id: 'knuth', locator: '23'
    #-> (Knuth, 1968, p. 23)

Documentation
-------------
* [CiteProc Documentation](http://rubydoc.info/gems/citeproc/)
* [CiteProc-Ruby API Documentation](http://rubydoc.info/gems/citeproc-ruby/)
* [CSL-Ruby API Documentation](http://rubydoc.info/gems/csl/)

Optional Dependencies
---------------------
CiteProc-Ruby tries to minimize hard dependencies for increased compatibility.
You can speed up the XML parsing by installing
[Nokogiri](https://rubygems.org/gems/nokogiri); otherwise the REXML from the
Ruby standard library will be used.

Similarly, you can install either of the gems
[EDTF](https://rubygems.org/gems/edtf) or
[Chronic](https://rubygems.org/gems/chronic) to support a wide range of
additional inputs for date variables.

CSL Styles and Locales
----------------------
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

Compatibility
-------------
The cite processor and the CSL API libraries have been developed for MRI,
Rubinius, and JRuby. Please note that we try to support only Ruby versions
1.9.3 and upwards.

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
CiteProc is dual licensed under the AGPL and the FreeBSD license.
