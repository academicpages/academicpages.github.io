LaTeX::Decode
=============

[![Build Status](https://travis-ci.org/inukshuk/latex-decode.png?branch=master)](https://travis-ci.org/inukshuk/latex-decode)

LaTeX::Decode is a Ruby gem to convert LaTeX input to Unicode. Its original
use was as an input filter for [BibTeX-Ruby](http://rubygems.org/gems/bibtex-ruby)
but can be used independently to decode LaTeX. Many of the patterns used by
this Ruby gem are based on François Charette's equivalent Perl module
[LaTeX::Decode](https://github.com/fc7/LaTeX-Decode).

Quickstart
----------

    $ [sudo] gem install latex-decode
    $ irb
    >> require 'latex/decode'
    >> LaTeX.decode "dipl\\^{o}me d'\\'{e}tudes sup\\'erieures"
    => "diplôme d'études supérieures"

Compatibility
-------------

Unicode handling is one of the major differences between Ruby 1.8 and newer
version; LaTeX::Decode; nevertheless, we try to support 1.8 as best as possible.

Issues
------

Please use the tracker of the project's
[GitHub repository](https://github.com/inukshuk/latex-decode) to report any
issues. When describing intended behaviour, please use the extremely simple
syntax of the Cucumber features used by LaTeX::Decode; for instance, you could
describe the example above as:

    Feature: Decode LaTeX accents
      As a hacker who works with LaTeX
      I want to be able to decode LaTeX accents

      Scenario: A French sentence
        When I decode the string "dipl\\^{o}me d'\\'{e}tudes sup\\'erieures"
        Then the result should be "diplôme d'études supérieures"

Credits
-------

Kudos and thanks to all [contributors](https://github.com/inukshuk/latex-decode/contributors)
who have made LaTeX::Decode possible!

Copyright (C) 2011-2015 [Sylvester Keil](sylvester.keil.or.at)

Copyright (C) 2010 François Charette

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
