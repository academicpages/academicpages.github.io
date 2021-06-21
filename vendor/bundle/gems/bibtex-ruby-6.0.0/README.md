BibTeX-Ruby
===========

BibTeX-Ruby is the Rubyist's swiss-army-knife for all things BibTeX. It
includes a parser for all common BibTeX objects (@string, @preamble, @comment
and regular entries) and a sophisticated name parser that tokenizes correctly
formatted names; BibTeX-Ruby recognizes BibTeX string replacements, joins
values containing multiple strings or variables, supports cross-references,
and decodes common LaTeX formatting instructions to unicode; if you are in a
hurry, it also allows for easy export/conversion to formats such as YAML,
JSON, CiteProc/CSL, XML (BibTeXML, requires `rexml`), and RDF (experimental).

For a list of projects using BibTeX-Ruby, take a look at the
[project wiki](https://github.com/inukshuk/bibtex-ruby/wiki/Projects-Using-BibTeX-Ruby).


Quickstart
----------
Install and load BibTeX-Ruby in an IRB session:

    $ [sudo] gem install bibtex-ruby
    $ irb
    >> require 'bibtex'

Open a BibTeX bibliography:

    b = BibTeX.open('./ruby.bib')

Select a BibTeX entry and access individual fields:

    b['pickaxe'].title
    #=> "Programming Ruby 1.9: The Pragmatic Programmer's Guide"
    b[:pickaxe].author.length
    #=> 3
    b[:pickaxe].author.to_s
    #=> "Thomas, D. and Fowler, Chad and Hunt, Andy"
    b[:pickaxe].author[2].first
    #=> "Andy"

Query a bibliography:

    b['@book'].length
    #=> 3 - the number books in the bibliography
    b['@article'].length
    #=> 0 - the number of articles in the bibliography
    b['@book[year=2009]'].length
    #=> 1 - the number of books published in 2009

Extend first name initials throughout your bibliography:

    b.extend_initials ['Dave', 'Thomas']
    b[:pickaxe].author.to_s
    #=> "Thomas, Dave and Fowler, Chad and Hunt, Andy"

You can also extend all names in the bibliography to their prototypical
(i.e., the longest available) form:

    b.extend_initials! #=> extends all names in the bibliography

Use with caution as this method will treat two names as identical if they
look the same in their `#sort_order(:initials => true)` form.

Unify certain fields across the bibliography:

    b.unify :publisher, /o'?reilly/i, "O'Reilly"

    b.unify :publisher, /^penguin/i do |entry|
      entry.publisher = 'Penguin Books'
      entry.address = 'London'
    end

This will unify various spellings of entries published by O'Reilly and Penguin.

Render your bibliography in one of
[many different citation styles](https://github.com/citation-style-language/styles)
(requires the **citeproc-ruby** gem):

    require 'citeproc'
    CiteProc.process b[:pickaxe].to_citeproc, :style => :apa
    #=> "Thomas, D., Fowler, C., & Hunt, A. (2009). Programming Ruby 1.9: The Pragmatic Programmer's
      Guide. The Facets of Ruby. Raleigh, North Carolina: The Pragmatic Bookshelf."
    CiteProc.process b[:pickaxe].to_citeproc, :style => 'chicago-author-date'
    #=> "Thomas, Dave, Chad Fowler, and Andy Hunt. 2009. Programming Ruby 1.9: The Pragmatic
      Programmer's Guide. The Facets of Ruby.Raleigh, North Carolina: The Pragmatic Bookshelf."
    CiteProc.process b[:pickaxe].to_citeproc, :style => :mla
    #=> "Thomas, Dave, Chad Fowler, and Andy Hunt. Programming Ruby 1.9: The Pragmatic Programmer's
      Guide. Raleigh, North Carolina: The Pragmatic Bookshelf, 2009."

Save a bibliography to a file:

    b.save
    #=> saves the original file
    b.save_to(file)
    #=> saves the bibliography in a new file


Compatibility
-------------
The BibTeX-Ruby gem has been developed and tested on Ruby 2.x, 1.9.3, and 1.8;
it has been confirmed to work with JRuby, Rubinius, and REE, however, there
have been repeated [issues](https://github.com/inukshuk/bibtex-ruby/issues)
(performance mostly) with MacRuby caused by MacRuby's current StringScanner
implementation.

Starting with BibTeX-Ruby version 3.0, support for Ruby versions 1.9.2 and
earlier has been dropped; most features will likely continue to work, but
compliance with old Rubies is not a priority going forward.


Documentation
-------------
It is very easy to use BibTeX-Ruby. You can use the top level utility methods
**BibTeX.open** and **BibTeX.parse** to open a '.bib' file or to parse a
string containing BibTeX contents. By default, BibTeX-Ruby will discard all
text outside of regular BibTeX elements; however, if you wish to include
everything, simply add `:include => [:meta_content]` to your invocation of
**BibTeX.open** or **BibTeX.parse**.

Once BibTeX-Ruby has parsed your '.bib' file, you can easily access individual
entries. For example, if you set up your bibliography as follows:

    b = BibTeX.parse <<-END
    @book{pickaxe,
      address = {Raleigh, North Carolina},
      author = {Thomas, Dave and Fowler, Chad and Hunt, Andy},
      publisher = {The Pragmatic Bookshelf},
      series = {The Facets of Ruby},
      title = {Programming Ruby 1.9: The Pragmatic Programmer's Guide},
      year = {2009}
    }
    END

You could easily access it, using the entry's key, 'pickaxe', like so:
`b[:pickaxe]`; you also have easy access to individual fields, for example:
`b[:pickaxe][:author]`. Alternatively, BibTeX-Ruby accepts ghost methods to
conveniently access an entry's fields, similar to **ActiveRecord::Base**.
Therefore, it is equally possible to access the 'author' field above as
`b[:pickaxe].author`.

BibTeX-Ruby wraps all values of fields in an entry in Value
objects. This is necessary to transparently handle different types of values
(e.g., strings, dates, names etc.). These Value objects are designed to be
hardly discernible from regular Ruby strings, however, if you ever run into a
problem with a field's value, simply convert it to a string by calling the
`#to_s` method.

Instead of parsing strings you can also create BibTeX elements directly in
Ruby:

    > bib = BibTeX::Bibliography.new

Using a Hash:

    > bib << BibTeX::Entry.new({
        :bibtex_type => :book,
        :key => :rails,
        :address => 'Raleigh, North Carolina',
        :author => 'Ruby, Sam and Thomas, Dave, and Hansson, David Heinemeier',
        :booktitle => 'Agile Web Development with Rails',
        :edition => 'third',
        :keywords => 'ruby, rails',
        :publisher => 'The Pragmatic Bookshelf',
        :series => 'The Facets of Ruby',
        :title => 'Agile Web Development with Rails',
        :year => '2009'
      })

Or programmatically:

    > book = BibTeX::Entry.new
    > book.type = :book
    > book.key = :mybook
    > bib << book


### Cross References

From version 2.0, BibTeX-Ruby correctly resolves entry cross-references,
which are commonly used for entries with type `inbook`, `incollection`,
and `inproceedings`. When an entry has a valid citation key in the field
`crossref`, BibTeX-Ruby will return any fields inherited from the parent
entry:

    > b = BibTeX.parse <<-END
    @inbook{fraassen_1989b,
      Crossref = {fraassen_1989},
      Pages = {40-64},
      Title = {Ideal Science: David Lewis's Account of Laws},
    }

    @book{fraassen_1989,
      Address = {Oxford},
      Author = {Bas C. van Fraassen},
      Publisher = {Oxford University Press},
      Title = {Laws and Symmetry},
      Year = 1989
    }
    END
    > b['fraassen_1989b'].booktitle
    => <"Laws and Symmetry">


### Queries

Since version 1.3 BibTeX-Ruby implements a simple query language to search
Bibliographies via the `Bibliography#query` (or `Bibliography#q`) methods.
Additionally, you can access individual elements or groups of elements via
their index using `Bibliography#[]`; this accessor also exposes some of the
query functionality with the exception of yielding to a block. For instance:

    bib[-1]
    => Returns the last element of the Bibliography or nil
    bib[1,2]
    => Returns the second and third elements or nil
    bib[1..2]
    => Same as above

    bib[:key]
    => Returns the first entry with key 'key' or nil
    bib['key']
    => Returns all entries with key 'key' or []

    bib['@article']
    => Returns all entries of type 'article' or []
    bib['!@book']
    => Returns all entries of any type other than 'book' or []
    bib['@preamble']
    => Returns all preamble objects (this is the same as Bibliography#preambles) or []
    bib[/ruby/]
    => Returns all objects that match 'ruby' anywhere or []

    bib['@incollection[booktitle]']
    => Returns all in-collection entries with a booktitle or []

    # note that the above includes entries inheriting the book title
    # from a cross-referenced entry!

    bib['@book[keywords=ruby]']
    => Returns all books whose keywords attribute equals 'ruby' or []
    bib['@book[keywords!=ruby]']
    => Returns all books whose keywords attribute does not equal 'ruby'
    bib['@book[keywords/=ruby]']
    => Same as above

    bib.q('@book[keywords ^= ruby]')
    => Returns all books whose keywords attribute matches /^ruby/
    bib.q('@book[keywords ~= ruby]')
    => Returns all books whose keywords attribute matches /ruby/
    bib['@book[keywords!~ruby]']
    => Returns all books whose keywords attribute does not match /ruby/ or don't have keywords attribute

    bib.q('@article[year<=2007]')
    => Returns all articles published in 2007 or earlier
    bib.query('@book') { |e| e.keywords.split(/,/).length > 1 }
    => Returns all book entries with two or more keywords or []

Queries offer syntactic sugar for common enumerator invocations:

    bib.query(:all, '@book')
    => same as bib.select { |b| b.has_type?(:book) }
    bib.query('@book')
    => same as above
    bib.query(:first, '@book')
    => same as bib.detect { |b| b.has_type?(:book) }
    bib.query(:none, '@book')
    => same as bib.reject { |b| b.has_type?(:book) }

You can also use queries to delete entries in your bibliography:

    bib.delete(/ruby/)
    => deletes all object that match 'ruby' in their string representation
    bib.delete('@comment')
    => strips all BibTeX comments from the bibliography


### String Replacement

If your bibliography contains BibTeX @string objects, you can let BibTeX-Ruby
replace the strings for you. You have access to a bibliography's strings via
**BibTeX::Bibliography#strings** or by using a '@string' query.
You can replace the string symbols of an object by calling the object's
the **replace** method. Thus, to replace all strings defined in bibliography
b you could use the following code:

    b.each do |obj|
      obj.replace(b.q('@string'))
    end
    
A shorthand version for replacing all strings in a given bibliography is the
`Bibliography#replace` method. Similarly, you can use the
`Bibliography#join` method to join individual strings together. For instance:

    > bib = BibTeX::Bibliography.new
    > bib.add BibTeX::Element.parse '@string{ foo = "foo" }'
    > bib << BibTeX::Element.parse '@string{ bar = "bar" }'
    > bib.add BibTeX::Element.parse <<-END
    >  @book{abook,
    >    author = foo # "Author",
    >    title = foo # bar
    >  }
    > END
    > puts bib[:abook].to_s
    @book{abook,
      author = foo # "Author",
      title = foo # bar
    }
    > bib.replace
    > puts bib[:abook].to_s
    @book{abook,
      author = "foo" # "Author",
      title = "foo" # "bar"
    }
    > bib.join
    @book{abook,
      author = {fooAuthor},
      title = {foobar}
    }

### Names

Since version 1.3, BibTeX-Ruby features a name parser. You can use the
top-level `BibTeX.names` utility to quickly parse individual name values.
Alternatively, you can call `Bibliography.parse_names` to convert all name
fields contained in the bibliography. When parsing BibTeX files, BibTeX-Ruby
will automatically convert names; if you do not want the names to be parsed
you can set the `:parse_names` parser option to false.

Note that the string replacement and concatenation features described above
are not supported for name objects; therefore, BibTeX-Ruby tries to replace
and join all values before name conversion; name fields containing string
symbols that cannot be replaced will not be parsed.

In the following example, string replacement can take place, thus all names
are parsed and can easily be mapped to their last names:

    BibTeX.parse(<<-END)[1].author.map(&:last)
      @string{ ht = "Nathaniel Hawthorne" }
      @book{key,
       author = ht # " and Melville, Herman"
      }
      END
    #=> ["Hawthorne", "Melville"]

Another useful method is `Bibliography#names` which returns all names in
your bibliography (authors, editors, translators). For example, to quickly
expand the initials of a name across your entire bibliography, you could
use the following snippet:

    b.names.each do |name|
      if name.sort_order =~ /^Poe, E/
        name.first = 'Edgar Allen'
      end
    end

There is also a short-hand for this use case:

    b.extend_initials ['Edgar Allen', 'Poe']

Alternatively, if your bibliography contains the same names in various
forms (e.g., 'Poe, Edgar A.', 'Poe, E.A.', 'Poe, E. Allen') you can also
set all names to their longest available form:

    b.extend_initials!

Use with caution, though, as this method will treat names as identical
as long as their initials are the same. That is to say, 'Poe, Eric A.' would
be extend to 'Poe, Edgar Allen'.

### Duplicates

Large bibliographies often contain duplicate data, i.e., duplicate entries
which are not completely identical (e.g., authors or editors with first
names or initials, titles using different casing, different keywords etc.).
BibTex-Ruby allows you to group your bibliography by any number of fields
in order to detect such duplicate entries.

    b.select_duplicates_by :year, :title
    #=> groups the bibliography by using the year and title field as key

    b.duplicates?
    #=> whether or not the bibliography contains any duplicates

For more complex requirements you can use the `#group_by` method directly.
This methods accepts a list of arguments whose value will be used for grouping
and, additionally, a block. The current digest and each individual entry will
be passed to the block and the block's return value is used as the final
digest.

The duplicate methods above, for example, do something like this:

    group_by(:year, :title) do |digest, entry|
      digest.gsub(/\s+/, '').downcase
    end

You can use this method, for example, to match entries only by their author's
last name and so on and so forth.

Since version 4.1.0, BibTeX-ruby supports parsing of names spelled in the East Asian order (last name, then first name). Names contain a Chinese, Japanese or Korean letter are currently assumed to be such names. If the name is written in comma-separated manner, it is parsed in the normal way.

    b = BibTeX.parse(<<-END)
    @book{key,
     title = "プログラミング言語 Ruby",
     author = "David Flanagan and まつもと ゆきひろ",
     translator = "卜部, 昌平 and 長尾, 高弘",
     year = "2009",
     publisher = "O'Reilly Japan"
    }
    END
    [*b[0].author, *b[0].translator].map(&:last) #=> [Flanagan, まつもと, 卜部, 長尾]

### Filters

Since version 1.3.8 BibTeX-Ruby comes with a plugin framework for input
filters. You can use the methods `convert` and `convert!` methods if `Value`,
`Entry` and `Bibliography` instances to easily convert string values according
to a given filter. Starting with version 1.3.9 BibTeX-Ruby includes a
LaTeX filter that depends on the
[latex-decode gem](http://rubygems.org/gems/latex-decode). Example:

    faust = '@book{faust, title = {Faust: Der Trag\"odie Erster Teil}}'
    BibTeX.parse(faust).convert(:latex)[:faust].title
    #=> "Faust: Der Tragödie Erster Teil"

Conditional conversions are also supported:

    faust1 = '@book{faust1, title = {Faust: Der Trag\"odie Erster Teil}}'
    faust2 = '@book{faust2, title = {Faust: Der Trag\"odie Zweiter Teil}}'
    p BibTeX.parse(faust1 + faust2).convert(:latex) { |e| e.key == :faust2 }.to_s
    
Returns:

    @book{faust1,
      title = {Faust: Der Trag\"odie Erster Teil}
    }
    @book{faust2,
      title = {Faust: Der Tragödie Zweiter Teil}
    }

If you need to express a condition on the basis of individual fields, use the
conversion methods of BibTeX::Entry with a block instead (the block will be
passed the key and value of each field prior to conversion).

When working with Bibliographies that contain LaTeX it is often best to
apply the filter upon opening or parsing the Bibliography. You can do this,
by passing the `:filter` option:

   BibTeX.open 'references.bib', :filter => :latex


### Exports

Furthermore, BibTeX-Ruby allows you to export your bibliography for processing
by other tools. Currently supported formats include YAML, JSON, and XML.

Of course, you can also export your bibliography back to BibTeX; if you
include `:meta_content', your export should be identical to the original
'.bib' file, except for whitespace, blank lines and letter case (BibTeX-Ruby
will downcase all keys).

In order to export your bibliography use **#to\_s**, **#to\_yaml**,
**#to\_json**, or **#to\_xml**, respectively. For example, the following line
constitutes a simple BibTeX to YAML converter:

    >> BibTeX.open('example.bib').to_yaml

Starting with version 2.0, BibTeX-Ruby's `#to_xml` exports your bibliography
to the [BibTeXML](http://bibtexml.sf.net/) format via `rexml`. By passing the option
`:extended => true` you can make use of the BibTeXML's extended format which
will return individual person elements and name tokens (provided you have
successfully parsed the names of your bibliography).

    > BibTeX.parse(<<-END).to_xml(:extended => true).write($stdout, 2)
    " @book{pickaxe,
    "   Address = {Raleigh, North Carolina},
    "     Author = {Thomas, Dave, and Fowler, Chad, and Hunt, Andy},
    "     Publisher = {The Pragmatic Bookshelf},
    "     Title = {Programming Ruby 1.9: The Pragmatic Programmer's Guide},
    "     Year = {2009}
    "   }
    " END

This example parse a BibTeX entry, formats it as extended BibTeXML,
and writes the following XML to standard out:

```xml
<?xml version='1.0' encoding='UTF-8'?>
<bibtex:file xmlns:bibtex='http://bibtexml.sf.net/'>
  <bibtex:entry id='pickaxe'>
    <bibtex:book>
      <bibtex:address>Raleigh, North Carolina</bibtex:address>
      <bibtex:author>
        <bibtex:person>
          <bibtex:first>Dave</bibtex:first>
          <bibtex:last>Thomas</bibtex:last>
        </bibtex:person>
        <bibtex:person>
          <bibtex:first>Chad</bibtex:first>
          <bibtex:last>Fowler</bibtex:last>
        </bibtex:person>
        <bibtex:person>
          <bibtex:first>Andy</bibtex:first>
          <bibtex:last>Hunt</bibtex:last>
        </bibtex:person>
      </bibtex:author>
      <bibtex:publisher>The Pragmatic Bookshelf</bibtex:publisher>
      <bibtex:title>
        Programming Ruby 1.9: The Pragmatic Programmer&apos;s Guide
      </bibtex:title>
      <bibtex:year>2009</bibtex:year>
    </bibtex:book>
  </bibtex:entry>
</bibtex:file>
```

Look at the 'examples' directory for more elaborate examples of a BibTeX to
YAML and a BibTeX to HTML converter using **#to_citeproc** to format a
bibliography using [CSL](http://citationstyles.org/).

BibTeX-Ruby offers an API which lets you manipulate BibTeX objects (string
replacement, name parsing etc.); however, sometimes you just want quick access
to your bibliography's contents. In these cases the **to_hash** method is
useful (use **to_a** if you are only interested in the bibliography's
contents): it converts all objects into simple Ruby hashes made up of symbols
and strings. Furthermore, often you would like to control what sort of quotes
are used in an export; therefore, all conversion methods accept an options
hash which lets you define what quotes to use (note that BibTeX-Ruby will
always use regular double quotes if a value consists of more than one token,
because these tokens will be concatenated using BibTeX's '#' operator).

    >> BibTeX.parse(<<-END).to_a # implies: :quotes => ['{','}']
    @book{pickaxe,
      Address = {Raleigh, North Carolina},
      Author = {Thomas, Dave, and Fowler, Chad, and Hunt, Andy},
      Publisher = {The Pragmatic Bookshelf},
      Title = {Programming Ruby 1.9: The Pragmatic Programmer's Guide},
      Year = {2009}
    }
    END
    => [{:bibtex_key=>:pickaxe, :bibtex_type=>:book,
      :address=>"{Raleigh, North Carolina}",
      :author=>"{Thomas, Dave, and Fowler, Chad, and Hunt, Andy}",
      :publisher=>"{The Pragmatic Bookshelf}",
      :title=>"{Programming Ruby 1.9: The Pragmatic Programmer's Guide}",
      :year=>"{2009}"}]

For post-processing in Ruby most of the time you do not need any explicit
quotes; therefore you can simply add the :quotes option with an empty string:

    >> BibTeX.parse(<<-END).to_a(:quotes => '')
    ...
    END
    => [{:bibtex_key=>:pickaxe, :bibtex_type=>:book,
      :address=>"Raleigh, North Carolina",
      :author=>"Thomas, Dave, and Fowler, Chad, and Hunt, Andy",
      :publisher=>"The Pragmatic Bookshelf",
      :title=>"Programming Ruby 1.9: The Pragmatic Programmer's Guide",
      :year=>"2009"}]


The Parser
----------
The BibTeX-Ruby parser is generated using the awesome
[racc](http://i.loveruby.net/en/projects/racc/) parser generator. You can take
look at the LALR grammar in the file
[lib/bibtex/bibtex.y](https://github.com/inukshuk/bibtex-ruby/blob/master/lib/bibtex/bibtex.y).

For more information about the BibTeX format and the parser's idiosyncrasies
[refer to the project wiki](https://github.com/inukshuk/bibtex-ruby/wiki/The-BibTeX-Format).


Contributing
------------
The BibTeX-Ruby source code is
[hosted on GitHub](https://github.com/inukshuk/bibtex-ruby/).
You can check out a copy of the latest code using Git:

    $ git clone https://github.com/inukshuk/bibtex-ruby.git

If you've found a bug or have a question, please open an issue on the
[BibTeX-Ruby issue tracker](https://github.com/inukshuk/bibtex-ruby/issues).
For extra credit, clone the BibTeX-Ruby repository, write a failing
example, or cucumber feature, fix the bug and submit a pull request (for
useful examples, take a look at the cucumber features in the
[features/issues/](https://github.com/inukshuk/bibtex-ruby/blob/master/features/issues)
directory).

The parser generator [racc](http://i.loveruby.net/en/projects/racc/) is
required to generate the BibTeX parser and the name parser; you do not need
to install it to use the bibtex-ruby gem.

To run the tests and cucumber examples execute these commands (from within
the bibtex-ruby directory):

    $ [sudo] gem install bundler
    $ [sudo] bundle install
    $ bundle exec rake

To execute the test suite continuously while you're working run:

    $ bundle exec guard



Credits
-------

Copyright 2011-2015 [Sylvester Keil](http://sylvester.keil.or.at/).

Kudos to all [contributors](https://github.com/inukshuk/bibtex-ruby/contributors)
who have made BibTeX-Ruby possible.

This software is distributed under the terms and conditions of the GNU GPL.
See LICENSE for details.
