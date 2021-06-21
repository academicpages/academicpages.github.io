# Releasing Ruby-Enum

There are no hard rules about when to release ruby-enum. Release bug fixes frequently, features not so frequently and breaking API changes rarely.

### Release

Run tests, check that all tests succeed locally.

```
bundle install
rake
```

Check that the last build succeeded in [Travis CI](https://travis-ci.org/dblock/ruby-enum) for all supported platforms.

Add a date to this release in [CHANGELOG.md](CHANGELOG.md).

```
### 0.2.2 (2015/7/10)
```

Remove the line with "Your contribution here.", since there will be no more contributions to this release.

Commit your changes.

```
git add README.md CHANGELOG.md lib/ruby-enum/version.rb
git commit -m "Preparing for release, 0.2.2."
```

Release.

```
$ rake release

ruby-enum 0.2.2 built to pkg/ruby-enum-0.2.2.gem.
Tagged v0.2.2.
Pushed git commits and tags.
Pushed ruby-enum 0.2.2 to rubygems.org.
```

### Prepare for the Next Version

Add the next release to [CHANGELOG.md](CHANGELOG.md).

```
### 0.2.3 (Next)

* Your contribution here.
```

Increment the third version number in [lib/ruby-enum/version.rb](lib/ruby-enum/version.rb).

Commit your changes.

```
git add CHANGELOG.md lib/ruby-enum/version.rb
git commit -m "Preparing for next development iteration, 0.2.3."
git push origin master
```
