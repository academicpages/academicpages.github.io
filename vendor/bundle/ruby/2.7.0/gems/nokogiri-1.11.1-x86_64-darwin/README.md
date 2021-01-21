<div><img src="https://nokogiri.org/images/nokogiri-serif-black.png" align="right"/></div>

# Nokogiri

Nokogiri (鋸) makes it easy and painless to work with XML and HTML from Ruby. It provides a sensible, easy-to-understand API for reading, writing, modifying, and querying documents. It is fast and standards-compliant by relying on native parsers like libxml2 (C) and xerces (Java).

## Guiding Principles

Some guiding principles Nokogiri tries to follow:

- be secure-by-default by treating all documents as **untrusted** by default
- be a **thin-as-reasonable layer** on top of the underlying parsers, and don't attempt to fix behavioral differences between the parsers


## Features Overview

- DOM Parser for XML and HTML4
- SAX Parser for XML and HTML4
- Push Parser for XML and HTML4
- Document search via XPath 1.0
- Document search via CSS3 selectors, with some jquery-like extensions
- XSD Schema validation
- XSLT transformation
- "Builder" DSL for XML and HTML documents


## Status

[![Concourse CI](https://ci.nokogiri.org/api/v1/teams/nokogiri-core/pipelines/nokogiri/jobs/cruby-2.7/badge)](https://ci.nokogiri.org/teams/nokogiri-core/pipelines/nokogiri)
[![Appveyor CI](https://ci.appveyor.com/api/projects/status/xj2pqwvlxwuwgr06/branch/master?svg=true)](https://ci.appveyor.com/project/flavorjones/nokogiri/branch/master)
[![Code Climate](https://codeclimate.com/github/sparklemotion/nokogiri.svg)](https://codeclimate.com/github/sparklemotion/nokogiri)
[![Test Coverage](https://api.codeclimate.com/v1/badges/59c67b0e8976027a45ad/test_coverage)](https://codeclimate.com/github/sparklemotion/nokogiri/test_coverage)

[![Gem Version](https://badge.fury.io/rb/nokogiri.svg)](https://rubygems.org/gems/nokogiri)
[![SemVer compatibility](https://api.dependabot.com/badges/compatibility_score?dependency-name=nokogiri&package-manager=bundler&version-scheme=semver)](https://dependabot.com/compatibility-score/?dependency-name=nokogiri&package-manager=bundler)
[![Tidelift dependencies](https://tidelift.com/badges/package/rubygems/nokogiri)](https://tidelift.com/subscription/pkg/rubygems-nokogiri?utm_source=rubygems-nokogiri&utm_medium=referral&utm_campaign=readme)


## Support and Help

All official documentation is posted at https://nokogiri.org (the source for which is at https://github.com/sparklemotion/nokogiri.org/, and we welcome contributions).

### Reading

Your first stops for API documentation should be:

- RDocs: https://nokogiri.org/rdoc/index.html
- An excellent community-maintained [Cheat Sheet](https://github.com/sparklemotion/nokogiri/wiki/Cheat-sheet)


### Questions

If you'd like to talk to a human:

- The Discord chat channel is `#nokogiri-💎` at https://discord.gg/UyQnKrT
- The Gitter chat channel is https://gitter.im/sparklemotion/nokogiri
- The IRC chat channel is `#nokogiri` on freenode.
- The Nokogiri mailing list is active at https://groups.google.com/group/nokogiri-talk
- The Nokogiri bug tracker is at https://github.com/sparklemotion/nokogiri/issues

Consider subscribing to [Tidelift][tidelift] which provides license assurances and timely security notifications for your open source dependencies, including Nokogiri. [Tidelift][tidelift] subscriptions also help the Nokogiri maintainers fund our [automated testing](https://ci.nokogiri.org) which in turn allows us to ship releases, bugfixes, and security updates more often.

  [tidelift]: https://tidelift.com/subscription/pkg/rubygems-nokogiri?utm_source=rubygems-nokogiri&utm_medium=referral&utm_campaign=readme


### Security and Vulnerability Reporting

Please report vulnerabilities at https://hackerone.com/nokogiri

Full information and description of our security policy is in [`SECURITY.md`](SECURITY.md)


### Semantic Versioning Policy

Nokogiri follows [Semantic Versioning](https://semver.org/) (since 2017 or so). [![Dependabot's SemVer compatibility score for Nokogiri](https://api.dependabot.com/badges/compatibility_score?dependency-name=nokogiri&package-manager=bundler&version-scheme=semver)](https://dependabot.com/compatibility-score/?dependency-name=nokogiri&package-manager=bundler)

We bump `Major.Minor.Patch` versions following this guidance:

`Major`: (we've never done this)

- Significant backwards-incompatible changes to the public API that would require rewriting existing application code.
- Some examples of backwards-incompatible changes we might someday consider for a Major release are at [`ROADMAP.md`](ROADMAP.md).

`Minor`:

- Features and bugfixes.
- Updating packaged libraries for non-security-related reasons.
- Dropping support for EOLed Ruby versions. [Some folks find this objectionable](https://github.com/sparklemotion/nokogiri/issues/1568), but [SemVer says this is OK if the public API hasn't changed](https://semver.org/#what-should-i-do-if-i-update-my-own-dependencies-without-changing-the-public-api).
- Backwards-incompatible changes to internal or private methods and constants. These are detailed in the "Changes" section of each changelog entry.

`Patch`:

- Bugfixes.
- Security updates.
- Updating packaged libraries for security-related reasons.


## Installation

Requirements:

- Ruby >= 2.5
- JRuby >= 9.2.0.0


### Native Gems: Faster, more reliable installation

"Native gems" contain pre-compiled libraries for a specific machine architecture. On supported platforms, this removes the need for compiling the C extension and the packaged libraries, or for system dependencies to exist. This results in **much faster installation** and **more reliable installation**, which as you probably know are the biggest headaches for Nokogiri users.

### Supported Platforms

As of v1.11.0, Nokogiri ships pre-compiled, "native" gems for the following platforms:

- Linux: `x86-linux` and `x86_64-linux` (req: `glibc >= 2.17`), including musl platforms like Alpine
- Darwin/MacOS: `x86_64-darwin` and `arm64-darwin`
- Windows: `x86-mingw32` and `x64-mingw32`
- Java: any platform running JRuby 9.2 or higher

To determine whether your system supports one of these gems, look at the output of `bundle platform` or `ruby -e 'puts Gem::Platform.local.to_s'`.

If you're on a supported platform, either `gem install` or `bundle install` should install a native gem without any additional action on your part. This installation should only take a few seconds, and your output should look something like:

``` sh
$ gem install nokogiri
Fetching nokogiri-1.11.0-x86_64-linux.gem
Successfully installed nokogiri-1.11.0-x86_64-linux
1 gem installed
```


### Other Installation Options

Because Nokogiri is a C extension, it requires that you have a C compiler toolchain, Ruby development header files, and some system dependencies installed.

The following may work for you if you have an appropriately-configured system:

``` bash
gem install nokogiri
```

If you have any issues, please visit [Installing Nokogiri](https://nokogiri.org/tutorials/installing_nokogiri.html) for more complete instructions and troubleshooting.


## How To Use Nokogiri

Nokogiri is a large library, and so it's challenging to briefly summarize it. We've tried to provide long, real-world examples at [Tutorials](https://nokogiri.org/tutorials/toc.html).

### Parsing and Querying

Here is example usage for parsing and querying a document:

```ruby
#! /usr/bin/env ruby

require 'nokogiri'
require 'open-uri'

# Fetch and parse HTML document
doc = Nokogiri::HTML(URI.open('https://nokogiri.org/tutorials/installing_nokogiri.html'))

# Search for nodes by css
doc.css('nav ul.menu li a', 'article h2').each do |link|
  puts link.content
end

# Search for nodes by xpath
doc.xpath('//nav//ul//li/a', '//article//h2').each do |link|
  puts link.content
end

# Or mix and match
doc.search('nav ul.menu li a', '//article//h2').each do |link|
  puts link.content
end
```


### Encoding

Strings are always stored as UTF-8 internally.  Methods that return
text values will always return UTF-8 encoded strings.  Methods that
return a string containing markup (like `to_xml`, `to_html` and
`inner_html`) will return a string encoded like the source document.

__WARNING__

Some documents declare one encoding, but actually use a different
one. In these cases, which encoding should the parser choose?

Data is just a stream of bytes. Humans add meaning to that stream. Any
particular set of bytes could be valid characters in multiple
encodings, so detecting encoding with 100% accuracy is not
possible. `libxml2` does its best, but it can't be right all the time.

If you want Nokogiri to handle the document encoding properly, your
best bet is to explicitly set the encoding.  Here is an example of
explicitly setting the encoding to EUC-JP on the parser:

```ruby
  doc = Nokogiri.XML('<foo><bar /></foo>', nil, 'EUC-JP')
```


## Technical Overview

### Guiding Principles

As noted above, two guiding principles of the software are:

- be secure-by-default by treating all documents as **untrusted** by default
- be a **thin-as-reasonable layer** on top of the underlying parsers, and don't attempt to fix behavioral differences between the parsers

Notably, despite all parsers being standards-compliant, there are behavioral inconsistencies between the parsers used in the CRuby and JRuby implementations, and Nokogiri does not and should not attempt to remove these inconsistencies. Instead, we surface these differences in the test suite when they are important/semantic; or we intentionally write tests to depend only on the important/semantic bits (omitting whitespace from regex matchers on results, for example).


### CRuby

The Ruby (a.k.a., CRuby, MRI, YARV) implementation is a C extension that depends on libxml2 and libxslt (which in turn depend on zlib and possibly libiconv).

These dependencies are met by default by Nokogiri's packaged versions of the libxml2 and libxslt source code, but a configuration option `--use-system-libraries` is provided to allow specification of alternative library locations. See [Installing Nokogiri](https://nokogiri.org/tutorials/installing_nokogiri.html) for full documentation.

We provide native gems by pre-compiling libxml2 and libxslt (and potentially zlib and libiconv) and packaging them into the gem file. In this case, no compilation is necessary at installation time, which leads to faster and more reliable installation.

See [`LICENSE-DEPENDENCIES.md`](LICENSE-DEPENDENCIES.md) for more information on which dependencies are provided in which native and source gems.


### JRuby

The Java (a.k.a. JRuby) implementation is a Java extension that depends primarily on Xerces and NekoHTML for parsing, though additional dependencies are on `isorelax`, `nekodtd`, `jing`, `serializer`, `xalan-j`, and `xml-apis`.

These dependencies are provided by pre-compiled jar files packaged in the `java` platform gem.

See [`LICENSE-DEPENDENCIES.md`](LICENSE-DEPENDENCIES.md) for more information on which dependencies are provided in which native and source gems.


## Contributing

```bash
bundle install
bundle exec rake compile test
```


## Code of Conduct

We've adopted the Contributor Covenant code of conduct, which you can read in full in [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).


## License

This project is licensed under the terms of the MIT license.

See this license at [`LICENSE.md`](LICENSE.md).


### Dependencies

Some additional libraries may be distributed with your version of Nokogiri. Please see [`LICENSE-DEPENDENCIES.md`](LICENSE-DEPENDENCIES.md) for a discussion of the variations as well as the licenses thereof.


## Authors

- Mike Dalessio
- Aaron Patterson
- Yoko Harada
- Akinori MUSHA
- John Shahid
- Karol Bucek
- Lars Kanis
- Sergio Arbeo
- Timothy Elliott
- Nobuyoshi Nakada
